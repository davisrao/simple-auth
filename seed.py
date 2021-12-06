"""simple file to run & create db / tables"""

from app import db

db.drop_all()
db.create_all()

db.session.commit()