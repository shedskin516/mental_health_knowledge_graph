from flask import Blueprint, current_app, request, jsonify

from api.dao.disease import DiseaseDAO

disease_routes = Blueprint("disease", __name__, url_prefix="/api/disease")


# get disease detail by disease name
@disease_routes.route('/<disease_name>', methods = ['POST', 'GET'])
def get_disease(disease_name):
    dao = DiseaseDAO(current_app.driver)
    output = dao.getDisease(disease_name)
    return jsonify(output)

