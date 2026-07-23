<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { fetchProject } from '@/api/client'
import type { Project } from '@/api/types'
import ErrorState from '@/components/ErrorState.vue'
import LoadingSpinner from '@/components/LoadingSpinner.vue'
import RichContent from '@/components/RichContent.vue'
import TechBadge from '@/components/TechBadge.vue'
import { usePageMeta } from '@/composables/usePageMeta'

const route = useRoute()
const project = ref<Project | null>(null)
const loading = ref(true)
const error = ref('')

async function loadProject() {
  loading.value = true
  error.value = ''
  try {
    project.value = await fetchProject(route.params.slug as string)
  } catch {
    error.value = 'Project not found.'
    project.value = null
  } finally {
    loading.value = false
  }
}

watch(
  () => route.params.slug,
  () => loadProject(),
  { immediate: true },
)

usePageMeta(
  computed(() => project.value?.title || 'Project'),
  computed(() => project.value?.description),
)
</script>

<template>
  <LoadingSpinner v-if="loading" />
  <ErrorState v-else-if="error" :message="error" />

  <article v-else-if="project" class="mx-auto max-w-3xl px-4 py-12 sm:px-6">
    <div v-if="project.thumbnail" class="mb-8 overflow-hidden rounded-xl">
      <img :src="project.thumbnail" :alt="project.title" class="w-full object-cover" />
    </div>

    <h1 class="text-3xl font-bold text-white mb-4">{{ project.title }}</h1>
    <p class="text-muted mb-6">{{ project.description }}</p>

    <div class="flex flex-wrap gap-2 mb-6">
      <TechBadge v-for="tech in project.tech_stack" :key="tech" :label="tech" />
    </div>

    <div class="flex gap-4 mb-10">
      <a
        v-if="project.github_url"
        :href="project.github_url"
        target="_blank"
        rel="noopener noreferrer"
        class="rounded-lg bg-surface-light border border-slate-700 px-4 py-2 text-sm text-white hover:border-accent transition-colors"
      >
        GitHub
      </a>
      <a
        v-if="project.live_url"
        :href="project.live_url"
        target="_blank"
        rel="noopener noreferrer"
        class="rounded-lg bg-accent px-4 py-2 text-sm text-white hover:bg-accent-hover transition-colors"
      >
        Live Demo
      </a>
    </div>

    <RichContent v-if="project.content" :html="project.content" />
  </article>
</template>
