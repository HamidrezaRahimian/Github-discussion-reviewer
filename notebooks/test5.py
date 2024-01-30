import requests
import re
from string_extraction_function import extract_text_between_strings
from text_search_function import search_string_in_text
from code_extraction_function import  extract_code_blocks
from print_codeblocks_function import print_code_blocks
from nomark_code_extraction_function import filter_python_expressions

def search_github_discussion_gql(username, repository, discussion_number, start_string, end_string, search_strings, token):
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
        
        # Extrahiere den Text zwischen start_string und end_string
        extracted_text = extract_text_between_strings(discussion_body, start_string, end_string)
        if extracted_text:
            print(f'Text zwischen "{start_string}" und "{end_string}": {extracted_text}')

        # Durchsuche den Text der Diskussion nach den gewünschten Zeichenfolgen
        search_string_in_text(discussion_body, search_strings, "Diskussion")

        # Extrahiere Codeblöcke aus dem Diskussionsbeitrag und speichere sie in einer Liste
        code_blocks = extract_code_blocks(discussion_body)
        

        comments = discussion_data.get('comments', {}).get('nodes', [])
        for comment in comments:
            comment_body = comment.get('body', '')
            # Extrahiere den Text zwischen start_string und end_string für jeden Kommentar
            extracted_comment_text = extract_text_between_strings(comment_body, start_string, end_string)
            if extracted_comment_text:
                print(f'Text zwischen "{start_string}" und "{end_string}" in Kommentar: {extracted_comment_text}')
            
            search_string_in_text(comment_body, search_strings, "Kommentar")

            # Extrahiere Codeblöcke aus dem Kommentar und speichere sie in derselben Liste
            code_blocks.extend(extract_code_blocks(comment_body))

        filter_python_expressions(discussion_body)

        # Gib die Liste der Codeblöcke aus
        return code_blocks

    elif response.status_code == 404:
        print(f'Diskussion mit Nummer {discussion_number} wurde nicht gefunden.')
    else:
        print(f'Fehler bei der Anfrage: {response.status_code}')

# GitHub Benutzername, Repository, Diskussionsnummer und persönliches Token
github_username = 'UngemachM'
repository_name = 'ProgrammingMoritzUngemach'
discussion_number = 11
personal_token = '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'

# Suchzeichenfolgen, nach denen gesucht werden soll
search_strings = ['Pythorn', 'GirlHub']

# Zeichenfolgen, zwischen denen der Text extrahiert werden soll
start_string = 'Start:'
end_string = 'End:'

# Durchsuche die Diskussion nach den gewünschten Zeichenfolgen, extrahiere Text und Codeblöcke
code_blocks_array = search_github_discussion_gql(github_username, repository_name, discussion_number, start_string, end_string, search_strings, personal_token)

# Gib das Array der Codeblöcke aus
print_code_blocks(code_blocks_array)

