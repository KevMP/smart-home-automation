import React from 'react';
import { Form, Button, Row, Col } from 'react-bootstrap';
import Footer from '../components/common/footer';  // Make sure the path is correct

const Login = () => {
  document.body.style.overflowX = 'hidden';

  return (
    <div fluid style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <div style={{ flex: '1' }}>
        <Row className="justify-content-md-center" style={{ marginTop: '5%' }}>
          <Col xs lg="6">
            <h2 style={{ color: '#0056b3', marginBottom: '20px', textAlign: 'center', fontSize: '36px' }}>Login</h2>
            <Form>
              <Form.Group controlId="username">
                <Form.Label style={{ fontSize: '24px' }}>Username</Form.Label>
                <Form.Control type="text" placeholder="Enter username" style={{ fontSize: '18px' }} />
              </Form.Group>

              <Form.Group controlId="password">
                <Form.Label style={{ fontSize: '24px' }}>Password</Form.Label>
                <Form.Control type="password" placeholder="Password" style={{ fontSize: '18px' }} />
              </Form.Group>

              <Form.Group controlId="mfa">
                <Form.Check type="checkbox" label="Enable Multi-Factor Authentication" style={{ fontSize: '18px' }} />
              </Form.Group>

              <div style={{ textAlign: 'center' }}>
                <Button variant="primary" type="submit" style={{ fontSize: '18px' }}>
                  Login
                </Button>
              </div>
            </Form>
          </Col>
        </Row>
      </div>
      <Footer />
    </div>
  );
};

export default Login;
