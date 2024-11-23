from flask import Flask
from routes.customer_routes import customer_route

app = Flask(__name__)


app.register_blueprint(customer_route)

if __name__ == "__main__":
    app.run(debug = True , port = 5012)

    