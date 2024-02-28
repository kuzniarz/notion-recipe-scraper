import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        In case you need help, look into the 
        <div
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          React Documentation
        </div>
      </header>
      <ApiResponse />
    </div>
  );
}

function ApiResponse() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(json => setData(json))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="apiResponse">{data ? <pre>{JSON.stringify(data, null, 2)}</pre> : 'Loading...'}</div>
  );
}

export default App;
