from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://images.yaoota.com/Zn1GtntKyaVe2hIrp27tRTEJADM=/trim/yaootaweb-production-ke/media/crawledproductimages/1ac8a519b7edd9932fadcc9dea2d1eeb42af81bd.jpg" 
def connect_db(app):
    """ Connect to database """

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ Adoptable pet data model """

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """ Return pet image """

        return self.photo_url or DEFAULT_IMAGE_URL