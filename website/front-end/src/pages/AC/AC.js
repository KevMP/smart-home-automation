import React, { useEffect, useState } from 'react'
import { Container, Row, Col, Card, Button, Form } from 'react-bootstrap'
import { BiSolidThermometer } from 'react-icons/bi'
import { MdWbSunny, MdOpacity } from 'react-icons/md'
import axios from 'axios'

function CombinedACComponent () {
  const [formData, setFormData] = useState({
    max_temp: 0,
    min_temp: 0,
    max_humidity: 0,
    min_humidity: 0,
    max_occupancy: 0,
    occupancy: 0,
    is_celsius: false,
    ac_status: false,
    humidity: 0,
    temperature: 0
  })

  useEffect(() => {
    (async () => {
      try {
        axios.get('http://localhost:3001/api/v1/ac')
          .then(response => {
            setFormData(response.data)
          })
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    })()
  }, [])

  const handleSave = () => {
    axios.post('http://localhost:3001/api/AC', formData)
      .then(response => {
        alert('Settings saved successfully!')
      })
      .catch(error => {
        console.error('Error saving settings:', error)
        alert('Error saving settings.')
      })
  }

  function convertTemperature (value, isCelsius) {
    const numericValue = parseFloat(value)
    console.log(numericValue)
    return parseFloat(isCelsius ? ((numericValue - 32) * 5) / 9 : ((numericValue * 9) / 5) + 32).toFixed(2)
  }

  const handleSwitch = () => {
    const isCelsius = !formData.is_celsius
    const updatedFormData = {
      ...formData,
      is_celsius: isCelsius,
      temperature: convertTemperature(formData.temperature, isCelsius),
      max_temp: convertTemperature(formData.max_temp, isCelsius),
      min_temp: convertTemperature(formData.min_temp, isCelsius)
    }

    setFormData(updatedFormData)
  }

  return (
    <Container fluid>
       <Row className="justify-content-center align-items-center">
          <Col xs={12} md={4} className="mb-4">
              <Card className="shadow" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
                  <Card.Body>
                      <Card.Title className="text-white text-center">AC Status</Card.Title>

                      <div className="d-flex align-items-center justify-content-between mb-3">
                          <div className="d-flex align-items-center">
                              <BiSolidThermometer className="text-white me-2" />
                              <Card.Text className="text-white mb-0">
                                  Temperature: {formData.is_celsius ? `${formData.temperature}°C` : `${formData.temperature}°F`}
                              </Card.Text>
                          </div>

                          <div className={`text-center bg-${formData.ac_status ? 'success' : 'danger'} bg-gradient text-white rounded-3 p-2`}>
                              <span>{formData.ac_status ? 'ON' : 'OFF'}</span>
                          </div>
                      </div>

                      <div className="d-flex align-items-center">
                          <MdOpacity className="text-white me-2" />
                          <Card.Text className="text-white mb-0">
                              Humidity: {formData.humidity}%
                          </Card.Text>
                      </div>
                  </Card.Body>
              </Card>
        </Col>

          <Col xs={12} md={4} className="mb-4 mt-5">
            <div className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
                <h3 className="text-white text-center mb-4">AC Controls</h3>

                <div className="d-flex align-items-center mb-4">
                    <div className={`text-center bg-${formData.ac_status ? 'success' : 'danger'} bg-gradient text-white rounded-3 p-3 h2`}>
                        <BiSolidThermometer />
                    </div>
                    <div className="d-flex flex-column align-items-start ms-4">
                        <div className="d-flex align-items-center">
                            <MdWbSunny className="text-white me-2" />
                            <p className='text-white lh-sm text-center'>Temperature: </p>
                            <p className='text-white ms-3'>{formData.is_celsius ? `${parseFloat(formData.min_temp).toFixed(2)}°C - ${parseFloat(formData.max_temp).toFixed(2)}°C` : `${parseFloat(formData.min_temp).toFixed(2)}°F - ${parseFloat(formData.max_temp).toFixed(2)}°F`}</p>
                        </div>
                        <div className="d-flex align-items-center">
                            <MdOpacity className="text-white me-2" />
                            <p className='text-white lh-sm text-center'>Humidity:</p>
                            <p className='text-white ms-3'>{`${formData.min_humidity}% - ${formData.max_humidity}%`}</p>
                        </div>
                    </div>
                </div>

                <Button onClick={handleSwitch} variant="dark" className="mb-3">{formData.is_celsius ? 'Switch to °F' : 'Switch to °C'}</Button>

                <div className="d-flex justify-content-between align-items-center mb-3">
                    <Form.Range
                        value={formData.min_temp}
                        min={formData.is_celsius ? 0 : 32}
                        step={0.01}
                        max={formData.is_celsius ? 40 : 104}
                        onChange={(e) => setFormData({ ...formData, min_temp: parseFloat(e.target.value) })}
                    />
                    <Form.Range
                        value={formData.max_temp}
                        min={formData.is_celsius ? 0 : 32}
                        max={formData.is_celsius ? 40 : 104}
                        onChange={(e) => setFormData({ ...formData, max_temp: parseFloat(e.target.value) })}
                    />
                </div>

                <div className="d-flex justify-content-between align-items-center mb-3">
                    <Form.Range
                        value={formData.min_humidity}
                        min={0}
                        step={0.01}
                        max={100}
                        onChange={(e) => setFormData({ ...formData, min_humidity: parseInt(e.target.value) })}
                    />
                    <Form.Range
                        value={formData.max_humidity}
                        min={0}
                        max={100}
                        onChange={(e) => setFormData({ ...formData, max_humidity: parseInt(e.target.value) })}
                    />
                </div>

                <label className="text-white d-block mb-2">Occupancy Max: {formData.max_occupancy}</label>
                    <Form.Range
                      value={formData.max_occupancy}
                      min={0}
                      max={100}
                      onChange={(e) => setFormData({ ...formData, max_occupancy: parseInt(e.target.value) })}
                      />
                <div>
                    <Button variant="primary" className="mb-3 mt-5" onClick={handleSave}>Save Settings</Button>
                </div>
            </div>
        </Col>
      </Row>
    </Container>
  )
}

export default CombinedACComponent
