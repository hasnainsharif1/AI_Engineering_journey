import asyncio
from datahub.fetchers.weather import WeatherFetcher

async def test():
    fetcher = WeatherFetcher()
    result = await fetcher.fetch()
    print("Source:", result["source"])
    print("Status:", result["status"])
    for city in result["data"]:
        print(f"{city['city']}: {city['temperature']}C, humidity: {city['humidity']}%")

asyncio.run(test())