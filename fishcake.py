class fishcake:
    def __init__(self, **kwargs):
        self.size=10
        self.flavor="팥"
        self.price=100

        if "size" in kwargs:
            self.size= kwargs.get("size")
        if "flavor" in kwargs:
            self.flavor=kwargs.get("flavor")
        if "price" in kwargs:
            self.price=kwargs.get("price")

    def show(self):
        print("붕어빵 크기{}".format(self.size))
        print("붕어빵 종류{}".format(self.flavor))
        print("붕어빵 가격{}".format(self.price))
        print("*"*30)

fish1 = fishcake()
fish2 = fishcake(size=20, price=30)
fish3 = fishcake(flavor="초콜릿", size=15)

fish1.show()
fish2.show()
fish3.show()

class marcket(fishcake):
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)
        self.market_price = self.price + margin
    def show(self):
        print(self.flavor,self.market_price)
fish1=marcket(size=20, price=500)
fish1.show()
