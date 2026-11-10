from services.theme_service import ThemeService
from exceptions.theme_exception import DuplicateThemeError,ThemeNotFoundError
import pytest

@pytest.fixture
def theme_service():
    return ThemeService()

def test_add_theme(theme_service):
    theme_service.add_theme(theme_name="Little Teddy", category="Teddy", price=2500)
    assert len(theme_service.get_all_themes()) == 1
    
def test_duplicate_add_theme(theme_service):
    theme_service.add_theme(theme_name="Little Teddy", category="Funny", price=2400)
    with pytest.raises(DuplicateThemeError, match="Duplicate item"):
        theme_service.add_theme(theme_name="Little Teddy", category="Teddy", price=1800)

@pytest.mark.parametrize("price",[-100,200,-500])
def test_add_theme_negative_price(theme_service,price):
    with pytest.raises(ValueError):
        theme_service.add_theme(theme_name="Little Teddy", category="Teddy", price=price)
        
@pytest.mark.parametrize("theme_name",[None, "", " ", 123])
def test_add_theme_invalid_name(theme_service,theme_name):
    with pytest.raises(ValueError):
        theme_service.add_theme(theme_name=theme_name, category="Teddy", price=3000)

@pytest.mark.parametrize("category",[None,""," " , 123])
def test_add_theme_invalid_category(theme_service,category):
    with pytest.raises(ValueError):
        theme_service.add_theme(theme_name="Little Teddy", category=category, price=500)
        
def test_list_of_theme(theme_service):
   theme_service.add_theme(theme_name="Little Teddy", category="Funny", price=1450)
   result = theme_service.get_all_themes()
   assert len(result) == 1
   assert result[0]["theme_name"] == "Little Teddy"
   assert result[0]["category"] == "Funny"
   assert result[0]["price"] == 1450
   
def test_get_theme_by_category(theme_service):
    theme_service.add_theme(theme_name="Little Teddy", category="Funny", price=1500)
    theme_service.add_theme(theme_name="Forest Grump", category="Adventure", price=1650)
    theme_service.add_theme(theme_name="Police officer", category="Funny", price=2450)
    
    result = theme_service.get_all_themes()
    assert len(result) == 3
    result_1 = theme_service.get_theme_by_category("Funny")
    assert len(result_1) == 2
    assert result_1[0]["theme_name"] == "Little Teddy"
    assert result_1[0]["category"] == "Funny"
    assert result_1[0]["price"] == 1500
    assert result_1[1]["theme_name"] == "Police officer"
    assert result_1[1]["category"] == "Funny"
    assert result_1[1]["price"] == 2450
    result_2 = theme_service.get_theme_by_category("Adventure")
    assert len(result_2) == 1
    assert result_2[0]["theme_name"] == "Forest Grump"
    assert result_2[0]["category"] == "Adventure"
    assert result_2[0]["price"] == 1650