from app import *
from app.model import *
import datetime

# Post Sample Data
"""post_first = MKT_COMMENT(Question_ID=1, Comment="Hello", User_ID=1, Created_On="")
post_second = MKT_COMMENT(Question_ID=2, Comment="Nice", User_ID=2, Created_On="")
post_third = MKT_COMMENT(Question_ID=3, Comment="bye", User_ID=3, Created_On="")"""

post_first = MKT_ANSWER(QuestionID=1, Answer="you should", User=1, Created_On="")
post_second = MKT_ANSWER(QuestionID=1, Answer="you try", User=2, Created_On="")
post_third = MKT_ANSWER(QuestionID=1, Answer="you add", User=3, Created_On="")


db.session.add(post_first)

db.session.add(post_second)

db.session.add(post_third)

db.session.commit()
