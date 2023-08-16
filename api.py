from flask import Flask
from flask_restful import Resource, Api
from tratamento_de_dados import cep_list, bairro_list

app = Flask(__name__)
api = Api(app)
host = '127.0.0.1'
port = 5000

ceps = {}
bairros = {}

class api_up(Resource):
    def get(self):
        return 'API UP!! 😁'

class get_ceps(Resource):
    def get(self):
        return cep_list
    
class get_bairros(Resource):
    def get(self):
        return bairro_list
    
api.add_resource(api_up, '/')
api.add_resource(get_ceps, '/ceps')
api.add_resource(get_bairros, '/bairros')

if __name__ == '__main__':
    from waitress import serve
    print("Server running on: {}:{} 🚀".format(host, port))
    serve(app, host=host, port=port )
