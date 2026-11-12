from exceptions.theme_exception import ThemeNotFoundError, DuplicateThemeError

class ThemeService: 
    
    def __init__(self):
        self.is_available = True
        self.list_of_themes = []
        
    def _validate_theme(self, theme_name):
        if theme_name is None:
            raise ValueError("Theme name cannot be empty")
        if not isinstance(theme_name, str):
            raise ValueError("Theme name must be string")
        if not theme_name.strip():
            raise ValueError("Theme name cannot be empty or just whitspace ")
        
    def _validate_category(self, category):
        if category is None:
            raise ValueError("Category cannot be empty")
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if not category.strip():
            raise ValueError("Category cannot be empty or just whitspace")
        
    def _validate_price(self,price):
        if price is None:
            raise ValueError("Price cannot be empty")
        if not isinstance(price,(int,float)):
            raise ValueError("Category must be a number or float")
        if price < 0 :
            raise ValueError("Price cannot be negative value")
        if price < 500:
            raise ValueError("Price cannot be less than 500")
        
    def add_theme(self,theme_name, category, price ):
        self._validate_theme(theme_name)
        self._validate_category(category)
        self._validate_price(price)
        for i in self.list_of_themes:
            if i["theme_name"] == theme_name.strip():
                raise DuplicateThemeError("Duplicate item")
        theme = {"theme_name":theme_name, "category":category, "price":price,"is_available":self.is_available}
        self.list_of_themes.append(theme)
    
    def get_all_themes(self): 
        return self.list_of_themes
    
    def get_theme_by_category(self,category):
        self._validate_category(category)
        list_of_category = []
        for i in self.list_of_themes:
            if i["category"].strip().casefold() == category.strip().casefold():
                list_of_category.append(i)
        return list_of_category
    
    def update_theme_availability(self, theme_name, availability:bool):
        for i in self.list_of_themes:
            if i["theme_name"] == theme_name:
                i["is_available"] = availability
                return f'Updated successfully'
        raise ThemeNotFoundError("Theme Not found!")
    
    def update_theme(self, theme_name , update_data:dict):
        for i in self.list_of_themes:
            if i["theme_name"] == theme_name:         # Theme Name validation and duplication check 
                if "theme_name" in update_data:
                    if update_data["theme_name"] is None:
                        raise ValueError("Theme name cannot be None")
                    if not isinstance(update_data["theme_name"], str):
                        raise ValueError("Theme name must be string")
                    if not update_data["theme_name"].strip():
                        raise ValueError("The theme name cannot be empty or just whitspace")
                    for j in self.list_of_themes:
                         if j is not i:
                            if j["theme_name"] == update_data["theme_name"]:
                                raise DuplicateThemeError("Theme already exist")
                if "category" in update_data:          # Category field validation
                    if update_data["category"] is None:
                        raise ValueError("Category cannot be empty")
                    if not isinstance(update_data["category"], str):
                        raise ValueError("Category must be a string")
                    if not update_data["category"].strip():
                        raise ValueError("Categeory cannto be empty or just whitespace")
                if "price" in update_data:           # price validation
                    if update_data["price"] is None:
                        raise ValueError("price cannot be none")
                    if not isinstance(update_data["price"], (int,float)):
                        raise ValueError("Price must be integer")
                    if update_data["price"] < 0 :
                        raise ValueError("Price cannot be negative valude")
                    if update_data["price"] < 500 :
                        raise ValueError("Minimum price is 500")
              # update block   
                if "theme_name" in update_data:
                     i["theme_name"] = update_data["theme_name"].strip()
                if "category" in update_data:
                    i["category"] = update_data["category"].strip()
                if "price" in update_data:    
                    i["price"] = update_data["price"]     
                return i
        raise ThemeNotFoundError("Theme Not found!")

    def theme_delete(self,theme_name):
        for i in self.list_of_themes:
            if i["theme_name"] == theme_name.strip():
                self.list_of_themes.remove(i)
                return f"Successfully Deleted"
        raise ThemeNotFoundError("Theme Not found!")
