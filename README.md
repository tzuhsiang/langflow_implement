# Langflow Implement

這是 Langflow 自建部署專案，包含：

- Langflow (流程編排工具)
- PostgreSQL (持久化資料庫)
- Docker Compose 管理
- vLLM：本地化推論引擎，使用 Hugging Face 模型 (如 Llama3)

## 📂 專案結構
```
langflow_implement/
└── docker-compose.yml       # Docker 設定檔
└── README.md                 # 說明文件
└── langflow-data/            # Langflow 設定與流程資料
└── langflow-postgres/        # PostgreSQL 資料庫
└── models/                    # 本地模型儲存目錄
    └── models--meta-llama--Llama-3.1-8B-Instruct/
        └── snapshots/
            └── manual-20250305/
                └── model.safetensors
                └── config.json
                └── tokenizer.json (or other tokenizer files)
```


## 🚀 使用流程
1. 下載模型並放置到指定位置

請先下載好模型 (e.g., meta-llama/Llama-3.1-8B-Instruct)，放到如下路徑：
```
./models/models--meta-llama--Llama-3.1-8B-Instruct/snapshots/manual-20250305/
```
2. 目錄權限設定 (optional)

若遇到權限問題：
```
chmod -R 777 langflow-data langflow-postgres models
```

3. 啟動服務
```
docker compose up -d
```

4. 開啟 Langflow 編排介面
[http://localhost:7860](http://localhost:7860)


---

## 📦 資料持久化

| 資料位置 | 說明 |
|---|---|
| langflow-data | Langflow的流程與設定檔 |
| langflow-postgres | PostgreSQL資料庫 |
| models | 本地模型檔案 |

---

## ⚠️ 注意

- 若權限有問題，記得檢查Volume目錄權限：
    ```bash
    chmod -R 777 langflow-data langflow-postgres
    ```

- 如果要重置DB：
    ```bash
    rm -rf langflow-postgres
    mkdir langflow-postgres
    chmod 777 langflow-postgres
    ```

---

## 📬 聯絡
Author: TzuHsiang Huang
