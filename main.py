from fastapi import FastAPI
from src.bot.api import app as bot_app
import uvicorn


app = FastAPI()
app.include_router(router=bot_app)


if __name__ == '__main__':
    uvicorn.run(app)
