/**
 * InsightHub AI — Utility Functions
 */

/**
 * Format a file size in bytes to a human-readable string.
 * @param {number} bytes
 * @returns {string}  e.g. "2.4 MB"
 */
export function formatFileSize(bytes) {
  if (bytes === 0) return '0 B'
  const k = 1024
  const sizes = ['B', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(1))} ${sizes[i]}`
}

/**
 * Format a Date or ISO string to a relative time string.
 * @param {Date|string} date
 * @returns {string}  e.g. "2 minutes ago"
 */
export function formatRelativeTime(date) {
  const now = new Date()
  const then = new Date(date)
  const diffMs = now - then
  const diffSec = Math.floor(diffMs / 1000)
  const diffMin = Math.floor(diffSec / 60)
  const diffHr = Math.floor(diffMin / 60)

  if (diffSec < 60) return 'just now'
  if (diffMin < 60) return `${diffMin}m ago`
  if (diffHr < 24) return `${diffHr}h ago`
  return then.toLocaleDateString()
}

/**
 * Get the file extension from a filename.
 * @param {string} filename
 * @returns {string}  e.g. "pdf"
 */
export function getFileExtension(filename) {
  return filename.split('.').pop()?.toLowerCase() || ''
}

/**
 * Truncate a string to a max length with ellipsis.
 * @param {string} str
 * @param {number} max
 * @returns {string}
 */
export function truncate(str, max = 50) {
  return str.length > max ? str.slice(0, max) + '…' : str
}

/**
 * Generate a random UUID v4.
 * @returns {string}
 */
export function generateId() {
  return crypto.randomUUID()
}
