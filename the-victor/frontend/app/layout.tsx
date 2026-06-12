import type { Metadata } from 'next';
import { Inter, Space_Grotesk } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' });
const spaceGrotesk = Space_Grotesk({ subsets: ['latin'], variable: '--font-space-grotesk', weight: ['500', '600', '700'] });

export const metadata: Metadata = {
  title: 'The Victor - AI Web Builder',
  description: 'The most intelligent AI Web Builder by CEO',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="th" className="dark">
      <body className={`${inter.variable} ${spaceGrotesk.variable} bg-[#0a0a0f] text-white antialiased`}>
        {children}
      </body>
    </html>
  );
}