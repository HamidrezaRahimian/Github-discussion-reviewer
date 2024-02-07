
import requests
from code_extraction_function import  extract_code_blocks
from spelling import  correct_spelling
from nomark_code_extraction_function import  filter_python_expressions


def universal_gql(username, repository, discussion_number, token, function):
    api_url = 'https://api.github.com/graphql'
    
    # GraphQL-Abfrage mit dreifachen doppelten Anführungszeichen
    graphql_query = """query GetDiscussion($owner: String!, $repo: String!, $discussionNumber: Int!) {
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
    }""".replace("\n", " ")  # Zeilenumbrüche durch Leerzeichen ersetzen, um Syntaxfehler zu vermeiden

    headers = {'Authorization': f'token {token}'}
    variables = {"owner": username, "repo": repository, "discussionNumber": discussion_number}
    json_payload = {"query": graphql_query, "variables": variables}
    
    response = requests.post(api_url, json=json_payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        discussion_data = data.get('data', {}).get('repository', {}).get('discussion', {})
        discussion_title = discussion_data.get('title', '')
        discussion_body = discussion_data.get('body', '')

        if function == "extract_code":
          code_blocks = extract_code_blocks(discussion_body)
        elif function == "spelling":
          code_blocks = correct_spelling(discussion_body)
        elif function == "nomark":
          code_blocks = filter_python_expressions(discussion_body)
        

        comments = discussion_data.get('comments', {}).get('nodes', [])
        for comment in comments:
            comment_body = comment.get('body', '')
            

            # Extrahiere Codeblöcke aus dem Kommentar und speichere sie in derselben Liste
            if function == "extract_code":
              code_blocks.extend(extract_code_blocks(comment_body))
            elif function == "nomark":
              code_blocks.extend(filter_python_expressions(comment_body))

        # Gib die Liste der Codeblöcke aus
        return code_blocks

    elif response.status_code == 404:
        print(f'Diskussion mit Nummer {discussion_number} wurde nicht gefunden.')
    else:
        print(f'Fehler bei der Anfrage: {response.status_code}')