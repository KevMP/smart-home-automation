import React, { useState, useEffect } from 'react'
import { Container, Row, Modal, Button } from 'react-bootstrap'
import AIComponent from './AI'
import DatabaseComponent from './Database'
import ACComponent from './AC'
import ACStatusCard from './AC_Status'
import axios from 'axios'

function Developer () {
  const [showConfirmation, setShowConfirmation] = useState(false)
  const [currentAction, setCurrentAction] = useState(null)
  // eslint-disable-next-line no-unused-vars
  const [formData, setFormData] = useState({
    max_temp: 0,
    min_temp: 0,
    max_humidity: 0,
    min_humidity: 0,
    occupancy_max: 0,
    occupancy: 0,
    is_celsius: false,
    ac_status: false,
    humidity: 0,
    temperature: 0
  })
  const [isFetching, setIsFetching] = useState(true)
  const handleOpenConfirmation = (action) => {
    setCurrentAction(action)
    setShowConfirmation(true)
  }

  useEffect(() => {
    (async () => {
      try {
        axios.get('/api/v1/developer')
          .then(response => {
            setFormData(response.data)
          })
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    })()
  }, [])

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
                <ACComponent openConfirmation={handleOpenConfirmation} formData={formData} setFormData={setFormData} />
                <ACStatusCard formData={formData} />
                <div className='align-items-center d-flex justify-content-center '>
                  <Button
                  variant="primary"
                  size="lg"
                  onClick={() => setIsFetching(prevState => !prevState)}
                  >
                    {isFetching ? 'Pause Fetching' : 'Resume Fetching'}
                  </Button>
                </div>
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
