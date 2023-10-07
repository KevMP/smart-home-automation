import React, { useState } from 'react'
import { Col, Button, Modal, Table } from 'react-bootstrap'

function AIComponent ({ openConfirmation }) {
  const [showModal, setShowModal] = useState(false)

  // Sample data for the modal display. This would be dynamically fetched in a real app scenario.
  const aiData = {
    occupancy: 'Yes',
    temperature: '72°F',
    humidity: '45%',
    acStatus: 'On'
  }

  return (
        <>
            <Col xs={12} md={4} className="mb-4">
                <div className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
                    <h3 className="text-white text-center mb-4">AI Dashboard</h3>
                    <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={() => { /* Train function here */ }}>Train</Button>
                    <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'red', borderColor: 'red' }} onClick={() => openConfirmation('eraseMemory')}>Erase Memory</Button>
                    <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={() => setShowModal(true)}>Display Data</Button>
                </div>
            </Col>

            <Modal show={showModal} onHide={() => setShowModal(false)} centered>
                <Modal.Header closeButton>
                    <Modal.Title>AI Data</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Table striped bordered hover variant="dark">
                        <tbody>
                            <tr>
                                <td>Occupancy</td>
                                <td>{aiData.occupancy}</td>
                            </tr>
                            <tr>
                                <td>Temperature</td>
                                <td>{aiData.temperature}</td>
                            </tr>
                            <tr>
                                <td>Humidity</td>
                                <td>{aiData.humidity}</td>
                            </tr>
                            <tr>
                                <td>AC Status</td>
                                <td>{aiData.acStatus}</td>
                            </tr>
                        </tbody>
                    </Table>
                </Modal.Body>
            </Modal>
        </>
  )
}

export default AIComponent
