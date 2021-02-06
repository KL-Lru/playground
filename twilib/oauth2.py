from base import TwiBase

class OAuth2Hundler(TwiBase):
    """
    ログインなしでアプリ側で勝手に諸々やるタイプの認証(OAuth2)をするクラス
    """
    def __init__(self, consumer_key, consumer_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.base_url = 'https://api.twitter.com/oauth2/'

    def postToken(self):
        """
        Bearer Tokenの生成
        """
        url = self.urlJoin('token')
        session = self.oauth2NotAuthorizedSession()
        self.bearer_token = session.fetch_token(token_url = url, client_id = self.consumer_key, client_secret = self.consumer_secret)
        return self.bearer_token
