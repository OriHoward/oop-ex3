from json import JSONEncoder
from typing import Any


class GraphEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        to_json_dict = getattr(o, "to_json_dict", None)
        if callable(to_json_dict):
            return o.to_json_dict()
        return o.__dict__
