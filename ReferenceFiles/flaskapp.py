from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from models.modeldb import db
from resources import GLResource
from resources.GLResource import GLbyHolding
from resources.tradehistoryResource import TradeHistoryResource

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:monkeyxx@192.168.1.135:5432/postgres'
app.config['SQLALCHEMY_ENABLE_POOL_PRE_PING'] = True
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello from Flask second another!'


api.add_resource(TradeHistoryResource, "/tradehistory/")
api.add_resource(GLbyHolding, "/GL/")

if __name__ == '__main__':
    app.run()
