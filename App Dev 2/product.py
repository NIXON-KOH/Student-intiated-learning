class Products:
    def __init__(self, name, pricing, categories,gender,color,typed, rating,image):
        self.__name = name
        self.__pricing = pricing
        self.__categories = categories
        self.__gender = gender
        self.__color = color
        self.__typed = typed
        self.__rating = rating
        self.__image = image

    #Accessors 
    def get_name(self):
        return self.__name
    
    def get_pricing(self):
        return self.__pricing
    
    def get_categories(self):
        return self.__categories
    
    def get_gender(self):
        return self.__gender
    
    def get_color(self):
        return self.__color
    
    def get_typed(self):
        return self.__typed
    
    def get_rating(self):
        return self.__rating

    def get_image(self):
        return self.__image
    
    #Mutators
    def set_name(self, name):
        self.__name  = name
    
    def set_pricing(self, pricing):
        self.__pricing = pricing
    
    def set_categories(self,categories):
        self.__categories = categories
    
    def set_gender(self,gender):
        self.__gender = gender

    def set_color(self,color):
        self.__color = color

    def set_typed(self,typed):
        self.__typed = typed

    def set_rating(self,rating):
        self.__rating = rating
    
    def set_image(self,image):
        self.__image = image