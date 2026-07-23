<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { fetchProfile } from '@/api/client'
import type { Profile } from '@/api/types'

const profile = ref<Profile | null>(null)

onMounted(async () => {
  try {
    profile.value = await fetchProfile()
  } catch {
    profile.value = null
  }
})
</script>

<template>
  <footer class="border-t border-slate-800 bg-surface-light">
    <div class="mx-auto max-w-6xl px-4 py-8 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
      <p class="text-sm text-muted">
        &copy; {{ new Date().getFullYear() }} {{ profile?.name || 'Developer' }}. All rights reserved.
      </p>
      <div v-if="profile" class="flex items-center gap-4">
        <a
          v-if="profile.github"
          :href="profile.github"
          target="_blank"
          rel="noopener noreferrer"
          class="text-muted hover:text-accent transition-colors text-sm"
        >
          GitHub
        </a>
        <a
          v-if="profile.linkedin"
          :href="profile.linkedin"
          target="_blank"
          rel="noopener noreferrer"
          class="text-muted hover:text-accent transition-colors text-sm"
        >
          LinkedIn
        </a>
        <a
          v-if="profile.email"
          :href="`mailto:${profile.email}`"
          class="text-muted hover:text-accent transition-colors text-sm"
        >
          Email
        </a>
      </div>
    </div>
  </footer>
</template>
