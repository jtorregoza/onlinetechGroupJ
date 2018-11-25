from models import db, User

"""Create Data"""
user = User(username='username',
            password='password',
            first_name='first_name',
            last_name='last_name')
db.session.add(user)
db.session.commit()
