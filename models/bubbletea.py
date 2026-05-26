from typing import NotRequired, TypedDict

class BubbleTea(TypedDict):
    id: NotRequired[int]
    name: str
    temperature: str
    precio: float
    active: bool
