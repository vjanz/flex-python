SHELL = bash.exe
run-api: #db-upgrade
	source .env && uvicorn src.app.main:app --reload