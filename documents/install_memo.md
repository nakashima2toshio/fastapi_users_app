##### install library & Packages

- pip install pytest httpx
- pip install alembic
- alembic init alembic
- alembic revision --autogenerate -m "Initial migration"
- alembic upgrade head

##### test data

- python databases/init_data.py


rm -rf alembic/versions/*

alembic revision --autogenerate -m "Update UUID to string"
alembic upgrade head
python app_databases/init_data.py
