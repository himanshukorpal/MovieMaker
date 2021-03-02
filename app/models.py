from app import db

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)


    def __repr__(self):
        return f'<Template {self.title}>'

