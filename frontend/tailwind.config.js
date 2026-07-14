/** @type {import('tailwindcss').Config} */
export default {
  // ── Purge / Content ────────────────────────────────────────
  content: [
    './index.html',
    './src/**/*.{js,jsx,ts,tsx}',
  ],

  // ── Dark Mode ──────────────────────────────────────────────
  darkMode: 'class',

  theme: {
    extend: {
      // ── Brand Colors ───────────────────────────────────────
      colors: {
        brand: {
          50:  '#eef2ff',
          100: '#e0e7ff',
          200: '#c7d2fe',
          300: '#a5b4fc',
          400: '#818cf8',
          500: '#6366f1',   // Primary indigo
          600: '#4f46e5',
          700: '#4338ca',
          800: '#3730a3',
          900: '#312e81',
          950: '#1e1b4b',
        },
        surface: {
          900: '#0d0d14',   // App background
          800: '#13131f',   // Sidebar
          700: '#1a1a2e',   // Cards
          600: '#22223b',   // Elevated elements
          500: '#2d2d4e',   // Borders / dividers
        },
        accent: {
          purple: '#8b5cf6',
          cyan:   '#06b6d4',
          green:  '#10b981',
          amber:  '#f59e0b',
          red:    '#ef4444',
        },
      },

      // ── Typography ─────────────────────────────────────────
      fontFamily: {
        sans:  ['Inter', 'system-ui', 'sans-serif'],
        mono:  ['JetBrains Mono', 'Fira Code', 'monospace'],
        display: ['Inter', 'sans-serif'],
      },

      // ── Spacing ────────────────────────────────────────────
      spacing: {
        18: '4.5rem',
        88: '22rem',
        sidebar: '280px',
      },

      // ── Border Radius ──────────────────────────────────────
      borderRadius: {
        '2xl': '1rem',
        '3xl': '1.5rem',
      },

      // ── Animations ─────────────────────────────────────────
      keyframes: {
        'fade-in': {
          '0%': { opacity: '0', transform: 'translateY(8px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        'slide-in-left': {
          '0%': { opacity: '0', transform: 'translateX(-16px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        },
        'pulse-slow': {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.5' },
        },
        'shimmer': {
          '0%': { backgroundPosition: '-200% 0' },
          '100%': { backgroundPosition: '200% 0' },
        },
        'typing': {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0' },
        },
      },
      animation: {
        'fade-in':      'fade-in 0.3s ease-out',
        'slide-in-left':'slide-in-left 0.3s ease-out',
        'pulse-slow':   'pulse-slow 2s ease-in-out infinite',
        'shimmer':      'shimmer 2s linear infinite',
        'typing':       'typing 1s ease-in-out infinite',
      },

      // ── Box Shadow ─────────────────────────────────────────
      boxShadow: {
        'glow-brand': '0 0 20px rgba(99, 102, 241, 0.3)',
        'glow-cyan':  '0 0 20px rgba(6, 182, 212, 0.3)',
        'card':       '0 4px 24px rgba(0, 0, 0, 0.4)',
        'inner-glow': 'inset 0 1px 0 rgba(255, 255, 255, 0.05)',
      },

      // ── Backdrop Blur ──────────────────────────────────────
      backdropBlur: {
        xs: '2px',
      },
    },
  },

  plugins: [],
}
