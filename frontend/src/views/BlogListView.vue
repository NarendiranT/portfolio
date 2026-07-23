<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { fetchBlogPosts } from '@/api/client'
import type { BlogPost } from '@/api/types'
import BlogCard from '@/components/BlogCard.vue'
import ErrorState from '@/components/ErrorState.vue'
import LoadingSpinner from '@/components/LoadingSpinner.vue'
import { usePageMeta } from '@/composables/usePageMeta'

const posts = ref<BlogPost[]>([])
const loading = ref(true)
const error = ref('')

usePageMeta('Blog', 'Thoughts on development, tools, and tech')

onMounted(async () => {
  try {
    posts.value = await fetchBlogPosts()
  } catch {
    error.value = 'Failed to load blog posts.'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="mx-auto max-w-6xl px-4 py-12 sm:px-6">
    <h1 class="text-3xl font-bold text-white mb-2">Blog</h1>
    <p class="text-muted mb-10">Writing about code, tools, and lessons learned.</p>

    <LoadingSpinner v-if="loading" />
    <ErrorState v-else-if="error" :message="error" />
    <div v-else-if="posts.length" class="grid gap-6 sm:grid-cols-2">
      <BlogCard v-for="post in posts" :key="post.slug" :post="post" />
    </div>
    <p v-else class="text-muted text-center py-20">No blog posts yet.</p>
  </div>
</template>
