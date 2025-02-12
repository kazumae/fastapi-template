from src.database import SessionLocal
from src.models import Test


def seed_tests() -> None:
    db = SessionLocal()
    try:
        test_data = [
            Test(
                name="テスト1",
                description="これはテストデータ1です。",
                test_master_id=1,  # TEST001のID
            ),
            Test(
                name="テスト2",
                description="これはテストデータ2です。",
                test_master_id=1,  # TEST001のID
            ),
            Test(
                name="テスト3",
                description="これはテストデータ3です。",
                test_master_id=2,  # TEST002のID
            ),
            Test(
                name="テスト4",
                description="これはテストデータ4です。",
                test_master_id=2,  # TEST002のID
            ),
            Test(
                name="テスト5",
                description="これはテストデータ5です。",
                test_master_id=3,  # TEST003のID
            ),
        ]
        db.add_all(test_data)
        db.commit()
        print("テストデータを追加しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        db.rollback()
    finally:
        db.close()
