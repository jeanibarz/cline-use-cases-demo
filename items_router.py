from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.get("/")
async def read_items():
    return [{"name": "Foo"}, {"name": "Bar"}]


@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
