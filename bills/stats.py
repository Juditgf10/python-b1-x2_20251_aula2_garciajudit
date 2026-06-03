# Write your imports here
from itertools import count, product

from .item import Bill, Product
from .entity import Buyer, Seller

class OrderType:
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        self.bills = bills

    def find_top_sell_product(self) -> tuple[Product, int]:
        products_count = {}
        for bill in self.bills:
            for product in bill.products:
                if product.product_id not in products_count:
                    products_count[product.product_id] = [product, 0]
                products_count[product.product_id][1] += 1
        product, count = max(
        products_count.values(),
        key=lambda x: x[1]
        )
        return (product, count)


    def find_top_two_sellers(self) -> list:
        totals = {}
        for bill in self.bills:
            seller = bill.seller
            if seller not in totals:
                totals[seller] = 0
            totals[seller] += bill.calculate_total()
        ordered = sorted(totals.items(), key=lambda x: x[1], reverse=True)
        return [seller for seller, total in ordered[:2]]   


    def find_buyer_lowest_total_purchases(self):
        totals = {}
        for bill in self.bills:
            buyer = bill.buyer
            if buyer not in totals:
                totals[buyer] = 0
            totals[buyer] += bill.calculate_total()
        buyer = min(totals, key=totals.get)
        return buyer, totals[buyer]


    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        products = []
        for bill in self.bills:
             for product in bill.products:
                  products.append(
                    (product, product.calculate_total_taxes())
                  )
        reverse = (order_type == OrderType.DES)
        products.sort(key=lambda x: x[1], reverse=reverse)
        return products
        

    def show(self):
        print("Bills")
        for bill in self.bills:
            bill.print()
