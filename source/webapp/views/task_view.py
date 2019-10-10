from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from webapp.forms import TaskForm
from webapp.models import Task, Status, Types, Project


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'Tasks'
    paginate_by = 5
    paginate_orphans = 1

    def get_queryset(self):
        return Task.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Status'] = Status.objects.all()
        context['Types'] = Types.objects.all()
        return context


class TaskView(DetailView):
    template_name = 'view.html'
    model = Task
    context_object_name = 'Task'


class TaskCreateView(CreateView):
    template_name = 'create/create.html'
    form_class = TaskForm

    def form_valid(self, form):
        project_pk = self.kwargs.get('pk')
        project = get_object_or_404(Project,pk=project_pk)
        project.task.create(**form.cleaned_data)
        return redirect('project_view', pk=project_pk)


class TaskUpdateView(UpdateView):
    template_name = 'update/update.html'
    model = Task
    form_class = TaskForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'delete/delete.html'
    model = Task
    success_url = reverse_lazy('index')
    context_object_name = 'task'
