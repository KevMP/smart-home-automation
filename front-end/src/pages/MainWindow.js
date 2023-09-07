import React from 'react';
import { Button, Container } from 'react-bootstrap';
import Header from '../components/nav';
import Footer from '../components/footer'; 

const MainWindow = () => {
  return (
    <>
      <Container fluid style={{ 
          display: 'flex', 
          flexDirection: 'column', 
          minHeight: '100vh', 
          margin: '0', 
          padding: '0'
      }}>
        <Header />  {/* Include Header component here */}
        <div style={{ 
            flex: '1', 
            display: 'flex', 
            flexDirection: 'column', 
            justifyContent: 'center', 
            alignItems: 'center'
        }}>
          <h2 style={{ color: '#0056b3', fontSize: '36px', marginBottom: '30px' }}>Main Window</h2>
          <div style={{
            width: '40%',  
            textAlign: 'center',
            border: '1px solid #ccc',  
            boxShadow: '0px 4px 8px rgba(0,0,0,0.1)',  
            padding: '20px',
            borderRadius: '10px'  
          }}>
            <div style={{ marginBottom: '20px' }}>
              <Button variant="primary" size="lg" style={{ minHeight: '60px', width: '100%' }} href='/dashboard'>Dashboard</Button>
            </div>
            <div style={{ marginBottom: '20px' }}>
              <Button variant="primary" size="lg" style={{ minHeight: '60px', width: '100%' }} href='/temp' >Temperature Control</Button>
            </div>
            <div style={{ marginBottom: '20px' }}>
              <Button variant="primary" size="lg" style={{ minHeight: '60px', width: '100%' }} href='/settings' >Occupancy Settings</Button>
            </div>
            <div style={{ marginBottom: '20px' }}>
              <Button variant="primary" size="lg" style={{ minHeight: '60px', width: '100%' }} href='/help' >Help & Support</Button>
            </div>
          </div>
        </div>
      </Container>
      <div style={{ height: '100px' }}> {/* Fixed height for the footer */}
        <Footer />  {/* Include Footer component here */}
      </div>
    </>
  );
};

export default MainWindow;
