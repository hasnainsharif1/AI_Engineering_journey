import time
import httpx
from contextlib import contextmanager
from datahub.logger import logger


class ManagedSession:
    """Class-based async context manager — opens an httpx client on enter, closes it on exit."""

    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.client: httpx.AsyncClient | None = None

    async def __aenter__(self) -> httpx.AsyncClient:
        # called when `async with ManagedSession() as client:` starts
        # creates and returns a ready-to-use HTTP client
        self.client = httpx.AsyncClient(timeout=self.timeout)
        logger.debug("HTTP session opened")
        return self.client

    async def __aexit__(self, *_):
        # called when the `async with` block ends — even if an error was raised
        # always closes the client to free the connection
        if self.client:
            await self.client.aclose()
            logger.debug("HTTP session closed")


@contextmanager
def timed_block(label: str):
    """Generator-based context manager — logs how long the wrapped block took."""

    start = time.perf_counter()
    logger.info(f"[{label}] started")

    # yield pauses here and hands control to the `with` block
    yield

    # resumes here after the `with` block finishes
    elapsed_ms = (time.perf_counter() - start) * 1000
    logger.info(f"[{label}] finished in {elapsed_ms:.2f}ms")
