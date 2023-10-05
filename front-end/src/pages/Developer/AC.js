import React, { useState } from 'react'
import { Button, Form, ToggleButton, ToggleButtonGroup, Col } from 'react-bootstrap'

function ACComponent () {
  const [temperature, setTemperature] = useState({ min: 64.4, max: 86 })
  const [humidity, setHumidity] = useState({ min: 30, max: 60 })
  const [occupancy, setOccupancy] = useState('Yes') // or 'No'
  const [isCelsius, setIsCelsius] = useState(false)

  return (
        <Col xs={12} md={4} className="mb-4">
            <div className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
                <h3 className="text-white text-center mb-4">AC Controls</h3>

                <div className="d-flex justify-content-between align-items-center mb-3">
                    <label className="text-white">Temperature ({isCelsius ? '°C' : '°F'})</label>
                    <Button onClick={() => setIsCelsius(!isCelsius)} variant="dark">{isCelsius ? 'Switch to °F' : 'Switch to °C'}</Button>
                </div>
                <Form.Range
                    value={temperature.min}
                    min={isCelsius ? 0 : 32}
                    max={isCelsius ? 40 : 104}
                    onChange={(e) => setTemperature({ ...temperature, min: parseFloat(e.target.value) })}
                    className="mb-2"
                />
                <Form.Range
                    value={temperature.max}
                    min={isCelsius ? 0 : 32}
                    max={isCelsius ? 40 : 104}
                    onChange={(e) => setTemperature({ ...temperature, max: parseFloat(e.target.value) })}
                    className="mb-2"
                />

                <label className="text-white d-block mb-2">Humidity (%)</label>
                <Form.Range
                    value={humidity.min}
                    min={0}
                    max={100}
                    onChange={(e) => setHumidity({ ...humidity, min: parseInt(e.target.value) })}
                    className="mb-2"
                />
                <Form.Range
                    value={humidity.max}
                    min={0}
                    max={100}
                    onChange={(e) => setHumidity({ ...humidity, max: parseInt(e.target.value) })}
                    className="mb-2"
                />

                <label className="text-white d-block mb-2">Occupancy</label>
                <ToggleButtonGroup type="radio" name="occupancy" defaultValue={occupancy} onChange={setOccupancy}>
                    <ToggleButton value="Yes" variant="dark">Yes</ToggleButton>
                    <ToggleButton value="No" variant="dark">No</ToggleButton>
                </ToggleButtonGroup>
            </div>
        </Col>
  )
}

export default ACComponent
