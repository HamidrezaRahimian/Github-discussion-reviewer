##  FACHKOMPETENZ (40 Punkte)

**Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)**

Haben die folgenden Punkte der prozedutalen Programmierung verwendet: 
* [Funktionen](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/Test4.py)  um es übersichtlicher zu machen 
* Stringverarbeitung, da die Daten die verarbeiten werden Text sind. > Bei der Spelling kontrolle wird zum Beispiel im String gesucht und Fehler ersetzt 
* verschiedene Datentypen und Variablen wie:

`max_hinweis_länge=12`

`aktuelles_format = None`

`eindeutige_codehinweise = []`

`corrected_text = spell(text)`

`data = response.json()`

* Wir haben eigentlich in jeder Datei [if](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/test7.py), [else](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/nomark_search_github_discussion_gql.py) , [elif](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/search_github_discussion_gql_code.py) Kontrilstrukturen verwendet um die logische Struktur umzusetzen. Auch Schleifen haben wir verwenden: [for](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/nomark_code_extraction_function.py), [for2](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/text_search_function.py)  
* verschiedene Operatoren, meistens bei  Abfragen mit if/else  und Zuweisungen

`if request.method == 'POST':`

`__name__ == '__main__':`

`if start_index != -1 and end_index != -1:`

`github_username = request.form['username']`

`repository_name = request.form['repository']`

* Auch E/A-Operatoren haben wir, die auf der Website eingegeben werden müssen, um zum GitHub-repository zu kommen und die entsprechende Diskussion auszuwerten.  Anschließend werden die Auswertung ausgegeben.

________
**Sie können die Syntax und Semantik von Python (10)**
[go to the link to see ](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/Stable/stable/nomark_code_extraction_function.py)
>Die herrausforderung hierbei war , code zu erkennen , und mit dem rest der zeile auszugeben.

Probleme dabei waren nicht immer alle codewörter in dem text auszugeben, sondern immer nur bis zum zeilenende.

mithilfe eine rliste werden dabei alle codehinweise darauf überprüft ob sie sich schon in de rliste befinden und so nicht nochmal hinzugefügt werden 
Um die formatierung gleich zu halten wird der jeweile codehinweis nach länge eingeordnet und wird auf 12 zeichen aufgefüllt, sodass am ende alle gleichlang sind und das format gut aussieht


* Syntax z.B: Einrückung, Kommentare, die einzelnen Anweisungen pro Zeile, Zuweisung von Variablen
* Semantik z.B.: Datentypen wie Liste, Kontrollstrukturen, Schleifen, Funktionen, Bibliotheken   
* Beispiel 
________
**Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)**

* Wir haben unser Projekt selbstständig entworfen und die verschiedenen Bestandteile gecoded. Am Ende und beim einfügen von jeder weiteren Funktion haben wir das Programm getestet. Erst wenn es funktioniert hat haben wir weitere Funktionen hinzugefügt. > verschiedene Test.py dateien zeigen unserern 
* Fortschritt wobei [test7.py](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/test7.py) die aktuellste Version ist.
* Nachfolgend ein Bild von den verschiedenen Commits, wo man sieht das jeder mitgearbeitet hat und ein Bild von einem Discord call, wo wir uns über unser Projekt und Probleme etc. ausgetauscht haben.

![commit2](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/91d17b99-4e45-4de7-9421-246a62a2a8a8)

<img width="947" alt="commits 2" src="https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/143603503/c4c8b68f-aa25-4634-88a8-363a0a968c4a">



<img width="955" alt="Screenshot 2024-02-11 173803" src="https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/143603503/1ca80a1a-47d0-4260-84cf-e7e66d4f9952">


<img width="960" alt="Screenshot 2024-02-11 173943" src="https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/143603503/ffb9ede1-0427-4f88-9bee-885588630ac9">


________

 **Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)**

* verscheiden Datenstrukturen haben wir verwendet
* Datenstrukturen sind zum Beispiel Liste, Tupel, Dictionary, Array, Set
* Wir sind auf den nachfolgenden Code besonders stolz, da das die Basis ist mit der wir zugriff auf Github via API bekommen und die Daten von da entsprechend abspeichern.  Darunter noch weitere Beispiele für datenstrukturen

![array](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/220a3398-789d-45cd-80b8-895cb5d4823c)


`content = file_data['content']`

`variables = {"owner": username,"repo": repository,"discussionNumber": discussion_number }`

`discussion_data = data.get('data', {}).get('repository', {}).get('discussion', {})`

`discussion_title = discussion_data.get('title', '')`

`discussion_body = discussion_data.get('body', '')`




________

##  METHODENKOMPETENZ (10 Punkte)
**Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)**

* Wir haben die beiden Entwicklungsumgebungen vsCode und Jupiter Notebook(GitHub) verwendet, um unser Programm zu verwirklichen
* Da beide miteinander agieren können, haben wir in vsCode den code geschrieben und getestet und dann hochgeladen in GitHub, um so auch unabhängig voneinander gleichzeitig an dem Projekt zu arbeiten.
* Wir haben auch die Git API verwendet.
* Nachfolgend 2 Bilder von GitHub und von unserem Repository in vsCode geklont. 


![githubuse](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/d9e0f7af-55cf-4d0e-82f0-84fab50e4ee5)
![Vscode](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/6d94ea91-bc1a-41d6-9d34-c44a3f3b1a7e)

<img width="701" alt="copilot" src="https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/143603503/807eb0d1-541d-40a2-97d1-b0fa1839a3c8">


________


## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

 **Die Studierenden können ihre Software erläutern und begründen. (5)**


* Hamidreza hat uns seine Spelling-Funktion erklärt. wie läuft die Funktion und Libraries die er benutzt und welche änderungen nötig waren damit programm schneller läuft.
* Da Moritz den ersten Commit zum Programm gemacht hat, hat er uns erklärt wie man Zugriff auf die API bekommt, damit wir alle an dem Projekt arbeiten können.
* Saskia hat Hamidreza und Moritz beigebracht wie wir Copilot installieren und effizient benutzen können .

![alex](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/179e8511-a2a7-4bf8-97a5-d6a1f55fc017)
![moritz](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/3d0933f7-01ab-4bfe-a7f7-ca7f373c4b02)
![saskia](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/3ee83fee-da3b-434f-b4ac-39f67332143f)

________

 **Sie können existierenden Code analysieren und beurteilen. (5)**

![review](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/8950bff1-4071-417b-bcb6-cd4c9da3f1a5)
![review2](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/d64c7ffb-ded1-4054-b4a9-7a533662f34c)


________
 **Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)**

* Wir haben gelernt wie man [zugriff](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/Test.py) auf die GitHub Repository bekommt mittels API. das sogar auf 2 unterschiedliche Arten, da die 2, für unseren Zweck besser geeignet ist
* Zum Umgang mit der API haben wir die  KI befragt
* Wir haben gelernt wie man Python und HTML/CSS zusammenbringt, um die Website zu starten
* Wir haben verschiedene Bibliotheken passend zu unserem Code eingebunden
* Wir haben vsCode und Jupiter Notebook verwendet. Beides sind Entwicklungsumgebungen (Integrated Development Environments, IDEs). Beide können miteinander aggieren.
* wir haben das Projekt mit anderen Gruppen mitgeteilt und durch ein paar meetings kleine Feedback und Reviews besonders in bezug of Design und usersurface bekommen.
* 
![image](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/143603503/9c737fdd-e7f7-4d49-a7c2-a2b9bb0ea173)
![preview](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/143603503/d257a86b-45ff-4254-a46a-9a50e1520381)
![peer2](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/143603503/ddf0afac-385a-4b49-9bcc-482cb4571002)
![review2](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/d8f82957-e900-4c4a-b2d2-fac274a42619)

![review](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/assets/152854589/1403b9d8-7514-4210-b6b6-0f76a38e63c8)



________
## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

 **Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)**

* Unsere [Problemstellung](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/README.md) hatte mit den GitHUb-Discussions zu tun, denn oftmals hatte man verschiedene Rechtschreibfehler drinnen oder Formatfehler bei der einbindung für code > Dafür haben wir eine Website gebaut, die uns den auf Rechtschreibung korrigierten Text ausgibt und uns code/möglichen code zeigt, damit wir schauen können, ob dass wirklich code ist oder nicht.
* Wir hatten zum Beispiel ein Problem bei der Spelling-Funktion durch das das laden der Website mit den Ausgaben fast 1 Minute gedauert hat. Nach der peer Review ist aufgefallen, das Spelling jedes Wort einzeln durchgeht und deswegen so lange braucht. > Abändern des Codes hat das Problem gelöst.
* Wir hatten auch Probleme mit vsCode, da die Commits bei anfangs  Saskia zwar durchgegangen sind aber nicht in GitHub angezeigt worden. Auch hatten wir beim Commiten Fehler, da zwei Personen an der gleichen Datei gearbeitet haben und deshalb keiner die neueste Version hatte und commiten konnte.
* Wir sind stolz einmal auf den [Zugriff](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/Test.py) auf GitHub, da das unsere Basis ist und wir das unbedingt gebraucht haben. Desweiteren sind wir auch stolz auf die Code Erkennung und die mögliche [Code](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/nomark_code_extraction_function.py) erkennung da beides häufige Fehler sind und wir diese Funktion unbedingt umsetzen wollten.

________

##  Martikel Nr.

 - 1478661
 - 8855870
 - 1299169
 

