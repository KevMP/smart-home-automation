from flask import Blueprint, jsonify, request, current_app
from smart_ac_simulation.smart_ac_simulation import SmartACEnvironment
import asyncio
import websockets
import json

developer_bp = Blueprint('developer', __name__)

async def ai_agent_request(state):
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(state))
        
        response = await websocket.recv()
        return json.loads(response)

async def ai_agent_train():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({ 'command': "start_training" }))
        
        response = await websocket.recv()
        return json.loads(response)

def convert(val, is_celsius):
    return val * 9 / 5 + 32 if is_celsius else val - 32 * 5 / 9

@developer_bp.route('/api/v1/ac', methods=['GET', 'POST'])
def ac():
    if request.method == "POST":
        current_app.logger.debug(f"Updating AC Parameters...")
        data = request.get_json()
        env = SmartACEnvironment()
        state = env.get_current_state()
        
        if env['is_celsius'] != data.get('is_celsius'):
            env.smart_thermostat.set_temperature(convert(state['temperature'], env['is_celsius']))
            env.temperature_sensor.set_range(convert(env['min_temp'], env['is_celsius']), convert(env['max_temp'], env['is_celsius']))
    else:
        current_app.logger.debug(f"Fetching AC parameters...")
        env = SmartACEnvironment()
        # current_app.logger.debug(f"Loading AC with values: {env.get_current_state()}")
        return jsonify(env.get_current_state())
    

@developer_bp.route('/api/v1/ai', methods=['GET', 'POST'])
def ai():
    if request.method == "POST":
        current_app.logger.debug(f"Sending signal to train...")
        asyncio.run(ai_agent_train())
        return jsonify()
    else:
        return jsonify()