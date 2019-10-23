from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView


from webapp.forms import StatusForm
from webapp.models import Status


class StatusCreateView(CreateView):
    template_name = 'create/create_status.html'
    model = Status
    form_class = StatusForm
    success_url = '/'


class StatusUpdateView(UpdateView):
    template_name = 'update/update_status.html'
    model = Status
    form_class = StatusForm
    context_object_name = 'status'
    success_url = '/'


class StatusDeleteView(DeleteView):
    template_name = 'delete/delete_ status.html'
    model = Status
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'status'
