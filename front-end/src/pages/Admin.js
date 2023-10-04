import React, { useState } from 'react';
import { Container, Col, Button } from 'react-bootstrap';
import axios from 'axios';

function Admin() {
    const [hoveredButton, setHoveredButton] = useState(null);

    const trainAI = async () => {
        try {
            const response = await axios.post('/api/v1/train');
            console.log('Training response:', response.data);
        } catch (error) {
            console.error('Error training AI:', error);
        }
    };

    return (
        <Container fluid style={{ height: '100vh', backgroundColor: '#F2F4F8' }} className="d-flex align-items-center justify-content-center">
            <Col xs={12} md={6} className="text-center">
                <h1 className="mb-4" style={{ color: 'rgb(9, 69, 120)', borderBottom: '2px solid rgb(9, 69, 120)', paddingBottom: '10px' }}>AI Training Dashboard</h1>
                <Button 
                    className={`mb-2 ${hoveredButton === 'fill' && 'active'}`} 
                    onMouseEnter={() => setHoveredButton('fill')}
                    onMouseLeave={() => setHoveredButton(null)}
                    style={{ backgroundColor: 'rgb(9, 69, 120)', borderColor: 'rgb(9, 69, 120)' }}
                >
                    Fill Up Database
                </Button>
                <br />
                <Button 
                    className={`mb-2 ${hoveredButton === 'clearDB' && 'active'}`} 
                    onMouseEnter={() => setHoveredButton('clearDB')}
                    onMouseLeave={() => setHoveredButton(null)}
                    style={{ backgroundColor: 'rgb(9, 69, 120)', borderColor: 'rgb(9, 69, 120)' }}
                >
                    Clear Database
                </Button>
                <br />
                <Button 
                    className={`mb-2 ${hoveredButton === 'clearMem' && 'active'}`} 
                    onMouseEnter={() => setHoveredButton('clearMem')}
                    onMouseLeave={() => setHoveredButton(null)}
                    style={{ backgroundColor: 'rgb(9, 69, 120)', borderColor: 'rgb(9, 69, 120)' }}
                >
                    Clear Memory
                </Button>
                <br />
                <Button 
                    className="mb-2" 
                    style={{ backgroundColor: 'rgb(9, 69, 120)', borderColor: 'rgb(9, 69, 120)' }}
                    onClick={trainAI}
                >
                    Train
                </Button>
            </Col>
        </Container>
    );
}

export default Admin;
