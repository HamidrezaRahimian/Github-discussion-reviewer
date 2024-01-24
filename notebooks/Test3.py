import requests

def get_github_discussion_with_token_gql(username, repository, discussion_number, token):
    # GitHub GraphQL API-Endpunkt
    api_url = 'https://api.github.com/graphql'

    # GraphQL-Abfrage für Diskussionsdetails
    graphql_query = """
    query GetDiscussion($owner: String!, $repo: String!, $discussionNumber: Int!) {
      repository(owner: $owner, name: $repo) {
        discussion(number: $discussionNumber) {
          title
          body
        }
      }
    }
    """

    # Setze den Authorization-Header mit dem persönlichen Token
    headers = {'Authorization': f'token {token}'}

    # GraphQL-Abfragevariablen
    variables = {
        "owner": username,
        "repo": repository,
        "discussionNumber": discussion_number
    }

    # JSON-Payload für die GraphQL-Abfrage
    json_payload = {
        "query": graphql_query,
        "variables": variables
    }

    # Sende die Anfrage an die GitHub GraphQL API mit dem Token
    response = requests.post(api_url, json=json_payload, headers=headers)

    # Überprüfe, ob die Anfrage erfolgreich war (Statuscode 200)
    if response.status_code == 200:
        # JSON-Daten aus der Antwort extrahieren
        data = response.json()

        # Extrahiere Informationen über die Diskussion
        discussion_data = data.get('data', {}).get('repository', {}).get('discussion', {})
        discussion_title = discussion_data.get('title', '')
        discussion_body = discussion_data.get('body', '')

        return discussion_title, discussion_body
    elif response.status_code == 404:
        print(f'Diskussion mit Nummer {discussion_number} wurde nicht gefunden.')
        return None, None
    else:
        # Drucke einen allgemeinen Fehler, wenn die Anfrage nicht erfolgreich war
        print(f'Fehler bei der Anfrage: {response.status_code}')
        return None, None

# GitHub Benutzername, Repository, Diskussionsnummer und persönliches Token
github_username = 'UngemachM'
repository_name = 'ProgrammingMoritzUngemach'
discussion_number = 10
personal_token = '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'

# Rufe die Informationen über eine Diskussion von GitHub ab (GraphQL)
discussion_title, discussion_body = get_github_discussion_with_token_gql(github_username, repository_name, discussion_number, personal_token)

# Überprüfe, ob die Diskussion erfolgreich abgerufen wurde
if discussion_title is not None and discussion_body is not None:
    # Drucke Informationen über die Diskussion
    print(f'Titel der Diskussion: {discussion_title}')
    print(f'Inhalt der Diskussion:\n{discussion_body}')
else:
    print('Diskussion konnte nicht abgerufen werden.')
