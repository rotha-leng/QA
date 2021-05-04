from app import *
from flask_blog.model import *

# Post Sample Data
post_first = Post(Title="First Post", Content="Content for the first post")
post_second = Post(Title="Second Post",Content="Content for the second post")

post_third = Post(Title="Second Post",Content="Content for the third post")


db.session.add(post_first)

db.session.add(post_second)

db.session.add(post_third)

db.session.commit()

#Author Sample Data


Samnang = Author(AuthorName="Samnang",AuthorPassword="123456")
Rady = Author(AuthorName="Rady",AuthorPassword="654321")
Narun = Author(AuthorName="Narun",AuthorPassword="24689")


with app.app_context():
    db.session.add(Samnang)
    db.session.add(Rady)
    db.session.add(Narun)
    db.session.commit()

