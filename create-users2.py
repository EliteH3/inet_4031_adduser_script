#!/usr/bin/python3

# INET4031
# Miles Mattes
# Date Created 03/23/2026
# Date Last Modified 03/23/2026

# os is used to execute Linux system commands.
# re is used to detect comment lines starting with '#'.
# sys is used to read command-line arguments (input filename).
import os
import re
import sys


def main():
    # Ensure a filename was provided
    if len(sys.argv) != 2:
        print("Usage: ./create-users2.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]

    # Prompt user for dry-run mode
    mode = input("Run in dry-run mode? (Y/N): ").strip().upper()
    dry_run = (mode == "Y")

    # Open and read the input file
    with open(filename, 'r') as f:
        for line in f:
            original_line = line.strip()

            # Check for comment lines (starting with '#')
            match = re.match("^#", line)

            # Split line into fields
            fields = line.strip().split(':')

            # Handle skipped/comment lines
            if match:
                if dry_run:
                    print(f"SKIPPING: '{original_line}' is a comment line.")
                continue

            # Handle invalid field count
            if len(fields) != 5:
                if dry_run:
                    print(f"ERROR: '{original_line}' does not contain 5 fields.")
                continue

            # Extract user data
            username = fields[0]
            password = fields[1]
            gecos = "%s %s,,," % (fields[3], fields[2])

            # Split groups
            groups = fields[4].split(',')

            # Create user
            print(f"==> Creating account for {username}...")
            cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"

            if dry_run:
                print(cmd)
            else:
                os.system(cmd)

            # Set password
            print(f"==> Setting the password for {username}...")
            cmd = f"/bin/echo -ne '{password}\\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"

            if dry_run:
                print(cmd)
            else:
                os.system(cmd)

            # Assign groups
            for group in groups:
                # '-' means no group assignment
                if group != '-':
                    print(f"==> Assigning {username} to the {group} group...")
                    cmd = f"/usr/sbin/adduser {username} {group}"

                    if dry_run:
                        print(cmd)
                    else:
                        os.system(cmd)


if __name__ == '__main__':
    main()
