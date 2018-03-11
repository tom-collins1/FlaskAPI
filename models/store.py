from db import db

class StoreModel(db.Model):  #have made itemmodel an extension of SQLAlchemy so inherits its functions
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    items = db.relationship('ItemModel', lazy='dynamic')  #looking for items that share store.id as relationship
    #it will go into itemmodel and see that there is field with foreignkey based on stores.id
    #and essentially does inner join on tables by this storeid
    #However each time we create a store or an item it will automatically create a relationship object
    #so by including the lazy 'dynamic' we don't do that YET, when we call the JSON, instead of just calling a 
    #list 'items' it will call a query to fetch the items from the table, hence the .all() at the end
    
    def __init__(self, name):
        self.name = name
        
    def json(self):
        return {'name':self.name, 'items':[item.json() for item in self.items.all()]}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()   #select * from __tablename__ where name = name
    
    def save_to_db(self):       #was insert, but it also acts as update
        db.session.add(self)     #SQLAlchemy can turn row into object and vice versa
        db.session.commit()      #session is a collection of objects we write to the db

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit() 