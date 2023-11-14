import React from 'react'
import { Form, Button } from 'react-bootstrap'

const ActivationFuncs = [
  'deserialize',
  'elu',
  'exponential',
  'gelu',
  'get',
  'hard_sigmoid',
  'linear',
  'mish',
  'relu',
  'selu',
  'serialize',
  'sigmoid',
  'softmax',
  'softplus',
  'softsign',
  'swish',
  'tanh'
]

const LayerComponent = ({ layer, onRemove, onChange }) => {
  return (
    <div className="mb-3 p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
      <Form.Group className="mb-3">
        <Form.Label className="text-white">Neurons</Form.Label>
        <Form.Control
          type="number"
          min="1"
          name="neurons"
          value={layer.neurons}
          onChange={e => onChange(e, layer.id)}
        />
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label className="text-white">Input Shape</Form.Label>
        <Form.Control
          type="number"
          min="1"
          name="input_shape"
          value={layer.input_shape}
          onChange={e => onChange(e, layer.id)}
        />
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label className="text-white">Activation Function</Form.Label>
        <Form.Select
          name="activation"
          value={layer.activation}
          onChange={e => onChange(e, layer.id)}
        >
            {ActivationFuncs.map((func, index) => {
              return <option key={index} value={func}>{func}</option>
            })}
        </Form.Select>
      </Form.Group>
      <Button variant="danger" onClick={() => onRemove(layer.id)}>Remove Layer</Button>
    </div>
  )
}

export default LayerComponent
