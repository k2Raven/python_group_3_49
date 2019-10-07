from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View


class UpdateView(View):
    template_name = None
    model = None
    form_class = None
    redirect_url = None
    key_kwarg = 'pk'
    context_object_name = None

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwarg)
        context = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=context)

        return render(request, self.template_name, context={'form': form, self.context_object_name: context})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get(self.key_kwarg)
        context = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=context, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        context = {'form': form}
        return render(self.request, self.template_name, context)

    def get_redirect_url(self):
        return self.redirect_url


class DeleteView(View):
    template_name = None
    model = None
    confirm_deletion = True
    error_deletion = True
    redirect_url = None
    key_kwarg = 'pk'
    context_object_name = None
    text_error = 'Ошибка'
    error_name = 'error'

    def get(self, request, *args, **kwargs):
        self.odject = get_object_or_404(self.model, pk=kwargs.get(self.key_kwarg))
        if self.confirm_deletion:
            return render(request, self.template_name, context={self.context_object_name: self.odject})
        else:
            self.odject_delete()
            return redirect(self.get_redirect_url())

    def post(self,request, *args, **kwargs):
        self.odject = get_object_or_404(self.model, pk=kwargs.get(self.key_kwarg))
        if self.error_deletion:
            self.odject_delete()
            return redirect(self.get_redirect_url())
        else:
            try:
                self.odject_delete()
                return redirect(self.get_redirect_url())
            except ProtectedError:
                return render(request, self.template_name, context={self.context_object_name: self.odject, self.error_name: self.text_error})

    def odject_delete(self):
        self.odject.delete()

    def get_redirect_url(self):
        return self.redirect_url
