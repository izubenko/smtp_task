import requests


base_url = "http://demo8955896.mockable.io/"
headers = {"Content-Type": "application/json"}


def make_request(
        method: str, url: str, **kwargs  # 'GET', 'POST', 'PUT'
) -> requests.Response:
    return requests.request(method, url, headers=headers, **kwargs)


def get(url: str, **kwargs) -> requests.Response:
    return make_request("GET", url, **kwargs)


def test_get_team_members():
    response = get(base_url + "members")
    response_body = response.json()['data']
    assert response.status_code == 200
    resp_members_list = response_body['members']
    members_list = [
        {'ID': '025a626c4c9c', 'day_birth': 650792792, 'email': 'phillip.jackson@domain.com', 'first_name': 'Phillip',
         'hr_department': 'UK(Head Office)', 'last_name': 'Jackson', 'level': 'sinior', 'mobile': 3806795421782,
         'position': 'software engineer', 'probation_period': 3},
        {'ID': '428fab00290d', 'day_birth': 1061019992, 'email': 'john.wilson@domain.com', 'first_name': 'John',
         'hr_department': 'UK(Head Office)', 'last_name': 'Wilson', 'level': 'middle', 'mobile': 38068723491001,
         'position': 'software engineer', 'probation_period': 6},
        {'ID': '34ec4eb66ba8', 'day_birth': 813488373, 'email': 'robert.dove@domain.com', 'first_name': 'Robert',
         'hr_department': 'UK(Head Office)', 'last_name': 'Dove', 'level': 'sinior', 'mobile': 380960234248772,
         'position': 'QA engineer', 'probation_period': 3}]
    assert resp_members_list == members_list


def test_get_team_member():
    member_id = "428fab00290d"
    response = get(base_url + f"member/{member_id}")
    response_body = response.json()['data']
    assert response.status_code == 200
    response_dict = {'ID': '428fab00290d', 'day_birth': 1061019992, 'email': 'john.wilson@domain.com',
                     'first_name': 'John', 'hr_department': 'UK(Head Office)', 'last_name': 'Wilson',
                     'level': 'middle', 'mobile': 38068723491001, 'position': 'software engineer',
                     'probation_period': 6}
    assert response_dict == response_body
