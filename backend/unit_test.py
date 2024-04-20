import pytest
from database import User, Project, Transaction, Survey
from objects import UserInfo


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

    project.create_project(fake_project_info)
    project.delete_project_by_name("Fake Project")


if __name__ == "__main__":
    pytest.main(["-s", "unit_test.py"])
