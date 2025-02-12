# FastAPI開発環境

FastAPI、MySQL、MinIO、MailHogを使用した開発環境のセットアップです。

## 必要条件

- Docker
- Docker Compose

## セットアップ手順

1. リポジトリをクローン
```bash
git clone <repository-url>
cd <project-directory>
```

2. 環境変数ファイルの準備
```bash
cp .env.example .env
```

3. Dockerコンテナの起動
```bash
docker-compose up -d
```

4. マイグレーションの実行
```bash
docker-compose exec app alembic upgrade head
```

## 各サービスへのアクセス

- FastAPI アプリケーション: http://localhost:8000
- FastAPI Swagger UI: http://localhost:8000/docs
- MinIO Console: http://localhost:9001
  - ユーザー名: minio_admin
  - パスワード: minio_password
- MailHog Web UI: http://localhost:8025
- MySQL: localhost:3306

## 環境の切り替え

### 開発環境
- `.env`ファイルを使用
- ローカルのDockerコンテナを使用

### 本番環境
- `.env.prod`ファイルを使用
- 実際の本番サービスに接続

環境の切り替えは以下のコマンドで行います：

```bash
# 開発環境
ENV_FILE=.env docker-compose up -d

# 本番環境
ENV_FILE=.env.prod docker-compose up -d
```

## プロジェクト構成 