/**
 * InsightHub AI — Global State Store (Zustand)
 * Manages app-wide state: documents, chat sessions, UI state.
 */
import { create } from 'zustand'
import { devtools } from 'zustand/middleware'

const useAppStore = create(
  devtools(
    (set, get) => ({
      // ── Documents ───────────────────────────────────────────
      documents: [],           // List of uploaded documents
      setDocuments: (docs) => set({ documents: docs }),
      addDocument: (doc) => set((state) => ({ documents: [...state.documents, doc] })),
      removeDocument: (id) =>
        set((state) => ({ documents: state.documents.filter((d) => d.document_id !== id) })),

      // ── Chat Sessions ───────────────────────────────────────
      sessions: [],            // List of chat sessions
      activeSessionId: null,   // Currently open session
      setActiveSession: (id) => set({ activeSessionId: id }),
      addSession: (session) => set((state) => ({ sessions: [...state.sessions, session] })),

      // ── Chat Messages ───────────────────────────────────────
      messages: [],            // Messages in the active session
      setMessages: (msgs) => set({ messages: msgs }),
      addMessage: (msg) => set((state) => ({ messages: [...state.messages, msg] })),
      clearMessages: () => set({ messages: [] }),

      // ── UI State ────────────────────────────────────────────
      sidebarOpen: true,
      toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
      isStreaming: false,
      setIsStreaming: (v) => set({ isStreaming: v }),
      isUploading: false,
      setIsUploading: (v) => set({ isUploading: v }),
    }),
    { name: 'InsightHubStore' }
  )
)

export default useAppStore
