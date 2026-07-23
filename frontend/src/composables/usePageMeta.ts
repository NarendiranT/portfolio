import { type MaybeRefOrGetter, toValue, watchEffect } from 'vue'

export function usePageMeta(
  title: MaybeRefOrGetter<string>,
  description?: MaybeRefOrGetter<string | undefined>,
) {
  watchEffect(() => {
    const t = toValue(title)
    document.title = t ? `${t} | Developer Portfolio` : 'Developer Portfolio'

    const desc = description ? toValue(description) : undefined
    if (desc) {
      let meta = document.querySelector('meta[name="description"]')
      if (!meta) {
        meta = document.createElement('meta')
        meta.setAttribute('name', 'description')
        document.head.appendChild(meta)
      }
      meta.setAttribute('content', desc)
    }
  })
}
