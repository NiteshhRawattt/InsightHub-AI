import { Routes, Route } from 'react-router-dom'
import HomePage from '@/pages/HomePage'
import ChatPage from '@/pages/ChatPage'

/**
 * App — Root component with route definitions.
 * Add new routes here as features are built.
 */
function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/chat" element={<ChatPage />} />
      <Route path="/chat/:sessionId" element={<ChatPage />} />
    </Routes>
  )
}

export default App
