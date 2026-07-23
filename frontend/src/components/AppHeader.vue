<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink, useRoute } from 'vue-router'

const route = useRoute()
const mobileOpen = ref(false)

const links = [
  { to: '/', label: 'Home' },
  { to: '/projects', label: 'Projects' },
  { to: '/blog', label: 'Blog' },
  { to: '/about', label: 'About' },
]

function isActive(path: string) {
  if (path === '/') return route.path === '/'
  return route.path.startsWith(path)
}
</script>

<template>
  <header class="sticky top-0 z-50 border-b border-slate-800 bg-surface/95 backdrop-blur">
    <nav class="mx-auto flex max-w-6xl items-center justify-between px-4 py-4 sm:px-6">
      <RouterLink to="/" class="text-lg font-bold text-white hover:text-accent transition-colors">
        Portfolio
      </RouterLink>

      <ul class="hidden md:flex items-center gap-8">
        <li v-for="link in links" :key="link.to">
          <RouterLink
            :to="link.to"
            class="text-sm font-medium transition-colors"
            :class="isActive(link.to) ? 'text-accent' : 'text-muted hover:text-white'"
          >
            {{ link.label }}
          </RouterLink>
        </li>
      </ul>

      <button
        class="md:hidden text-muted hover:text-white"
        aria-label="Toggle menu"
        @click="mobileOpen = !mobileOpen"
      >
        <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path
            v-if="!mobileOpen"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16M4 18h16"
          />
          <path
            v-else
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
    </nav>

    <div v-if="mobileOpen" class="md:hidden border-t border-slate-800 px-4 py-4">
      <RouterLink
        v-for="link in links"
        :key="link.to"
        :to="link.to"
        class="block py-2 text-sm font-medium"
        :class="isActive(link.to) ? 'text-accent' : 'text-muted'"
        @click="mobileOpen = false"
      >
        {{ link.label }}
      </RouterLink>
    </div>
  </header>
</template>
