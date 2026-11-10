from pydantic import BaseModel,Field, ConfigDict, model_validator
from typing import Optional

class ThemeCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    theme_name : str = Field(..., min_length=3)
    category : str = Field(..., min_length=3)
    price : int = Field(ge =500)

class Theme_update(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    theme_name : Optional[str] = Field(default=None,min_length=3)
    category : Optional[str] = Field(default=None,min_length=3)
    price : Optional[int] = Field(default=None,ge=500)
    
    @model_validator(mode="after")
    def check_atleast_one_value(self):
        if not self.model_fields_set:
            raise ValueError ("Provide alteast one parameter to update")
        if "theme_name" in self.model_fields_set and self.theme_name is None:
            raise ValueError ("Theme name cannot be None")
        if "category" in self.model_fields_set and self.category is None:
            raise ValueError("category cannot by None")
        if "price" in self.model_fields_set and self.price is None:
            raise ValueError("Price cannot be None")
        return self

class ThemeUpdateAvailability(BaseModel):
    is_available : bool = Field(...)