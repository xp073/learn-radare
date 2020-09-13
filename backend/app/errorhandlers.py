from flask import request
def bind_error_handlers(flask_app):
    # code is too repeating here, if possible find a way to do it more compactly
    @flask_app.errorhandler(404)
    def error_404(e):
        flask_app.logger.error(f'{str(e)}')
        return {'error_code': 404, 'error': str(e)}, 404

    @flask_app.errorhandler(403)
    def error_403(e):
        flask_app.logger.error(f'{str(e)}')

        return {'error_code': 403, 'error': str(e)}, 403

    @flask_app.errorhandler(410)
    def error_410(e):
        flask_app.logger.error(f'{str(e)}')
        return {'error_code': 410, 'error': str(e)}, 410

    @flask_app.errorhandler(500)
    def error_500(e):
        flask_app.logger.error(f'{str(e)}')
        return {'error_code': 500, 'error': str(e)}, 500
