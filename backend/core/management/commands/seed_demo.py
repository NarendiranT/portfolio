from django.core.management.base import BaseCommand

from blog.models import BlogPost
from core.models import Profile
from projects.models import Project


class Command(BaseCommand):
    help = "Seed demo profile, projects, and blog posts"

    def handle(self, *args, **options):
        profile, created = Profile.objects.get_or_create(
            pk=1,
            defaults={
                "name": "Jane Developer",
                "headline": "Full-stack developer building web apps with Vue and Django",
                "bio": "<p>Hi, I'm Jane — a developer passionate about clean code, great UX, and open source.</p>",
                "skills": ["Python", "Django", "Vue.js", "TypeScript", "PostgreSQL", "Docker"],
                "github": "https://github.com",
                "linkedin": "https://linkedin.com",
                "email": "jane@example.com",
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS("Created profile"))

        projects_data = [
            {
                "title": "TaskFlow",
                "slug": "taskflow",
                "description": "A collaborative task management app with real-time updates.",
                "content": "<p>TaskFlow helps teams organize work with kanban boards and notifications.</p>",
                "tech_stack": ["Vue 3", "Django", "Redis", "WebSockets"],
                "github_url": "https://github.com",
                "live_url": "https://example.com",
                "featured": True,
                "order": 1,
            },
            {
                "title": "DevMetrics",
                "slug": "devmetrics",
                "description": "Analytics dashboard for tracking developer productivity metrics.",
                "content": "<p>DevMetrics aggregates GitHub and CI data into actionable insights.</p>",
                "tech_stack": ["Python", "FastAPI", "PostgreSQL", "Chart.js"],
                "github_url": "https://github.com",
                "featured": True,
                "order": 2,
            },
            {
                "title": "Blog CMS",
                "slug": "blog-cms",
                "description": "Headless CMS for developer blogs with markdown support.",
                "content": "<p>A lightweight CMS built for developers who love writing in markdown.</p>",
                "tech_stack": ["Django", "DRF", "Vue 3"],
                "live_url": "https://example.com",
                "featured": False,
                "order": 3,
            },
        ]

        for data in projects_data:
            _, created = Project.objects.update_or_create(slug=data["slug"], defaults=data)
            if created:
                self.stdout.write(f"Created project: {data['title']}")

        blog_data = [
            {
                "title": "Building a Portfolio with Vue and Django",
                "slug": "building-portfolio-vue-django",
                "excerpt": "How I built a decoupled portfolio site with a rich text admin.",
                "content": "<p>This post walks through the architecture decisions behind this portfolio site.</p>",
                "tags": ["vue", "django", "portfolio"],
                "order": 1,
            },
            {
                "title": "Why I Switched to TypeScript",
                "slug": "why-i-switched-to-typescript",
                "excerpt": "TypeScript caught bugs before they hit production — here's my experience.",
                "content": "<p>After a year of TypeScript, I wouldn't go back to plain JavaScript for large apps.</p>",
                "tags": ["typescript", "javascript"],
                "order": 2,
            },
        ]

        for data in blog_data:
            _, created = BlogPost.objects.update_or_create(slug=data["slug"], defaults=data)
            if created:
                self.stdout.write(f"Created blog post: {data['title']}")

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully"))
