"""Models for Adopt"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet"""
    __tablename__ = "pets"

    def get_default_photo_url(self):
        """Return default photo url"""
        return 'https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg'
    
    default_photo_url = property(fget=get_default_photo_url)

    id        = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name      = db.Column(db.String(70), nullable=False)
    species   = db.Column(db.String(70), nullable=False)
    age       = db.Column(db.Integer)
    notes     = db.Column(db.String(2200))
    photo_url = db.Column(
                db.String(2048), 
                nullable=False,
                default=get_default_photo_url
            )
    available = db.Column(db.Boolean(), nullable=False, default=True)
    
    def __repr__(self):
        p = self
        return f'<Pet id={p.id} name={p.name} species={p.species} age={p.age} notes={p.notes} photo_url={p.photo_url}>'

