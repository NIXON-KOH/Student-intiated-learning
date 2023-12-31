class User:
    def __init__(self, id_, Role, name, JoinDate, Password, Image, Email):
        self.__id_ = id_
        self.__Role = Role
        self.__name = name
        self.__JoinDate = JoinDate
        self.__Password = Password
        self.__Image = Image
        self.__Email = Email

    def set_id_(self, id_):
        self.__id_ = id_

    def get_id_(self):
        return self.__id_

    def set_Role(self, Role):
        self.__Role = Role

    def get_Role(self):
        return self.__Role

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_JoinDate(self, JoinDate):
        self.__JoinDate = JoinDate

    def get_JoinDate(self):
        return self.__JoinDate

    def set_Password(self, Password):
        self.__Password = Password

    def get_Password(self):
        return self.__Password

    def set_Image(self, Image):
        self.__Image = Image

    def get_Image(self):
        return self.__Image

    def set_Email(self, Email):
        self.__Email = Email

    def get_Email(self):
        return self.__Email


class Customer(User):
    def __init__(self, id_, Role, name, JoinDate, Password, Image, Email, Address, PaymentMethod, Cart, History, Points):
        super().__init__(id_, Role, name, JoinDate, Password, Image, Email)
        self.__Address = Address
        self.__PaymentMethod = PaymentMethod
        self.__Cart = Cart
        self.__History = History
        self.__Points = Points

    def set_Address(self, Address):
        self.__Address = Address

    def get_Address(self):
        return self.__Address

    def set_PaymentMethod(self, PaymentMethod):
        self.__PaymentMethod = PaymentMethod

    def get_PaymentMethod(self):
        return self.__PaymentMethod

    def set_Cart(self, Cart):
        self.__Cart = Cart

    def get_Cart(self):
        return self.__Cart

    def set_History(self, History):
        self.__History = History

    def get_History(self):
        return self.__History

    def set_Points(self, Points):
        self.__Points = Points

    def get_Points(self):
        return self.__Points
    
class Admin(User):
    def __init__(self, id_, Role, name, JoinDate, Password, Image, Email):
        super().__init__(id_, Role, name, JoinDate, Password, Image, Email)