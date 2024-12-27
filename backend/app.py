from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import os

from routes import routes 

app = Flask(__name__)
api = Api(app)      

CORS(app)

@app.route('/')
def hello_aody():
    return "Hello, CardioCare Members"

# Routes
api.add_resource(routes.ModelPredict, '/predict')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default ke 5000 jika PORT tidak tersedia
    app.run(host="0.0.0.0", port=port)
