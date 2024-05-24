#!/usr/bin/env python3

import argparse
import json
import os

def fetch_author(line: str) -> str:
    """Extract the name of the author from the corresponding line

    Args:
        line (str): 2nd line of the log entry for a commit

    Returns:
        str: Name of the author

    >>> fetch_author("Author: Linus Torvalds <torvalds@ppc970.osdl.org>")
    'Linus Torvalds'
    >>> fetch_author("Author: Guido van Rossum <guido@python.org>")
    'Guido van Rossum'
    >>> fetch_author("Author: Erich Gamma <egamma@microsoft.com>")
    'Erich Gamma'
    >>> fetch_author("Author: Miklos Szeredi <miklos@szeredi.hu>")
    'Miklos Szeredi'
    """
    return line[7:line.index("<")].strip()


def fetch_email(line: str) -> str:
    """Extract the email of the author from the corresponding line

    Args:
        line (str): 2nd line of the log entry for a commit

    Returns:
        str: Email of the author

    >>> fetch_email("Author: Linus Torvalds <torvalds@ppc970.osdl.org>")
    'torvalds@ppc970.osdl.org'
    >>> fetch_email("Author: Guido van Rossum <guido@python.org>")
    'guido@python.org'
    >>> fetch_email("Author: Erich Gamma <egamma@microsoft.com>")
    'egamma@microsoft.com'
    >>> fetch_email("Author: Miklos Szeredi <miklos@szeredi.hu>")
    'miklos@szeredi.hu'
    """
    return line[line.index("<")+1:line.index(">")].strip()


def fetch_date(line: str) -> str:
    """Extract the date of the commit from the corresponding line

    Args:
        line (str): 3rd line of the log entry for a commit

    Returns:
        str: Date of the commit

    >>> fetch_date("Date:   2005-04-16T15:20:36-07:00")
    '2005-04-16T15:20:36-07:00'
    >>> fetch_date("Date:   1990-08-09T14:25:15+00:00")
    '1990-08-09T14:25:15+00:00'
    """
    return line[5:].strip()


def fetch_changes(line: str) -> int:
    """Extract the number of files changed from the corresponding line

    Args:
        line (str): 4th line of the log entry for a commit

    Returns:
        int: Number of files changed

    >>> fetch_changes("2 files changed, 5 insertions(+), 2 deletions(-)")
    2
    >>> fetch_changes("1 file changed, 3 insertions(+)")
    1
    >>> fetch_changes("1 file changed, 1 insertion(+), 1 deletion(-)")
    1
    >>> fetch_changes("14 file changed, 36 insertions(+), 44 deletions(-)")
    14
    """
    return int(line[:line.index("file")])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse git log file and save it to json")
    parser.add_argument("log_file", help="Path to git log file")
    parser.add_argument("--author", "-a", action="store_true", help="Include author name in output")
    parser.add_argument("--email", "-e", action="store_true", help="Include author email in output")
    parser.add_argument("--date", "-d", action="store_true", help="Include commit date in output")
    parser.add_argument("--changes", "-c", action="store_true", help="Include number of changes in output")
    args = parser.parse_args()

    if not os.path.exists(args.log_file):
        print("The file does not exist")
        exit(1)

    if not args.author and not args.email and not args.date and not args.changes:
        args.author = args.email = args.date = args.changes = True
        
    commits = []
    commit = {}

    with open(args.log_file) as f:    
        for line in f:
            if line.startswith("Author") and args.author: commit["author"] = fetch_author(line)
            if line.startswith("Author") and args.email: commit["email"] = fetch_email(line)
            if line.startswith("Date") and args.date: commit["date"] = fetch_date(line)
            if "changed," in line:
                if args.changes: commit["changes"] = fetch_changes(line)
                commits.append(commit)
                commit = {}

    with open(os.path.splitext(args.log_file)[0]+".json", "w") as f:
        f.write(json.dumps(commits, indent=1))
