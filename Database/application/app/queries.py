from models import User


"""Querying Data Primary Key"""
User.query.get('primary_key')

"""Filter"""
User.query.filter_by(column='filter_value').first()
User.query.filter_by(column='filter_value').all()

User.query.filter_by(User.first_name == 'first_name').first()
User.query.filter_by(User.first_name == 'first_name').first()

"""Order"""
User.query.order_by(User.last_name).first()
User.query.order_by(User.last_name).all()

User.query.order_by(User.last_name.desc()).first()
User.query.order_by(User.last_name.desc()).all()

"""Limit"""
User.query.limit(1).first()
User.query.limit(1).all()

"""Offset"""
User.query.offset(1).first()
User.query.offset(1).all()