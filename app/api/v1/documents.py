from fastapi import APIRouter

router = APIRouter()


@router.get("/documents", tags=["documents"])
def get_documents():
    pass
