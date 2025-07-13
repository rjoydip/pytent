from fastapi import FastAPI, Request, Response

from packages.log import get_logger

logger = get_logger(__name__)
logger.info("API is starting up")

app = FastAPI()


@app.middleware("http")
async def logger_middleware(request: Request, call_next):
    response = await call_next(request)

    # Exclude /healthcheck endpoint from producing logs
    if request.url.path != "/healthcheck":
        if 400 <= response.status_code < 500:
            logger.error("Client error")
        elif response.status_code >= 500:
            logger.error("Server error")
        else:
            logger.info("OK")

    return response


@app.get("/healthcheck")
async def healthcheck():
    return Response("Running ...")

@app.get("/")
def root():
    return {"msg": "API is working"}
