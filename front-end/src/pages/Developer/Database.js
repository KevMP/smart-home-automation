import React, { useState } from 'react'
import { Button, Modal, Table, Col } from 'react-bootstrap'

function DatabaseComponent ({ openConfirmation }) {
  const [showModal, setShowModal] = useState(false)

  const dbData = [
    { id: 1, name: 'Data 1', value: 'Value A' },
    { id: 2, name: 'Data 2', value: 'Value B' }
  ]

  return (
        <>
            <Col xs={12} md={4} className="mb-4">
                <div className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
                    <h3 className="text-white text-center mb-4">Database Operations</h3>
                    <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={() => { /* Fill with fake data function here */ }}>Fill with fake data</Button>
                    <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'red', borderColor: 'red' }} onClick={() => openConfirmation('eraseMemory')}>Erase all data</Button>
                    <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={() => setShowModal(true)}>Display Data</Button>
                </div>
            </Col>

            <Modal show={showModal} onHide={() => setShowModal(false)} centered>
                <Modal.Header closeButton>
                    <Modal.Title>Database Data</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Table striped bordered hover variant="dark">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Value</th>
                            </tr>
                        </thead>
                        <tbody>
                            {dbData.map(data => (
                                <tr key={data.id}>
                                    <td>{data.id}</td>
                                    <td>{data.name}</td>
                                    <td>{data.value}</td>
                                </tr>
                            ))}
                        </tbody>
                    </Table>
                </Modal.Body>
            </Modal>
        </>
  )
}

export default DatabaseComponent
