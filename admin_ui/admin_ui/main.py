import os

import httpx
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from admin_ui.chroma_client import (
    heartbeat,
    get_collection_count,
    list_collections,
    query_collection,
    get_chunks,
)
from admin_ui.config import settings

app = FastAPI(title="RAG Admin UI")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


def verify_token(request: Request):
    token = request.query_params.get("token") or request.headers.get("X-Admin-Token")
    if token != settings.admin_api_token:
        raise HTTPException(status_code=403, detail="Invalid admin token")
    return token


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, token: str = Depends(verify_token)):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "token": token,
            "alive": heartbeat(),
            "count": get_collection_count(),
            "collections": list_collections(),
            "collection": settings.chroma_collection,
            "indexer_url": settings.indexer_api_url,
        },
    )


@app.post("/api/reindex")
async def reindex(_token: str = Depends(verify_token)):
    async with httpx.AsyncClient(timeout=600.0) as client:
        resp = await client.post(f"{settings.indexer_api_url}/reindex")
    return JSONResponse(content=resp.json())


@app.get("/api/search")
async def search_api(
    q: str = Query(...),
    doc_type: str | None = Query(None),
    n: int = Query(5),
    _token: str = Depends(verify_token),
):
    where = {"doc_type": doc_type} if doc_type else None
    results = query_collection(q, n_results=n, where=where)
    return JSONResponse(content=results)


@app.get("/search", response_class=HTMLResponse)
async def search_page(request: Request, token: str = Depends(verify_token)):
    return templates.TemplateResponse(
        request,
        "search.html",
        {"token": token},
    )


@app.get("/chunks", response_class=HTMLResponse)
async def chunks_page(
    request: Request,
    doc_type: str | None = Query(None),
    source: str | None = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=200),
    token: str = Depends(verify_token),
):
    where: dict | None = {}
    if doc_type:
        where["doc_type"] = doc_type
    if source:
        where["source"] = source
    if not where:
        where = None

    data = get_chunks(skip=skip, limit=limit, where=where)
    return templates.TemplateResponse(
        request,
        "chunks.html",
        {
            "token": token,
            "chunks": data,
            "doc_type": doc_type,
            "source": source,
            "skip": skip,
            "limit": limit,
            "zip": zip,
        },
    )


if __name__ == "__main__":
    uvicorn.run(app, host=settings.admin_ui_host, port=settings.admin_ui_port)
