The next [code ](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/Test3.py) uses the requests library in Python to interact with the GitHub GraphQL API and retrieve information about a specific discussion in a GitHub repository. It defines a function that sends a GraphQL query with authentication headers, processes the response, and returns the discussion title and body. The code then calls the function with the required parameters and prints the retrieved information if successful.

We also addes a few funktions in seperate files to have a better overview in the code files in which all the functionality comes together:

- [one](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/spelling.py) for checking the spellings
- [one ](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/print_codeblocks_function.py)for a better  output of the codeblocks
- [one](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/search_github_discussion_gql_code.py) for  searching  for code blocks in a specific GitHub discussion, extracting them from the discussion body, comments, and storing 
  them in a list.
- [one ](https://github.com/HamidrezaRahimian/Github-discussion-reviewer/blob/main/notebooks/nomark_search_github_discussion_gql.py)to filter out Python code expressions from the text, and returns them as a list.