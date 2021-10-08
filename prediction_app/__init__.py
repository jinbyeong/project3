from flask import Flask

def create_app():
    app = Flask(__name__)

    
    from prediction_app.routes import home
    app.register_blueprint(home)

    return app

if __name__=="__main__" :
    app = create_app()
    app.run(debug=True)