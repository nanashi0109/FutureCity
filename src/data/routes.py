from model.transport_network.route import Route

class Routes:
    __routes = []

    @classmethod
    def get_one_route(cls, id: int) -> Route | None:
        for route in cls.__routes:
            if route.id == id:
                return route
        return
    
    @classmethod
    def get_all_routes(cls) -> list[Route]:
        return cls.__routes

    @classmethod
    def create_route(cls, route: Route) -> None:
        cls.__routes.append(route)

    @classmethod
    def delete_route(cls, id: int) -> None:
        for route in cls.__routes:
            if route.id == id:
                cls.__routes.remove(route)
        
    
    @classmethod
    def update(cls, route: Route) -> None:
        for route_i in cls.__routes:
            if route_i.id == route.id:
                cls.__routes(route_i) = route