import pytest

from src.data.routes import Routes
from src.model.transport_network.route import Route

route1 = Route(id= 1, name='Route 1', count_stops=5, count_transport_on_line=0)
route2 = Route(id= 2, name='Route 1', count_stops=5, count_transport_on_line=0)
route3 = Route(id= 3, name='Route 1', count_stops=5, count_transport_on_line=0)
route4 = Route(id= 4, name='Route 1', count_stops=5, count_transport_on_line=0)
route5 = Route(id= 5, name='Route 1', count_stops=5, count_transport_on_line=0)

Routes.create_route(route1)
Routes.create_route(route2)
Routes.create_route(route3)
Routes.create_route(route4)
Routes.create_route(route5)


@pytest.mark.parametrize('data, extend_result', [
    Routes.get_one_route(1), Route(id= 1, name='Route 1', count_stops=5, count_transport_on_line=0)
])
def test_get_one_route(data, extend_result):
    assert data == extend_result


# @pytest.mark.parametrize('data, extend_result', [
#     Routes.get_all_routes(), {

# }
# ])
# def test_get_one_route(data, extend_result):
#     assert data == extend_result