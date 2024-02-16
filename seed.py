from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

p1 = Pet(name='Garfield', species="cat", age=8, photo_url='https://www.usatoday.com/gcdn/-mm-/f6f3f3cf43d5448402a4073afc01a172a751fe0c/c=266-0-4432-3132/local/-/media/2018/02/11/USATODAY/USATODAY/636539511833123779-USP-News--Westminster-Kennel-Club-Dog-Show.1.jpg', notes='Loves lasagna and hates Mondays')
p2 = Pet(name='Dug', species="dog", age=2, photo_url='https://goldenmeadowsretrievers.com/wp-content/uploads/2023/08/Why-Do-Golden-Retrievers-Smile.webp', notes='Easily distracted by squirrels')
p3 = Pet(name='Spike', species="porcupine", age=0, photo_url='https://images.squarespace-cdn.com/content/v1/5e7368b3afeddc0b272b356e/1634793145626-RLSPCJ8A8LBEKWV3E8YR/4E6FD8B3-45F0-44D3-8891-039A0299650E.jpeg?format=1500w')

db.session.add_all([p1, p2, p3])
db.session.commit()



