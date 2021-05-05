from app import *
from app.model import *
import datetime

# Post Sample Data
post_first =MKT_QUESTION (Title ="Customer Images Status Pending", Body="I am upload a kaliLnux",BestAnswer=1, Tag=" ",Vote=1, User=1, Created= datetime.datetime.now().strftime("%Y-%m-%d"))
post_second =MKT_QUESTION (Title ="Is it posible to point a subdirectory to another domain?", Body="I maybe asking a stupid question here ", BestAnswer=1, Tag=" ",Vote=1, User=1,Created=datetime.datetime.now().strftime("%Y-%m-%d"))
post_third =MKT_QUESTION (Title ="Set Up With Domain", Body="I am upload a kaliLnux",BestAnswer=1, Tag=" ",Vote=1, User=1,Created=datetime.datetime.now().strftime("%Y-%m-%d"))

db.session.add(post_first)

db.session.add(post_second)

db.session.add(post_third)

db.session.commit()

