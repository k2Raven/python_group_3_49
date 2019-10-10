from django.views.generic import ListView

from webapp.models import Project


class ProjectView(ListView):
    template_name = 'project_list.html'
    context_object_name = 'Projects'
    paginate_by = 5
    paginate_orphans = 1

    def get_queryset(self):
        return Project.objects.order_by('-created_at')