from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectListView(ListView):
    template_name = 'project_list.html'
    context_object_name = 'projects'
    paginate_by = 5
    paginate_orphans = 1

    def get_queryset(self):
        return Project.objects.order_by('created_at')


class ProjectView(DetailView):
    template_name = 'project_view.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.task.order_by('-created_at')
        context['tasks'] = tasks
        return context


class ProjectCreateView(CreateView):
    template_name = 'create/create_project.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'update/update_project.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})