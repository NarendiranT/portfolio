from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    resume = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "name",
            "headline",
            "bio",
            "avatar",
            "skills",
            "github",
            "linkedin",
            "email",
            "resume",
        ]

    def get_avatar(self, obj):
        if obj.avatar:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return None

    def get_resume(self, obj):
        if obj.resume:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.resume.url)
            return obj.resume.url
        return None
