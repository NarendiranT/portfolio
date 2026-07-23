<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { fetchProfile } from '@/api/client'
import type { Profile } from '@/api/types'
import ErrorState from '@/components/ErrorState.vue'
import LoadingSpinner from '@/components/LoadingSpinner.vue'
import RichContent from '@/components/RichContent.vue'
import TechBadge from '@/components/TechBadge.vue'
import { usePageMeta } from '@/composables/usePageMeta'

const profile = ref<Profile | null>(null)
const loading = ref(true)
const error = ref('')

usePageMeta('About', 'Learn more about me')

onMounted(async () => {
  try {
    profile.value = await fetchProfile()
  } catch {
    error.value = 'Failed to load profile.'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <LoadingSpinner v-if="loading" />
  <ErrorState v-else-if="error" :message="error" />

  <div v-else-if="profile" class="mx-auto max-w-3xl px-4 py-12 sm:px-6">
    <div class="flex flex-col sm:flex-row items-start gap-8 mb-10">
      <div
        v-if="profile.avatar"
        class="h-32 w-32 shrink-0 overflow-hidden rounded-full border-2 border-accent"
      >
        <img :src="profile.avatar" :alt="profile.name" class="h-full w-full object-cover" />
      </div>
      <div
        v-else
        class="flex h-32 w-32 shrink-0 items-center justify-center rounded-full border-2 border-slate-700 bg-surface-light text-3xl font-bold text-accent"
      >
        {{ profile.name.charAt(0) }}
      </div>
      <div>
        <h1 class="text-3xl font-bold text-white">{{ profile.name }}</h1>
        <p class="mt-2 text-lg text-muted">{{ profile.headline }}</p>
        <div class="mt-4 flex flex-wrap gap-4">
          <a
            v-if="profile.github"
            :href="profile.github"
            target="_blank"
            rel="noopener noreferrer"
            class="text-sm text-accent hover:text-accent-hover"
          >
            GitHub
          </a>
          <a
            v-if="profile.linkedin"
            :href="profile.linkedin"
            target="_blank"
            rel="noopener noreferrer"
            class="text-sm text-accent hover:text-accent-hover"
          >
            LinkedIn
          </a>
          <a
            v-if="profile.email"
            :href="`mailto:${profile.email}`"
            class="text-sm text-accent hover:text-accent-hover"
          >
            {{ profile.email }}
          </a>
          <a
            v-if="profile.resume"
            :href="profile.resume"
            target="_blank"
            rel="noopener noreferrer"
            class="text-sm text-accent hover:text-accent-hover"
          >
            Download Resume
          </a>
        </div>
      </div>
    </div>

    <section class="mb-10">
      <h2 class="text-xl font-semibold text-white mb-4">About Me</h2>
      <RichContent :html="profile.bio" />
    </section>

    <section v-if="profile.skills.length">
      <h2 class="text-xl font-semibold text-white mb-4">Skills</h2>
      <div class="flex flex-wrap gap-2">
        <TechBadge v-for="skill in profile.skills" :key="skill" :label="skill" />
      </div>
    </section>
  </div>
</template>
