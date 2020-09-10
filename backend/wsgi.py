from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.from_pyfile(config)
    else:
        pass #TODO: create default config

    try:
        from app import api
        app.register_blueprint(api)
        app.logger.info("API blueprint registered.")
    except Exception as e:
        app.logger.error(f"API blueprint could not register: {e}")
    # Add more register blueprints here, using the pattern above

    @app.route('/test')
    def test():
        return 'test'

    return app
