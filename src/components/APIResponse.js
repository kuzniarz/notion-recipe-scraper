import React, { useState, useEffect } from 'react';

function ApiResponse() {
    const [data, setData] = useState(null);
  
    useEffect(() => {
      fetch('https://jsonplaceholder.typicode.com/todos/1') // TODO: This is just a placeholder
        .then(response => response.json())
        .then(json => setData(json))
        .catch(error => console.error(error));
    }, []);
  
    return (
      <div className="apiResponse">{data ? <pre>{JSON.stringify(data, null, 2)}</pre> : 'Loading...'}</div>
    );
  }

  export default ApiResponse;