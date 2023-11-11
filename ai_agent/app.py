import asyncio
import websockets
import logging
import json
from ai_agent.agent import DQNAgent  
import numpy as np

from smart_ac_simulation.smart_ac_simulation import SmartACEnvironment

logging.basicConfig(level=logging.INFO)

state_size = 3  # occupancy, temperature, humidity
action_size = 3  # TURN_ON_AC, TURN_OFF_AC, SET_TEMP
agent = DQNAgent(state_size, action_size)

async def handler(websocket, path):
    logging.info("WebSocket connection opened")
    try:
        async for message in websocket:
            logging.info(f"Received message from client: {message}")
            data = json.loads(message)

            if data.get('command') == 'start_training':
                asyncio.create_task(start_training(agent))
                await websocket.send(json.dumps({'status': 'training_started'}))
            else:
                pass

    except websockets.exceptions.ConnectionClosed as e:
        logging.warning(f"WebSocket connection closed: {e}")

async def start_training(agent):
    logging.info("Starting training...")
    logging.info("Opening environment...")
    environment = SmartACEnvironment()
    logging.info("Beginning Training...")
    agent.train_agent_fixed(environment)
    logging.info("Training finished. Saving the model...")
    agent.save()

async def start_server():
    server = await websockets.serve(handler, "localhost", 6789)
    logging.info("Agent is listening...")
    await server.wait_closed()

asyncio.run(start_server())
