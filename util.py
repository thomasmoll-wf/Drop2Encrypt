import dropbox
import os
import sys
import webbrowser
import json

def connect(key, secret):
    """
    Connect and authenticate with dropbox
    """

    access_type = "dropbox"
    session = dropbox.session.DropboxSession(key,
                                             secret,
                                             access_type)

    request_token = session.obtain_request_token()

    url = session.build_authorize_url(request_token)
    msg = "Opening %s. Please make sure this application is allowed before continuing."
    print msg % url
    webbrowser.open(url)
    raw_input("Press enter to continue")
    access_token = session.obtain_access_token(request_token)

    return access_token

def genkey(key, secret):

    access_token = connect(key, secret);
    tokens = 'secret.keys'
    token_file = open(tokens,'w')
    keys = {'client_key': access_token.key, 'client_secret': access_token.secret}
    token_file.write(json.dumps(keys))
    token_file.close()
    print("Token Written to file!\n\n")

def loadkeys()
    #TODO
    pass