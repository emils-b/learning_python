
class Company:

    def __init__(self, name, starting_cap):
        self.name = name
        self.starting_cap = starting_cap
        self.deals = []
        self.purchases = 0
        self.sales = 0

    def deals_print(self):
        for d in self.deals:
            print(d.buyer + " " + d.seller)

    def get_sales_total(self):
        sales = 0
        for deal in self.deals:
            if deal.seller == self.name:
                sales += int(deal.sum_with_curr[0:-3])
        return sales

    def get_purchases_total(self):
        purchases = 0
        for deal in self.deals:
            if deal.buyer == self.name:
                purchases += int(deal.sum_with_curr[0:-3])
        return purchases

    def get_final_balance(self):
        balance = self.starting_cap + self.get_sales_total() - self.get_purchases_total()
        return balance

    def get_total_purchases_count(self):
        purchases_counter = 0
        for deal in self.deals:
            if deal.buyer == self.name:
                purchases_counter += 1
        return purchases_counter

    def get_total_sales_count(self):
        sales_counter = 0
        for deal in self.deals:
            if deal.seller == self.name:
                sales_counter += 1
        return sales_counter

    def get_purchase_stats(self):
        print("Starting balance was: "+str(self.starting_cap)+". Final balance is: "+str(self.get_final_balance())+
              ".\nTotal purchases made: "+str(self.get_total_purchases_count())+
              " Total sales made: "+str(self.get_total_sales_count())+".")

