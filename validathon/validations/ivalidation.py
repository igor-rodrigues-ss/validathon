#!-*-coding:utf-8-*-

from typing import Any
from abc import ABC, abstractmethod
from validathon.result import ValidationResult


class IValidation(ABC):

    @abstractmethod
    def validate(self, key: str, value: Any) -> ValidationResult:
        pass
