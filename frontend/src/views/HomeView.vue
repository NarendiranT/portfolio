<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { RouterLink } from 'vue-router'
import { fetchBlogPosts, fetchProfile, fetchProjects } from '@/api/client'
import type { BlogPost, Profile, Project } from '@/api/types'
import BlogCard from '@/components/BlogCard.vue'
import ErrorState from '@/components/ErrorState.vue'
import LoadingSpinner from '@/components/LoadingSpinner.vue'
import ProjectCard from '@/components/ProjectCard.vue'
import { usePageMeta } from '@/composables/usePageMeta'

const profile = ref<Profile | null>(null)
const featuredProjects = ref<Project[]>([])
const recentPosts = ref<BlogPost[]>([])
const loading = ref(true)
const error = ref('')

usePageMeta('Home', 'Narendiran portfolio showcasing projects and blog posts')

onMounted(async () => {
  try {
    const [profileData, projects, posts] = await Promise.all([
      fetchProfile(),
      fetchProjects(),
      fetchBlogPosts(),
    ])
    profile.value = profileData
    featuredProjects.value = projects.filter((p) => p.featured).slice(0, 3)
    recentPosts.value = posts.slice(0, 3)
  } catch {
    error.value = 'Failed to load homepage content.'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <LoadingSpinner v-if="loading" />
  <ErrorState v-else-if="error" :message="error" />

  <div v-else>
    <section class="mx-auto max-w-6xl px-4 py-20 sm:px-6">
      <div class="max-w-2xl">
        <p class="text-accent font-medium mb-2">Hello, I'm</p>
        <h1 class="text-4xl sm:text-5xl font-bold text-white mb-4">
          {{ profile?.name }}
        </h1>
        <p class="text-xl text-muted mb-8">{{ profile?.headline }}</p>
        <div class="flex flex-wrap gap-4">
          <RouterLink
            to="/projects"
            class="rounded-lg bg-accent px-6 py-3 text-sm font-medium text-white hover:bg-accent-hover transition-colors"
          >
            View Projects
          </RouterLink>
          <a
            v-if="profile?.github"
            :href="profile.github"
            target="_blank"
            rel="noopener noreferrer"
            class="rounded-lg border border-slate-700 px-6 py-3 text-sm font-medium text-white hover:border-accent transition-colors"
          >
            GitHub
          </a>
          <a
            v-if="profile?.resume"
            :href="profile.resume"
            target="_blank"
            rel="noopener noreferrer"
            class="rounded-lg border border-slate-700 px-6 py-3 text-sm font-medium text-white hover:border-accent transition-colors"
          >
            Resume
          </a>
        </div>
      </div>
    </section>

    <section v-if="featuredProjects.length" class="mx-auto max-w-6xl px-4 py-12 sm:px-6">
      <div class="flex items-center justify-between mb-8">
        <h2 class="text-2xl font-bold text-white">Featured Projects</h2>
        <RouterLink to="/projects" class="text-sm text-accent hover:text-accent-hover">
          View all &rarr;
        </RouterLink>
      </div>
      <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <ProjectCard v-for="project in featuredProjects" :key="project.slug" :project="project" />
      </div>
    </section>

    <section v-if="recentPosts.length" class="mx-auto max-w-6xl px-4 py-12 sm:px-6 pb-20">
      <div class="flex items-center justify-between mb-8">
        <h2 class="text-2xl font-bold text-white">Recent Blog Posts</h2>
        <RouterLink to="/blog" class="text-sm text-accent hover:text-accent-hover">
          View all &rarr;
        </RouterLink>
      </div>
      <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <BlogCard v-for="post in recentPosts" :key="post.slug" :post="post" />
      </div>
    </section>
  </div>
</template>
