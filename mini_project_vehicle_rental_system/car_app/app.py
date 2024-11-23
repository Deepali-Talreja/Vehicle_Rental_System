from flask import Flask 
from routes.car_routes import car_route

app = Flask(__name__)

app.register_blueprint(car_route)

if __name__ == "__main__":
    app.run(debug = True , port = 5011)