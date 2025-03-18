import pytest
from src.data.warehouse import ProcessingMining as pm
from src.model.resource import Resource
from src.model.citizen import Citizen

@pytest.fixture(scope='module', autouse=True)
def setup_stat():
    pm.clear_warehouse()
    pm.clear_statistic()
    params = [{'name': 'still', 'category' : 'iron', 'date': '15.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'D', 'citizen' :Citizen(name = 'Egor', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'still', 'category' : 'iron', 'date': '15.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'D', 'citizen' :Citizen(name = 'Egor', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'gold', 'category' : 'iron', 'date': '15.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'D', 'citizen' :Citizen(name = 'Bob', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'dub', 'category' : 'wood', 'date': '18.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'A', 'citizen' :Citizen(name = 'Bob', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'dub', 'category' : 'wood', 'date': '18.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'A', 'citizen' :Citizen(name = 'Bob', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'topol', 'category' : 'wood', 'date': '18.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'A', 'citizen' :Citizen(name = 'Max', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'topol', 'category' : 'wood', 'date': '18.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'A', 'citizen' :Citizen(name = 'Max', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'coal', 'category' : 'coal', 'date': '18.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'B', 'citizen' :Citizen(name = 'Max', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'coal', 'category' : 'coal', 'date': '25.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'B', 'citizen' :Citizen(name = 'Max', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'coal', 'category' : 'coal', 'date': '25.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'B', 'citizen' :Citizen(name = 'Crul', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'coal', 'category' : 'coal', 'date': '25.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'C', 'citizen' :Citizen(name = 'Crul', age = 45, gender = 'male', education = None, social_rating = 8)},
                {'name': 'gold', 'category' : 'iron', 'date': '25.05.2025', 'weight': 25.5, 'color': 'gray', 'grade':  'C', 'citizen' :Citizen(name = 'Crul', age = 45, gender = 'male', education = None, social_rating = 8)}]
                
    for elem in params:
        resource = Resource(**elem)
        pm.add_resource_in_warehouse(resource)

def test_return_all_statistic():
    result = pm.return_all_statistic()
    assert type(result) == list
    assert len(result) == 12

def test_return_statistic_for_date():
    result = pm.return_statistic_for_date('15.05.2025')
    assert type(result) == list
    assert len(result) == 3

    result = pm.return_statistic_for_date('01.01.2025')
    assert result == []

def test_return_weight_for_category():
    result = pm.return_weight_for_category('iron')
    assert result == 76.5

    result = pm.return_weight_for_category('coal')
    assert result == 102.0

    result = pm.return_weight_for_category('nonexistent')
    assert result == 0

def test_return_weight_for_params():
    result = pm.return_weight_for_params('still', 'gray', 'D')
    assert result == 51.0

    result = pm.return_weight_for_params('gold', 'gray', 'C')
    assert result == 25.5

    result = pm.return_weight_for_params('nonexistent', 'gray', 'C')
    assert result == 0

def test_return_statistic_for_citizen():
    result = pm.return_statistic_for_citizen('Egor')
    assert type(result) == list
    assert len(result) == 2

    result = pm.return_statistic_for_citizen('nonexistent')
    assert result == []

def test_add_resource_in_warehouse():
    new_resource = Resource(name='silver', category='metal', date='01.01.2025', weight=10.0, color='silver', grade='A', citizen=Citizen(name='John', age=30, gender='male', education=None, social_rating=5))
    pm.add_resource_in_warehouse(new_resource)

    result = pm.return_all_statistic()
    assert len(result) == 13

def test_update_weight_resource_in_warehouse():
    result = pm.update_weight_resource_in_warehouse('still', 'gray', 'D', 100.0)
    assert result == True

    result = pm.update_weight_resource_in_warehouse('nonexistent', 'gray', 'C', 100.0)
    assert result == False

def test_update_citizen_in_statistic():
    new_resource = Resource(name='still', category='iron', date='15.05.2025', weight=25.5, color='gray', grade='D', citizen=Citizen(name='John', age=30, gender='male', education=None, social_rating=5))
    result = pm.update_citizen_in_statistic(new_resource)
    assert result == True

    new_resource = Resource(name='nonexistent', category='iron', date='15.05.2025', weight=25.5, color='gray', grade='D', citizen=Citizen(name='John', age=30, gender='male', education=None, social_rating=5))
    result = pm.update_citizen_in_statistic(new_resource)
    assert result == False

def test_del_data_statistic():
    resource_to_delete = Resource(name='still', category='iron', date='15.05.2025', weight=25.5, color='gray', grade='D', citizen=Citizen(name='Egor', age=45, gender='male', education=None, social_rating=8))
    result = pm.del_data_statistic(resource_to_delete)
    assert result == True

    result = pm.del_data_statistic(resource_to_delete)
    assert result == False

def test_del_data_in_warehouse():
    result = pm.del_data_in_warehouse('still', 'gray', 'D')
    assert result == True

    result = pm.del_data_in_warehouse('nonexistent', 'gray', 'C')
    assert result == False

def test_clear_warehouse():
    pm.clear_warehouse()
    result = pm.return_weight_for_category('iron')
    assert result == 0

def test_clear_statistic():
    pm.clear_statistic()
    result = pm.return_all_statistic()
    assert result == []