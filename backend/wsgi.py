from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    import os
    if config:
        app.config.from_pyfile(config)
    else:
        #default config
        app.config['RADARE_INSTALL_DIR'] = "../radare2-install"
        app.config['REACT_BUILD_DIR'] = ""


        app.config['SECRET_KEY'] = os.urandom(32).hex()

    try: # registering session manager
        from app import r2pipewrapper
        app.sm = r2pipewrapper.sm
        app.logger.info("SessionManager registered.")
    except Exception as e:
        app.logger.error(f"SessionManager could not register: {e}")


    try: # registering errorhandlers
        from app import errorhandlers
        errorhandlers.bind_error_handlers(app)
        app.logger.info("Errorhandlers registered.")
    except Exception as e:
        app.logger.error(f"Errorhandlers could not register: {e}")

    try:  # registering api
        # app.logger.info(f"Trying to register API BP. CWDIR: {os.getcwd()}")
        from app import api
        app.register_blueprint(api.api)
        app.logger.info("API blueprint registered.")
    except Exception as e:
        app.logger.error(f"API blueprint could not register: {e}")
    # Add more register blueprints here, using the pattern above

    @app.route('/test')
    def test():
        return 'test'

    return app
