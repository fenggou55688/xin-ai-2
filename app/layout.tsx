// app/layout.tsx
import '../styles/globals.css'; // 確保有這一行！

export const metadata = {
  title: 'Your App Title',
  description: 'Your description here',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
