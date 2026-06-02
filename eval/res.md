GET /health
{
  "status": "ok"
}
POST /ask
{
  "query": "什么是RAG？",
  "k": 3
}
{
  "answer": "根据提供的参考资料，其中并未明确给出RAG（检索增强生成）的直接定义或全称。因此，无法回答“什么是RAG”。",
  "sources": [
    {
      "filename": "rag_notes.md",
      "score": 1.136,
      "preview": "解析层 (VLM - 视觉语言模型)： 专门对付包含图表的 PDF，把图片里的复杂财报转换成干净的文..."
    }
  ]
}
{
  "query": "什么是RAG？",
  "k": 10
}
{
  "answer": "不知道",
  "sources": [
    {
      "filename": "rag_notes.md",
      "score": 1.136,
      "preview": "解析层 (VLM - 视觉语言模型)： 专门对付包含图表的 PDF，把图片里的复杂财报转换成干净的文..."
    }
  ]
}

{
  "query": "什么是RAG？",
  "k": 3
}
## 下面是完成修复之后的结果
{
  "answer": "RAG，全称Retrieval-Augmented Generation（检索增强生成），是一种结合了检索系统和生成式大模型的技术范式。它通过在生成回答前先检索相关上下文片段，并将这些片段作为提示词注入大模型，以强制模型基于真实数据回答，从而提升答案的时效性、专业性和可溯源性。",
  "sources": [
    {
      "filename": "rag_notes.md",
      "score": 0.732,
      "preview": "## 什么是RAG？ * RAG，全称Retrieval-Augmented Generation(..."
    }
  ]
}
{
  "query": "什么时候应该使用RAG？",
  "k": 3
}
{
  "answer": "根据参考资料，当业务知识更新极快且需要严格事实时，应该使用RAG。例如，在做金融财报分析助手时，数据每天都在变且不容许胡说八道，此时必须用RAG，因为它的知识更新成本低且可解释性强。",
  "sources": [
    {
      "filename": "rag_notes.md",
      "score": 0.8434,
      "preview": "* 组装生成(Generation & Citation):拼接上下文，调用大模型生成答案，并流式输..."
    }
  ]
}
{
  "query": "RAG的全链路是什么？",
  "k": 3
}
{
  "answer": "根据参考资料，RAG的全链路包括两个阶段：\n\n1. **离线建库阶段**：涉及数据解析和清洗（Data Parsing/Cleaning），例如将PDF、Word、HTML等转化为纯文本，复杂图表使用视觉大模型或版面分析工具转为md格式或单独总结为文本。\n\n2. **组装生成阶段**：拼接上下文，调用大模型生成答案，并流式输出（SSE），同时附带Citation（引用来源）以保证可解释性。",
  "sources": [
    {
      "filename": "rag_notes.md",
      "score": 0.7464,
      "preview": "## 什么是RAG？ * RAG，全称Retrieval-Augmented Generation(..."
    }
  ]
}
{
  "query": "RAG和微调有什么区别？",
  "k": 3
}
{
  "answer": "根据参考资料，RAG（检索增强生成）和微调（Fine-tuning）的主要区别在于适用场景不同：\n\n1. **RAG** 适用于业务知识更新极快、需要严格事实的场景（如金融财报分析助手）。它通过外部实时检索相关上下文，让模型基于真实数据回答，知识更新成本低，可解释性强，能有效抑制幻觉。\n2. **微调** 适用于需要改变模型输出格式、语气或特定技能的场景（如输出特定JSON格式、克隆客服语气、医疗报告格式生成）。它主要改变模型的行为模式和能力，而不是提供外部知识。\n\n高阶做法通常是将两者结合：先用微调改变模型的语气和逻辑思维，再用RAG提供实时外挂知识。",
  "sources": [
    {
      "filename": "rag_notes.md",
      "score": 0.6076,
      "preview": "* 组装生成(Generation & Citation):拼接上下文，调用大模型生成答案，并流式输..."
    }
  ]
}
{
  "query": "什么是Tool Calling？？",
  "k": 3
}
{
  "answer": "不知道",
  "sources": [
    {
      "filename": "rag_notes.md",
      "score": 1.0064,
      "preview": "### 在线问答阶段 * 查询预处理/重写(Query Processing / Rewrite):..."
    }
  ]
}
{
  "query": "北京今天的天气怎么样？",
  "k": 3
}
{
  "answer": "不知道。",
  "sources": [
    {
      "filename": "rag_notes.md",
      "score": 1.2117,
      "preview": "2. 适用微调 (Fine-tuning) 的场景（需要改变模型的输出格式、语气或特定技能）： 如果..."
    }
  ]
}
{
  "query": "原神是什么类型的游戏？",
  "k": 3
}
{
  "answer": "原神是由米哈游开发的一款开放世界冒险游戏。",
  "sources": [
    {
      "filename": "genshin.md",
      "score": 0.417,
      "preview": "原神是由米哈游开发的一款开放世界冒险游戏"
    },
    {
      "filename": "rag_notes.md",
      "score": 1.203,
      "preview": "生成层 (重型 LLM，如 DeepSeek-R1 / GPT-4o)： 这是坐镇大后方的“主治医师..."
    }
  ]
}