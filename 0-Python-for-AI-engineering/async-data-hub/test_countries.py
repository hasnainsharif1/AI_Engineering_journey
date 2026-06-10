import asyncio
from datahub.fetchers.countries import CountriesFetcher

async def test():
    fetcher = CountriesFetcher(region="asia")
    result = await fetcher.fetch()
    print("Source:", result["source"])
    print("Status:", result["status"])
    print(f"Total countries: {len(result['data'])}")
    for country in result["data"][:5]:  # print first 5 only
        print(f"  {country['name']} | capital: {country['capital']} | pop: {country['population']:,}")

asyncio.run(test())
