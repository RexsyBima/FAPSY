from fastapi import FastAPI

app = FastAPI()

from . import routing  # noqa
