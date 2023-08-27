import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';

const Header = () => {
  return (
    <Navbar style={{ 
        backgroundColor: '#f2f2f2', 
        borderBottom: '2px solid #0056b3', 
        boxShadow: '0px 2px 5px rgba(0,0,0,0.1)',
        paddingLeft: '20px'  // Added left padding
    }}>
      <Navbar.Brand href="#home" style={{ 
          color: '#0056b3', 
          fontWeight: 'bold',
          fontSize: '24px'
      }}>
        Smart Home Automation
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="#home" style={{ 
              color: '#0056b3',
              fontSize: '18px'
          }}>
            Home
          </Nav.Link>
          <Nav.Link href="#features" style={{ color: '#0056b3', fontSize: '18px' }}>Features</Nav.Link>
          <Nav.Link href="#pricing" style={{ color: '#0056b3', fontSize: '18px' }}>Pricing</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};



export default Header;
