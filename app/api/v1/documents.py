from fastapi import APIRouter

router = APIRouter(tags=["Documents"])


@router.get("/documents")
def get_all_documents() -> None:
    pass
