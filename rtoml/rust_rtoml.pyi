from datetime import datetime
from typing import Any, Callable

def deserialize(toml: str, parse_datetime: Callable[[str], datetime]) -> Any: ...
def serialize(obj: Any) -> str: ...