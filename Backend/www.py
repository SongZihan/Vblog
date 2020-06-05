from application import app
from pages.api import api
from pages.get_data import get_data

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(get_data, url_prefix="/get_data")
