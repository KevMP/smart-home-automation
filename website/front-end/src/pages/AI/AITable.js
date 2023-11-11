import React from 'react'
import { Modal, Table } from 'react-bootstrap'

function AITable ({ aiData, onHide, show }) {
  return (
    <>
    <Modal show={show} onHide={onHide} centered>
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

export default AITable
