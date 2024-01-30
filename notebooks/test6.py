from flask import Flask, render_template, request
import requests
import re
from string_extraction_function import extract_text_between_strings
from text_search_function import search_string_in_text
from code_extraction_function import  extract_code_blocks
from print_codeblocks_function import print_code_blocks
from nomark_code_extraction_function import filter_python_expressions

app = Flask(__name__)


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
# Definiere die Route für die Webanwendung
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Benutzername, Repository, Diskussionsnummer und persönliches Token aus dem Webformular abrufen
        github_username = request.form['username']
        repository_name = request.form['repository']
        discussion_number = int(request.form['discussion_number'])
        personal_token = request.form['personal_token']

        # Suchzeichenfolgen, nach denen gesucht werden soll
        search_strings = request.form.get('search_strings', '').split(',')

        # Zeichenfolgen, zwischen denen der Text extrahiert werden soll
        start_string = request.form['start_string']
        end_string = request.form['end_string']

        # Rufe die GitHub-Diskussionsfunktion auf
        code_blocks_array = search_github_discussion_gql(github_username, repository_name, discussion_number, start_string, end_string, search_strings, personal_token)

        code_blocks = [] 
        # Zeige das Ergebnis in der Webanwendung an
        return render_template('result.html', code_blocks=code_blocks_array)

    # Zeige das Eingabeformular an
    return render_template('index3.html')

if __name__ == '__main__':
    app.run(debug=True)
