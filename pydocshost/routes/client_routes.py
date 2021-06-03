from flask import (Flask)
from pathlib import Path


def client_routes(app: Flask, client_path: Path):
    @app.route(f"/static/<path:folder>/<path:filename>")
    def client_static_proxy(folder, filename):
        return app.send_static_file(f"client/static/{folder}/{filename}")

    @app.route("/manifest.json")
    def client_static_proxy_manifest():
        return app.send_static_file("client/manifest.json")

    @app.route("/index.html")
    def client_static_proxy_index():
        return app.send_static_file("client/index.html")

    @app.route("/")
    def client_static_proxy_main():
        return app.send_static_file("client/index.html")
