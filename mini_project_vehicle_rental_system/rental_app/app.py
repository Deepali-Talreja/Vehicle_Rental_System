from flask import Flask
from routes.rental_routes import rental_route

app = Flask(__name__)

#CORS (app , resources = {r"/api/*" : {"origins" : "https://127.0.0.1:5500"}})


app.register_blueprint(rental_route)

if __name__ == "__main__":
    app.run(debug = True , port = 5007)

