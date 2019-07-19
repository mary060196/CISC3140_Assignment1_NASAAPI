# NASA EPIC API Assignment

This is the 1st assignment in the Brooklyn College Summer 2019 CISC 3140 class.

## Notes:
  - It is imperative to keep all the files and directories in this project in *the same* folder, so that the templates and the static files will be applied when the application launches.
  - The files in this assignment were created, compiled, and run on a Windows PC. It is hoped they run on other platforms as well!
  - The python file was added the lines below, so that (1) creating a flask alias and writing ```flask run``` will not be needed anymore (2) the localhost webpage will open automatically, and (3) the debugger will be available for this application running process. Hence, it is sufficient to type only ```python apiass.py``` to (1))compile the file (2) alias and run Flask (3) have the localhost automatically opened in the web browser.
   ```python
   if __name__ == "__main__":
    webbrowser.open_new("http://localhost:5000/EPIC_API")
    app.run('localhost', 5000, True, use_reloader=False)
   ```
  - The optional variable ```use_reloader``` in the ```run``` function above was assigned with ```False``` so that the browser does not open two pages simultaneously.
  - The python file includes exception-catching code that checks if a valid API Key was entered. If not, the user is re-directed to the intro page, which displays a message: 'The API Key you entered is either wrong or the request rate for that key has surpassed. Please enter another API Key.' Feel free to test this option!

**Thank you for Reading!**
Miriam Briskman
