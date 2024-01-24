import base64
import requests

def get_github_file_content(username, repository, branch, file_path):
    # GitHub API-Endpunkt für den Inhalt einer Datei
    api_url = f'https://api.github.com/repos/{username}/{repository}/contents/{file_path}?ref={branch}'

    # Sende die Anfrage an die GitHub API
    response = requests.get(api_url)

    # Überprüfe, ob die Anfrage erfolgreich war (Statuscode 200)
    if response.status_code == 200:
        # JSON-Daten aus der Antwort extrahieren
        file_data = response.json()

        # Base64-dekodiere den Dateiinhalt
        content = file_data['content']
        decoded_content = base64.b64decode(content).decode('utf-8')  # Python 3

        return decoded_content
    else:
        # Drucke einen Fehler, wenn die Anfrage nicht erfolgreich war
        print(f'Fehler bei der Anfrage: {response.status_code}')
        return None

# GitHub Benutzername, Repository und Dateipfad
github_username = 'UngemachM'
repository_name = 'ProgrammingMoritzUngemach'
branch_name = 'codespace-opulent-spoon-5ggrxwpvrv6ph7465'
file_path = 'notebooks/Dictionary.py'

# Rufe den Dateiinhalt von GitHub ab
file_content = get_github_file_content(github_username, repository_name, branch_name, file_path)

# Drucke den Dateiinhalt
print(file_content)
