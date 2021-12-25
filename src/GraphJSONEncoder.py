from json import JSONEncoder
from typing import Any

"""
This class is a custom Encoder that is used to write the objects to a json file.
If an object has the `to_json_dict` function then it uses this function to get the dict the represents the object,
otherwise we use the default __dict__ to represent the object.
More information can be found here: https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
"""


class GraphEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        to_json_dict = getattr(o, "to_json_dict", None)
        if callable(to_json_dict):
            return o.to_json_dict()
        return o.__dict__
