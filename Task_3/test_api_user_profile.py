import requests

form_data = {
    "username": (None, "Nastya379"),
    "password": (None, "2d94b3b2a2")
}

url_login = "https://test-stand.gb.ru/gateway/login"

response = requests.post(url_login, files=form_data)

print("Статус код авторизации:", response.status_code)
print("Ответ авторизации:", response.text)

assert response.status_code == 200, f"Ошибка авторизации: {response.status_code}"

try:
    data = response.json()
    token = data.get("token")
    user_id = data.get("id") or data.get("user_id")
    username = data.get("username")

    print(f" Получен токен: {token}")
    print(f" ID пользователя: {user_id}")
    print(f" Имя пользователя: {username}")
except Exception as e:
    print(" Не удалось распарсить JSON:", e)
    exit()

url_profile = f"https://test-stand.gb.ru/api/users/profile/{user_id}"
headers_profile = {
    "X-Auth-Token": token
}

response_profile = requests.get(url_profile, headers=headers_profile)

print("Статус код профиля:", response_profile.status_code)
print("Ответ профиля:", response_profile.text)

assert response_profile.status_code == 200, f"Ошибка получения профиля: {response_profile.status_code}"

profile_data = response_profile.json()
assert profile_data.get("username") == username, "Имя пользователя не совпадает!"

print(" Проверка успешна. Имя пользователя совпадает.")