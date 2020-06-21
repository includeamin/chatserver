from models.Websocket import HeadersModel


def get_headers(data: tuple) -> HeadersModel:
    data: dict = data[0]
    return HeadersModel(**data)
