from model.transport_network.route import Route

class Routes:
    __routes = []

    @classmethod
    async def get_one_route(cls, id: int) -> Route | None:
        for route in cls.__routes:
            if route.id == id:
                return route
        return
    
    @classmethod
    async def get_all_routes(cls) -> list[Route]:
        return cls.__routes

    @classmethod
    async def create_route(cls, route: Route) -> None:
        for route_i in cls.__routes:
            if route_i.id == route.id:
                route.id = len(cls.__transports) + 1
                break
        cls.__routes.append(route)

    @classmethod
    async def delete_route(cls, id: int) -> None:
        for route in cls.__routes:
            if route.id == id:
                cls.__routes.remove(route)
        
    
    @classmethod
    async def update(cls, route: Route) -> None:
        for route_i in cls.__routes:
            if route_i.id == route.id:
                cls.__routes(route_i) = route