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
      <Navbar.Brand href="/" style={{ 
          color: '#0056b3', 
          fontWeight: 'bold',
          fontSize: '24px'
      }}>
        Smart Home Automation
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="/dashboard" style={{ 
              color: '#0056b3',
              fontSize: '18px'
          }}>
            Home
          </Nav.Link>
          <Nav.Link href="/login" style={{ color: '#0056b3', fontSize: '18px' }}>Login</Nav.Link>
          <Nav.Link href="/admin" style={{ color: '#0056b3', fontSize: '18px' }}>Admin</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};



export default Header;
