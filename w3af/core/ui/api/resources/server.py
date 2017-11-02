from w3af.core.ui.api import app

from flask import request
import os, sys

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/restart', methods=['GET'])
def restart():
    shutdown_server()
    app.restart = True
    return 'Server restarting ...'

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
