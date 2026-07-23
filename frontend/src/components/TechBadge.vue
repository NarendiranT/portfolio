<script setup lang="ts">
defineProps<{
  label: string
}>()
</script>

<template>
  <span class="inline-block rounded-full bg-accent/20 px-3 py-1 text-xs font-medium text-accent">
    {{ label }}
  </span>
</template>
