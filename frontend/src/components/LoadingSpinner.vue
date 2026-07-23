<script setup lang="ts">
defineProps<{
  message?: string
}>()
</script>

<template>
  <div class="flex flex-col items-center justify-center py-20 gap-3">
    <div class="h-8 w-8 animate-spin rounded-full border-2 border-accent border-t-transparent" />
    <p v-if="message" class="text-sm text-muted">{{ message }}</p>
  </div>
</template>
