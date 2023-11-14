import React, { useState, useEffect } from 'react'
import { ProgressBar, Button, Container, Row, Col, ListGroup } from 'react-bootstrap'
import axios from 'axios'
import io from 'socket.io-client'

function TrainingView () {
  const [episode, setEpisode] = useState(0)
  const [step, setStep] = useState(0)
  const [hyperparameters, setHyperparameters] = useState({})
  const [trainingComplete, setTrainingComplete] = useState(false)

  const socket = io('http://localhost:3001', { reconnection: true, reconnectionAttempts: Infinity, reconnectionDelay: 1000 })

  const handleSubmit = (e) => {
    e.preventDefault()
    try {
      axios.post('http://localhost:3001/api/v1/train')
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }

  useEffect(() => {
    try {
      socket.on('training_update', (data) => {
        console.log(data)
        setEpisode(data.episode)
        setStep(data.step)
      })

      socket.on('training_complete', () => {
        setTrainingComplete(true)
      })

      socket.on('disconnect', (reason) => {
        console.log('Disconnected:', reason)
      })
    } catch (error) {
      console.log(error)
    }

    return () => {
      socket.off('training_update')
      socket.off('training_complete')
      socket.off('disconnect')
      socket.disconnect()
    }
  }, [socket])

  useEffect(() => {
    axios.get('http://localhost:3001/api/v1/train')
      .then(response => {
        setHyperparameters(response.data)
      })
      .catch(error => {
        console.error('Error fetching hyperparameters:', error)
      })
  }, [])

  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col md={6}>
        <div className="d-flex flex-column align-items-center">
          <h2 className="text-center mb-4 mt-5">AI Training Dashboard</h2>
          <Button variant="success" onClick={handleSubmit}>Start Training</Button>
        </div>
          <h4 className="my-4">Hyperparameters</h4>

          <ListGroup>
            {Object.entries(hyperparameters).map(([key, value]) => (
              <ListGroup.Item key={key}>{key}: {value}</ListGroup.Item>
            ))}
          </ListGroup>
          <h4 className='mt-5' >Training Progress</h4>
          <ProgressBar className='mb-5' now={episode * 10 + step} label={`${10 * episode + step}%`} />
          {trainingComplete && <p>Training complete!</p>}

          <h4>Episode Progress</h4>
          <ProgressBar className='mb-5' now={episode * 10} label={`${10 * episode}%`} />

          <h4>Step Progress</h4>
          <ProgressBar className='mb-5' now={step * 10} label={`${10 * step}%`} />
        </Col>
      </Row>
    </Container>
  )
}

export default TrainingView
