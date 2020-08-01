#!-*-coding:utf-8-*-

from dataclasses import dataclass
# from validathon.ivalidate import IValidation
from typing import Any

@dataclass
class ValidationResult:
    field: str
    msg: str
    valid: bool
    exc: Exception = None
    validation: Any = None

