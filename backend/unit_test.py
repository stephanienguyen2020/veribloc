import pytest
from database import User, Project, Transaction, Survey
from objects import UserInfo, ProjectInfo, TransactionInfo, SurveyInfo


def test_ping_user_db():
    user = User()
    assert user.ping() == True


def test_ping_project_db():
    project = Project()
    assert project.ping() == True


def test_ping_transaction_db():
    transaction = Transaction()
    assert transaction.ping() == True

def test_ping_survey_db():
    survey = Survey()
    assert survey.ping() == True

def test_insert_user():
    user = User()
    user_info = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john_doe@gmail.com",
        password="password123",
        projects=["Project 1", "Project 2"],
        participated_projects=["Project 3", "Project 4"],
        balance=100.0,
        payment={"method": "bitcoin", "amount": 50.0},
    ).to_dict()

    user.insert_user(user_info)
    user.delete_user_by_email("john_doe@gmail.com")

def test_create_project():
    project = Project()
    fake_project_info = {
        "title": "Fake Project",
        "description": "This is a fake project",
        "owner": "Fake Owner",
        "members": ["Member 1", "Member 2"],
        "participants": ["Participant 1", "Participant 2"],
        "is_active": True,
        "start_date": None,
        "end_date": None,
        "budget": 0.0,
        "salary": 0.0
    }

    project.insert_project(fake_project_info)
    project.delete_project("Fake Project", "Fake Owner")


def test_pay(): 
    # Create fake users
    user = User()

    buyer_info = UserInfo(
        first_name="Jane",
        last_name="Doe",
        email="jane_doe@gmail.com",
        password="password321",
        projects=["Project 1", "Project 2"],
        participated_projects=[],
        balance=100.0,
        payment={"method": "bitcoin", "amount": 50.0},
    ).to_dict()

    user.insert_user(buyer_info)
    buyer_id = user.get_user_id(buyer_info["email"], buyer_info["password"])

    seller_info = UserInfo(
        first_name="John",
        last_name="Doe",
        email="john_doe@gmail.com",
        password="password123",
        projects=[""],
        participated_projects=["Project 1"],
        balance=100.0,
        payment={"method": "bitcoin", "amount": 50.0},
    ).to_dict()

    user.insert_user(seller_info)
    seller_id = user.get_user_id(seller_info["email"], seller_info["password"])

    transaction = Transaction()
    transaction_info = TransactionInfo(
        transaction_id="123",
        project_id="Project 1",
        seller_id=seller_id,
        buyer_id=buyer_id,
        amount=10.0
    ).to_dict()

    transaction.pay(transaction_info)



if __name__ == "__main__":
    pytest.main(["-s", "unit_test.py"])
