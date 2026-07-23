<script setup lang="ts">
import { RouterLink } from 'vue-router'
import TechBadge from '@/components/TechBadge.vue'
import type { Project } from '@/api/types'

defineProps<{
  project: Project
}>()

function formatDate(date: string) {
  return new Date(date).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
  })
}
</script>

<template>
  <RouterLink
    :to="`/projects/${project.slug}`"
    class="group block overflow-hidden rounded-xl border border-slate-800 bg-surface-light transition-all hover:border-accent/50 hover:shadow-lg hover:shadow-accent/5"
  >
    <div class="aspect-video bg-slate-800 overflow-hidden">
      <img
        v-if="project.thumbnail"
        :src="project.thumbnail"
        :alt="project.title"
        class="h-full w-full object-cover transition-transform group-hover:scale-105"
      />
      <div v-else class="flex h-full items-center justify-center text-muted text-sm">
        No image
      </div>
    </div>
    <div class="p-5">
      <h3 class="text-lg font-semibold text-white group-hover:text-accent transition-colors">
        {{ project.title }}
      </h3>
      <p class="mt-2 text-sm text-muted line-clamp-2">{{ project.description }}</p>
      <div class="mt-3 flex flex-wrap gap-2">
        <TechBadge v-for="tech in project.tech_stack.slice(0, 4)" :key="tech" :label="tech" />
      </div>
      <p class="mt-3 text-xs text-muted">{{ formatDate(project.created_at) }}</p>
    </div>
  </RouterLink>
</template>
