import asyncio
from datahub.fetchers.posts import PostsFetcher

async def test():
    fetcher = PostsFetcher(limit=5)
    result = await fetcher.fetch()
    print("Source:", result["source"])
    print("Status:", result["status"])
    for post in result["data"]:
        print(f"  [{post['id']}] user:{post['userId']} — {post['title']}")

asyncio.run(test())
