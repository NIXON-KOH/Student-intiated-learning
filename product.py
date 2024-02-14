class Items:
    def __init__(self,id_,name, Image, Stocks, Desc, Type):
        self.__id_ = id_
        self.__name = name
        self.__Image = Image
        self.__Stocks = Stocks
        self.__Desc = Desc
        self.__Type = Type
        

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    
    def set_ID(self, id_):
        self.__id_ = id_
    def get_ID(self):
        return self.__id_

    def set_Image(self, Image):
        self.__Image = Image

    def get_Image(self):
        return self.__Image

    def set_Stocks(self, Stocks):
        self.__Stocks = Stocks

    def get_Stocks(self):
        return self.__Stocks

    def set_Desc(self, Desc):
        self.__Desc = Desc

    def get_Desc(self):
        return self.__Desc

    def set_Type(self, Type):
        self.__Type = Type

    def get_Type(self):
        return self.__Type
    
 
    

class Product(Items):
    def __init__(self,id_, name,Image, Stocks, Desc, points,Type, categories,RetailCost,gender,ListCost):
        super().__init__(id_, name, Image, Stocks, Desc,Type)
        self.__points = points
        self.__Categories = categories
        self.__RetailCost = RetailCost
        self.__gender = gender
        self.__ListCost = ListCost
    
    def set_Categories(self, Categories):
        self.__Categories = Categories

    def get_Categories(self):
        return self.__Categories
    
    def set_points(self, points):
        self.__points = points

    def get_points(self):
        return self.__points
    
    def set_RetailCost(self, RetailCost):
        self.__RetailCost = RetailCost 
    
    def get_RetailCost(self):
        return self.__RetailCost

    def get_gender(self):
        return self.__gender
    
    def set_gender(self,gender):
        self.__gender = gender

    def set_ListCost(self, ListCost):
        self.__ListCost = ListCost

    def get_ListCost(self):
        return self.__ListCost
    
    
class Rewards(Items):
    def __init__(self,id_, name,Image, Stocks, Desc, Type, points,Status):
        super().__init__(id_, name, Image, Stocks, Desc, Type)
        self.__points = points
        self.__Status = Status #active or inactive
    
    def get_points(self):
        return self.__points
    
    def Change_point(self,change):
        self.__points -= change

    def set_status(self, status):
        self.__Status = status

    def get_status(self):
        return self.__Statusw
    