import uvicorn

from config import app_config, uvicorn_config
from tools import app_initializer

app_config = app_config.app_config

app = app_initializer.create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", **uvicorn_config.uvicorn_config)
