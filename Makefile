SHELL = bash.exe
run-api: #db-upgrade
	source .env && uvicorn src.app.main:app --port=8000 --reload
db-upgrade:
	 source .env && cd src && alembic revision --autogenerate
run-migrations:
	source .env && cd src && alembic upgrade head