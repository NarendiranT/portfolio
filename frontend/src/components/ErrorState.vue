<script setup lang="ts">
defineProps<{
  message?: string
}>()
</script>

<template>
  <div class="py-20 text-center">
    <p class="text-red-400 text-lg">{{ message || 'Something went wrong. Please try again.' }}</p>
  </div>
</template>
