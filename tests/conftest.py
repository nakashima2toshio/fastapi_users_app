import pytest
from fastapi.testclient import TestClient
from databases.database import Base, engine
from main import app


@pytest.fixture(scope="module")
def test_client():
    # テスト用のデータベースを作成
    Base.metadata.create_all(bind=engine)
    client = TestClient(app)
    yield client
    # テストが終了したらデータベースを削除
    Base.metadata.drop_all(bind=engine)
