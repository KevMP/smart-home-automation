from flask import Blueprint, jsonify, request
from sensors import SmartACEnvironment
from AI.basicai import BasicAi
import numpy as np
import logging

developer_bp = Blueprint('developer', __name__)

@developer_bp.route('/api/v1/developer', methods=['GET', 'POST'])
def developer():
    data = request.get_json()
    action = data.get('action', None)
    origin = data.get('origin', None)
    
    logging.info(f"Developer endpoint hit with action: {action} and origin: {origin}")
    
    if origin == "AI":
        if action == "train":
            global global_agent
            global_agent = BasicAi()
            global_agent.simulation()
            logging.info("Training completed")
            return jsonify({"status": "Training completed"})
        elif action == "query":
            if not global_agent:
                logging.error("Agent not trained!")
                return jsonify({"error": "Agent not trained!"}), 400

            environment = SmartACEnvironment()
            state = np.array([environment.get_current_state()])
            action = global_agent.choose_action(state)
            environment.step(action)

            return jsonify(environment.get_ac_status())
    elif origin == "DB":
        pass

    else:
        logging.warning(f"Unrecognized origin: {origin}")
        return jsonify({"error": "Unrecognized origin!"}), 400