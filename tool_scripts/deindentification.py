import os
import json
import requests

origin_data_folder="/home/thhuang/voc_data/bli_data/json"
processed_data_folder="/home/thhuang/myproject/langflow_implement/processed_json"

langflow_api="http://localhost:7860/api/v1/run/306915ac-ecf9-4b22-a5e9-f6ccd1659de4?stream=false"
# langflow_api="http://localhost:7860/api/v1/run/3609db05-62d9-4cec-8dd6-5f9a2fdde803?stream=false"


url = "http://localhost:7860"

try:
    # 發送 GET 請求
    response = requests.get(url, timeout=5)
    
    # 檢查回應狀態碼
    if response.status_code == 200:
        print("成功連接到 API:", url)
    else:
        print(f"無法連接到 API，狀態碼: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("連接失敗，錯誤訊息:", e)


#讀取origin_data_folder的json檔案
def read_json_files(folder_path):
    json_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                json_data.append(data)
    return json_data

#將json檔案寫入processed_data_folder
def write_json_files(folder_path, json_data):
    for i, data in enumerate(json_data):
        file_path = os.path.join(folder_path, f'processed_{i}.json')
        with open(file_path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    data_list=read_json_files(origin_data_folder)

    # 準備 API 請求
    headers = {"Content-Type": "application/json"}
    result_list=[]
    total_dialogues=len(data_list)

    dialogues_counter=1

    for i in data_list[:1]:

        counter=1
        total_sentences=len(i["conversations"])
        # processed_conversations=[]
        for sentence in i["conversations"]:

            data={"input_value": json.dumps(sentence["content"])}

            try:
                response=requests.post(langflow_api, headers=headers, json=data)
                content=response.json()['outputs'][0]['outputs'][0]['results']['text']["text"]
                sentence["content"]=content
                print(f"對話處理進度：{dialogues_counter}/{total_dialogues}，語句處理進度總共：{counter}/{total_sentences}")
            except:
                print("Error in response:", response.text)
            
            counter+=1
        
        result_list.append(i)
        print(f"總共{total_dialogues}筆對話，第{dialogues_counter}筆對話處理成功")
        dialogues_counter+=1
        

    write_json_files(processed_data_folder, result_list)

main()