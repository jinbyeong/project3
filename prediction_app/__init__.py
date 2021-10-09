from flask import Flask

def create_app():
    app = Flask(__name__)

    
    from prediction_app.routes import home, result
    app.register_blueprint(home.homebp)
    app.register_blueprint(result.resultbp)
    return app

if __name__=="__main__" :
    app = create_app()
    app.run(debug=True)