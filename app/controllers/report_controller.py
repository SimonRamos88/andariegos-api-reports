from flask import Blueprint, request, jsonify, current_app
from marshmallow import ValidationError

report_bp = Blueprint('report_bp', __name__)

@report_bp.route('/', methods=['POST'])
def create_report():
    try:
        data = request.get_json()
        result = current_app.report_service.create_report(data)
        return jsonify({'message': 'Report created', 'id': str(result.inserted_id)}), 201
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@report_bp.route('/<string:report_id>', methods=['GET'])
def get_report(report_id):
    report = current_app.report_service.get_report(report_id)
    if not report:
        return jsonify({'error': 'Report not found'}), 404
    return jsonify(report), 200

@report_bp.route('/', methods=['GET'])
def get_all_reports():
    reports = current_app.report_service.get_all_reports()
    return jsonify(reports), 200

@report_bp.route('/<string:report_id>', methods=['PUT'])
def update_report(report_id):
    try:
        data = request.get_json()
        result = current_app.report_service.update_report(report_id, data)
        if result.modified_count == 0:
            return jsonify({'error': 'Report not found'}), 404
        return jsonify({'message': 'Report updated'}), 200
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@report_bp.route('/<string:report_id>', methods=['DELETE'])
def delete_report(report_id):
    result = current_app.report_service.delete_report(report_id)
    if result.deleted_count == 0:
        return jsonify({'error': 'Report not found'}), 404
    return jsonify({'message': 'Report deleted'}), 200