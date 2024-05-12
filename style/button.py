from datetime import date

today = date.today()
print("Current Date : ", today)


def create_app():
    app = Flask(__name__)
    moment.init_app(app)
    return app
app = create_app(prod_config)