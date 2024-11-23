from flask import Flask
from routes.feedback_routes import feedback_route

app=Flask(__name__)

app.register_blueprint(feedback_route)

if __name__=="__main__":
    app.run(debug=True,port=5013)

    

