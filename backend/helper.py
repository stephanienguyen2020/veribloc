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
    
