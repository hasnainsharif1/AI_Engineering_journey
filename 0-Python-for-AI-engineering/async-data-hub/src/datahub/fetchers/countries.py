from datahub.base import FetchResult
from datahub.config import COUNTRIES_BASE_URL, HTTP_TIMEOUT
from datahub.context import ManagedSession
from datahub.decorators import timer, with_retry
from datahub.logger import logger

BASE_URL = COUNTRIES_BASE_URL

DEFAULT_REGION = "asia"


class CountriesFetcher:

    def __init__(self, region: str = DEFAULT_REGION):
        # region to fetch — e.g. "asia", "europe", "africa"
        self.region = region

    @timer
    @with_retry
    async def fetch(self) -> FetchResult:
        results = []

        async with ManagedSession(timeout=HTTP_TIMEOUT) as client:
            response = await client.get(f"{BASE_URL}/region/{self.region}")

            # raise immediately on 4xx or 5xx
            response.raise_for_status()

            countries = response.json()

            for country in countries:
                # name is nested under name.common in the API response
                name = country["name"]["common"]

                # capital is a list — take the first entry, default to None if missing
                capital = country.get("capital", [None])[0]

                results.append({
                    "name": name,
                    "capital": capital,
                    "population": country["population"],
                    "region": country["region"],
                })

                logger.debug(f"{name}: population {country['population']:,}")

        return FetchResult(source="restcountries", data=results, status="ok")
