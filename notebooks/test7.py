from flask import Flask, render_template, request
from universal_gql import universal_gql

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

        extract_code = "extract_code"
        code_blocks_array = universal_gql(github_username, repository_name, discussion_number, personal_token,extract_code)


        # Call GitHub discussion function to get code blocks without markdown
        nomark = "nomark"
        nomark_code_array = universal_gql(github_username, repository_name, discussion_number, personal_token, nomark)

        spelling = "spelling"
        corrected_text_array = universal_gql(github_username, repository_name, discussion_number, personal_token,spelling)


        # Zeige das Ergebnis in der Webanwendung an
        return render_template('result.html', code_blocks=code_blocks_array, nomark_code=nomark_code_array, corrected_text=corrected_text_array)          #nomark_code=nomark_code_array
    # Zeige das Eingabeformular an
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
