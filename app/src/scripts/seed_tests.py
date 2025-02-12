from sqlalchemy.orm import Session

from src.database import SessionLocal
from src.models import Test


def seed_tests():
    db = SessionLocal()
    try:
        test_data = [
            Test(name="テスト1", description="これはテストデータ1です。"),
            Test(name="テスト2", description="これはテストデータ2です。"),
            Test(name="テスト3", description="これはテストデータ3です。"),
        ]
        db.add_all(test_data)
        db.commit()
        print("テストデータを追加しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_tests()
