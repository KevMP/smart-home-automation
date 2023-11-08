import React from 'react'
import { Button, Form, Col } from 'react-bootstrap'
import { BiSolidThermometer } from 'react-icons/bi'
import { MdWbSunny, MdOpacity } from 'react-icons/md'
import axios from 'axios'

function ACComponent ({ formData, setFormData }) {
  const handleSave = () => {
    const payload = {
      origin: 'AC',
      action: 'update'
    }

    axios.post('localhost:3001/api/developer', { ...payload, ...formData })
      .then(response => {
        console.log(response.data)
        alert('Settings saved successfully!')
      })
      .catch(error => {
        console.error('Error saving settings:', error)
        alert('Error saving settings.')
      })
  }

  function convertTemperature (value, isCelsius) {
    const numericValue = parseFloat(value)
    console.log(numericValue)
    return parseFloat(isCelsius ? ((numericValue * 9) / 5) + 32 : ((numericValue - 32) * 5) / 9).toFixed(2)
  }

  const handleSwitch = () => {
    const isCelsius = !formData.is_celsius
    const updatedFormData = {
      ...formData,
      is_celsius: isCelsius,
      temperature: convertTemperature(formData.temperature, isCelsius),
      max_temp: convertTemperature(formData.max_temp, isCelsius),
      min_temp: convertTemperature(formData.min_temp, isCelsius)
    }

    setFormData(updatedFormData)
  }

  return (
        <Col xs={12} md={4} className="mb-4">
            <div className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
                <h3 className="text-white text-center mb-4">AC Controls</h3>

                <div className="d-flex align-items-center mb-4">
                    <div className={`text-center bg-${formData.ac_status ? 'success' : 'danger'} bg-gradient text-white rounded-3 p-3 h2`}>
                        <BiSolidThermometer />
                    </div>
                    <div className="d-flex flex-column align-items-start ms-4">
                        <div className="d-flex align-items-center">
                            <MdWbSunny className="text-white me-2" />
                            <p className='text-white lh-sm text-center'>Temperature: </p>
                            <p className='text-white ms-3'>{formData.is_celsius ? `${formData.min_temp}°F - ${formData.max_temp}°F` : `${formData.min_temp}°C - ${formData.max_temp}°C`}</p>
                        </div>
                        <div className="d-flex align-items-center">
                            <MdOpacity className="text-white me-2" />
                            <p className='text-white lh-sm text-center'>Humidity:</p>
                            <p className='text-white ms-3'>{`${formData.min_humidity}% - ${formData.max_humidity}%`}</p>
                        </div>
                    </div>
                </div>

                <Button onClick={handleSwitch} variant="dark" className="mb-3">{formData.is_celsius ? 'Switch to °F' : 'Switch to °C'}</Button>

                <div className="d-flex justify-content-between align-items-center mb-3">
                    <Form.Range
                        value={formData.min_temp}
                        min={formData.is_celsius ? 32 : 0}
                        max={formData.is_celsius ? 104 : 40}
                        onChange={(e) => setFormData({ ...formData, min_temp: parseFloat(e.target.value) })}
                    />
                    <Form.Range
                        value={formData.max_temp}
                        min={formData.is_celsius ? 32 : 0}
                        max={formData.is_celsius ? 104 : 40}
                        onChange={(e) => setFormData({ ...formData, max_temp: parseFloat(e.target.value) })}
                    />
                </div>

                <div className="d-flex justify-content-between align-items-center mb-3">
                    <Form.Range
                        value={formData.min_humidity}
                        min={0}
                        max={100}
                        onChange={(e) => setFormData({ ...formData, min_humidity: parseInt(e.target.value) })}
                    />
                    <Form.Range
                        value={formData.max_humidity}
                        min={0}
                        max={100}
                        onChange={(e) => setFormData({ ...formData, max_humidity: parseInt(e.target.value) })}
                    />
                </div>

                <label className="text-white d-block mb-2">Occupancy Max: {formData.occupancy_max}</label>
                    <Form.Range
                            value={formData.occupancy_max}
                            min={0}
                            max={100}
                            onChange={(e) => setFormData({ ...formData, occupancy_max: parseInt(e.target.value) })}
                        />
                <div>
                    <Button variant="primary" className="mb-3 mt-5" onClick={handleSave}>Save Settings</Button>
                </div>
            </div>
        </Col>
  )
}

export default ACComponent
