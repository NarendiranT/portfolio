<script setup lang="ts">
import DOMPurify from 'dompurify'
import { computed } from 'vue'

const props = defineProps<{
  html: string
}>()

const sanitized = computed(() => DOMPurify.sanitize(props.html))
</script>

<template>
  <div class="prose-content" v-html="sanitized" />
</template>
