from models import db, User


user = User.query.get('id')
db.session.delete(user)
db.session.commit()