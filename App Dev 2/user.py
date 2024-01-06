class User:
    def __init__(self,name, password, email,role,cart):
        self.__name = name
        self.__password = password
        self.__email = email
        self.__role = role
        self.__cart = cart

    #Accessors
    def get_name(self):
        return self.__name
        
    def get_password(self):
        return self.__password
        
    def get_email(self):
        return self.__email
    
    def get_role(self):
        return self.__role

    def get_cart(self):
        return self.__cart
    
    #Mutators
    def set_name(self,name):
        self.__name = name
    
    def set_password(self,password):
        self.__password = password
    
    def set_email(self,email):
        self.__email = email

    def set_role(self,role):
        self.__role = role

    def set_cart(self,cart):
        self.__cart = cart