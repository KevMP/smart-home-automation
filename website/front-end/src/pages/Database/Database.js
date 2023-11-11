import React, { useState } from 'react'
import { Button, Col, Row } from 'react-bootstrap'
import ConfirmationModal from '../../components/common/ConfirmationModal'
import DBTable from './DBTable'

function DatabaseComponent () {
  const [showModal, setShowModal] = useState(false)
  const [showConfirmation, setShowConfirmation] = useState(false)

  const dbData = [
    { id: 1, name: 'Data 1', value: 'Value A' },
    { id: 2, name: 'Data 2', value: 'Value B' }
  ]

  const onConfirm = () => {
    console.log('test')
  }

  return (
        <>
        <Row className="justify-content-center align-items-center mt-5">
            <Col xs={12} md={4} className="mb-4">
                <div className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
                    <h3 className="text-white text-center mb-4">Database Operations</h3>
                    <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={() => { /* Fill with fake data function here */ }}>Fill with fake data</Button>
                    <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'red', borderColor: 'red' }} onClick={() => setShowConfirmation(true)}>Erase all data</Button>
                    <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={() => setShowModal(true)}>Display Data</Button>
                </div>
            </Col>
        </Row>
        <ConfirmationModal
        show={showConfirmation}
        onHide={() => setShowConfirmation(false)}
        onConfirm={onConfirm}
        />
        <DBTable
        show={showModal}
        onHide={() => setShowModal(false)}
        dbData={dbData}
        />
        </>
  )
}

export default DatabaseComponent
