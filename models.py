from pydantic import BaseModel, Field

class File(BaseModel):
    operation: str = Field(..., example="check_exists")
    file_path: str = Field(..., example="/path/to/file")

class SuccessResponse(BaseModel):
    status: str = Field(..., example="success")
    exists: bool = Field(..., example=True)

class ErrorResponse(BaseModel):
    status: str = Field(..., example="failure")
    error: str = Field(..., example="An error occurred")
