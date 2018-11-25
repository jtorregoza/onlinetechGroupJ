from models import db, User


user = User.query.get('id')
user.password = 'password'
db.session.commit()