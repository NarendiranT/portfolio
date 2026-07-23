<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { fetchBlogPost } from '@/api/client'
import type { BlogPost } from '@/api/types'
import ErrorState from '@/components/ErrorState.vue'
import LoadingSpinner from '@/components/LoadingSpinner.vue'
import RichContent from '@/components/RichContent.vue'
import TechBadge from '@/components/TechBadge.vue'
import { usePageMeta } from '@/composables/usePageMeta'

const route = useRoute()
const post = ref<BlogPost | null>(null)
const loading = ref(true)
const error = ref('')

function formatDate(date: string | null) {
  if (!date) return ''
  return new Date(date).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

async function loadPost() {
  loading.value = true
  error.value = ''
  try {
    post.value = await fetchBlogPost(route.params.slug as string)
  } catch {
    error.value = 'Blog post not found.'
    post.value = null
  } finally {
    loading.value = false
  }
}

watch(
  () => route.params.slug,
  () => loadPost(),
  { immediate: true },
)

usePageMeta(
  computed(() => post.value?.title || 'Blog'),
  computed(() => post.value?.excerpt),
)
</script>

<template>
  <LoadingSpinner v-if="loading" />
  <ErrorState v-else-if="error" :message="error" />

  <article v-else-if="post" class="mx-auto max-w-3xl px-4 py-12 sm:px-6">
    <time class="text-sm text-muted">{{ formatDate(post.published_at) }}</time>
    <h1 class="text-3xl font-bold text-white mt-2 mb-4">{{ post.title }}</h1>

    <div v-if="post.tags.length" class="flex flex-wrap gap-2 mb-8">
      <TechBadge v-for="tag in post.tags" :key="tag" :label="tag" />
    </div>

    <div v-if="post.cover_image" class="mb-8 overflow-hidden rounded-xl">
      <img :src="post.cover_image" :alt="post.title" class="w-full object-cover" />
    </div>

    <RichContent v-if="post.content" :html="post.content" />
  </article>
</template>
