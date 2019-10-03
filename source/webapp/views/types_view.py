from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView


from webapp.forms import TypesForm
from webapp.models import Types


class TypesCreateView(View):

    def get(self, request, *args, **kwargs):
        form = TypesForm()
        context = {'form': form}
        return render(request, 'create/create_types.html', context)

    def post(self, request, *args, **kwargs):
        form = TypesForm(data=request.POST)
        if form.is_valid():
            Types.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('/')
        else:
            return render(request, 'create/create_types.html', context={'form': form})


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
        return render(request, 'delete/delete_ status.html', context={'types': types})

    def post(self, *args, **kwargs):
        types = get_object_or_404(Types, pk=kwargs.get('pk'))
        types.delete()
        return redirect('index')


