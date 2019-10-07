from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import TaskForm
from webapp.models import Task, Status, Types
from webapp.views.base_view import UpdateView, DeleteView


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
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    template_name = 'update/update.html'
    model = Task
    form_class = TaskForm
    redirect_url = 'index'
    key_kwarg = 'pk'
    context_object_name = 'task'


class TaskDeleteView(DeleteView):
    template_name = 'delete/delete.html'
    model = Task
    redirect_url = 'index'
    key_kwarg = 'pk'
    context_object_name = 'task'
