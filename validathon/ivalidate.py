#!-*-coding:utf-8-*-

from abc import ABC, abstractmethod
from typing import Any

from validathon.validation_result import ValidationResult

REQUIRED_KEY = 'campo_não_existe_123456'





class IValidation(ABC):

    @abstractmethod
    def validate(self, key: str, value: Any) -> ValidationResult:
        pass
