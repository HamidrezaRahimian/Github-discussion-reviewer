import requests

def get_github_user(username):
    api_url = f'https://api.github.com/users/{username}'
    response = requests.get(api_url)

    if response.status_code == 200:
        user_data = response.json()
        print(f"Username: {user_data['login']}")
        print(f"Name: {user_data['name']}")
        print(f"Public Repositories: {user_data['public_repos']}")
    else:
        print(f"Error: {response.status_code}")

# Beispielaufruf
get_github_user('UngemachM')
