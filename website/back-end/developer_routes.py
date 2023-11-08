from flask import Blueprint, jsonify, request
from smart_ac_simulation.smart_ac_simulation import SmartACEnvironment, SmartThermostat, OccupancySensor, TemperatureSensor, HumiditySensor
import numpy as np
import logging

developer_bp = Blueprint('developer', __name__)

@developer_bp.route('/api/v1/developer', methods=['GET', 'POST'])
def developer():
    if request.method == 'POST':
        data = request.get_json()
        action = data.get('action', None)
        origin = data.get('origin', None)
        
        logging.info(f"Developer endpoint hit with action: {action} and origin: {origin}")
        
        if origin == "AI":
            if action == "train":
                # smart_ac_environment.OccupancySensor()
                # global global_agent
                # global_agent = BasicAi()
                # global_agent.simulation()
                # logging.info("Training completed")
                return jsonify()
            elif action == "query":
                # if not global_agent:
                #     logging.error("Agent not trained!")
                #     return jsonify({"error": "Agent not trained!"}), 400

                # environment = SmartACEnvironment()
                # state = np.array([environment.get_current_state()])
                # action = global_agent.choose_action(state)
                # environment.step(action)

                # return jsonify(environment.get_ac_status())
                return jsonify()
        elif origin == "DB":
            pass
        elif origin == "AC":
            if action == "update":
                data.get('temperature', None)
                data.get('humidity', None)
                data.get('occupancy', None)
                data.get('temperature', None)

        else:
            logging.warning(f"Unrecognized origin: {origin}")
            return jsonify({"error": "Unrecognized origin!"}), 400
    else:
        return jsonify(SmartACEnvironment().get_current_state())