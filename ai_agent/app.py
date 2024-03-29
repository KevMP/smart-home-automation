import asyncio
import websockets
import logging
import json
from ai_agent.agent import DQNAgent  
import numpy as np

from smart_ac_simulation.smart_ac_simulation import SmartACEnvironment

logging.basicConfig(level=logging.INFO)

# state_size = 3  # occupancy, temperature, humidity
# action_size = 3  # TURN_ON_AC, TURN_OFF_AC, SET_TEMP
agent = DQNAgent()

async def handler(websocket, path):
    logging.info("WebSocket connection opened")
    try:
        async for message in websocket:
            logging.info(f"Received message from client: {message}")
            data = json.loads(message)

            action = data.pop('command', {})
            if action == 'start_training':
                asyncio.create_task(start_training(agent, websocket))
            if action == 'get_hyperparameters':
                await websocket.send(json.dumps(agent.get_hyperparameters()))
            if action == 'update_hyperparameters':
                agent.update_hyperparameters(data)
            if action == 'select_profile':
                agent.select_model(data['profile'])

    except websockets.exceptions.ConnectionClosed as e:
        logging.warning(f"WebSocket connection closed: {e}")

async def start_training(agent, websocket):
    logging.info("Starting training...")
    logging.info("Opening environment...")
    environment = SmartACEnvironment()
    logging.info("Beginning Training...")
    
    await agent.train_agent_fixed(environment, websocket=websocket)
    
    logging.info("Training finished. Saving the model...")
    agent.save()

async def start_server():
    server = await websockets.serve(handler, "localhost", 6789)
    logging.info("Agent is listening...")
    await server.wait_closed()

asyncio.run(start_server())
