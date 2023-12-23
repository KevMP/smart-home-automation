import React from 'react'
import { Card, Col } from 'react-bootstrap'
import { BiSolidThermometer } from 'react-icons/bi'
import { MdOpacity } from 'react-icons/md'

function ACStatusCard ({ formData }) {
  return (
        <Col xs={12} md={4} className="mb-4">
            <Card className="shadow" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
                <Card.Body>
                    <Card.Title className="text-white text-center">AC Status</Card.Title>

                    <div className="d-flex align-items-center justify-content-between mb-3">
                        <div className="d-flex align-items-center">
                            <BiSolidThermometer className="text-white me-2" />
                            <Card.Text className="text-white mb-0">
                                Temperature: {formData.temperature}°
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
  )
}

export default ACStatusCard
