from flask import Flask
from routes.city_routes import city_route

app=Flask(__name__)

app.register_blueprint(city_route)

if __name__=="__main__":
    app.run(debug=True,port=5010)

