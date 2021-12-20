from dataclasses import dataclass, asdict
from typing import Dict, Any


BAD_REQUEST = 400
INTERNAL_SERVER_ERROR = 500



class InvalidUsage(Exception):
    """Exception representation invalid usage of the API services."""


    status_code = 400


    def __init__(self, message, status_code=None, payload=None):
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload


    def __str__(self):
        return self.message



@dataclass
class ErrorResponse:
    """Class representing error response data for the API service."""



    status_code: str
    name: str 
    message: str
    details: Dict[str, Any] = None


    def to_dict(self):
        return asdict(self)