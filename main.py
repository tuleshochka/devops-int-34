import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/healthz", status_code=200)
async def check_healthz():
    return {"message": "OK"}

@app.get("/", status_code=302)
async def root():
    return RedirectResponse("/docs", status_code=302)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port = 8000, reload=True)