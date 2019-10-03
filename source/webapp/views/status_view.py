from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView


from webapp.forms import StatusForm
from webapp.models import Status


class StatusCreateView(View):

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        context = {'form': form}
        return render(request, 'create/create_status.html', context)

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('/')
        else:
            return render(request, 'create/create_status.html', context={'form': form})


class StatusUpdateView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data={
            'name': status.name
        })
        return render(request, 'update/update_status.html', context={'form': form, 'status': status})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.name = form.cleaned_data['name']
            status.save()
            return redirect('index')
        else:
            return render(request, 'update/update_status.html', context={'form': form, 'status': status})


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        return render(request, 'delete/delete_ status.html', context={'status': status})

    def post(self, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        status.delete()
        return redirect('index')
