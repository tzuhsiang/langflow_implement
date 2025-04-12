#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import os

# 讀取 flows 目錄的 JSON 檔案
flows_dir = "flows"
json_files = [f for f in os.listdir(flows_dir) if f.endswith(".json")]

for json_file in json_files:
    try:
        with open(os.path.join(flows_dir, json_file), "r", encoding="utf-8") as f:
            flow_data = json.load(f)
            # 移除 user_id 和 folder_id
            if "user_id" in flow_data:
                del flow_data["user_id"]
            if "folder_id" in flow_data:
                del flow_data["folder_id"]

        
        # 發送請求並指定正確的 Content-Type
        response = requests.post(
            "http://localhost:7860/api/v1/flows/",
            json=flow_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.ok:
            print(f"Flow {json_file} 匯入成功")
        else:
            print(f"匯入失敗: {json_file}")
            print(f"狀態碼: {response.status_code}")
            print(f"錯誤訊息: {response.text}")
            
    except Exception as e:
        print(f"處理 {json_file} 時發生錯誤: {str(e)}")
