from flask import Blueprint, request, jsonify
from src.main.composer.create_person_composer import create_person_composer
from src.main.composer.find_person_composer import find_person_composer
from src.main.composer.update_person_composer import update_person_composer
from src.main.composer.delete_person_composer import delete_person_composer
from src.main.adapter.request_adapter import request_adapter

person_blueprint = Blueprint('person', __name__)


@person_blueprint.route('/create', methods=['POST'])
def create_person():
    http_response = request_adapter(request, create_person_composer())
    return jsonify(http_response.body, http_response.status_code)


@person_blueprint.route('/find', methods=['GET'])
def find_person():
    http_response = request_adapter(request, find_person_composer())
    return jsonify(http_response.body, http_response.status_code)


@person_blueprint.route('/update', methods=['PUT'])
def update_person():
    http_response = request_adapter(request, update_person_composer())
    return jsonify(http_response.body, http_response.status_code)


@person_blueprint.route('/delete', methods=['DELETE'])
def delete_person():
    http_response = request_adapter(request, delete_person_composer())
    return jsonify(http_response.body, http_response.status_code)
