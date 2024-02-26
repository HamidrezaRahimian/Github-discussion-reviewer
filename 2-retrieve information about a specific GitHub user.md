This is our first [code ](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/Test.py)component. 
If we give the variable username an active account name, we can call up the corresponding information of the Github account.

```
 import requests

def get_github_user(username):
    api_url = f'https://api.github.com/users/{username}'
    response = requests.get(api_url) 
    if response.status_code == 200:
        user_data = response.json()
        print(f"Username: {user_data['login']}")
        print(f"Name: {user_data['name']}")
        print(f"Public Repositories: {user_data['public_repos']}")
    else:
        print(f"Error: {response.status_code}")
```

The code is a Python script that uses the requests library to interact with the GitHub API and retrieve information about a specific GitHub user. It starts by importing the requests library, which allows us to send HTTP requests and handle responses from the GitHub API.

The code defines a function called get_github_user that takes a username as input. This function is responsible for fetching and displaying information about a GitHub user. Inside the function, an API URL is constructed using the parameter username.
To retrieve the information, the code sends an HTTP GET request to the constructed API URL using the requests.get function. The response from the server is stored in the response variable.

The code then checks the status code of the response. If the status code is 200, it means the request was successful. In this case, the user's data is extracted from the response using response.json() and printed. The printed information includes the username, name, and the number of public repositories the user has.
If the status code is not 200, the code prints an error message displaying the status code of the response.


In summary, this Python script allows us to retrieve and display information about a GitHub user by making a request to the GitHub API. 
This gives us the basis for further functions that use the saved data as source fot the data we want to improve with our whole coding projekt