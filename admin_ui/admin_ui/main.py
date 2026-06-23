import os

import httpx
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from admin_ui.chroma_client import (
    heartbeat,
    get_collection_count,
    list_collections,
    query_collection,
    get_chunks,
    get_collection_info,
    clear_collection,
    delete_collection,
)
from admin_ui.config import settings

app = FastAPI(title="RAG Admin UI")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


def verify_token(request: Request):
    return "no-auth"


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


@app.get("/api/collections")
async def api_list_collections(_token: str = Depends(verify_token)):
    collections = list_collections()
    result = []
    for name in collections:
        info = get_collection_info(name)
        if info:
            result.append(info)
    return JSONResponse(content={"collections": result})


@app.get("/api/collections/{name}")
async def api_collection_info(
    name: str = Path(...),
    _token: str = Depends(verify_token),
):
    info = get_collection_info(name)
    if info is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return JSONResponse(content=info)


@app.post("/api/collections/{name}/clear")
async def api_clear_collection(
    name: str = Path(...),
    _token: str = Depends(verify_token),
):
    try:
        deleted = clear_collection(name)
        return JSONResponse(
            content={"status": "success", "collection": name, "deleted_chunks": deleted}
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/api/collections/{name}/delete")
async def api_delete_collection(
    name: str = Path(...),
    _token: str = Depends(verify_token),
):
    try:
        delete_collection(name)
        return JSONResponse(
            content={"status": "success", "message": f"Collection {name} deleted"}
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


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
