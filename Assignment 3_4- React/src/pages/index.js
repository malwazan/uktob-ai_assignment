import Image from 'next/image'
import { Inter } from 'next/font/google'
import Link from 'next/link';

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div class="h-screen flex flex-col justify-center">
        <div class="flex justify-center mb-5">
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            <Link href="/simple-form">
              Assignment 3 - Simple Form
            </Link>
          </button>
        </div>
        <div class="flex justify-center">
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            <Link href="/todo">
              Assignment 4 - Todo App
            </Link>
          </button>
        </div>
      </div>
    </main>
  )
}
