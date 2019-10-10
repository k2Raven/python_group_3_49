from django.views.generic import ListView, DetailView

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
