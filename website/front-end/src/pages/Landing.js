import React from 'react'
import { Container, Row, Col, Button } from 'react-bootstrap'

function Landing () {
  return (
        <Container fluid style={{ height: '100vh', backgroundColor: '#F2F4F8' }}>
            <Row className="justify-content-center align-items-center h-100">
                <Col xs={12} md={6}>
                    <h1 style={{ color: 'rgb(9, 69, 120)' }}>Welcome to Our AI Home Efficiency Solution</h1>
                    <p style={{ fontSize: '18px', color: '#555' }}>
                        Leveraging the power of artificial intelligence, we aim to make homes smarter, more efficient, and eco-friendly. Dive in to explore the future of smart living.
                    </p>
                    <Button style={{ backgroundColor: 'rgb(9, 69, 120)', borderColor: 'rgb(9, 69, 120)' }}>Learn More</Button>
                </Col>
                <Col xs={12} md={6}>
                    <div style={{ width: '100%', height: '300px', backgroundColor: 'rgba(9, 69, 120, 0.1)' }}>
                        Image/GFX Here
                    </div>
                </Col>
            </Row>
        </Container>
  )
}

export default Landing
