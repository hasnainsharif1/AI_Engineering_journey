from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, field_validator

@dataclass(frozen=True)
class FetchConfig:
    url: str
    timeout: int = 10
    max_retries: int = 3


class WeatherData(BaseModel):
    city: str
    temperature: float
    humidity: Optional[float] = None
    country: str
    @field_validator('temperature')
    @classmethod
    def validation_temperature(cls, value):
        if value < -100 or value > 100:
            raise ValueError('Temperature must be between -100 and 100 degrees Celsius')
        return value
    

class PostData(BaseModel):
    id: int
    title: str
    userId: int
    body: str

