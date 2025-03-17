from fastapi import APIRouter, Body
from src.model.transport_network.route import Route
from src.data.routes import Routes


router = APIRouter(prefix="/route")


@router.get("/")
def get_routes():
    routes = Routes.get_all_routes()

    return {"status": "ok", "routes": routes}

@router.post("/add-route")
def add_route(route: Route):
    Routes.create_route(route)

    return {"status": "ok"}

@router.delete("/delete-route/{id}")
def delete_route(id: int):
    Routes.delete_route(id)

    return {"status": "ok"}

@router.patch("/route/{id}")
def update_route(route: Route):
    Routes.update(route)

    return {"status": "ok"}