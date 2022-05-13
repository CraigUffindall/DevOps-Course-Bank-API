"""Integration tests for app.py"""
from typing import Type
from urllib import response
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client: FlaskClient):
    # act
    response = client.post('/accounts/Account1')

    # assert
    assert response.status_code == 200
    assert response.data.decode().strip() == '{"name": "Account1"}'


def test_account_creation_with_blank_name(client: FlaskClient):
    # act
    response = client.post('/accounts/   ')

    # assert
    assert response.status_code == 400
    assert response.data.decode().strip() == '{"message": "Account name cannot be None or empty"}'


def test_get_account_which_exists(client: FlaskClient):
    # arrange
    response = client.post('/accounts/Account1')

    # act
    response = client.get('/accounts/Account1')

    # assert
    assert response.status_code == 200
    assert response.data.decode().strip() == '{"name": "Account1"}'


def test_get_account_which_does_not_exist(client: FlaskClient):
    # arrange
    response = client.post('/accounts/Account1')

    # act
    response = client.get('/accounts/Account2')

    # assert
    assert response.status_code == 404
    assert response.data.decode().strip() == '{"message": "Account not found. You have requested this URI [/accounts/Account2] but did you mean /accounts/<string:name> ?"}'