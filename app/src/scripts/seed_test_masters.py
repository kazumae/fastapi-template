from src.database import SessionLocal
from src.models import TestMaster


def seed_test_masters() -> None:
    db = SessionLocal()
    try:
        test_masters = [
            TestMaster(
                code="TEST001",
                name="テストマスター1",
                description="これはテストマスター1です。",
            ),
            TestMaster(
                code="TEST002",
                name="テストマスター2",
                description="これはテストマスター2です。",
            ),
            TestMaster(
                code="TEST003",
                name="テストマスター3",
                description="これはテストマスター3です。",
            ),
        ]
        db.add_all(test_masters)
        db.commit()
        print("テストマスターデータを追加しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_test_masters()
