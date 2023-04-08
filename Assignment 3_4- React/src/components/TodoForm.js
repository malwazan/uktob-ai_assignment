import React, { useState } from 'react';

function TodoForm({ onSubmit }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!text.trim()) {
        alert("Error: Please enter todo text!")
        return
    }

    onSubmit(text);
    setText('');
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <div className="flex items-center">
        <label htmlFor="todo-input" className="mr-2">
          Enter a todo:
        </label>
        <input
          type="text"
          id="todo-input"
          value={text}
          onChange={(e) => setText(e.target.value)}
          className="border rounded py-2 px-3 mr-2"
        />
        <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Add
        </button>
      </div>
    </form>
  );
}

export default TodoForm;

