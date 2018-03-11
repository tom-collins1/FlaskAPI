from db import db

class ItemModel(db.Model):  #have made itemmodel an extension of SQLAlchemy so inherits its functions
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))  #used to talk to the store objects id field
    store = db.relationship('StoreModel')  #will look into storemodel and know they are linked by stores.id
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
        
    def json(self):
        return {'name':self.name, 'price':self.price, 'store_id' : self.store_id}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()   #select * from __tablename__ where name = name
    
    def save_to_db(self):       #was insert, but it also acts as update
        db.session.add(self)     #SQLAlchemy can turn row into object and vice versa
        db.session.commit()      #session is a collection of objects we write to the db

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit() 