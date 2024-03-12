class Ticket:
    price = 100
    f_price = price*1.2
    def f_day(self):
        self.c_price = 0.5 * self.f_price
        adult = float(input("几个大人:"))
        children = float(input("几个小孩:"))
        total = adult*self.f_price+children*self.c_price
        print("总价格为:%d" % total)

    def n_day(self):
        self.c_price = 0.5 * self.price
        adult = float(input("几个大人:"))
        children = float(input("几个小孩:"))
        total = adult*self.price+children*self.c_price
        print("总价格为:%d" % total)

a = Ticket()
a.n_day()
a.f_day()