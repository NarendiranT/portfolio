<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { fetchProjects } from '@/api/client'
import type { Project } from '@/api/types'
import ErrorState from '@/components/ErrorState.vue'
import LoadingSpinner from '@/components/LoadingSpinner.vue'
import ProjectCard from '@/components/ProjectCard.vue'
import { usePageMeta } from '@/composables/usePageMeta'

const projects = ref<Project[]>([])
const loading = ref(true)
const error = ref('')

usePageMeta('Projects', 'Browse my development projects')

onMounted(async () => {
  try {
    projects.value = await fetchProjects()
  } catch {
    error.value = 'Failed to load projects.'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="mx-auto max-w-6xl px-4 py-12 sm:px-6">
    <h1 class="text-3xl font-bold text-white mb-2">Projects</h1>
    <p class="text-muted mb-10">A collection of things I've built.</p>

    <LoadingSpinner v-if="loading" />
    <ErrorState v-else-if="error" :message="error" />
    <div v-else-if="projects.length" class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
      <ProjectCard v-for="project in projects" :key="project.slug" :project="project" />
    </div>
    <p v-else class="text-muted text-center py-20">No projects yet.</p>
  </div>
</template>
