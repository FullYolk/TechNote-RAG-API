from fastapi import FastAPI,HTTPException
from schemas import AskRequest,AskResponse
from rag_service import answer_with_rag, rag_vector_store_cache, get_vector_store
from index_service import rebuild_vectorstore
import logging
from contextlib import asynccontextmanager
from db import init_db, log_query
import time

init_db()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

@asynccontextmanager
async def lifespan(app:FastAPI):
    logging.info("服务启动 开始预热Chroma向量库")
    get_vector_store()
    logging.info("预热完成")

    yield

    logging.info("服务关闭")

app = FastAPI(title="RAG微服务", lifespan=lifespan)


@app.get("/health")
def check_health():
    return {"status":"ok"}

@app.post("/ask",response_model=AskResponse)
def ask(request:AskRequest):
    try:
        safe_query = request.query.replace("\n", " ")
        if len(safe_query) > 30:
            safe_query = safe_query[:30] + "..."
        logging.info(f"收到请求|query:{safe_query}|k:{request.k}")
        start = time.perf_counter()
        res = answer_with_rag(request.query, request.k)
        latency_ms = int((time.perf_counter() - start) * 1000)
        log_query(request.query, res.answer, res.sources, latency_ms)
        return AskResponse(**res)
    except Exception as e:
        logging.error(f"发生错误，异常为{str(e)}",exc_info=True)
        raise HTTPException(status_code=500,detail="llm service error")
    
@app.post("/rebuild_index")
def rebuild_index():
    try:
        rag_vector_store_cache()
        res = rebuild_vectorstore()
        rag_vector_store_cache()
        logging.info("已更新向量库")
        return {
            "status":"ok",
            "detail":res
        }
    except Exception as e:
        logging.error(f"发生错误，异常为{str(e)}",exc_info=True)
        raise HTTPException(status_code=500,detail="建库错误")
