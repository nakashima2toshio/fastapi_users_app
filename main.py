# main.py
import logging
from logging.handlers import RotatingFileHandler
from fastapi import FastAPI
from models import user_models, todo_task_models, sns_models  # すべてのモデルをインポート
from routers import todo_task_router, sns_router, user_router
from app_databases.database import engine, Base

# ログフォーマットの設定
"""
%(name)s: ロガー（ロギングチャネル）の名前
%(levelno)s: メッセージの数値型のロギングレベル（DEBUG、INFO、WARNING、ERROR、CRITICAL）
%(levelname)s: メッセージのテキスト型のロギングレベル（"DEBUG"、"INFO"、"WARNING"、"ERROR"、"CRITICAL"）
%(pathname)s: ロギング呼び出しが行われたソースファイルの完全なパス名（利用可能な場合）
%(filename)s: パス名のファイル名部分
%(module)s: モジュール（ファイル名の名前部分）
%(lineno)d: ロギング呼び出しが行われたソースライン番号（利用可能な場合）
%(funcName)s: 関数名
"""
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# コンソールハンドラーの設定
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# ファイルハンドラーの設定 (ログのローテーション)
file_handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=10)
file_handler.setFormatter(formatter)

# ロガーの設定
logging.basicConfig(level=logging.INFO, handlers=[console_handler, file_handler])
logger = logging.getLogger(__name__)

# すべてのモデルをインポートした後にテーブルを作成
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to FastAPI Users App"}


app.include_router(todo_task_router.router, prefix="/todo", tags=["todo_task"])
app.include_router(sns_router.router, prefix="/sns", tags=["sns"])
app.include_router(user_router.router)
