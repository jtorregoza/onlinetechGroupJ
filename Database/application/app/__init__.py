from application.app.models import db

app = FLASK(__tablename__, static_folder=None)
static_folder=None)
db.init_app(app)
