import React from 'react'
import { Card, Col } from 'react-bootstrap'
import { BiSolidThermometer } from 'react-icons/bi' // Thermometer icon
import { MdOpacity } from 'react-icons/md' // Icons for temperature and humidity

function ACStatusCard ({ currentTemperature, currentHumidity, acStatus }) {
  return (
        <Col xs={12} md={4} className="mb-4">
            <Card className="shadow" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
                <Card.Body>
                    <Card.Title className="text-white text-center">AC Status</Card.Title>

                    <div className="d-flex align-items-center justify-content-between mb-3">
                        <div className="d-flex align-items-center">
                            <BiSolidThermometer className="text-white me-2" />
                            <Card.Text className="text-white mb-0">
                                Temperature: {currentTemperature}°
                            </Card.Text>
                        </div>

                        <div className={`text-center bg-${acStatus ? 'success' : 'danger'} bg-gradient text-white rounded-3 p-2`}>
                            <span>{acStatus ? 'ON' : 'OFF'}</span>
                        </div>
                    </div>

                    <div className="d-flex align-items-center">
                        <MdOpacity className="text-white me-2" />
                        <Card.Text className="text-white mb-0">
                            Humidity: {currentHumidity}%
                        </Card.Text>
                    </div>
                </Card.Body>
            </Card>
        </Col>
  )
}

export default ACStatusCard
