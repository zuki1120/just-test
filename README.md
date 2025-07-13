# just-test

```
multi_agent_rewriter/
│
├── main.py                         # 入口主程式
├── config.py                       # 設定檔，包括 LLM 選擇、迭代次數等
│
├── agents/
│   ├── base_agent.py              # Agent 抽象基底
│   ├── rewriter_agent.py          # Agent A & B：將 input rewrite 成問題敘述 + SOP
│   └── judge_agent.py             # 判斷 Agent A/B 輸出相似性的 agent
│
├── utils/
│   ├── similarity.py              # 用來計算輸出相似性的工具（embedding / cosine similarity）
│   └── formatter.py               # 格式處理與比對原始 input 的工具
│   └── llm_judge.py                 ← llm-based 比對邏輯
│
|── llm/
|   ├── __init__.py
|   ├── openai_wrapper.py
|   ├── claude_wrapper.py
|   └── mistral_wrapper.py
└── logs/
    └── iteration_log.txt          # 儲存每一輪輸出差異與調整紀錄

```