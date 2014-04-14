# Include the Dropbox SDK libraries
from dropbox import client, rest, session
 
# Get your app key and secret from the Dropbox developer website
APP_KEY = '6gccue9fycfx31b'
APP_SECRET = 'wrtegtt4cu3z05e'
 
# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'dropbox'
 
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
 
# We will use the OAuth token we generated already. The set_token API 
# accepts the oauth_token and oauth_token_secret as inputs.
sess.set_token("a117lsxqf4v0tpx7", "cui6kwmyp60xwkp")
 
# Create an instance of the dropbox client for the session. This is
# all we need to perform other actions
client = client.DropboxClient(sess)
 
# Let's upload a file!
f = open('gl.html')
response = client.put_file('/gl.html', f)
print "uploaded:", response