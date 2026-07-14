/**
 * InsightHub AI — Chat Page
 * Main chat interface. Full implementation in next phase.
 */
function ChatPage() {
  return (
    <div className="min-h-screen bg-surface-900 flex items-center justify-center">
      <div className="text-center space-y-3 animate-fade-in">
        <div className="w-16 h-16 rounded-2xl bg-surface-700 border border-surface-500 flex items-center justify-center mx-auto">
          <span className="text-3xl">💬</span>
        </div>
        <h2 className="text-2xl font-semibold text-white">Chat Interface</h2>
        <p className="text-gray-500 text-sm">
          Full chat UI — implemented in the next phase.
        </p>
        <a href="/" className="btn-ghost text-sm">
          ← Back to Home
        </a>
      </div>
    </div>
  )
}

export default ChatPage
