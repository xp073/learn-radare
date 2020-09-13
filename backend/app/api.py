from flask import Blueprint, current_app, request

api = Blueprint(name='api', url_prefix="/api", import_name='api')

@api.route('/test')
def api_test():
    return 'test'

@api.route('/create_radare_session', methods=["POST"])
def api_create_radare_session():
    dir = request.values['dir']
    id = current_app.sm.create_radare_session(dir)
    return {"session_id": id}

@api.route('/execute', methods=["POST"])
def api_execute():
    id = request.values['id']
    cmd = request.values['command']
    out = current_app.sm[id].execute(cmd)
    return {"output": out}
