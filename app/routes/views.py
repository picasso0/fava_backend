from fastapi import APIRouter, HTTPException, Query
from database import get_db_connection
import pyodbc
from datetime import datetime
from fastapi.responses import StreamingResponse
import urllib.parse

import io
import csv

router = APIRouter()

@router.get("/view/vwPersonnelOrgInfoo")
async def vwPersonnelOrgInfoo(
    skip: int = Query(0, ge=0, description="Number of rows to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of rows to return"),
    # compid: int = Query()
):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"""
        SELECT * FROM Psn.vwPersonnelOrgInfo
        ORDER BY PersonnelID
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY;
        """
        cursor.execute(query, (skip, limit))

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results

    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.get("/view/companies")
async def companies(
    skip: int = Query(0, ge=0, description="Number of rows to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of rows to return")
):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM ent.vwCompPr
        ORDER BY ID
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY;
        """
        
        cursor.execute(query, (skip, limit))

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results

    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()



@router.get("/view/ShaghelCalculationResult")
async def ShaghelCalculationResult(
    skip: int = Query(0, ge=0, description="Number of rows to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of rows to return"),
    id: int =Query()
):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM ent.vwCompPr
        ORDER BY ID
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY;
        """
        
        cursor.execute(query, (skip, limit))

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results

    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()


@router.get("/view/ActoShaghelinInfo")
async def ActoShaghelinInfo(
    skip: int = Query(0, ge=0, description="Number of rows to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of rows to return"),
    id: int = Query()
):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"""
        SELECT * FROM dbo.ActoShaghelinInfo
        WHERE CompPrID={id}
        ORDER BY RegNo
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY;
        """
        
        cursor.execute(query, (skip, limit))

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results

    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()

@router.get("/view/ActoBazneshasteInfo")
async def ActoBazneshasteInfo(
    skip: int = Query(0, ge=0, description="Number of rows to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of rows to return"),
    id: int = Query()
):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"""
        SELECT * FROM dbo.ActoBazneshasteInfo
        WHERE CompanyID={id}
        ORDER BY RegNo
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY;
        """
        
        cursor.execute(query, (skip, limit))

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results

    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()
            
            
@router.get("/view/ActoBazneshasteFinalValue")
async def ActoBazneshasteFinalValue(
    skip: int = Query(0, ge=0, description="Number of rows to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of rows to return"),
    id: int = Query()
):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"""
        SELECT * FROM dbo.ActoBazneshasteFinalValue
        WHERE CompanyID={id}
        ORDER BY RegNo
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY;
        """
        
        cursor.execute(query, (skip, limit))

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results

    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()
  

@router.get("/view/VwShaghelCalculationResult")
async def VwShaghelCalculationResult(
    skip: int = Query(0, ge=0, description="Number of rows to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of rows to return"),
    id: str = Query()
):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"""
        SELECT * FROM Acto.vwShaghelCalculationResult
        WHERE MngmntTitle='{id}'
        ORDER BY RegNo
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY;
        """
        
        start = datetime.now()
        print(query)
        cursor.execute(query, (skip, limit))
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        end = datetime.now()
        print("spend time : ",end-start)
        return results

    except pyodbc.Error as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()
  


@router.get("/view/VwShaghelCalculationResult/csv")
async def VwShaghelCalculationResult_csv(
    id: str = Query(...)
):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"""
        SELECT * FROM Acto.vwShaghelCalculationResult
        WHERE MngmntTitle='{id}'
        ORDER BY RegNo;
        """
        start = datetime.now()
        print(query)
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        end = datetime.now()
        print("spend time : ", end - start)

        # Write CSV data to a string buffer
        output_str = io.StringIO()
        writer = csv.writer(output_str)
        writer.writerow(columns)  # header row
        writer.writerows(rows)    # data rows

        # Encode CSV string to UTF-8 bytes
        csv_bytes = output_str.getvalue().encode('utf-8')

        # Wrap bytes in a BytesIO stream for StreamingResponse
        output_bytes = io.BytesIO(csv_bytes)

        # Properly encode filename for HTTP header (RFC 5987)
        filename = f"VwShaghelCalculationResult_{id}.csv"
        quoted_filename = urllib.parse.quote(filename)
        content_disposition = f"attachment; filename*=UTF-8''{quoted_filename}"

        return StreamingResponse(
            output_bytes,
            media_type="text/csv; charset=utf-8",
            headers={"Content-Disposition": content_disposition}
        )

    except pyodbc.Error as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()