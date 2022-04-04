import uvicorn
from fastapi import FastAPI

from app.routers import films

app = FastAPI()
app.include_router(films.router)


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # внутри запускается на 8000, а снаружи это 8004
    # Вот только приходиться перезапускать при изменениях. Зато быстро, не чита джанге

