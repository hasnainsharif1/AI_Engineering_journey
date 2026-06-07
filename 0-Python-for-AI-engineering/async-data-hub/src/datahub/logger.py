import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss} | {level} | {name} | {message}")
logger.add("logs/datahub.log", level="DEBUG", rotation="5 MB", retention="3 days")


def get_logger(name: str = "datahub"):
    return logger.bind(name=name)


__all__ = ["logger", "get_logger"]
