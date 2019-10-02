from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView


from webapp.forms import TaskForm, StatusForm, TypesForm
from webapp.models import Task, Status, Types


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
        return render(request, 'create.html', context)

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
            return render(request, 'create.html', context={'form': form})


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
        return render(request, 'update.html', context={'form': form, 'task': task})

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
            return render(request, 'update.html', context={'form': form, 'task': task.pk})


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'delete.html', context={'task': task})

    def post(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')


class StatusCreateView(View):

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        context = {'form': form}
        return render(request, 'create_status.html', context)

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('/')
        else:
            return render(request, 'create_status.html', context={'form': form})


class TypesCreateView(View):

    def get(self, request, *args, **kwargs):
        form = TypesForm()
        context = {'form': form}
        return render(request, 'create_types.html', context)

    def post(self, request, *args, **kwargs):
        form = TypesForm(data=request.POST)
        if form.is_valid():
            Types.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('/')
        else:
            return render(request, 'create_types.html', context={'form': form})


class TypesUpdateView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        types = get_object_or_404(Types, pk=pk)
        form = TypesForm(data={
            'name': types.name
        })
        return render(request, 'update_types.html', context={'form': form, 'types': types})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        types = get_object_or_404(Types, pk=pk)
        form = TypesForm(data=request.POST)
        if form.is_valid():
            types.name = form.cleaned_data['name']
            types.save()
            return redirect('index')
        else:
            return render(request, 'update_types.html', context={'form': form, 'types': types})


class StatusUpdateView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data={
            'name': status.name
        })
        return render(request, 'update_status.html', context={'form': form, 'status': status})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.name = form.cleaned_data['name']
            status.save()
            return redirect('index')
        else:
            return render(request, 'update_status.html', context={'form': form, 'status': status})