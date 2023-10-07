import React, { useState } from 'react'
import { Button, Form, ToggleButton, ToggleButtonGroup, Col } from 'react-bootstrap'
import { BiSolidThermometer } from 'react-icons/bi' // Importing the thermometer icon
import { MdWbSunny, MdOpacity } from 'react-icons/md' // Icons for temperature and humidity

function ACComponent () {
  const [temperature, setTemperature] = useState({ min: 64.4, max: 86 })
  const [humidity, setHumidity] = useState({ min: 30, max: 60 })
  const [occupancy, setOccupancy] = useState('Yes') // or 'No'
  const [isCelsius, setIsCelsius] = useState(false)
  const acStatus = true // Example status, replace with actual status if needed

  return (
        <Col xs={12} md={4} className="mb-4">
            <div className="p-3 shadow rounded" style={{ backgroundColor: 'rgb(9, 69, 120)' }}>
                <h3 className="text-white text-center mb-4">AC Controls</h3>

                <div className="d-flex align-items-center mb-4">
                    <div className={`text-center bg-${acStatus ? 'success' : 'danger'} bg-gradient text-white rounded-3 p-3 h2`}>
                        <BiSolidThermometer />
                    </div>
                    <div className="d-flex flex-column align-items-start ms-4">
                        <div className="d-flex align-items-center">
                            <MdWbSunny className="text-white me-2" />
                            <p className='text-white lh-sm text-center'>Temperature: </p>
                            <p className='text-white ms-3'>{isCelsius ? `${temperature.min}°C - ${temperature.max}°C` : `${temperature.min}°F - ${temperature.max}°F`}</p>
                        </div>
                        <div className="d-flex align-items-center">
                            <MdOpacity className="text-white me-2" />
                            <p className='text-white lh-sm text-center'>Humidity:</p>
                            <p className='text-white ms-3'>{`${humidity.min}% - ${humidity.max}%`}</p>
                        </div>
                    </div>
                </div>

                <Button onClick={() => setIsCelsius(!isCelsius)} variant="dark" className="mb-3">{isCelsius ? 'Switch to °F' : 'Switch to °C'}</Button>

                <div className="d-flex justify-content-between align-items-center mb-3">
                    <Form.Range
                        value={temperature.min}
                        min={isCelsius ? 0 : 32}
                        max={isCelsius ? 40 : 104}
                        onChange={(e) => setTemperature({ ...temperature, min: parseFloat(e.target.value) })}
                    />
                    <Form.Range
                        value={temperature.max}
                        min={isCelsius ? 0 : 32}
                        max={isCelsius ? 40 : 104}
                        onChange={(e) => setTemperature({ ...temperature, max: parseFloat(e.target.value) })}
                    />
                </div>

                <div className="d-flex justify-content-between align-items-center mb-3">
                    <Form.Range
                        value={humidity.min}
                        min={0}
                        max={100}
                        onChange={(e) => setHumidity({ ...humidity, min: parseInt(e.target.value) })}
                    />
                    <Form.Range
                        value={humidity.max}
                        min={0}
                        max={100}
                        onChange={(e) => setHumidity({ ...humidity, max: parseInt(e.target.value) })}
                    />
                </div>

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
