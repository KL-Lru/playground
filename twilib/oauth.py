import urllib.parse as parser
import webbrowser
from base import TwiBase

class OAuthHundler(TwiBase):
    """
    普通にログインして利用する形式の認証(OAuth1)をするクラス
    """
    # 普通にログインして使用するタイプの認証
    base_url = 'https://api.twitter.com/oauth/'
    def __init__(self, consumer_key, consumer_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    def postRequestToken(self, 
            oauth_callback, 
            x_auth_access_type = None
        ):
        """
        Request Token(認証前のAccess Token)を取得する

        Parameters
        ----------
        oauth_callback: require
            callback先のurlを指定する
            app設定にてwhitelistに含まれているurlのみ受理される
        x_auth_access_type: optional
            ユーザが許可する権限をreadまたはwriteとして指定する
            app設定とは異なる権限が必要な場合のみ指定
        """
        payloads = self.makePayloads(locals())        
        session = self.oauth1NotAuthorizedSession()
        url = self.urlJoin('request_token')

        res = session.post(url, params = payloads)
        querys = {k:v[0] for k,v in parser.parse_qs(res.text).items()}
        return querys

    def getAuthenticate(self, 
            oauth_token, 
            force_login = None, 
            screen_name = None
        ):
        """
        認証ページを開く
        (既に認証済みの場合はスキップ)

        Parameters
        ----------
        oauth_token: require
            Requests Tokenを指定する
        force_login: optional
            手動でのログインを強制とする
        screen_name: optional
            ログインするユーザを指定する
        """
        payloads = self.makePayloads(locals())        
        url = self.urlJoin('authenticate')
        # this requests must be in browser
        webbrowser.open(f'{url}?{parser.urlencode(payloads)}', new=1)

    def getAuthotize(self, 
            oauth_token, 
            force_login = None, 
            screen_name = None
        ):
        """
        認証ページを開く
        (既に認証済みでも再度認証を求める)

        Parameters
        ----------
        oauth_token: require
            Requests Tokenを指定する
        force_login: optional
            手動でのログインを強制とする
        screen_name: optional
            ログインするユーザを指定する
        """
        payloads = self.makePayloads(locals())
        url = self.urlJoin('authorize')
        # this requests must be in browser
        webbrowser.open(f'{url}?{parser.urlencode(payloads)}', new=1)

    def postAccessToken(self, oauth_token, oauth_verifier):
        """
        Access Tokenを認証する

        Parameters
        ----------
        oauth_token: require
            Request Tokenを指定
        oauth_verifier: require
            認証ページでの認証後に得られる認証コード
            認証後callbackしたurlパラメータとしてくっついてる奴
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1NotAuthorizedSession()
        url = self.urlJoin('access_token')
        res = session.post(url, params = payloads)
        querys = {k:v[0] for k,v in parser.parse_qs(res.text).items()}
        self.access_token   = querys['oauth_token']
        self.access_secret  = querys['oauth_token_secret']
        return querys

    # --- utils
    def authentication(self, oauth_callback):
        """
        パッとテストしたい時用の何か

        Parameters
        ----------
        oauth_callback: require
            callback url
        """
        querys = self.postRequestToken(oauth_callback)
        print(querys)
        self.getAuthenticate(querys['oauth_token'])
        token = input('oauth_token?: ')         # replace this to read callback url
        verifier = input('oauth_verifier?: ')
        res = self.postAccessToken(token, verifier)
        return res
