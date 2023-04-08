import React from 'react';

function TodoList({ todos, onDelete }) {

  return (
    <ul className="divide-y divide-gray-300">
      {todos.map((todo, index) => (
        <li key={index} className="flex items-center py-4">
          <input
            type="text" readOnly="true"
            value={todo.text}
            className="border-b-2 border-gray-300 py-2 px-3 mr-4 w-full bg-gray-300"
          />
          <button
            onClick={() => onDelete(index)}
            className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
            Delete
          </button>
        </li>
      ))}
    </ul>
  );
}

export default TodoList;
