from fastapi import APIRouter, HTTPException
from database import get_db_connection
import pyodbc

from models import (
    AGetMinParams,
    AGetMaxParams,
    SaraneHazineRefahiParams,
    SaraneDarmanParams,
    HazineAeleMandiParams,
    HazineOvladParams,
    SaraneTaminAtieParams,
    EidiParams
)

router = APIRouter()

@router.post("/execute/AGetMin")
async def a_get_min(params: AGetMinParams):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dbo.AGetMin(?, ?)", params.P1, params.P2)
        result = cursor.fetchone()
        return {"result": result[0]}
    except pyodbc.Error as e:
        raise HTTPException(500, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.post("/execute/AGetMax")
async def a_get_max(params: AGetMaxParams):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dbo.AGetMax(?, ?, ?, ?)", params.P1, params.P2, params.P3, params.P4)
        result = cursor.fetchone()
        return {"result": result[0]}
    except pyodbc.Error as e:
        raise HTTPException(500, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.post("/execute/SaraneHazineRefahi")
async def sarane_hazine_refahi(params: SaraneHazineRefahiParams):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dbo.SaraneHazineRefahi(?)", params.Y)
        result = cursor.fetchone()
        return {"result": result[0]}
    except pyodbc.Error as e:
        raise HTTPException(500, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.post("/execute/SaraneDarman")
async def sarane_darman(params: SaraneDarmanParams):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dbo.SaraneDarman(?)", params.Y)
        result = cursor.fetchone()
        return {"result": result[0]}
    except pyodbc.Error as e:
        raise HTTPException(500, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.post("/execute/HazineAeleMandi")
async def hazine_aele_mandi(params: HazineAeleMandiParams):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dbo.HazineAeleMandi(?)", params.YHamsar)
        result = cursor.fetchone()
        return {"result": result[0]}
    except pyodbc.Error as e:
        raise HTTPException(500, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.post("/execute/HazineOvlad")
async def hazine_ovlad(params: HazineOvladParams):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dbo.HazineOvlad(?, ?, ?)", params.Y1, params.Y2, params.TedadFarzamd)
        result = cursor.fetchone()
        return {"result": result[0]}
    except pyodbc.Error as e:
        raise HTTPException(500, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.post("/execute/SaraneTaminAtie")
async def sarane_tamin_atie(params: SaraneTaminAtieParams):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dbo.SaraneTaminAtie(?)", params.Y)
        result = cursor.fetchone()
        return {"result": result[0]}
    except pyodbc.Error as e:
        raise HTTPException(500, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.post("/execute/Eidi")
async def eidi(params: EidiParams):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dbo.eidi(?)", params.Y)
        result = cursor.fetchone()
        return {"result": result[0]}
    except pyodbc.Error as e:
        raise HTTPException(500, detail=str(e))
    finally:
        if conn:
            conn.close()
