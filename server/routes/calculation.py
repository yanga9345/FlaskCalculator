from flask import jsonify, request
from flask_restx import Namespace, Resource
from server import app, api
from server.routes import prometheus
from server.services import eval_service


calc_namespace = Namespace('calculation', description='Simple Calculator')
api.add_namespace(calc_namespace)


@calc_namespace.route("")
class Calculator(Resource):
    @api.param('expr', description='expression', type='string')
    @prometheus.track_requests
    def get(self):
        return jsonify({"result":


eval_service.safe_eval(request.args.get("expr"))})
