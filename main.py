from fastapi import FastAPI, HTTPException
from services.theme_service import ThemeService
from models.theme import ThemeCreate, Theme_update, ThemeUpdateAvailability
from exceptions.theme_exception import ThemeNotFoundError, DuplicateThemeError

app = FastAPI()

a = ThemeService()

@app.get("/")
def home():
    return {"message": "Welcome to Baby studio App"}

@app.get("/themes")
def get_themes(): 
    result=a.get_all_themes()
    return result

@app.post("/themes", status_code=201)
def add_themes(theme : ThemeCreate):
    try:
        a.add_theme(theme.theme_name, theme.category, theme.price)
        return {"message": "Succesfully added"}
    except DuplicateThemeError:
        raise HTTPException(status_code=409, detail="Duplicate theme Exist")
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid Input")
    
@app.patch("/theme/{theme_name}")
def update_theme(theme_name:str ,theme : Theme_update):
    update_data = theme.model_dump(exclude_unset=True)
    try:
        a.update_theme(theme_name, update_data)
        return {"message": "Successfully updated"}
    except ThemeNotFoundError :
        raise HTTPException(status_code=404, detail="Theme Not Found")
    except DuplicateThemeError:
        raise HTTPException(status_code=409, detail="Duplicate Theme Exist")
    except ValueError:
        raise HTTPException(status_code=422, detail='InvalidInput')

@app.delete("/theme/{theme_name}")
def delete_theme(theme_name: str):
    try:
       a.theme_delete(theme_name)
       return {"message": "Successfully Deleted"}
    except ThemeNotFoundError:
            raise HTTPException(status_code=404, detail="ThemeNotFoundError")

@app.patch("/theme/{theme_name}/availability")
def update_availability(theme_name:str, availability: ThemeUpdateAvailability):
    try:
        a.update_theme_availability(theme_name,availability.is_available)
        return {"message":"Sucessfully updated"}
    except ThemeNotFoundError:
        raise HTTPException(status_code=404, detail="Theme not found")