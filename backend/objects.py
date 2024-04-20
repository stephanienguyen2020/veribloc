from dataclasses import dataclass
from datetime import datetime, timedelta
from pydantic import BaseModel
@dataclass
class UserInfo(BaseModel): 
    first_name: str
    last_name: str
    email: str
    password: str
    institution: str = None
    projects: list = None
    participated_projects: list = None
    is_active: bool = True
    balance: float = 0.0
    payment: dict = None
    
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "institution": self.institution,
            "projects": self.projects,
            "participated_projects": self.participated_projects,
            "is_active": self.is_active,
            "balance": self.balance,
            "payment": self.payment,
        }
     
@dataclass
class ProjectInfo(BaseModel): 
    title: str
    description: str
    owner: str
    members: list
    participants: list
    is_active: bool = True
    project_type: str = "private"
    start_date: str = None
    end_date: str = None
    budget: float = 0.0
    salary: float = 0.0
        
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "owner": self.owner,
            "members": self.members,
            "participants": self.participants,
            "is_active": self.is_active,
            "project_type": self.project_type,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "budget": self.budget,
            "salary": self.salary,
        }
    
@dataclass
class TransactionInfo(BaseModel):
    transaction_id: str
    project_id: str
    seller_id: str
    buyer_id: str
    amount: float
    valid_until: str = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "project_id": self.project_id,
            "seller_id": self.seller_id,
            "buyer_id": self.buyer_id,
            "amount": self.amount,
            "valid_until": self.valid_until,
        }
    

class SurveyInfo(BaseModel):
    def __init__(self, seller_id, buyer_id, project_id, content, answers, is_accepted, feedback=""):
        self.seller_id = seller_id
        self.buyer_id = buyer_id
        self.project_id = project_id
        self.content = content
        self.answers = answers
        self.is_accepted = is_accepted
        self.feedback = feedback

    def to_dict(self):
        return {
            "seller_id": self.seller_id,
            "buyer_id": self.buyer_id,
            "project_id": self.project_id,
            "content": self.content,
            "answers": self.answers,
            "is_accepted": self.is_accepted,
            "feedback": self.feedback,
        }
    
    def __str__(self):
        return f"Survey: {self.content} from {self.seller_id} to {self.buyer_id} for project {self.project_id} with answers {self.answers} and feedback {self.feedback}"
    
    def __repr__(self):
        return f"Survey: {self.content} from {self.seller_id} to {self.buyer_id} for project {self.project_id} with answers {self.answers} and feedback {self.feedback}"