from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView
from django.db.models import ProtectedError


from webapp.forms import TypesForm
from webapp.models import Types


class TypesCreateView(CreateView):
    template_name = 'create/create_types.html'
    model = Types
    form_class = TypesForm
    success_url = '/'


class TypesUpdateView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        types = get_object_or_404(Types, pk=pk)
        form = TypesForm(data={
            'name': types.name
        })
        return render(request, 'update/update_types.html', context={'form': form, 'types': types})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        types = get_object_or_404(Types, pk=pk)
        form = TypesForm(data=request.POST)
        if form.is_valid():
            types.name = form.cleaned_data['name']
            types.save()
            return redirect('index')
        else:
            return render(request, 'update/update_types.html', context={'form': form, 'types': types})


class TypesDeleteView(View):
    def get(self, request, *args, **kwargs):
        types = get_object_or_404(Types, pk=kwargs.get('pk'))
        return render(request, 'delete/delete_types.html', context={'types': types})

    def post(self, request, *args, **kwargs):
        types = get_object_or_404(Types, pk=kwargs.get('pk'))
        try:
            types.delete()
            return redirect('index')
        except ProtectedError:
            error = 'Ошибка: Используется в задачах, удалить нельзя!!!'
            return render(request, 'delete/delete_types.html', context={'types': types, 'error' : error})


