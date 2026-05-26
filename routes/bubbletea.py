
from fastapi import APIRouter
from typing import Any

from models.bubbletea import BubbleTea
from utils.db_connection import get_connection as get_db_connection

router = APIRouter()

conn = get_db_connection()

@router.get("/bubbleteas")
def get_bubble_teas_from_aieven() -> dict[str, bool | tuple[dict[str, Any], ...]]:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM bubbletea WHERE active = TRUE")
        row = cur.fetchall()
    return {"ok": True, "result": row}

@router.get("/bubbleteas/{id}")
def get_bubble_teas_from_aieven_by_id(id: int) -> dict:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM bubbletea WHERE id = %s AND active = TRUE", (id))
        row = cur.fetchone()
    return {"ok": True, "result": row}

@router.post("/bubbleteas")
def create_bubble_tea_from_aieven(bubble_tea: BubbleTea) -> dict[str, bool | BubbleTea]:
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO bubbletea (name, temperature, precio, active) VALUES (%s, %s, %s, %s)",
            (bubble_tea["name"], bubble_tea["temperature"], bubble_tea["precio"], bubble_tea["active"]),
        )
        conn.commit()
    return {"ok": True, "result": bubble_tea}

@router.put("/bubbleteas/{id}")
def update_bubble_tea_from_aieven_by_id(id: int, bubble_tea: BubbleTea) -> dict[str, bool | BubbleTea]:
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE bubbletea SET name = %s, temperature = %s, precio = %s, active = %s WHERE id = %s",
            (bubble_tea["name"], bubble_tea["temperature"], bubble_tea["precio"], bubble_tea["active"], id),
        )
        conn.commit()
    return {"ok": True, "result": bubble_tea}

@router.delete("/bubbleteas/{id}")
def delete_bubble_tea_from_aieven_by_id(id: int) -> dict[str,
bool]:
    with conn.cursor() as cur:
        cur.execute("UPDATE bubbletea SET active = FALSE WHERE id = %s", (id,))
        conn.commit()
    return {"ok": True}
    
