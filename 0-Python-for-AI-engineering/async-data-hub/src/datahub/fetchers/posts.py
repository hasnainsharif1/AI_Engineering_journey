from datahub.base import FetchResult
from datahub.config import HTTP_TIMEOUT, POSTS_BASE_URL
from datahub.context import ManagedSession
from datahub.decorators import timer, with_retry
from datahub.logger import logger

BASE_URL = POSTS_BASE_URL


class PostsFetcher:

    def __init__(self, limit: int = 10):
        # how many posts to fetch — default 10
        self.limit = limit

    @timer
    @with_retry
    async def fetch(self) -> FetchResult:
        results = []

        async with ManagedSession(timeout=HTTP_TIMEOUT) as client:
            # _limit is a JSONPlaceholder query param that caps how many posts come back
            response = await client.get(f"{BASE_URL}/posts", params={"_limit": self.limit})

            # raise immediately on 4xx or 5xx
            response.raise_for_status()

            posts = response.json()

            for post in posts:
                results.append({
                    "id":     post["id"],
                    "userId": post["userId"],
                    "title":  post["title"],
                    "body":   post["body"],
                })

                logger.debug(f"Post {post['id']}: {post['title'][:40]}")

        return FetchResult(source="jsonplaceholder", data=results, status="ok")
