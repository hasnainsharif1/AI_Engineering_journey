import time
import functools
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from datahub.logger import logger


def timer(func):
    # functools.wraps keeps the original function name and docstring intact
    
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # record time before the function runs
        start = time.perf_counter()

        # actually call the async function and wait for it to finish
        result = await func(*args, **kwargs)

        # calculate how many milliseconds it took
        elapsed_ms = (time.perf_counter() - start) * 1000

        # log the function name and elapsed time
        logger.info(f"{func.__name__} finished in {elapsed_ms:.2f}ms")

        return result
    return wrapper


# retry decorator built from tenacity — applied directly as @with_retry on any async function
with_retry = retry(
    # stop after 3 total attempts (1 original + 2 retries)
    stop=stop_after_attempt(3),

    # wait 2s before retry 1, 4s before retry 2, capped at 8s
    wait=wait_exponential(multiplier=1, min=2, max=8),

    # only retry on network timeout or connection errors, not on bad data or 4xx responses
    retry=retry_if_exception_type((httpx.TimeoutException, httpx.ConnectError)),

    # if all 3 attempts fail, raise the original exception instead of a tenacity error
    reraise=True,
)
