"""Setup flask api."""
import flask
from .routes.client_routes import client_routes


def get_app(static_folder="../static", docs_directory=None, notebooks_directory=None, *args, **kwargs) -> flask.Flask:
    app = flask.Flask(__name__, static_folder=static_folder)

    docs_directory = docs_directory or app.root_path + "/" + "../static/docs"
    notebooks_directory = notebooks_directory or app.root_path + "/" + "../static/notebooks"

    # Client Static Paths
    @app.route("/app/<path:filename>")
    def static_proxy_app(filename):
        return app.send_static_file("app/" + filename)

    # Docs Static Paths
    @app.route("/docs/<path:filename>")
    def static_proxy_docs(filename):
        return flask.send_from_directory(docs_directory, filename)

    # Notebooks Static Paths
    @app.route("/notebooks/<path:filename>")
    def static_proxy_notebooks(filename):
        return flask.send_from_directory(notebooks_directory, filename)

    client_routes(app)
    return app


def run(port=8000, host="0.0.0.0", *args, **kwargs):
    """Run the flask server."""
    print(f"\nGo to http://localhost:{port}\n")
    app = get_app(*args, **kwargs)
    app.run(port=port, host=host)
