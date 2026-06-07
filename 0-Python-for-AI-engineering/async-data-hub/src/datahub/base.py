from abc import ABC, abstractmethod
from typing import Any, Protocol, TypedDict


# 1. Shape every fetcher must return
class FetchResult(TypedDict):
    source: str
    data: list[Any]
    status: str


class DataFetcher(Protocol):
    async def fetch(self) -> FetchResult: ...


class BaseAnalyzer(ABC):

    @abstractmethod
    def analyze(self, data: list[Any]) -> dict[str, Any]:
        """Process raw data and return computed stats."""
        ...

    @abstractmethod
    def summary(self) -> str:
        """Return a one-line human-readable summary."""
        ...
