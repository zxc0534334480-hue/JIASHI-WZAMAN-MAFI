from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="جياشي وزمن مافي",
    description="منصة تحليل معلومات حسابات TikTok العامة",
    version="1.0"
)

@app.get("/")
async def home():
    return {
        "name": "جياشي وزمن مافي",
        "status": "online",
        "message": "السيرفر يعمل بنجاح 🛡️"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "time": datetime.utcnow().isoformat()
    }
