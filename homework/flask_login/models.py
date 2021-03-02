from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self):
        return "<User(name='%s', email='%s', password='%s')>" % (
            self.name, self.email, self.password)

    class Order(db.Model):
        __tablename__ = 'order'

        id = db.Column(db.Integer, primary_key=True)
        order_time = db.Column(db.datetime.now().isoformat())
        user_id = db.Column(db.Integer)

        def __repr__(self):
            return "<Order(order_id='%s', order_time='%s', user_id='%s'>" % (self.id, self.order_time, self.user_id)

    class OrderLine(db.Model):
        __tablename__ = 'order_line'

        id = db.Column(db.Integer, primary_key=True)
        product_name = db.Column(db.String(80), unique=True, nullable=False)
        product_price = db.Column(db.Integer)

        def __repr__(self):
            return "<OrderLine(id='%s', product_name='%s', product_price='%s')>" % (
                self.id, self.product_name, self.product_price)
