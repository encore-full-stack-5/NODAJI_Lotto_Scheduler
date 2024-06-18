from fastapi import FastAPI
from contextlib import asynccontextmanager
from schedulers import lotto_num_scheduler

@asynccontextmanager
async def lifespan(app):
    lotto_num_scheduler.scheduler.start()
    yield
    print('finished')

app = FastAPI(lifespan=lifespan)

