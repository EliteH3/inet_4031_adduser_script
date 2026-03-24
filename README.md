# INET4031 Add Users Script and User List

## Program Description

This program automates the process of creating Linux user accounts from a formatted input file. Instead of manually creating each account one at a time, the script reads user information line by line and builds the necessary Linux commands automatically. This allows a system administrator to quickly create multiple user accounts in a consistent and efficient way.

Normally, a system administrator would manually use commands such as `adduser` to create a user, `passwd` to set a password, and `adduser username group` to assign group memberships. This script uses those same commands, but automates them by generating and executing them based on input data. This reduces human error and speeds up repetitive administrative tasks.

## Program User Operation

This program reads input from a file. Each valid line in the file represents one user account. The script processes each line, skips invalid or commented lines, and then prepares commands to create the user, set their password, and assign them to groups.

Before running the script, ensure it has executable permissions and verify whether you are performing a dry run or a live execution.

### Input File Format

Each line in the input file must contain five fields separated by colons in the following format:

username:password:last_name:first_name:groups

Example:

user01:Password123:Last01:First01:group01,group02

Field descriptions:

- username: The login name for the new user
- password: The password to assign to the account
- last_name: Used for the user’s full name (GECOS field)
- first_name: Used for the user’s full name (GECOS field)
- groups: One or more group names separated by commas

To skip a line in the input file, begin the line with the `#` character. The script will treat it as a comment and ignore it.

If you do not want the user added to any groups, use a dash `-` in the groups field.

Example:

user07:Password123:Last07:First07:-

### Command Execution

First, make the script executable if needed:

chmod +x create-users.py

Then run the script using input redirection:

./create-users.py < create-users.input

The `<` symbol redirects the contents of the input file into the script. The Python code reads each line using standard input and processes it one at a time.

You can also run it explicitly with Python:

python3 create-users.py < create-users.input

Note: You may need to run the script with elevated privileges (sudo) since it creates users and modifies system settings.

### Dry Run

A dry run allows you to verify the commands before actually making changes to the system.

To perform a dry run:
- Keep the `os.system(cmd)` lines commented out
- Uncomment the `print(cmd)` lines

This will display the commands that would be executed without actually creating users or modifying the system.

Once you confirm the commands are correct:
- Comment out the `print(cmd)` lines again
- Uncomment the `os.system(cmd)` lines to perform the real execution
