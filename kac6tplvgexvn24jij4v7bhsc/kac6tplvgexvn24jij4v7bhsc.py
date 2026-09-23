from typing import Any, Optional

from uuid import UUID as Uuid

class kac6tplvgexvn24jij4v7bhsc:
    def __init__(self, *args: Any, id: Optional[Uuid] = None, **kwargs: Any):
        self.conversion_values: list[Any] = []
        self.id: Optional[Uuid] = id
        for _conversion_value_ in args:
            self.conversion_values.append(_conversion_value_)
        for _value_ in kwargs.values():
            self.conversion_values.append(_value_)
        if "id" not in kwargs:
            self.conversion_values.append(id)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, kac6tplvgexvn24jij4v7bhsc):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        if self.id is None:
            raise RuntimeError("Id is not set yet! Either instantiate with an id or instantiate in an Enumeration class.")
        return hash(self.id)

    def to_id(self) -> Uuid:
        if self.id is None:
            raise RuntimeError("Id is not set yet! Either instantiate with an id or instantiate in an Enumeration class.")
        return self.id

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id})"
