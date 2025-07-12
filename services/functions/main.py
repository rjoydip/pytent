from packages.log import get_logger

logger = get_logger(__name__)
logger.info("API is starting up")

def main():
    logger.debug("this is a debug message")

if __name__ == "__main__":
    main()
