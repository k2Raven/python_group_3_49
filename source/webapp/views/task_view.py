from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView


from webapp.forms import TaskForm
from webapp.models import Task, Status, Types

#
# class IndexView(ListView):
#     template_name = 'index.html'
#     context_object_name = 'Tasks', 'Status', 'Types'
#     model = Task, Status, Types
#
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tasks'] = Task.objects.order_by('-created_at')
        context['Status'] = Status.objects.all()
        context['Types'] = Types.objects.all()
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
        return render(request, 'create/create.html', context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                types=form.cleaned_data['types']
            )
            return redirect('/')
        else:
            return render(request, 'create/create.html', context={'form': form})


class TaskUpdateView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data={
            'summary': task.summary,
            'description': task.description,
            'status': task.status_id,
            'types': task.types_id
        })
        return render(request, 'update/update.html', context={'form': form, 'task': task})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.types = form.cleaned_data['types']
            task.save()
            return redirect('index')
        else:
            return render(request, 'update/update.html', context={'form': form, 'task': task.pk})


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'delete/delete.html', context={'task': task})

    def post(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')