from flask import Blueprint, jsonify, current_app, request
from initialize_socket import socketio
from smart_ac_simulation.smart_ac_simulation import SmartACEnvironment
import asyncio
import websockets
import json
import uuid

developer_bp = Blueprint('developer', __name__)

async def ai_agent_train(data):
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps(data))
                
        async for message in ws:
            progress_data = json.loads(message)
            socketio.emit('training_update', progress_data)

async def ai_agent_request(message, data={}):
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        current_app.logger.debug(message)
        if message['command'] == 'update_hyperparameters':
            current_app.logger.debug("Sending parameterrs to AI...")
            await websocket.send(json.dumps({**message, **data}))
        else:
            await websocket.send(json.dumps(message))   
            
        response = await websocket.recv()
        return json.loads(response)


def start_training():
    asyncio.run(ai_agent_train({'command': "start_training"}))
    # socketio.emit('training_complete', {})

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
    try:
        if request.method == "POST":
            data = request.get_json()
            if data['command'] == 'update_hyperparameters':
                current_app.logger.debug(f"Changing parameters...")
                asyncio.run(ai_agent_request(message=data.pop('command'), data=data))
                return jsonify(), 200
            elif data['command'] == 'select_profile':
                current_app.logger.debug(f"Selecting profile...")
                asyncio.run(ai_agent_request(message=data.pop('command'), data=data))
                return jsonify(), 200
        else:
            current_app.logger.debug(f"Fetching hyperparameters...")
            response = asyncio.run(ai_agent_request({ 'command': "get_hyperparameters" }))
            response['layers'] = [{**layer, 'id': uuid.uuid4()} for layer in response['layers']]
            return jsonify(response), 200
    except Exception as e:
        current_app.logger.error(f"There was an exception...\n{e}")

@developer_bp.route('/api/v1/train', methods=['GET', 'POST'])
def train():
    if request.method == "POST":
        current_app.logger.debug("Sending signal to train...")
        socketio.start_background_task(start_training)
        return jsonify(), 200
    else:
        current_app.logger.debug(f"Fetching hyperparameters...")
        response = asyncio.run(ai_agent_request({ 'command': "get_hyperparameters" }))
        del response['layers']
        del response['models']
        return jsonify(response), 200
