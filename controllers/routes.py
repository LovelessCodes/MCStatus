import os

import requests
from pydantic import BaseModel
from starlite import Controller, Response, delete, get, post, put
from starlite.status_codes import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT,
                                   HTTP_500_INTERNAL_SERVER_ERROR)


class RoutesData(BaseModel):
    ip: str
    route: str


class NewRoute(BaseModel):
    address: str
    backend: str


class RoutesController(Controller):
    path = "/routes"

    @get()
    def get_routes(self) -> Response[list[str]]:
        routes_url = os.environ.get("ROUTES_URL")
        if routes_url is None:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content="ROUTES_URL is not set")
        r = requests.get(f"{routes_url}/routes",
                         headers={"Accept": "application/json"})
        if r.status_code != 200:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content=f"Error: {r.status_code}")
        routes = r.json()
        return Response(status_code=HTTP_200_OK, content=[k for k in routes])

    @post()
    def post_route(self, data: NewRoute) -> Response:
        routes_url = os.environ.get("ROUTES_URL")
        if routes_url is None:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content="ROUTES_URL is not set")
        r = requests.post(
            f"{routes_url}/routes",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data={
                "serverAddress": data.address,
                "backend": data.backend
            }
        )
        if r.status_code != 200:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content=f"Error: {r.status_code}")
        return Response(status_code=HTTP_201_CREATED)

    @put(path="/{address:str}")
    def put_route(self, address: str, data: NewRoute) -> Response:
        routes_url = os.environ.get("ROUTES_URL")
        if routes_url is None:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content="ROUTES_URL is not set")
        r = requests.delete(f"{routes_url}/routes/{address}")
        if r.status_code != 200:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content=f"Error on deletion: {r.status_code}")
        r = requests.post(
            f"{routes_url}/routes",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data={
                "serverAddress": data.address,
                "backend": data.backend
            }
        )
        if r.status_code != 200:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content=f"Error on creation: {r.status_code}")
        return Response(status_code=HTTP_200_OK, content="OK")

    @delete(path="/{address:str}", status_code=HTTP_204_NO_CONTENT, response_model=None)
    def delete_route(self, address: str) -> None:
        routes_url = os.environ.get("ROUTES_URL")
        if routes_url is None:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content="ROUTES_URL is not set")
        requests.delete(f"{routes_url}/routes/{address}")
        if r.status_code != 200:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content=f"Error on deletion: {r.status_code}")
        return Response(status_code=HTTP_204_NO_CONTENT)
