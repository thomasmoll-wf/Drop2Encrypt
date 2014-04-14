#Gen Token / Key

import dropbox
import os
import sys
import webbrowser

app_key = '6gccue9fycfx31b'
app_secret = 'wrtegtt4cu3z05e'

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

access_token = connect(app_key,app_secret);

#Dropbox Token
TOKENS = 'dropbox_token.txt'
token_file = open(TOKENS,'w')
token_file.write("%s|%s" % (access_token.key,access_token.secret) )
token_file.close()
print("Token Written to file!")

#GPG Key
#Generate a key pair 
