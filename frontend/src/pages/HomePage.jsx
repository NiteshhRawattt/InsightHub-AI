/**
 * InsightHub AI — Home Page
 * Landing / welcome screen. Full UI implemented in next phase.
 */
function HomePage() {
  return (
    <div className="min-h-screen bg-surface-900 flex items-center justify-center">
      <div className="text-center space-y-4 animate-fade-in">
        {/* Logo / Icon */}
        <div className="flex justify-center">
          <div className="w-20 h-20 rounded-3xl bg-gradient-to-br from-brand-500 to-accent-purple flex items-center justify-center shadow-glow-brand">
            <span className="text-4xl">🧠</span>
          </div>
        </div>

        {/* Heading */}
        <h1 className="text-5xl font-bold gradient-text">InsightHub AI</h1>
        <p className="text-gray-400 text-lg max-w-md mx-auto">
          Your AI-powered research assistant. Upload documents and chat with your knowledge.
        </p>

        {/* CTA */}
        <div className="pt-4">
          <a href="/chat" className="btn-primary text-base px-6 py-3">
            Get Started →
          </a>
        </div>

        {/* Status badge */}
        <p className="text-surface-500 text-xs pt-8">
          🚧 Foundation phase — features coming soon
        </p>
      </div>
    </div>
  )
}

export default HomePage
