from peewee import *
import datetime



db = SqliteDatabase('inventory.db')


class Product(Model):
    product_name = CharField()
    inventory = IntegerField(default=0)
    price = DecimalField(decimal_places=2, auto_round=True)
    unit_type = CharField(null = True)
    ideal_stock = IntegerField()
    image_path = CharField(null=True)
    last_updated = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def all(cls):
        return list(Product.select())

    @classmethod
    def add_product(cls, name, stock, price, unit_type, ideal_stock, image_path=None):
        product, created = Product.get_or_create(
            product_name=name,
            defaults={
                'inventory': stock,
                'price': price,
                'unit_type': unit_type,
                'ideal_stock': ideal_stock,
                'image_path': image_path
            }
        )
        return product
    
    # Deletes the chosen product
    @classmethod
    def delete_product(cls, name):
        product = Product.get_product(name)
        product.delete_instance()

    # Returns the information of the chosen product
    @classmethod
    def get_product(cls, name):
        product = Product.get(Product.product_name == name)
        return product
    
    #TODO other update methods

    # Updates price
    @classmethod
    def update_price(cls, name, increase):
        product = Product.get_product(name)
        product.price += increase
        product.save()

    # Update ideal stock
    @classmethod
    def update_ideal_stock(cls, name, increase):
        product = Product.get_product(name)
        product.ideal_stock += increase
        product.save()

    # Updates the current available stock of a product
    @classmethod
    def update_stock(cls, name, new_stock):
        product = Product.get_product(name)
        product.inventory += new_stock
        product.save()

        
    class Meta:
        database = db


# if __name__ == "__main__":
#     add_product("Toilet Paper", 5, 20.00, "rolls", 100, "images/tp.jpg")
#     update_stock("Toilet Paper", 5)
#     # Uncomment to test delete_product
#     """delete_product("Toilet Paper")"""