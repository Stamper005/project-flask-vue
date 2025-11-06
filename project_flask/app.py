from flask import Flask
from tel import tel_bp
from db import init_db
app = Flask(__name__)
app.register_blueprint(tel_bp,url_prefix='/tel')
init_db(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)