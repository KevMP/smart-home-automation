import React, { useState, useEffect } from 'react'
import { Row, Col, Form, Button, Dropdown } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import AITable from './AITable'
import ConfirmationModal from '../../components/common/ConfirmationModal'
import LayerComponent from './LayerComponent'
import { ToastContainer, toast } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'
const { v4: uuidv4 } = require('uuid')

const optimizers = [
  'Adam',
  'SGD',
  'RMSprop',
  'Adagrad',
  'Adadelta',
  'Adamax',
  'Nadam',
  'Ftrl'
]

function AIComponent () {
  const navigate = useNavigate()
  const [showModal, setShowModal] = useState(false)
  const [selectedModel, setSelectedModel] = useState(false)
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
    activation_functions: '',
    layers: [],
    models: [],
    model_identification: ''
  })

  useEffect(() => {
    (async () => {
      try {
        axios.get('http://localhost:3001/api/v1/ai')
          .then(response => {
            setSelectedModel(response.data.model_identification)
            setFormData(response.data)
          })
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    })()
  }, [])

  const handleModelSelect = (modelId) => {
    setSelectedModel(modelId)
  }

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
      axios.post('http://localhost:3001/api/v1/ai', formData)
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }
  const handleTrain = (e) => {
    e.preventDefault()
    try {
      navigate('/train')
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }
  const onConfirm = () => {
    console.log('test')
  }

  const validateForm = () => {
    const newErrors = {}
    const floatFields = ['gamma', 'epsilon', 'epsilon_min', 'epsilon_decay', 'learning_rate']
    floatFields.forEach(field => {
      if (!formData[field] || isNaN(formData[field]) || parseFloat(formData[field]) < 0) {
        toast.error('Must be a positive floating point number', {
          position: toast.POSITION.TOP_CENTER
        })
      }
    })

    const integerFields = ['state_size', 'action_size', 'neurons']
    integerFields.forEach(field => {
      if (!formData[field] || isNaN(formData[field]) || parseInt(formData[field]) < 1) {
        toast.error('Must be a positive integer', {
          position: toast.POSITION.TOP_CENTER
        })
      }
    })
    formData.layers.forEach(layer => {
      if (!layer.neurons || !layer.input_shape) {
        toast.error('Missing fields', {
          position: toast.POSITION.TOP_CENTER
        })
      }
    })

    return Object.keys(newErrors).length === 0
  }

  const handleLayerChange = (event, id) => {
    const { name, value } = event.target
    setFormData({ ...formData, layers: formData.layers.map(layer => layer.id === id ? { ...layer, [name]: value } : layer) })
  }

  const addLayer = () => {
    setFormData({ ...formData, layers: [...formData.layers, { id: uuidv4(), neurons: '', input_shape: '', activation: '' }] })
  }

  const removeLayer = (id) => {
    setFormData({ ...formData, layers: formData.layers.filter(layer => layer.id !== id) })
  }

  return (
    <>
    <ToastContainer />

    <Row className="justify-content-center align-items-center mt-5">
      <Col xs={12} md={4} className="mb-4">
        <div className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
          <Form.Label className="text-white">Profile</Form.Label>
          <Dropdown className="mb-3">
            <Dropdown.Toggle className="mb-3 d-block mx-auto" variant="primary" id="dropdown-basic">
              {selectedModel}
            </Dropdown.Toggle>

            <Dropdown.Menu>
              {formData.models.map((model, index) => (
                <Dropdown.Item key={index} onClick={() => handleModelSelect(model)}>
                  {model}
                </Dropdown.Item>
              ))}
            </Dropdown.Menu>
          </Dropdown>
        </div>
      </Col>
    </Row>

    <Row className="justify-content-center align-items-center mt-5">
      <Col xs={12} md={4} className="mb-4">
          <div className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
              <h3 className="text-white text-center mb-4">AI Dashboard</h3>
              <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={handleTrain}>Train</Button>
              <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'red', borderColor: 'red' }} onClick={handleSubmit}>Erase Memory</Button>
              <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={handleSubmit}>Test AI</Button>
              <Button className="mb-2 d-block mx-auto" style={{ backgroundColor: 'black', borderColor: 'black' }} onClick={() => setShowModal(true)}>Display Data</Button>
          </div>
      </Col>
    </Row>

    <Row className="justify-content-center align-items-center mt-5">
    <Col xs={12} md={6} className="mb-4">
      <Form className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }} onSubmit={handleSubmit}>
        <h3 className="text-white text-center mb-4">Neural Network Layers</h3>
        {formData.layers.map(layer => (
            <LayerComponent
              key={layer.id}
              layer={layer}
              onRemove={removeLayer}
              onChange={handleLayerChange}
            />
        ))}
        <Button variant="primary" onClick={addLayer}>Add Layer</Button>
          <h3 className="text-white text-center mb-4">Edit Hyperparameters</h3>
          {['gamma', 'epsilon', 'epsilon_min', 'epsilon_decay', 'learning_rate'].map(key => (
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
          {['state_size', 'action_size'].map(key => (
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
              </Form.Group>))}

              <Form.Group className="mb-3" controlId="formActivationFunctions">
                <Form.Label className="text-white">Optimizer</Form.Label>
                <Form.Select name="activation_functions" value={formData.optimizers} onChange={handleChange}>
                {optimizers.map((func, index) => (
                <option key={index} value={func}>{func}</option>
                ))}
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
