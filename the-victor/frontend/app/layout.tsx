import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'The Victor | AI Web Builder',
  description: 'The most intelligent AI Web Builder for CEOs. Built by Victor.',
  icons: {
    icon: '/favicon.ico',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="th">
      <body className="bg-[#0a0a0f] text-white antialiased">
        {children}
      </body>
    </html>
  )
}
