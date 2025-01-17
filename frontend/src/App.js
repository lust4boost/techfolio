import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [message, setMessage] = useState(''); // State to store the API response

    // Fetch data from the backend when the component loads
    useEffect(() => {
        axios.get('http://127.0.0.1:5000/api/test') // URL of the Flask endpoint
            .then(response => {
                setMessage(response.data.message); // Update the state with the response message
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []); // Empty dependency array ensures this runs only once when the component mounts

    return (
        <div>
            <h1>Welcome to Techfolio.ai</h1>
            <p>Backend says: {message}</p> {/* Display the message from the backend */}
        </div>
    );
}

export default App;

