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

## データベースマイグレーション (Alembic)

### マイグレーションの基本コマンド

1. 新しいマイグレーションファイルの作成
```bash
# モデルの変更を自動検出してマイグレーションファイルを生成
docker-compose exec app alembic revision --autogenerate -m "説明文"

# 空のマイグレーションファイルを生成
docker-compose exec app alembic revision -m "説明文"
```

2. マイグレーションの実行
```bash
# 最新バージョンまでマイグレーションを実行
docker-compose exec app alembic upgrade head

# 特定のバージョンまでマイグレーション
docker-compose exec app alembic upgrade <revision_id>

# 1つ前のバージョンに戻す
docker-compose exec app alembic downgrade -1

# 完全に初期状態に戻す
docker-compose exec app alembic downgrade base
```

3. マイグレーションの状態確認
```bash
# 現在のリビジョンを確認
docker-compose exec app alembic current

# マイグレーション履歴を表示
docker-compose exec app alembic history

# 詳細な履歴を表示
docker-compose exec app alembic history -v
```

### マイグレーションファイルの場所
- マイグレーションファイルは `app/migrations/versions/` ディレクトリに生成されます
- 各ファイルには upgrade() と downgrade() の2つの関数が含まれています
- 必要に応じて、これらの関数を手動で編集できます

## データベースシーディング

### シードデータの種類と構成

プロジェクトには2種類のシードデータがあります：

1. マスターデータ
   - 本番環境でも使用する基本データ
   - `app/src/scripts/seeds/master/` に定義
   - 例：マスタテーブルの基本データなど

2. 開発用テストデータ
   - 開発環境でのみ使用するテストデータ
   - `app/src/scripts/seeds/development/` に定義
   - 例：テスト用のダミーデータなど

### シードデータの投入方法

基本的なコマンド：

```bash
# すべてのデータを投入（マスターデータ + 開発用データ）
docker-compose exec app python -m src.scripts.seed

# マスターデータのみ投入
docker-compose exec app python -m src.scripts.seed --type master

# 開発用テストデータのみ投入
docker-compose exec app python -m src.scripts.seed --type development
```

### 環境別の推奨設定

1. 開発環境
```bash
# マスターデータと開発用データの両方を投入
docker-compose exec app python -m src.scripts.seed --type all
```

2. テスト環境
```bash
# マスターデータのみを投入
docker-compose exec app python -m src.scripts.seed --type master
```

3. 本番環境
```bash
# マスターデータのみを投入
docker-compose exec app python -m src.scripts.seed --type master
```

### 新しいシードデータの追加方法

1. マスターデータの追加
   - `app/src/scripts/seeds/master/` に新しいシードファイルを作成
   - `seed.py` の `run_master_seeds()` 関数に新しいシード関数を追加

2. 開発用テストデータの追加
   - `app/src/scripts/seeds/development/` に新しいシードファイルを作成
   - `seed.py` の `run_development_seeds()` 関数に新しいシード関数を追加

### 注意事項

- マスターデータは本番環境でも使用されるため、慎重に管理してください
- 開発用テストデータは本番環境に投入しないでください
- シードデータを更新した場合は、チーム内で共有してください
- 大量のテストデータが必要な場合は、ファクトリーの使用を検討してください

## その他の機能

- FastAPI Swagger UI: http://localhost:8000/docs
- MinIO Console: http://localhost:9001
- MailHog Web UI: http://localhost:8025

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