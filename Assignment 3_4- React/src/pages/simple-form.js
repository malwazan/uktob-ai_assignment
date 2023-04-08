import { useState } from 'react'

function SimpleForm() {
  const [text, setText] = useState('')
  const [count, setCount] = useState('')
  const [errors, setErrors] = useState({})
  const [message, setMessage] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    const validationErrors = {}

    // Validate text input
    if (!text.trim()) {
      validationErrors.text = 'Text is required'
    }

    // Validate age input
    if (!count.trim()) {
      validationErrors.count = 'Count is required'
    } else if (isNaN(Number(count))) {
      validationErrors.count = 'Count must be a number'
    } else if (Number(count) < 0 || Number(count) > 120) {
      validationErrors.count = 'count must be between 0 and 120'
    }

    if (Object.keys(validationErrors).length) {
      setErrors(validationErrors)
    } else {
      // Form is valid
      setErrors(validationErrors)
      let resp = text.repeat(count)
      setMessage(resp)
    }
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <form onSubmit={handleSubmit} className="w-full max-w-sm mx-auto">

        {/* Text Input */}
        <div className="mb-4">
          <label htmlFor="text" className="block text-gray-700 font-bold mb-2">
            Enter Text
          </label>
          <input
            type="text"
            id="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            className={`appearance-none border ${
              errors.text ? 'border-red-500' : 'border-gray-200'
            } rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline`}
          />
          {errors.text && <p className="text-red-500 text-xs italic">{errors.text}</p>}
        </div>

        {/* Count Input */}
        <div className="mb-4">
          <label htmlFor="count" className="block text-gray-700 font-bold mb-2">
            Enter Count
          </label>
          <input
            type="number"
            id="count"
            value={count}
            onChange={(e) => setCount(e.target.value)}
            className={`appearance-none border ${
              errors.count ? 'border-red-500' : 'border-gray-200'
            } rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline`}
          />
          {errors.count && <p className="text-red-500 text-xs italic">{errors.count}</p>}
        </div>

        {/* Submit Button */}
        <div className="flex items-center justify-center">
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Submit
          </button>
        </div>
      </form>

      {/* Text Area */}
      <textarea readOnly="true"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        className="bg-slate-200 mt-4 appearance-none border border-gray-200 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        placeholder="Response..."
        rows="5"
      />
    </main>
  )
}

export default SimpleForm
