# Tech Notes RAG QA

## 项目简介
一个基于 FastAPI + Chroma + OpenAI-compatible LLM 的技术笔记 RAG 问答服务。
支持对 Markdown 技术文档进行向量化检索，并基于检索上下文生成答案，同时返回来源信息。

## 技术栈
- Python
- FastAPI
- LangChain
- Chroma
- OpenAI-compatible API
- Pydantic

## 核心功能
- Markdown 文档加载
- 文本切分
- Embedding 向量化
- 向量检索 top-k
- 基于上下文回答问题
- 返回引用来源
- FastAPI /ask 接口
- **[New]** 基于 Lifespan 的向量库应用级预热与全局单例模式 (大幅降低首响延迟)
- **[New]** `/rebuild_index` 接口支持知识库热更新，无需重启服务
- **[New]** 底层接入 SQLite 实现全链路 RAG 日志埋点追踪 (Query, 耗时, 来源记录)

##  项目结构

```text
.
├── main.py                # FastAPI 路由入口
├── rag_service.py         # 核心业务层（原生 RAG 实现）
├── index_service.py       # 索引重构服务层 (处理热更新)
├── schemas.py             # 数据契约层（Pydantic 校验模型）
├── db.py                  # SQLite 数据库底层操作
├── embedding.py           # 向量化模型提取
├── rag_langchain_demo.py  # LangChain / LCEL 对照实现版本
├── app.db                 # SQLite 日志数据库 (自动生成)
├── chroma_db/             # 本地向量库持久化目录 (已在 .gitignore 忽略)
├── tools/   # 向量诊断与日志审查工具
└── .env                   # 环境变量配置 (已在 .gitignore 忽略)
```

## 快速开始
* 在根目录创建.env文件并添加以下变量：
```
LLM_API_KEY="your_api_key"
LLM_BASE_URL="your_base_url"
LLM_MODEL="your_model_name"
EMBEDDING_API_KEY="..."
EMBEDDING_BASE_URL="..."
EMBEDDING_MODEL="..."
```
* 建库
```
mkdir data
```

将你的md文件放入data文件夹中


由于 chroma_db/ 被 .gitignore 忽略，首次运行前需要先构建索引：
```
python build_vectorstore.py
```
或启动服务后调用：
```
POST /rebuild_index
```

看到文件目录下出现chroma_db/ 则建库完成


* 启动服务
```
uvicorn main:app --reload
```

* API调试
通过浏览器自动生成的swagger文档进行调试

## API 示例

### POST /ask

请求：
```
{
  "query": "什么是RAG？",
  "k": 3
}
```
响应：
```
{
  "answer": "...",
  "sources": [
    {
      "filename": "rag_notes.md",
      "score": 0.1234,
      "preview": "..."
    }
  ]
}
```
## 示例问题
- 什么是RAG？
- 什么时候应该使用RAG？
- RAG的全链路是什么？
- 什么是Tool Calling？

## 已知问题
- 当前数据集较小
- 检索结果可能集中于同一文档
- 尚未实现 rerank / hybrid search / query rewrite
- 如果 Windows 下 /rebuild_index 删除 chroma_db 失败，可先停止服务后执行 python build_vectorstore.py 重建索引。

## 优化计划
- **已完成**：重构 Chroma 为全局单例，并注入 FastAPI lifespan 实现服务预热。
- **已完成**：实现热重载机制与 SQLite 日志打点。
- **下一步**：构建 RAG 自动化评测脚本 (基于 eval 黄金测试集)。
- **未来计划**：引入 query rewrite (查询重写) 和 rerank (重排) 机制优化检索准确率。
- **未来计划**：加入 SSE 流式输出支持。
* 使用Docker构建镜像 一键部署