# Langflow Implement

這個專案提供了一個完整的 Langflow 自建部署環境，整合了 PostgreSQL 資料庫與可選的本地模型推論引擎 (vLLM)。

## 🌟 功能特色

- **Langflow**: 強大的視覺化流程編排工具
- **PostgreSQL**: 穩定且高效的持久化資料庫 (v16)
- **Docker Compose**: 一鍵部署，輕鬆管理服務
- **Flow 自動匯入**: 提供 `import_flow.py` 腳本，可自動將 `flows/` 資料夾內的流程匯入系統
- **vLLM (選用)**: 支援本地 LLM 推論 (如 Llama 3)，適合隱私敏感或需離線執行的場景

## 📂 專案結構

```bash
langflow_implement/
├── docker-compose.yml       # Docker 服務定義檔
├── README.md                # 專案說明文件
├── import_flow.py           # Flow 自動匯入腳本
├── flows/                   # 存放待匯入的 Flow JSON 檔案
├── langflow-data/           # Langflow 設定與流程資料 (Volume)
├── langflow-postgres/       # PostgreSQL 資料庫資料 (Volume)
├── env/
│   └── network.env          # 網路環境變數設定
└── models/                  # (選用) 本地模型儲存目錄
    └── models--meta-llama--Llama-3.1-8B-Instruct/
        └── snapshots/
            └── manual-20250305/
                └── ...
```

## 🚀 快速開始

### 1. 環境設定

複製範例環境變數檔，並視需要設定 Proxy：

```bash
cp env/network.env.sample env/network.env
```

### 2. 啟動服務

使用 Docker Compose 啟動 Langflow 與 PostgreSQL：

```bash
docker compose up -d
```

### 3. 使用 Langflow

服務啟動後，請在瀏覽器開啟：
[http://localhost:7860](http://localhost:7860)

---

## 🛠️ 進階功能

### 📥 自動匯入 Flows

專案內建 `import_flow.py` 腳本，可將 `flows/` 資料夾中的 JSON 流程檔自動匯入 Langflow。

**使用方式：**
1. 確保 Langflow 服務已啟動且可正常存取。
2. 將 Flow JSON 檔案放入 `flows/` 資料夾。
3. 在本機執行匯入腳本 (需確保已安裝 python requests 套件)：

```bash
python import_flow.py
```

### 🤖 啟用 vLLM 本地模型 (選用)

若需使用本地模型，請依照以下步驟操作：

1. **準備模型檔案**：
   下載模型 (e.g., meta-llama/Llama-3.1-8B-Instruct) 至以下路徑：
   ```
   ./models/models--meta-llama--Llama-3.1-8B-Instruct/snapshots/manual-20250305/
   ```

2. **啟用服務**：
   編輯 `docker-compose.yml`，取消註解 `vLLM` 相關區塊。

3. **重啟服務**：
   ```bash
   docker compose up -d
   ```

---

## 📦 資料持久化說明

| 資料夾 | 說明 |
|---|---|
| `langflow-data` | 儲存 Langflow 的設定檔與流程資料 |
| `langflow-postgres` | PostgreSQL 資料庫檔案，確保資料不因容器重啟而遺失 |
| `models` | (選用) 存放 vLLM 使用的本地模型權重檔 |

---

## ⚠️ 常見問題與注意事項

- **權限問題**：
  若遇到 `Permission denied` 錯誤，請檢查 Volume 目錄權限：
  ```bash
  chmod -R 777 langflow-data langflow-postgres models
  ```

- **重置資料庫**：
  **警告：此操作將刪除所有已儲存的流程與設定！**
  ```bash
  docker compose down
  rm -rf langflow-postgres
  mkdir langflow-postgres
  chmod 777 langflow-postgres
  docker compose up -d
  ```

---

## 📬 聯絡

Author: TzuHsiang Huang
