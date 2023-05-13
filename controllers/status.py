from enum import Enum

from mcstatus import BedrockServer, JavaServer
from pydantic import BaseModel
from starlite import Controller, post


class TypeEnum(str, Enum):
    java = "java"
    bedrock = "bedrock"


class StatusData(BaseModel):
    ip: str
    type: TypeEnum


class Status(StatusData):
    version: str
    players: int
    max_players: int
    latency: int
    description: str
    favicon: str


class StatusController(Controller):
    path = "/status"

    @post()
    def get_status(self, data: StatusData) -> Status:
        if data.type == TypeEnum.java:
            server = JavaServer.lookup(data.ip)
        elif data.type == TypeEnum.bedrock:
            server = BedrockServer.lookup(data.ip)
        else:
            raise Exception("Invalid type")

        status = server.status()

        data = Status(
            ip=data.ip,
            type=data.type,
            version=status.version.name,
            players=status.players.online,
            max_players=status.players.max,
            latency=status.latency,
            description=status.description,
            favicon=status.favicon
        )
        return data
