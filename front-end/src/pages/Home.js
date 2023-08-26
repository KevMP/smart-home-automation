import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';

import { Link } from 'react-router-dom';

function Home() {
  return (
    <Container className="mt-5 justify-content-center align-items-center">
        <h1 className="text-center mb-4">Smart Home Dashboard</h1>
        <Row className="mb-3">
            <Col md={4}>
                <Button variant="primary">Toggle Lights</Button>
            </Col>
            <Col md={4}>
                <Button variant="secondary">Adjust Thermostat</Button>
            </Col>
            <Col md={4}>
              <Link to='/view-data'>
                <Button variant="danger">View Data</Button>
              </Link>
            </Col>
        </Row>
    </Container>
  );
}

export default Home;