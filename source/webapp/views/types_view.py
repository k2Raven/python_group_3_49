from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView


from webapp.forms import TypesForm
from webapp.models import Types


class TypesCreateView(LoginRequiredMixin,CreateView):
    template_name = 'create/create_types.html'
    model = Types
    form_class = TypesForm
    success_url = '/'


class TypesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'update/update_types.html'
    model = Types
    form_class = TypesForm
    context_object_name = 'types'
    success_url = '/'


class TypesDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete/delete_types.html'
    model = Types
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'types'
