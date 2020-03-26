class Deal:
    buyer = ""
    seller = ""
    sum_with_curr = ""
    con_nr = 0

    def __init__(self, buyer, seller, sum_with_curr, con_nr):
        self.buyer = buyer
        self.seller = seller
        self.sum_with_curr = sum_with_curr
        self.con_nr = int(con_nr.split(" ")[1])
