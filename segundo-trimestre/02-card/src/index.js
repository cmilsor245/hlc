import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import { App } from './App'

export const SKILLS = [
  {
    skill: 'HTML + CSS',
    level: 'advanced',
    color: '#2662ea'
  },
  {
    skill: 'JavaScript',
    level: 'advanced',
    color: '#efd81d'
  },
  {
    skill: 'Web Design',
    level: 'advanced',
    color: '#c3dcaf'
  },
  {
    skill: 'Git and Github',
    level: 'intermediate',
    color: '#e84f33'
  },
  {
    skill: 'React',
    level: 'advanced',
    color: '#60dafb'
  },
  {
    skill: 'Svelte',
    level: 'beginner',
    color: '#ff3b00'
  }
]

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)