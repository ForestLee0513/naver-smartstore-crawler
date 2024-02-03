
from .controller.auth import auth_bp
from .controller.product import product_bp

def routes_list(app):
    app.register_blueprint(product_bp, url_prefix='/product')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    return app