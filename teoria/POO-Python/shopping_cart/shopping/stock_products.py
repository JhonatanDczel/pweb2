from .product_stock import ProductStock

class StockProducts:
  def __init__(self):
    self._products = {}

  def add_product(self, product):
    self._products[product.name] = product
    print(f"Producto {product.name} ({product.quantity} unidades) agregado en stock exitosamente...")

  def get_product(self, name):
    return self._products.get(name)

  def delete_products(self, name, quantity):
    if self._products[name].quantity >= quantity:
      self._products[name].quantity -= quantity 
    else:
      print("Producto no encontrado...")
