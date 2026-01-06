from fastapi import APIRouter

router = APIRouter(tags=["Users"])


@router.get("/users")
def get_all_users() -> None:
    pass
