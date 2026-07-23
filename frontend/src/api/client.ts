import axios from 'axios'
import type { BlogPost, PaginatedResponse, Profile, Project } from './types'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
})

export async function fetchProjects(): Promise<Project[]> {
  const { data } = await api.get<PaginatedResponse<Project>>('/api/projects/')
  return data.results
}

export async function fetchProject(slug: string): Promise<Project> {
  const { data } = await api.get<Project>(`/api/projects/${slug}/`)
  return data
}

export async function fetchBlogPosts(): Promise<BlogPost[]> {
  const { data } = await api.get<PaginatedResponse<BlogPost>>('/api/blog/')
  return data.results
}

export async function fetchBlogPost(slug: string): Promise<BlogPost> {
  const { data } = await api.get<BlogPost>(`/api/blog/${slug}/`)
  return data
}

export async function fetchProfile(): Promise<Profile> {
  const { data } = await api.get<Profile>('/api/profile/')
  return data
}

export default api
