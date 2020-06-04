from application import app
from pages.api import api

app.register_blueprint(api, url_prefix="/api")

