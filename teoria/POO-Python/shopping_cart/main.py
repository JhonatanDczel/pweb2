from shopping.product_stock import ProductStock
from shopping.stock_products import StockProducts
from shopping.shopping_cart import ShoppingCart

class Main:
  @staticmethod
  def main():
    stock = StockProducts()
    stock.add_product(ProductStock("monitor", 500, 100))
    stock.add_product(ProductStock("telefono", 150, 300))
    stock.add_product(ProductStock("teclado", 70, 50))
    stock.add_product(ProductStock("mouse", 50, 50))

    cart = ShoppingCart(stock)

    cart.add_item("monitor", 2)
    cart.add_item("telefono", 5)
    cart.add_item("teclado", 2)

    print()
    print(cart)

    cart.finalize_purchase()

      
  
Main.main()
