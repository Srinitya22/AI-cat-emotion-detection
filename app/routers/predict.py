from fastapi import APIRouter, UploadFile, File, Depends
from app.services.emotion import predict_from_audio
from app.dependencies import get_current_user

router = APIRouter(prefix="/predict", tags=["Prediction"])


@router.post("/audio")
def predict_audio(
    file: UploadFile = File(...),
    user=Depends(get_current_user)
):
    emotion = predict_from_audio(file)
    return {"emotion": emotion}
