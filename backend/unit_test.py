import pytest
import psycopg2
from database import User, Project, Transaction
from helper import UserInfo


def test_ping_user_db():
    user = User()
    assert user.ping() == True


def test_ping_project_db():
    project = Project()
    assert project.ping() == True


def test_ping_transaction_db():
    transaction = Transaction()
    assert transaction.ping() == True


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


if __name__ == "__main__":
    pytest.main(["-s", "unit_test.py"])
