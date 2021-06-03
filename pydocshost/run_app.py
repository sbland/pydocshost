"""Setup flask api."""
import flask
from .routes.client_routes import client_routes


def get_app(static_folder="../static", docs_directory="../static/docs", *args, **kwargs) -> flask.Flask:
    app = flask.Flask(__name__, static_folder=static_folder)

    # Client Static Paths
    @app.route("/app/<path:filename>")
    def static_proxy_app(filename):
        return app.send_static_file("app/" + filename)

    # Docs Static Paths

    @app.route("/docs/<path:filename>")
    def static_proxy_docs(filename):
        print(filename)
        print(app.root_path + docs_directory)
        return flask.send_from_directory(app.root_path + "/" + docs_directory, filename)

    client_routes(app)
    return app


def run(port=8000, host="0.0.0.0", *args, **kwargs):
    """Run the flask server."""
    print(f"\nGo to http://localhost:{port}\n")
    app = get_app(*args, **kwargs)
    app.run(port=port, host=host)
