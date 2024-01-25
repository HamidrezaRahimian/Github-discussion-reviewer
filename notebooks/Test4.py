import requests

def search_string_in_text(text, search_strings, label):
    """
    Durchsucht den Text nach den angegebenen Zeichenfolgen und gibt Funde aus.
    """
    for search_string in search_strings:
        if search_string.lower() in text.lower():
            print(f'Zeichenfolge "{search_string}" gefunden in {label}: {text}')

def search_github_discussion_gql(username, repository, discussion_number, search_strings, token):
    # GitHub GraphQL API-Endpunkt
    api_url = 'https://api.github.com/graphql'

    # GraphQL-Abfrage für Diskussionsdetails und Kommentare
    graphql_query = """
    query GetDiscussion($owner: String!, $repo: String!, $discussionNumber: Int!) {
      repository(owner: $owner, name: $repo) {
        discussion(number: $discussionNumber) {
          title
          body
          comments(first: 100) {
            nodes {
              body
            }
          }
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

        # Extrahiere Informationen über die Diskussion und Kommentare
        discussion_data = data.get('data', {}).get('repository', {}).get('discussion', {})
        discussion_title = discussion_data.get('title', '')
        discussion_body = discussion_data.get('body', '')

        # Durchsuche den Text der Diskussion nach den gewünschten Zeichenfolgen
        search_string_in_text(discussion_body, search_strings, "Diskussion")

        # Durchsuche den Text der Kommentare nach den gewünschten Zeichenfolgen
        comments = discussion_data.get('comments', {}).get('nodes', [])
        for comment in comments:
            comment_body = comment.get('body', '')
            search_string_in_text(comment_body, search_strings, "Kommentar")

    elif response.status_code == 404:
        print(f'Diskussion mit Nummer {discussion_number} wurde nicht gefunden.')
    else:
        # Drucke einen Fehler, wenn die Anfrage nicht erfolgreich war
        print(f'Fehler bei der Anfrage: {response.status_code}')

# GitHub Benutzername, Repository, Diskussionsnummer und persönliches Token
github_username = 'UngemachM'
repository_name = 'ProgrammingMoritzUngemach'
discussion_number = 10
personal_token = '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'

# Suchzeichenfolgen, nach denen gesucht werden soll
search_strings = ["123"]

# Durchsuche die Diskussion nach den gewünschten Zeichenfolgen
search_github_discussion_gql(github_username, repository_name, discussion_number, search_strings, personal_token)
