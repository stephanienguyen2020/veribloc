from dataclasses import dataclass

@dataclass
class UserInfo: 
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
class ProjectInfo: 
    title: str
    description: str
    owner: str
    members: list
    participants: list
    is_active: bool = True
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
            "start_date": self.start_date,
            "end_date": self.end_date,
            "budget": self.budget,
            "salary": self.salary,
        }
    
@dataclass
class Transaction:
    project_id: str
    seller_id: str
    buyer_id: str
    amount: float
    valid_until: str

    def to_dict(self):
        return {
            "project_id": self.project_id,
            "seller_id": self.seller_id,
            "buyer_id": self.buyer_id,
            "amount": self.amount,
            "valid_until": self.valid_until,
        }
    

class Survey:
    def __init__(self, survey_id, user_id, project_id, answers):
        self.survey_id = survey_id
        self.user_id = user_id
        self.project_id = project_id
        self.answers = answers

    def to_dict(self):
        return {
            "survey_id": self.survey_id,
            "user_id": self.user_id,
            "project_id": self.project_id,
            "answers": self.answers,
        }
    
    def __str__(self):
        return f"Survey ID: {self.survey_id}, User ID: {self.user_id}, Project ID: {self.project_id}, Answers: {self.answers}"
    
    def __repr__(self):
        return f"Survey ID: {self.survey_id}, User ID: {self.user_id}, Project ID: {self.project_id}, Answers: {self.answers}"