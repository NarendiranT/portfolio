from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Profile(models.Model):
    name = models.CharField(max_length=200)
    headline = models.CharField(max_length=300)
    bio = CKEditor5Field("Bio", config_name="default")
    avatar = models.ImageField(upload_to="profile/", blank=True)
    skills = models.JSONField(default=list, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    resume = models.FileField(upload_to="profile/", blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1, defaults={"name": "Developer", "headline": ""})
        return obj
