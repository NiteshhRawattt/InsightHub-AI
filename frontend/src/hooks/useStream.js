/**
 * InsightHub AI — useStream Hook
 * Custom hook for consuming Server-Sent Events (SSE) streaming responses.
 * Full implementation in next phase.
 */
import { useCallback, useRef } from 'react'

/**
 * useStream — consumes an SSE endpoint and appends chunks to state.
 *
 * @param {Function} onChunk   — called with each new text chunk
 * @param {Function} onDone    — called when the stream closes
 * @param {Function} onError   — called on stream error
 */
export function useStream({ onChunk, onDone, onError }) {
  const sourceRef = useRef(null)

  const startStream = useCallback((url) => {
    // TODO: Implement EventSource SSE connection
    // sourceRef.current = new EventSource(url)
    // sourceRef.current.onmessage = (e) => { ... }
    // sourceRef.current.onerror   = (e) => { ... }
    console.log('[useStream] Stream started (stub):', url)
  }, [])

  const stopStream = useCallback(() => {
    if (sourceRef.current) {
      sourceRef.current.close()
      sourceRef.current = null
    }
  }, [])

  return { startStream, stopStream }
}

export default useStream
