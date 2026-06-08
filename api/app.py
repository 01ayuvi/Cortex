from fastapi import FastAPI

app = FastAPI(
    title="Cortex API",
    description="AI-Powered Email Intelligence Backend",
    version="1.0"
)


@app.get("/")
def root():

    return {
        "message": "Cortex API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }