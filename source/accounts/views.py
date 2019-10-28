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