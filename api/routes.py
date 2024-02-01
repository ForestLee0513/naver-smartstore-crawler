
from .controller.product import product_bp

def routes_list(app):
    app.register_blueprint(product_bp, url_prefix='/product')
    return app