<script setup lang="ts">
import { RouterLink } from 'vue-router'
import TechBadge from '@/components/TechBadge.vue'
import type { BlogPost } from '@/api/types'

defineProps<{
  post: BlogPost
}>()

function formatDate(date: string | null) {
  if (!date) return ''
  return new Date(date).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}
</script>

<template>
  <RouterLink
    :to="`/blog/${post.slug}`"
    class="group block overflow-hidden rounded-xl border border-slate-800 bg-surface-light transition-all hover:border-accent/50"
  >
    <div v-if="post.cover_image" class="aspect-[2/1] overflow-hidden">
      <img
        :src="post.cover_image"
        :alt="post.title"
        class="h-full w-full object-cover transition-transform group-hover:scale-105"
      />
    </div>
    <div class="p-5">
      <time class="text-xs text-muted">{{ formatDate(post.published_at) }}</time>
      <h3 class="mt-2 text-lg font-semibold text-white group-hover:text-accent transition-colors">
        {{ post.title }}
      </h3>
      <p class="mt-2 text-sm text-muted line-clamp-2">{{ post.excerpt }}</p>
      <div v-if="post.tags.length" class="mt-3 flex flex-wrap gap-2">
        <TechBadge v-for="tag in post.tags" :key="tag" :label="tag" />
      </div>
    </div>
  </RouterLink>
</template>
