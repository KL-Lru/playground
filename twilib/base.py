from requests_oauthlib import OAuth1Session, OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import os
import urllib.parse as parser
import webbrowser

class TwiBase(object):
    """
     TwiBase 
     諸々いい感じにする奴
    """
    def __init__(self):
        self.base_url = ''
        self.consumer_key = None
        self.consumer_secret = None
        self.access_token = None
        self.access_token_secret = None
        self.bearer_token = None

    #region utils -----
    def urlJoin(self, suffix):
        return os.path.join(self.base_url, suffix)

    def makePayloads(self, local_variables):
        payloads = {}
        for key, val in local_variables.items():
            if key == 'self' or val is None:
                continue
            payloads[key] = val
        return payloads
    #endregion

    #region validators -----
    def validateSetUser(self, user_id, screen_name):
        if user_id is None and screen_name is None:
            raise RuntimeError('Must be set "user_id" or "screen_name"')

    def validateSpecifiedList(self, list_id, slug, owner_screen_name, owner_id):
        if list_id is None and (slug is None or (owner_screen_name is None and owner_id is None)):
            raise RuntimeError('Must be set "list_id" or , "slug" and "owner_screen_name" or "owner_id"')
    #endregion

    #region sessions -----
    def oauth1AuthorizedSession(self):
        if self.consumer_key == None or\
           self.consumer_secret == None or\
           self.access_token == None or\
           self.access_token_secret == None:
            raise RuntimeError('Not Authorized!')
        return OAuth1Session(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
    
    def oauth1NotAuthorizedSession(self):
        if self.consumer_key == None or\
           self.consumer_secret == None:
            raise RuntimeError('Not Avaliable Consumer!')
        return OAuth1Session(self.consumer_key, self.consumer_secret)
    
    def oauth2AuthorizedSession(self):
        if self.consumer_key == None or\
           self.consumer_secret == None or\
           self.bearer_token == None:
            raise RuntimeError('Not Authorized!')
        client = BackendApplicationClient(client_id = self.consumer_key)
        return OAuth2Session(client = client, token = self.bearer_token)

    def oauth2NotAuthorizedSession(self):
        if self.consumer_key == None or\
           self.consumer_secret == None or\
           self.bearer_token == None:
            raise RuntimeError('Not Avaliable Consumer!')
        client = BackendApplicationClient(client_id = self.consumer_key)
        return OAuth2Session(client = client)
    #endregion
