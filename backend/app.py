from fastapi import FastAPI
from database import User, Project, Transaction
from helper import UserInfo

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/signup")
def signup(user: UserInfo):
    try:
        db = User()
        db.insert_user(user.to_dict())
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.post("/login")
def login(email: str, password: str):
    try:
        db = User()
        user = db.get_user_by_email(email)
        if user["password"] == password:
            return {"status": "success", "user_id": str(user["_id"])}
        else:
            return {"status": "error", "message": "Invalid password"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.post("/create_project")
def create_project(project: dict):
    try:
        db = Project()
        db.insert_project(project)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.post("/search_project")
def search_project(query: dict):
    try:
        db = Project()
        projects = db.search_project(query)
        return {"status": "success", "projects": projects}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

@app.post("/update_project")
def update_project(id: str, project: dict):
    try:
        db = Project()
        db.update_project(id, project)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.post("/delete_project")
def delete_project(id: str):
    try:
        db = Project()
        db.delete_project_by_id(id)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.post("/create_transaction")
def create_transaction(transaction: dict):
    try:
        db = Transaction()
        db.insert_transaction(transaction)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.post("/search_transaction")
def search_transaction(query: dict):
    try:
        db = Transaction()
        transactions = db.search_transaction(query)
        return {"status": "success", "transactions": transactions}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.post("/update_transaction")
def update_transaction(id: str, transaction: dict):
    try:
        db = Transaction()
        db.update_transaction(id, transaction)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

