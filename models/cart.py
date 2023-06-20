from models.product import Product


class Cart:
    cartPackages = []
    cartPackageProduct = {'product': Product,
                          'quantity': 0}

    @classmethod
    def add_product_to_cart_packages(cls, test_product, quantity):
        cls.cartPackageProduct['product'] = test_product
        cls.cartPackageProduct['quantity'] = quantity
        cls.cartPackages.append(cls.cartPackageProduct)
