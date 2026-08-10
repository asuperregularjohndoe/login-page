from flask import Flask, Request, Response
from flask.globals import request as flask_request

def run_flask(app: Flask):
    def handler(event, context):
        flask_req = flask_request(
            method=event.get("method", "GET"),
            path=event.get("path", "/"),
            headers=event.get("headers", {}),
            data=event.get("body", b""),
            query_string=event.get("query", {}).get("query_string", b""),
        )
        response = app.full_dispatch_request(flask_req)
        return {
            "statusCode": response.status_code,
            "headers": response.headers,
            "body": response.get_data(as_text=False),
            "isBase64Encoded": False,
        }
    return handler

# For the on_request function
def handle(request):
    # Convert the Pages Functions request to Flask format
    flask_req = Request(
        method=request.method,
        path=request.url,
        headers={k: v[0] for k, v in request.headers.items()},
        data=request.body,
    )
    response = app.full_dispatch_request(flask_req)
    return Response(response.get_data(), status=response.status_code, headers=response.headers)
