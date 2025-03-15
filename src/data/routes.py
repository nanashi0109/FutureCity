from src.model.transport_network.route import Route

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
        for route_i in cls.__routes:
            if route_i.id == route.id:
                route.id = len(cls.__routes) + 1
                break
        cls.__routes.append(route)

    @classmethod
    def delete_route(cls, id: int) -> None:
        for route in cls.__routes:
            if route.id == id:
                cls.__routes.remove(route)
        
    
    @classmethod
    def update(cls, route: Route) -> None:
        target = cls.get_one_route(route.id)
        cls.delete_route(target.id)
        cls.create_route(route)
                