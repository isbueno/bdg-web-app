from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)

    from index.routes import index_blueprint
    app.register_blueprint(index_blueprint)

    from dna.routes import dna_blueprint
    app.register_blueprint(dna_blueprint)

    from login.routes import login_blueprint
    app.register_blueprint(login_blueprint)

    from login import login_manager
    login_manager.init_app(app)

    if app.config["TESTING"]:
        with app.app_context():
            db.drop_all()
            db.create_all()
            from util.crawler import get_data_from_sequencia
            get_data_from_sequencia(db)

            db.session.add(User(
                name="Isabely Bueno",
                email="23.isabelybueno@gmail.com",
                password="123456",
                birthdate=datetime(2003, 0o2, 23).date()
            ))
            db.session.commit()

    return app


from model import *

if __name__ == "__main__":
    app = create_app()
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)
