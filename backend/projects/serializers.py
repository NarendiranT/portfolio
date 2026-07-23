from rest_framework import serializers

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "title",
            "slug",
            "description",
            "tech_stack",
            "thumbnail",
            "featured",
            "github_url",
            "live_url",
            "order",
            "created_at",
        ]

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return None


class ProjectDetailSerializer(ProjectListSerializer):
    class Meta(ProjectListSerializer.Meta):
        fields = ProjectListSerializer.Meta.fields + ["content", "updated_at"]
