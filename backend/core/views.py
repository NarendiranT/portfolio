from rest_framework import generics
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.load()

    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()
        if not profile.name:
            return Response({"detail": "Profile not configured."}, status=404)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
