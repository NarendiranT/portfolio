<script setup lang="ts">
import { nextTick, onMounted, ref, watch } from 'vue'

const STORAGE_KEY = 'portfolio-chat-dismissed'

type Role = 'bot' | 'user'

interface Message {
  id: number
  role: Role
  text: string
}

const isOpen = ref(false)
const input = ref('')
const sending = ref(false)
const messagesEl = ref<HTMLElement | null>(null)
let nextId = 1

const messages = ref<Message[]>([
  {
    id: nextId++,
    role: 'bot',
    text: "Hi! I'm the portfolio assistant. Ask me about Narendiran, projects, the blog.",
  },
])

onMounted(() => {
  // Open automatically on first visit; stay closed after the user dismisses once.
  const dismissed = localStorage.getItem(STORAGE_KEY) === '1'
  isOpen.value = !dismissed
})

watch(isOpen, (open) => {
  if (open) {
    nextTick(() => scrollToBottom())
  }
})

function toggle() {
  isOpen.value = !isOpen.value
  if (!isOpen.value) {
    localStorage.setItem(STORAGE_KEY, '1')
  }
}

function close() {
  isOpen.value = false
  localStorage.setItem(STORAGE_KEY, '1')
}

function scrollToBottom() {
  const el = messagesEl.value
  if (el) el.scrollTop = el.scrollHeight
}

function replyFor(text: string): string {
  const q = text.toLowerCase()
  if (/(project|work|portfolio|built)/.test(q)) {
    return 'You can browse featured work on the Projects page. Open any card for tech stack, links, and details.'
  }
  if (/(blog|post|article|write)/.test(q)) {
    return 'Recent writing lives on the Blog page. Each post has a full write-up you can open from the list.'
  }
  if (/(about|who|bio|background)/.test(q)) {
    return 'The About page has a short bio and background. Say if you want a pointer to contact details.'
  }
  if (/(contact|email|hire|reach)/.test(q)) {
    return 'Check the About page and footer for contact options. You can also reach out via any links listed on the profile.'
  }
  if (/(hello|hi|hey)/.test(q)) {
    return 'Hello! Ask about profile, projects, blog posts.'
  }
  return "I'm a simple guide for this site right now. Try asking about projects, the blog, About, or contact."
}

async function send() {
  const text = input.value.trim()
  if (!text || sending.value) return

  messages.value.push({ id: nextId++, role: 'user', text })
  input.value = ''
  sending.value = true
  await nextTick()
  scrollToBottom()

  await new Promise((r) => setTimeout(r, 450))
  messages.value.push({ id: nextId++, role: 'bot', text: replyFor(text) })
  sending.value = false
  await nextTick()
  scrollToBottom()
}

function onKeydown(e: KeyboardEvent) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    void send()
  }
}
</script>

<template>
  <div class="fixed bottom-4 right-4 z-[60] flex flex-col items-end gap-3 sm:bottom-6 sm:right-6">
    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 translate-y-3 scale-95"
      enter-to-class="opacity-100 translate-y-0 scale-100"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0 scale-100"
      leave-to-class="opacity-0 translate-y-3 scale-95"
    >
      <section
        v-if="isOpen"
        class="flex h-[min(28rem,70vh)] w-[min(22rem,calc(100vw-2rem))] flex-col overflow-hidden rounded-2xl border border-slate-700 bg-surface-light shadow-2xl shadow-black/40"
        role="dialog"
        aria-label="Portfolio chatbot"
      >
        <header class="flex items-center justify-between gap-3 border-b border-slate-700 bg-surface px-4 py-3">
          <div class="min-w-0">
            <p class="truncate text-sm font-semibold text-white">Portfolio assistant</p>
            <p class="truncate text-xs text-muted">Ask about Me &amp;projects &amp; blog</p>
          </div>
          <button
            type="button"
            class="rounded-lg p-1.5 text-muted transition-colors hover:bg-slate-800 hover:text-white"
            aria-label="Close chat"
            @click="close"
          >
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </header>

        <div ref="messagesEl" class="flex-1 space-y-3 overflow-y-auto px-3 py-3">
          <div
            v-for="msg in messages"
            :key="msg.id"
            class="flex"
            :class="msg.role === 'user' ? 'justify-end' : 'justify-start'"
          >
            <p
              class="max-w-[85%] rounded-2xl px-3 py-2 text-sm leading-relaxed"
              :class="
                msg.role === 'user'
                  ? 'rounded-br-md bg-accent text-white'
                  : 'rounded-bl-md bg-slate-800 text-slate-200'
              "
            >
              {{ msg.text }}
            </p>
          </div>
          <div v-if="sending" class="flex justify-start">
            <p class="rounded-2xl rounded-bl-md bg-slate-800 px-3 py-2 text-sm text-muted">
              Typing…
            </p>
          </div>
        </div>

        <form class="border-t border-slate-700 bg-surface p-3" @submit.prevent="send">
          <div class="flex items-end gap-2">
            <label class="sr-only" for="chat-input">Message</label>
            <textarea
              id="chat-input"
              v-model="input"
              rows="1"
              placeholder="Ask something…"
              class="max-h-24 min-h-[2.5rem] flex-1 resize-none rounded-xl border border-slate-700 bg-surface-light px-3 py-2 text-sm text-slate-100 placeholder:text-slate-500 focus:border-accent focus:outline-none focus:ring-1 focus:ring-accent"
              @keydown="onKeydown"
            />
            <button
              type="submit"
              class="inline-flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-accent text-white transition-colors hover:bg-accent-hover disabled:cursor-not-allowed disabled:opacity-50"
              :disabled="!input.trim() || sending"
              aria-label="Send message"
            >
              <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M5 12h14M12 5l7 7-7 7"
                />
              </svg>
            </button>
          </div>
        </form>
      </section>
    </Transition>

    <button
      type="button"
      class="flex h-14 w-14 items-center justify-center rounded-full bg-accent text-white shadow-lg shadow-accent/30 transition-transform hover:bg-accent-hover hover:scale-105 focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2 focus-visible:ring-offset-surface"
      :aria-label="isOpen ? 'Minimize chat' : 'Open chat'"
      :aria-expanded="isOpen"
      @click="toggle"
    >
      <svg v-if="!isOpen" class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
        />
      </svg>
      <svg v-else class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>
  </div>
</template>
