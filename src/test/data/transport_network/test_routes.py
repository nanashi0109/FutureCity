import pytest

from src.data.routes import Routes
from src.model.transport_network.route import Route

route1 = Route(id= 1, name='Route 1', count_stops=5, count_transport_on_line=0)
route2 = Route(id= 2, name='Route 1', count_stops=5, count_transport_on_line=0)
route3 = Route(id= 3, name='Route 1', count_stops=5, count_transport_on_line=0)
route4 = Route(id= 4, name='Route 1', count_stops=5, count_transport_on_line=0)
route5 = Route(id= 5, name='Route 1', count_stops=5, count_transport_on_line=0)
route_test = Route(id= 1, name='Route 1', count_stops=5, count_transport_on_line=0)

Routes.create_route(route1)
Routes.create_route(route2)
Routes.create_route(route3)
Routes.create_route(route4)
Routes.create_route(route5)


@pytest.mark.parametrize('id, extend_result', [
    (1, {"id": 1, "name":'Route 1', "count_stops":5, "count_transport_on_line":0})
])
def test_get_one(id, extend_result):
    result_func= Routes.get_one_route(id) 
    
    assert result_func.id == extend_result['id'] and result_func.name == extend_result['name'] \
          and result_func.count_stops == extend_result['count_stops'] and result_func.count_transport_on_line == extend_result['count_transport_on_line']


@pytest.mark.parametrize('extend_result', [
    ([Route(id= 1, name='Route 1', count_stops=5, count_transport_on_line=0),
    Route(id= 2, name='Route 1', count_stops=5, count_transport_on_line=0),
    Route(id= 3, name='Route 1', count_stops=5, count_transport_on_line=0),
    Route(id= 4, name='Route 1', count_stops=5, count_transport_on_line=0),
    Route(id= 5, name='Route 1', count_stops=5, count_transport_on_line=0)])
])

def test_get_all(extend_result):
    data = Routes.get_all_routes()
    assert  data == extend_result

@pytest.mark.parametrize('id, extend_result', [
    (1, [Route(id= 2, name='Route 1', count_stops=5, count_transport_on_line=0),
    Route(id= 3, name='Route 1', count_stops=5, count_transport_on_line=0),
    Route(id= 4, name='Route 1', count_stops=5, count_transport_on_line=0),
    Route(id= 5, name='Route 1', count_stops=5, count_transport_on_line=0)])
])

def test_delete(id, extend_result):
    Routes.delete_route(id)
    data = Routes.get_all_routes()
    assert  data == extend_result

# create_route
@pytest.mark.parametrize('data, extend_result', [
    (Route(id= 6, name='Route 6', count_stops=5, count_transport_on_line=0),
     [
        Route(id= 2, name='Route 1', count_stops=5, count_transport_on_line=0),
        Route(id= 3, name='Route 1', count_stops=5, count_transport_on_line=0),
        Route(id= 4, name='Route 1', count_stops=5, count_transport_on_line=0),
        Route(id= 5, name='Route 1', count_stops=5, count_transport_on_line=0),
        Route(id= 6, name='Route 6', count_stops=5, count_transport_on_line=0)
        ])
    ])

def test_create(data, extend_result):
    
    Routes.create_route(data)
    data = Routes.get_all_routes()
    assert  data == extend_result






