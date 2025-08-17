# Flask with Docker

這是一個簡單的範例，透過 **Flask** 建立一個 Web Server，並使用 **Docker** 部署。  
應用程式會監聽 **3333 port**，並允許來自所有 IP 的請求。

## ✨ 功能特色
- 基於 Flask 的輕量級 Web 應用程式
- Docker 容器化部署
- 支援開發模式的即時程式碼同步

## 🚀 快速開始

### 步驟 1：建立 Docker 映像檔
```bash
sudo docker build -t <img_name>:<tag> <path>
docker build -t flask-docker-app -f docker/Dockerfile .
```

### 步驟 2：啟動容器

#### 方法 1：生產模式
```bash
docker run -d -p 3000:3333 --name flask-app flask-docker-app
```

#### 方法 2：開發模式（支援程式碼即時同步）
```bash
docker run -d -p 3000:3333 -v $(pwd)/app:/app --name flask-app flask-docker-app
```

### 步驟 3：訪問應用程式
開啟瀏覽器並前往：`http://localhost:3000`

## 🛠 管理指令

### 檢視執行中的容器
```bash
docker ps
```

### 停止容器
```bash
# 停止容器
docker stop flask-app
```

### 移除容器
```bash
docker rm flask-app
```

## 📂 專案結構
```
project-root/
├── app/                # Flask 應用程式目錄
│   ├── main.py         # 應用程式入口檔案
│   └── ...             # 其他應用程式檔案
├── Dockerfile          # Docker 映像檔建立設定
└── README.md           # 專案說明文件
```

## 📋 系統需求
- Docker Desktop: 4.42.1 或以上
- Python 3.13.7 （如需本地開發）

## 🔧 開發說明
- 容器內部使用 **3333 port**
- 對外映射到 **3000 port**
- 開發模式下修改 `app/` 目錄中的檔案會即時反映到容器中