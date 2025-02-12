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

### シードデータの追加方法

1. 基本的な使い方
```bash
# テストデータを投入
docker-compose exec app python -m src.scripts.seed_tests
```

2. シードデータの確認
```bash
# APIエンドポイントで確認
curl http://localhost:8000/tests

# 直接データベースで確認
docker-compose exec db mysql -u myapp_user -pmyapp_password myapp -e "SELECT * FROM tests;"
```

### 新しいシーダーの作成

1. `app/src/scripts/` ディレクトリに新しいシーダーファイルを作成
2. 以下のテンプレートを使用：

```python
from src.database import SessionLocal
from src.models import YourModel

def seed_your_model() -> None:
    db = SessionLocal()
    try:
        data = [
            YourModel(field1="value1", field2="value2"),
            YourModel(field1="value3", field2="value4"),
        ]
        db.add_all(data)
        db.commit()
        print("データを追加しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_your_model()
```

### トラブルシューティング

1. データベース接続の確認
```bash
docker-compose exec app python -c "from src.database import engine; print(engine.url)"
```

2. テーブルの存在確認
```bash
docker-compose exec db mysql -u myapp_user -pmyapp_password myapp -e "SHOW TABLES;"
```

3. テーブルのリセット
```bash
docker-compose exec db mysql -u myapp_user -pmyapp_password myapp -e "TRUNCATE TABLE table_name;"
```

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