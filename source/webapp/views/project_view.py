from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from webapp.forms import ProjectForm, SimpleSearchForm
from webapp.models import Project

from webapp.views.base_view import SearchView


class ProjectListView(SearchView):
    template_name = 'project_list.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['created_at']
    paginate_by = 5
    paginate_orphans = 1
    from_search = SimpleSearchForm

    def get_query(self):
        val = super().get_query()
        query = Q(name__icontains=val)
        return query


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
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UserPassesTestMixin, UpdateView):
    model = Project
    template_name = 'update/update_project.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def test_func(self):
        self.object = Project.objects.get(pk=self.kwargs['pk'])
        projects = Project.objects.filter(team__user=self.request.user)
        return self.object in projects

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'delete/delete_project.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:project_list')

    def test_func(self):
        self.object = Project.objects.get(pk=self.kwargs['pk'])
        projects = Project.objects.filter(team__user=self.request.user)
        return self.object in projects
