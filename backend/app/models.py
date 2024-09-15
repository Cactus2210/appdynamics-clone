from . import db

class APIStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    status_code = db.Column(db.Integer, nullable=False)
    latency = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<APIStatus {self.url}>'
