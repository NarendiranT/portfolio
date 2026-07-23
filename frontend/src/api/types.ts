export interface PaginatedResponse<T> {
  count: number
  next: string | null
  previous: string | null
  results: T[]
}

export interface Project {
  title: string
  slug: string
  description: string
  tech_stack: string[]
  thumbnail: string | null
  featured: boolean
  github_url: string
  live_url: string
  order: number
  created_at: string
  content?: string
  updated_at?: string
}

export interface BlogPost {
  title: string
  slug: string
  excerpt: string
  cover_image: string | null
  tags: string[]
  order: number
  published_at: string | null
  created_at: string
  content?: string
}

export interface Profile {
  name: string
  headline: string
  bio: string
  avatar: string | null
  skills: string[]
  github: string
  linkedin: string
  email: string
  resume: string | null
}
