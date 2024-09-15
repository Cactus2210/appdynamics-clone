from flask import Blueprint, jsonify, request
from .monitor.api_monitor import get_api_status
from .models import APIStatus

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/status', methods=['GET'])
def api_status():
    status = get_api_status()
    return jsonify(status), 200
