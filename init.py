from typing import Any, Mapping, Optional

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager


def create_app(test_config: Optional[Mapping[str, Any]] = None) -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("config")

    if test_config is not None:
        app.config.from_mapping(test_config)

    from app.common.util.db import db

    try:
        db.init_app(app)
    except Exception as e:
        app.logger.critical(str(e))

    from app.modules.usuario import usuario_controller

    app.register_blueprint(usuario_controller.bp)

    JWTManager(app)
    return app
