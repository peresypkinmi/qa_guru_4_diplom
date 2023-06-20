from models.product import Product


class Cart:
    cartPackages = []
    cartPackageProduct = {"product": Product,
                          "quantity": 0
                          }

    @staticmethod
    def add_product_to_cart(product, quantity):
        Cart.cartPackageProduct['product'] = product
        Cart.cartPackageProduct['quantity'] += quantity
        Cart.cartPackages.append(Cart.cartPackageProduct)
