from rest_framework import viewsets

from .models import Project
from .serializers import ProjectDetailSerializer, ProjectListSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "slug"

    def get_queryset(self):
        return Project.objects.filter(published=True)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProjectDetailSerializer
        return ProjectListSerializer
