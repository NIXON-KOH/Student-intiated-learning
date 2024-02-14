class Transaction:
    def __init__(self, date, products, cust, status, price):
        self.__date = date
        self.__products = products 
        self.__cust = cust
        self.__status = status
        self.__price = price
    
    def get_date(self):
        return self.__date
    def get_products(self):
        return self.__products
    def get_cust(self):
        return self.__cust
    def get_status(self):
        return self.__status
    def get_price(self):
        return self.__price
    
