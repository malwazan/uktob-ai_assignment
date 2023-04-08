import React, { useState } from 'react';
import TodoForm from '../components/TodoForm';
import TodoList from '../components/TodoList';

function Todo() {
  const [todos, setTodos] = useState([]);

  const handleAddTodo = (text) => {
    setTodos((prevTodos) => [...prevTodos, { text }]);
  };

  const handleUpdateTodo = (index, text) => {
    setTodos((prevTodos) => {
      const updatedTodos = [...prevTodos];
      updatedTodos[index].text = text;
      return updatedTodos;
    });
  };

  const handleDeleteTodo = (index) => {
    setTodos((prevTodos) => {
      const updatedTodos = [...prevTodos];
      updatedTodos.splice(index, 1);
      return updatedTodos;
    });
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
        <div className="max-w-2xl mx-auto px-4">
            <h1 className="text-2xl font-bold mb-4">My Assignmnet Todos</h1>
            <hr class="h-px my-8 bg-black border-0 dark:bg-gray-700" />
            <TodoForm onSubmit={handleAddTodo} />
            <TodoList todos={todos} onDelete={handleDeleteTodo} />
        </div>
    </main>
  );
}

export default Todo;
