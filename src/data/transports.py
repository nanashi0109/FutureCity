from model.transport_network.transports import Transport

class Transports:
    __transports = []

    @classmethod
    async def get_one_transport(cls, id: int) -> Transport | None:
        for transport in cls.__transports:
            if transport.id == id:
                return transport
        return
    
    @classmethod
    async def get_all_transports(cls) -> list[Transport]:
        return cls.__transports

    @classmethod
    async def create_transport(cls, transport: Transport) -> None:
        for transport_i in cls.__transports:
            if transport_i.id == transport.id:
                transport.id = len(cls.__transports) + 1
                break
        cls.__transports.append(transport)

    @classmethod
    async def delete_transport(cls, id: int) -> None:
        for transport in cls.__transports:
            if transport.id == id:
                cls.__transports.remove(transport)
        
    
    @classmethod
    async def update(cls, transport: Transport) -> None:
        for transport_i in cls.__transports:
            if transport_i.id == transport.id:
                cls.__transports(transport_i) = transport
        
