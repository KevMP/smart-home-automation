import React from 'react'
import { Modal, Button } from 'react-bootstrap'

const ConfirmationModal = ({ show, onHide, onConfirm }) => {
  return (
    <Modal show={show} onHide={onHide} centered>
      <Modal.Header closeButton>
        <Modal.Title>Warning!</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        Are you sure you want to proceed? This action cannot be undone.
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={onHide}>
          Cancel
        </Button>
        <Button variant="danger" onClick={onConfirm}>
          Confirm
        </Button>
      </Modal.Footer>
    </Modal>
  )
}

export default ConfirmationModal
