from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView


from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tasks'] = Task.objects.order_by('-created_at')
        return context


class TaskView(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Task'] = get_object_or_404(Task, pk=kwargs['task_id'])
        return context


class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        context = {'form': form}
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                types=form.cleaned_data['types']
            )
            return redirect('/')
        else:
            return render(request, 'create.html', context={'form': form})

