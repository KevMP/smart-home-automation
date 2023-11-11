import React, { useState, useEffect } from 'react'
import { Row, Col, Form, Button } from 'react-bootstrap'
import axios from 'axios'
import AITable from './AITable'
import ConfirmationModal from '../../components/common/ConfirmationModal'

function AIComponent () {
  const [showModal, setShowModal] = useState(false)
  const [showConfirmation, setShowConfirmation] = useState(false)
  const [formData, setFormData] = useState({
    gamma: '',
    epsilon: '',
    epsilon_min: '',
    epsilon_decay: '',
    learning_rate: '',
    state_size: '',
    action_size: '',
    neurons: '',
    learning_rate_optimizer: '',
    activation_functions: ''
  })

  useEffect(() => {
    (async () => {
      try {
        axios.get('http://localhost:3001/api/v1/ai')
          .then(response => {
            // setFormData(response.data)
          })
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    })()
  }, [])

  const aiData = {
    occupancy: 'Yes',
    temperature: '72°F',
    humidity: '45%',
    acStatus: 'On'
  }

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prevState => ({ ...prevState, [name]: value }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!validateForm()) {
      console.log('Error')
    }
    try {
      axios.post('http://localhost:3001/api/v1/ai')
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }

  const onConfirm = () => {
    console.log('test')
  }

  const validateForm = () => {
    const newErrors = {}
    const floatFields = ['gamma', 'epsilon', 'epsilon_min', 'epsilon_decay', 'learning_rate', 'learning_rate_optimizer']
    floatFields.forEach(field => {
      if (!formData[field] || isNaN(formData[field]) || parseFloat(formData[field]) < 0) {
        newErrors[field] = 'Must be a positive floating point number'
      }
    })

    const integerFields = ['state_size', 'action_size', 'neurons']
    integerFields.forEach(field => {
      if (!formData[field] || isNaN(formData[field]) || parseInt(formData[field]) < 1) {
        newErrors[field] = 'Must be a positive integer'
      }
    })
    return Object.keys(newErrors).length === 0
  }

  return (
    <>
    <Row className="justify-content-center align-items-center mt-5">
      <Col xs={12} md={4} className="mb-4">
          <div className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
              <h3 className="text-white text-center mb-4">AI Dashboard</h3>
              <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={handleSubmit}>Train</Button>
              <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'red', borderColor: 'red' }} onClick={handleSubmit}>Erase Memory</Button>
              <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={handleSubmit}>Display Data</Button>
          </div>
      </Col>
    </Row>
    <Row className="justify-content-center align-items-center mt-5">
    <Col xs={12} md={6} className="mb-4">
                    <Form className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }} onSubmit={handleSubmit}>
                        <h3 className="text-white text-center mb-4">Edit Hyperparameters</h3>
                        {['gamma', 'epsilon', 'epsilon_min', 'epsilon_decay', 'learning_rate', 'learning_rate_optimizer'].map(key => (
                            <Form.Group className="mb-3" controlId={`form${key}`} key={key}>
                                <Form.Label className="text-white">{key.replace(/_/g, ' ').toUpperCase()}</Form.Label>
                                <Form.Control
                                    type="number"
                                    step="0.001"
                                    min="0"
                                    name={key}
                                    value={formData[key]}
                                    onChange={handleChange}
                                />
                            </Form.Group>
                        ))}
                        {['state_size', 'action_size', 'neurons'].map(key => (
                            <Form.Group className="mb-3" controlId={`form${key}`} key={key}>
                                <Form.Label className="text-white">{key.replace(/_/g, ' ').toUpperCase()}</Form.Label>
                                <Form.Control
                                    type="number"
                                    min="1"
                                    step="1"
                                    name={key}
                                    value={formData[key]}
                                    onChange={handleChange}
                                />
                            </Form.Group>
                        ))}

                        <Form.Group className="mb-3" controlId="formActivationFunctions">
                            <Form.Label className="text-white">ACTIVATION FUNCTIONS</Form.Label>
                            <Form.Select name="activation_functions" value={formData.activation_functions} onChange={handleChange}>
                                <option value="relu">ReLU</option>
                                <option value="sigmoid">Sigmoid</option>
                                <option value="tanh">Tanh</option>
                            </Form.Select>
                        </Form.Group>

                        <Button variant="success" className="mb-2 d-block mx-auto" type="submit">
                            Update Hyperparameters
                        </Button>
                    </Form>
                </Col>
      <ConfirmationModal
        show={showConfirmation}
        onHide={() => setShowConfirmation(false)}
        onConfirm={onConfirm}
        />
      <AITable
        onHide={() => setShowModal(false)}
        show={showModal}
        aiData={aiData}
        />
    </Row>
    </>
  )
}

export default AIComponent
