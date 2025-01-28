from flask import Flask
from flask_cors import CORS
from app.routes import my

app = Flask(__name__)
CORS(app)
app.register_blueprint(my)

if __name__ == '__main__':
    app.run(debug=True)
