from application import db

class result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return ''.join([
        'id: ', self.id, 'r\n',
        'result: ', self.result, 'r\n'
        ])