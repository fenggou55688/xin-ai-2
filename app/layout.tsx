import '../styles/globals.css'; // << 加這行！

export const metadata = {
  title: 'Xin AI',
  description: 'Generated by ChatGPT',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
