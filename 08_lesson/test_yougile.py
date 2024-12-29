import requests

base_url = "https://yougile.com/api-v2/"
login_user = "if0hh@freesourcecodes.com"
pass_user = "йцфяфк537"
ID_Company = "02963f0a-472b-45cc-971f-04e7587b7c90"

def test_auth():
    payload = {
        "login": login_user,
        "password": pass_user
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(base_url + "auth/companies", json=payload, headers=headers)

    print(response.text)

def test_key():
    payload = {
        "login": login_user,
        "password": pass_user,
        "companyId": ID_Company
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(base_url + "auth/keys/get", json=payload, headers=headers)

    print(response.text)

def test_create_key():
    global token
    payload = {
        "login": login_user,
        "password": pass_user,
        "companyId": ID_Company
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(base_url + "auth/keys", json=payload, headers=headers)
    response_json = response.json()
    token = response_json.get("key")


    print(response.text)

def test_projects():
    global token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(base_url + "projects", headers=headers)


    print(response.text)

def test_create_projects():
    global token
    global project_id
    payload = {
        "title": "Проект X",
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(base_url + "projects", json=payload, headers=headers)
    response_json = response.json()
    project_id = response.json().get("id")

    print(response.text)

def test_get_one_project():
    global token
    global project_id
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(base_url + f"projects/{project_id}", headers=headers)

    print(response.text)

def test_change_project():
    global token
    global project_id
    payload = {
        "title": "Project X"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.put(base_url + f"projects/{project_id}", json=payload, headers=headers)

    print(response.text)

    #Негативные тесты

def test_create_key_empty_login_or_password():
    payload = {
        "login": "",  # Пустой логин
        "password": pass_user,
        "companyId": ID_Company
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(base_url + "auth/keys", json=payload, headers=headers)
    print(response.text)


def test_create_project_missing_title():
    global token
    payload = {}  # Отсутствует обязательное поле "title"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(base_url + "projects", json=payload, headers=headers)
    print(response.text)

def test_create_key_missing_company_id():
    payload = {
        "login": login_user,
        "password": pass_user,
        # "companyId" отсутствует, хотя это обязательное поле
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(base_url + "auth/keys", json=payload, headers=headers)
    print(response.text)

def test_get_project_missing_authorization():
    global project_id
    headers = {
        "Content-Type": "application/json",
        # Отсутствует заголовок Authorization
    }

    response = requests.get(base_url + f"projects/{project_id}", headers=headers)
    print(response.text)
