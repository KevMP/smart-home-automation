import React, { useState } from 'react'
import { Container, Row, Modal, Button } from 'react-bootstrap'
import AIComponent from './AI'
import DatabaseComponent from './Database'
import ACComponent from './AC'

function Developer () {
  const [showConfirmation, setShowConfirmation] = useState(false)
  const [currentAction, setCurrentAction] = useState(null)

  const handleOpenConfirmation = (action) => {
    setCurrentAction(action)
    setShowConfirmation(true)
  }

  const handleConfirm = () => {
    // Handle each action accordingly
    switch (currentAction) {
      case 'eraseMemory':
        // Erase Memory function
        break
      case 'eraseData':
        // Erase all Data function
        break
      default:
        break
    }
    setShowConfirmation(false)
  }

  return (
        <Container fluid style={{ backgroundColor: '#F2F4F8' }} className="py-5">
            <Row className="justify-content-center">
                <AIComponent openConfirmation={handleOpenConfirmation} />
                <DatabaseComponent openConfirmation={handleOpenConfirmation} />
                <ACComponent openConfirmation={handleOpenConfirmation} />
            </Row>

            <Modal show={showConfirmation} onHide={() => setShowConfirmation(false)} centered>
                <Modal.Header closeButton>
                    <Modal.Title>Warning!</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    Are you sure you want to proceed? This action cannot be undone.
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={() => setShowConfirmation(false)}>
                        Cancel
                    </Button>
                    <Button variant="danger" onClick={handleConfirm}>
                        Confirm
                    </Button>
                </Modal.Footer>
            </Modal>
        </Container>
  )
}

export default Developer
