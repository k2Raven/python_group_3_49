from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserCreationForm


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:project_list')

    else:
        form = UserCreationForm()
    return render(request, 'create.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'