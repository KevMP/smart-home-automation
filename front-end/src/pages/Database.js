import React, { useState, useEffect } from 'react';
import { Container } from 'react-bootstrap';
import axios from 'axios';

function Database() {
    const [data, setData] = useState(null);
    // const [error, setError] = useState(null);

    useEffect(() => {
        // Replace this URL with your database's API endpoint
        axios.get('/api/v1/view-data')
            .then(response => {
                setData(response.data);
            })
            .catch(error => {
                console.log(error);
                // setError(error);
            });
    }, []);

    return (
        <Container className="mt-5 justify-content-center align-items-center">
            <h1 className="text-center mb-4">Data from Database</h1>

            {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
        
        </Container>
    );
}

export default Database;