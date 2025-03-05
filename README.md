# Langflow Implement

這是 Langflow 自建部署專案，包含：

- Langflow (流程編排工具)
- PostgreSQL (持久化資料庫)
- Docker Compose 管理

## 📂 專案結構
```
langflow_implement/ 
├── docker-compose.yml # Docker設定檔 
├── README.md # 說明文件 
├── langflow-data/ # Langflow設定與流程資料 
└── langflow-postgres/ # PostgreSQL資料庫
```

## 🚀 使用方法
1. 先建立目錄
    ```bash
    mkdir -p langflow-data langflow-postgres
    chmod 777 langflow-data langflow-postgres
    ```

2. 啟動容器
    ```bash
    docker compose up -d
    ```

3. 開啟Langflow
    [http://localhost:7860](http://localhost:7860)

---

## 📦 資料持久化

| 資料位置 | 說明 |
|---|---|
| langflow-data | Langflow的流程與設定檔 |
| langflow-postgres | PostgreSQL資料庫 |

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
