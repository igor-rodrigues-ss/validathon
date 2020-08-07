#!-*-coding:utf-8-*-

from dataclasses import dataclass
from typing import Any

@dataclass
class ValidationResult:
    field_name: str
    msg: str
    valid: bool
    exc: Exception = None
    validation: Any = None

