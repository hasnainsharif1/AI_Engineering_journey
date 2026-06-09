from datahub.base import FetchResult
from datahub.config import HTTP_TIMEOUT, WEATHER_BASE_URL
from datahub.context import ManagedSession
from datahub.decorators import timer, with_retry
from datahub.logger import logger

BASE_URL = WEATHER_BASE_URL

# each city needs a name and its GPS coordinates
DEFAULT_CITIES = [
    {"name": "Islamabad", "latitude": 33.72, "longitude": 73.06},
    {"name": "Karachi",   "latitude": 24.86, "longitude": 67.01},
    {"name": "Lahore",    "latitude": 31.55, "longitude": 74.35},
]


class WeatherFetcher:

    def __init__(self, cities: list[dict] | None = None):
        # use provided cities or fall back to the defaults above
        self.cities = cities or DEFAULT_CITIES

    @timer        # logs how long fetch() takes
    @with_retry   # retries up to 3 times on timeout or connection error
    async def fetch(self) -> FetchResult:
        results = []

        # ManagedSession opens the httpx client here and closes it when the block ends
        async with ManagedSession(timeout=HTTP_TIMEOUT) as client:
            for city in self.cities:
                # build query params — ask Open-Meteo for temperature and humidity
                params = {
                    "latitude": city["latitude"],
                    "longitude": city["longitude"],
                    "current": "temperature_2m,relative_humidity_2m",
                }

                response = await client.get(BASE_URL, params=params)

                # raise an exception immediately if the API returned 4xx or 5xx
                response.raise_for_status()

                # pull out only the current weather block from the response
                current = response.json()["current"]

                results.append({
                    "city": city["name"],
                    "temperature": current["temperature_2m"],
                    "humidity": current["relative_humidity_2m"],
                })

                logger.debug(f"{city['name']}: {current['temperature_2m']}°C")

        # return in the FetchResult shape defined in base.py
        return FetchResult(source="open-meteo", data=results, status="ok")
