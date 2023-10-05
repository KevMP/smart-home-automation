import React, { useState, useEffect } from 'react';
import { Button, Container } from 'react-bootstrap';
import axios from 'axios';

const Dashboard = () => {
  const [data, setData] = useState({ ac_status: false, temp: ''});
  const [isFetching, setIsFetching] = useState(true);

  useEffect(() => {
    const fetchData = () => {
        // Only fetch if isFetching is true
        if (isFetching) {
            axios.get('/api/v1/dashboard')
                .then(response => {
                    console.log(response.data.temp);
                    setData(response.data);
                })
                .catch(error => {
                    console.error("Error fetching data: ", error);
                });
        }
    };

    fetchData(); // Fetch immediately

    const interval = setInterval(fetchData, 5000);

    return () => clearInterval(interval);  // Cleanup on unmount

}, [isFetching]);  // React on isFetching changes


  return (
    <>
      <Container fluid style={{ 
          display: 'flex', 
          flexDirection: 'column', 
          minHeight: '100vh', 
          margin: '0', 
          padding: '0'
      }}>
        <div style={{ 
            flex: '1', 
            display: 'flex', 
            flexDirection: 'column', 
            justifyContent: 'center', 
            alignItems: 'center'
        }}>
          <div className='d-flex align-items-center'>
              <div className={`text-center bg-${data.ac_status ? 'success' : 'danger'} bg-gradient text-white rounded-3 p-3 h2`}>
                  <i className="bi bi-thermometer-snow"></i>
              </div>
              
              <div className='d-flex flex-column align-items-start ms-4'>
                  <div className="d-flex align-items-center">
                      <p className='lh-sm text-center'>AC is:</p>
                      <p className={`lh-sm ${data.ac_status ? 'text-success' : 'text-danger'} ms-3`}>{data.ac_status ? 'ON' : 'OFF'}</p>
                  </div>
                  <div className="d-flex align-items-center">
                      <p className='lh-sm text-center'>AC Temp:</p>
                      <p className=' ms-3'>{data.temp}°C</p>
                  </div>
              </div>
          </div>
          <div>
          <Button variant="primary" size="lg" onClick={() => setIsFetching(prevState => !prevState)}>
            {isFetching ? 'Pause Fetching' : 'Resume Fetching'}
          </Button>
          </div>
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
    </>
  );
};

export default Dashboard;
