
import os
import re
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="جياشي وزمن مافي",
    description="TikTok Public Account Intelligence",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class ScanRequest(BaseModel):
    username: str


@app.get("/")
def home():
    return {
        "program": "جياشي وزمن مافي",
        "status": "online",
        "message": "محرك الفحص جاهز للتجهيز"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "time": datetime.now(timezone.utc).isoformat()
    }


@app.post("/scan")
def scan_account(request: ScanRequest):
    username = request.username.strip().lstrip("@")

    if not re.fullmatch(r"[A-Za-z0-9._]{2,24}", username):
        raise HTTPException(
            status_code=400,
            detail="اسم المستخدم غير صحيح"
        )

    api_key = os.getenv("HASDATA_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="لم يتم إعداد مفتاح خدمة البيانات"
        )

    return {
        "username": username,
        "profile_url": f"https://www.tiktok.com/@{username}",
        "status": "pending_integration",
        "message": (
            "تم تجهيز الطلب، لكن الربط بمصدر "
            "بيانات TikTok لم يكتمل بعد"
        ),
        "followers": None,
        "likes": None,
        "videos": None,
        "country": None
    }
