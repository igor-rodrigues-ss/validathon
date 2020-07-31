#!-*-coding:utf-8-*-

from dataclasses import dataclass


@dataclass
class ValidationResult:
    field: str
    msg: str
    valid: bool
    exc: Exception = None

