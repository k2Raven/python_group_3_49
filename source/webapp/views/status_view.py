from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView
from django.db.models import ProtectedError


from webapp.forms import StatusForm
from webapp.models import Status


class StatusCreateView(CreateView):
    template_name = 'create/create_status.html'
    model = Status
    form_class = StatusForm
    success_url = '/'


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

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        try:
            status.delete()
            return redirect('index')
        except ProtectedError:
            error = 'Ошибка: Используется в задачах, удалить нельзя!!!'
            return render(request, 'delete/delete_ status.html', context={'status': status, 'error': error})
