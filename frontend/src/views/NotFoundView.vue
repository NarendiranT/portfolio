<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { usePageMeta } from '@/composables/usePageMeta'

usePageMeta('Not Found')
</script>

<template>
  <div class="mx-auto max-w-6xl px-4 py-20 sm:px-6 text-center">
    <h1 class="text-6xl font-bold text-white mb-4">404</h1>
    <p class="text-muted mb-8">The page you're looking for doesn't exist.</p>
    <RouterLink
      to="/"
      class="rounded-lg bg-accent px-6 py-3 text-sm font-medium text-white hover:bg-accent-hover transition-colors"
    >
      Go Home
    </RouterLink>
  </div>
</template>
