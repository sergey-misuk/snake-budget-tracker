import sys
from EAPI import EAPI

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please provide a token"
        sys.exit(1)

    eAPI = EAPI()
    eAPI.authenticate(token=sys.argv[1])

    for i in eAPI.list_note_books():
        print i.name
