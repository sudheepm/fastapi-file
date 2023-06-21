from fastapi import APIRouter, Body
from pathlib import Path
from models import File, SuccessResponse, ErrorResponse

router = APIRouter()

@router.post("/file_operation", response_model=SuccessResponse, responses={400: {"model": ErrorResponse}})
async def perform_file_operation(file: File):
    if file.operation == "check_exists":
        file_path = Path(file.file_path)
        try:
            file_exists = file_path.is_file()
            return {
                "status": "success",
                "exists": file_exists
            }
        except Exception as e:
            return {
                "status": "failure",
                "error": str(e)
            }
    else:
        return {
            "status": "failure",
            "error": f"Unsupported operation: {file.operation}"
        }
