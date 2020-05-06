from application import db
from application.models import result

db.drop_all()
db.create_all()