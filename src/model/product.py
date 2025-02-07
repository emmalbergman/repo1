from peewee import *
import datetime
from typing import Optional



db = SqliteDatabase('inventory.db')


class Product(Model):
    product_name = CharField()
    inventory = IntegerField(default=0)
    price = DecimalField(decimal_places=2, auto_round=True)
    unit_type = CharField(null = True)
    ideal_stock = IntegerField()
    image_path = CharField(null=True)
    last_updated = DateTimeField(default=datetime.datetime.now)

    @staticmethod
    def all() -> list['Product']:
        return list(Product.select())

    @staticmethod
    def add_product(name: str, stock: int, price: float, unit_type: str, ideal_stock: int, image_path: str = None) -> 'Product':
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
    @staticmethod
    def delete_product(name: str):
        product = Product.get_product(name)
        product.delete_instance()

    # Returns the information of the chosen product
    @staticmethod
    def get_product(name: str) -> Optional['Product']:
        product = Product.get(Product.product_name == name)
        return product
    
    #TODO other update methods

    # Updates price
    @staticmethod
    def update_price(name: str, increase: float):
        product = Product.get_product(name)
        product.price += increase
        product.save()

    # Update ideal stock
    @staticmethod
    def update_ideal_stock(name: str, increase: int):
        product = Product.get_product(name)
        product.ideal_stock += increase
        product.save()

    # Updates the current available stock of a product
    @staticmethod
    def update_stock(name: str, increase: int):
        product = Product.get_product(name)
        product.inventory += increase
        product.save()

        
    class Meta:
        database = db


# if __name__ == "__main__":
#     add_product("Toilet Paper", 5, 20.00, "rolls", 100, "images/tp.jpg")
#     update_stock("Toilet Paper", 5)
#     # Uncomment to test delete_product
#     """delete_product("Toilet Paper")"""