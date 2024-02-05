from flask import Flask, render_template, request
from search_github_discussion_gql_code import search_github_discussion_gql_code
from nomark_search_github_discussion_gql import nomark_search_github_discussion_gql
from spelling_search_github_discussion_gql import spelling_search_github_discussion_gql

app = Flask(__name__)

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

        code_blocks_array = search_github_discussion_gql_code(github_username, repository_name, discussion_number, personal_token)

        # Call GitHub discussion function to get code blocks without markdown
        nomark_code_array = nomark_search_github_discussion_gql(github_username, repository_name, discussion_number, personal_token)

        corrected_text_array = spelling_search_github_discussion_gql(github_username, repository_name, discussion_number, personal_token)


        # Zeige das Ergebnis in der Webanwendung an
        return render_template('result.html', code_blocks=code_blocks_array, nomark_code=nomark_code_array, corrected_text=corrected_text_array)          #nomark_code=nomark_code_array
    # Zeige das Eingabeformular an
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
