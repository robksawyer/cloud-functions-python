import sys
import json
from wsgi_util import wsgi
from django.core.handlers.wsgi import WSGIRequest


def handle_http_event(app):
    environ = wsgi(json.loads(sys.stdin.read()))
    app.load_middleware()
    resp = app.get_response(WSGIRequest(environ))

    # handle streaming vs non streaming
    if resp.streaming:
        pass

    sys.stdout.write(json.dumps({
        'body': 'body',
        'status_code': resp.status_code,
        'headers': {},
    }))