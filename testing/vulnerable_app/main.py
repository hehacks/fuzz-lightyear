import os

from .app import get_current_application
from .core.routes import configure_routes


def main():
    app = get_current_application()

    configure_routes(app)

    app.run(
        '0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
    )