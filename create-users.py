#!/usr/bin/python3

# INET4031
# Miles Mattes
# Created 03/23/2026
# Last modified 03/23/2026

# os is used to execute Linux shell commands from within the script.
# re is used to check whether a line starts with a comment character.
# sys is used to read lines from standard input redirected from the input file.
import os
import re
import sys

def main():
    for line in sys.stdin:


        # Check whether the current line begins with "#" so comment lines
        # in the input file can be skipped and not processed as user data.
        match = re.match("^#",line)

        # Remove trailing whitespace and split the input line on ":" because
        # each user record is expected to contain five colon-separated fields.
        fields = line.strip().split(':')

        # Skip lines that are comments or that do not contain exactly the
        # five required fields expected by this script.
        if match or len(fields) != 5:
            continue

        # Store the account information from the input line. These values are
        # used to build the new account and populate the GECOS/full-name field
        # stored with the user entry.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split the last field into a list of groups so the user can be added
        # to multiple groups when the input file contains comma-separated values.
        groups = fields[4].split(',')

        # Print a status message showing which user account is about to be created.
        print("==> Creating account for %s..." % (username))
        # Build the adduser command that creates the account with a disabled
        # password at first and sets the user's GECOS information.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # Uncomment print(cmd) for a dry run to verify the command before execution.
        # Uncomment os.system(cmd) to actually create the user account.

        #print(cmd)
        os.system(cmd)

        # Print a status message showing that the password step is starting.
        print("==> Setting the password for %s..." % (username))

        # Build the command that passes the password twice into passwd so the
        # account password can be set non-interactively.        
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # Uncomment print(cmd) for a dry run to verify the command before execution.
        # Uncomment os.system(cmd) to actually set the user's password.
        
        #print(cmd)
        os.system(cmd)

        for group in groups:
            # A "-" means no group should be assigned. If the field contains
            # a real group name, add the user to that group.

            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)

                # Uncomment print(cmd) for a dry run to verify the command.
                # Uncomment os.system(cmd) to actually add the user to the group.                
                #print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
