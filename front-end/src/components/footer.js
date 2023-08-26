import React from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import { FaFacebook, FaTwitter, FaInstagram } from 'react-icons/fa';

const Footer = () => {
  return (
    <Container fluid style={{ backgroundColor: '#0056b3', color: '#ffffff', padding: '30px' }}>
      <Row>
        <Col md={4}>
          <h5>About Us</h5>
          <p>Smart Home Automation System enhances your lifestyle with automated solutions for your home.</p>
        </Col>
        <Col md={4}>
          <h5>Quick Links</h5>
          <ul style={{ listStyle: 'none', paddingLeft: '0' }}>
            <li><a href="#" style={{ color: '#ffffff', textDecoration: 'none' }}>Home</a></li>
            <li><a href="#" style={{ color: '#ffffff', textDecoration: 'none' }}>Features</a></li>
            <li><a href="#" style={{ color: '#ffffff', textDecoration: 'none' }}>Contact</a></li>
          </ul>
        </Col>
        <Col md={4}>
          <h5>Subscribe</h5>
          <Form inline>
            <Form.Control type="email" placeholder="Email" style={{ marginRight: '10px' }} />
            <Button variant="secondary">Subscribe</Button>
          </Form>
          <div style={{ marginTop: '20px' }}>
            <FaFacebook style={{ margin: '5px' }} />
            <FaTwitter style={{ margin: '5px' }} />
            <FaInstagram style={{ margin: '5px' }} />
          </div>
        </Col>
      </Row>
      <Row style={{ marginTop: '20px' }}>
        <Col md={12} style={{ textAlign: 'center' }}>
          <small>© 2023 Miami Dade College. All rights reserved.</small>
        </Col>
      </Row>
    </Container>
  );
};

export default Footer;
