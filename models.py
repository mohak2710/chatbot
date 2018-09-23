from app import db

class Orders(db.Model):
    order_id = db.Column(db.String(255), primary_key=True)
    email_id = db.Column(db.String(255))
    order_date = db.Column(db.DateTime(), server_default=db.func.now())
    delivery_date = db.Column(db.DateTime(), server_default=db.func.now())

    def __init__(self, order_id, email_id, order_date, delivery_date):
        self.order_id = order_id
        self.email_id = email_id
        self.order_date = order_date
        self.delivery_date = delivery_date

    def __repr__(self):
        return '<Order Id %r>' % self.order_id



