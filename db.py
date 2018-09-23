from sqlalchemy.sql import func
from sqlalchemy.sql.expression import bindparam
from datetime import timedelta
from sqlalchemy import Interval
from app.models import Orders, db
from datetime import datetime


#delivery_date = func.dateadd(func.now(), bindparam('tomorrow', timedelta(days=1), Interval()))
user1 = Orders('abc123', 'puneet@ct.com', datetime.now(), datetime.now() + timedelta(days=1))
user2 = Orders('def123', 'amit@ct.com', datetime.now(), datetime.now() + timedelta(days=1))
db.create_all()
db.session.add(user1)
db.session.add(user2)
db.session.commit()
#print(Orders.query.filter_by(email_id='puneet@ct.com').all())
