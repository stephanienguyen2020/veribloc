run_backend_local: 
	cd backend && uvicorn app:app --reload

test: 
	cd backend && python3 unit_tests.py