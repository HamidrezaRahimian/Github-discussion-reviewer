
import requests
from nomark_code_extraction_function import  filter_python_expressions

def nomark_search_github_discussion_gql(username, repository, discussion_number, token):
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

        # Extrahiere Codeblöcke aus dem Diskussionsbeitrag und speichere sie in einer Liste
        code_blocks = filter_python_expressions(sample_text)
        

        comments = discussion_data.get('comments', {}).get('nodes', [])
        for comment in comments:
            comment_body = comment.get('body', '')
            

            # Extrahiere Codeblöcke aus dem Kommentar und speichere sie in derselben Liste
            code_blocks.extend(filter_python_expressions(comment_body))

        # Gib die Liste der Codeblöcke aus
        return code_blocks,

    elif response.status_code == 404:
        print(f'Diskussion mit Nummer {discussion_number} wurde nicht gefunden.')
    else:
        print(f'Fehler bei der Anfrage: {response.status_code}')

sample_text = """
The purpos of this blog post is just to test out projekt capability of extracting code from posts.

```
testtesttesttesttesttest
test
test
test
test
```

import requests
import re
from string_extraction_function import extract_text_between_strings
from text_search_function import search_string_in_text
from code_extraction_function import  extract_code_blocks
from print_codeblocks_function import print_code_blocks

# Zeichne die Ränder des Quadrats
for i in range(seitenlänge):
    for j in range(seitenlänge):
        if i == 0 or i == seitenlänge - 1 or j == 0 or j == seitenlänge - 1:
            print(zeichen, end=' ')
        else:
            if i==1:
                print (" ", end=' ')
            if i==2:
# Zeichne die Ränder des Quadrats
for i in range(seitenlänge):
    for j in range(seitenlänge):
        if i == 0 or i == seitenlänge - 1 or j == 0 or j == seitenlänge - 1:
            print(zeichen, end=' ')
        else:
            if i==1:
                print (" ", end=' ')
            if i==2:
            





```
123124131
testtesttesttesttesttest
test
test
test
test
```
"""       