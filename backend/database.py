from pymongo import MongoClient
from dotenv import load_dotenv
import os
from objects import UserInfo, ProjectInfo, TransactionInfo, SurveyInfo

load_dotenv(override=True)

class User:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI"))

    def ping(self):
        try:
            self.client.admin.command("ping")
            return True
        except Exception as e:
            return False

    def get_users_database(self):
        return self.client["labcoin"]["users"]

    def insert_user(self, user):
        users = self.get_users_database()
        users.insert_one(user)

    def get_user_id_by_email(self, email):
        """
        Get user by email
        """
        users = self.get_users_database()
        return users.find_one({"email": email})["_id"]

    def get_user_by_id(self, id):
        users = self.get_users_database()
        return users.find_one({"_id": id})

    def update_user(self, email, user):
        users = self.get_users_database()
        users.update_one({"email": email}, {"$set": user})

    def delete_user_by_email(self, email):
        """
        Delete user by email
        """
        users = self.get_users_database()
        users.delete_one({"email": email})

    def get_user_id(self, email, password):
        users = self.get_users_database()
        return users.find_one({"email": email, "password": password})["_id"]


class Project:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI"))

    def ping(self):
        try:
            self.client.admin.command("ping")
            return True
        except Exception as e:
            return False
        
    def get_projects_database(self):
        return self.client["labcoin"]["projects"]

    def insert_project(self, project):
        projects = self.get_projects_database()
        projects.insert_one(project)

    def get_project(self, id):
        projects = self.get_projects_database()
        return projects.find_one({"_id": id})

    def update_project(self, id, project):
        projects = self.get_projects_database()
        projects.update_one({"_id": id}, {"$set": project})

    def search_project(self, query):
        projects = self.get_projects_database()
        return projects.find(query)
    
    def get_project_id(self, title, owner):
        projects = self.get_projects_database()
        return projects.find_one({"title": title, "owner": owner})
    
    def delete_project(self, title, owner):
        projects = self.get_projects_database()
        projects.delete_one({"title": title, "owner": owner})
    
class Transaction:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI"))

    def ping(self):
        try:
            self.client.admin.command("ping")
            return True
        except Exception as e:
            return False
        
    def get_transactions_database(self):
        return self.client["labcoin"]["transactions"]
    
    def insert_transaction(self, transaction):
        transactions = self.get_transactions_database()
        transactions.insert_one(transaction)

    def search_transaction(self, query):
        transactions = self.get_transactions_database()
        return transactions.find(query)
    
    def get_transactions(self, seller_id, buyer_id, project_id):
        transactions = self.get_transactions_database()
        return transactions.find({"seller_id": seller_id, "buyer_id": buyer_id, "project_id": project_id})
    
    def pay_helper(self, transaction): 
        try:
            userdb = User()
            seller = userdb.get_user_by_id(transaction.seller_id)
            buyer = userdb.get_user_by_id(transaction.buyer_id)

            
            if transaction.project_id in buyer["projects"]:
                if seller["balance"] < transaction.amount:
                    raise Exception("Seller does not have enough balance")
                
                seller["balance"] += transaction.amount
                buyer["balance"] -= transaction.amount
                userdb.update_user(seller["email"], seller)
                userdb.update_user(buyer["email"], buyer)
                return {"status": "success"}
            else: 
                raise Exception("Buyer is not a participant of the project")
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def pay(self, transaction: TransactionInfo):
        """
        Pay for a project with a transaction

        Args:
            TransactionInfo: Transaction information. Includes: 
            transaction_id (str): Transaction ID
            project_id (str): Project ID
            seller_id (str): Seller ID
            buyer_id (str): Buyer ID
            amount (float): Amount to pay
            valid_until (str): Valid duration. After this, transaction won't be accepted (default: 30 days from now)
        
        """
        # try:
        #     transactions = self.get_transactions_database()
        #     transactions.insert_one(transaction.to_dict())
        #     return self.pay_helper(transaction)
        # except Exception as e:
        #     return {"status": "error", "message": str(e)}

        transactions = self.get_transactions_database()
        transactions.insert_one(transaction)
        self.pay_helper(transaction)
        self.insert_transaction(transaction)


class Survey:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI"))

    def ping(self):
        try:
            self.client.admin.command("ping")
            return True
        except Exception as e:
            return False
        
    def get_surveys_database(self):
        return self.client["labcoin"]["surveys"]
    
    def insert_survey(self, survey):
        surveys = self.get_surveys_database()
        surveys.insert_one(survey)

    def get_survey(self, survey_id):
        surveys = self.get_surveys_database()
        return surveys.find_one({"survey_id": survey_id})
