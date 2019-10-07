from django.views.generic import CreateView


from webapp.forms import TypesForm
from webapp.models import Types
from webapp.views.base_view import UpdateView, DeleteView


class TypesCreateView(CreateView):
    template_name = 'create/create_types.html'
    model = Types
    form_class = TypesForm
    success_url = '/'


class TypesUpdateView(UpdateView):
    template_name = 'update/update_types.html'
    model = Types
    form_class = TypesForm
    redirect_url = 'index'
    key_kwarg = 'pk'
    context_object_name = 'types'


class TypesDeleteView(DeleteView):
    template_name = 'delete/delete_types.html'
    model = Types
    error_deletion = False
    redirect_url = 'index'
    key_kwarg = 'pk'
    context_object_name = 'types'
    text_error = 'Ошибка: Используется в задачах, удалить нельзя!!!'
