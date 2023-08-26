import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';

function Home() {
  return (
    <Container className="mt-5 justify-content-center align-items-center">
        <h1 className="text-center mb-4">Smart Home Dashboard</h1>

        <Row className="mb-3">
            <Col md={4}>
                <Button variant="primary" block>Toggle Lights</Button>
            </Col>
            <Col md={4}>
                <Button variant="secondary" block>Adjust Thermostat</Button>
            </Col>
            <Col md={4}>
                <Button variant="danger" block>Settings</Button>
            </Col>
        </Row>

    </Container>
  );
}

export default Home;