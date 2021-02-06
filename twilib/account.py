from base import TwiBase

class AccountHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/account'

    def getAccountSettings(self):
        """
            アカウント設定取得
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('settings.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getAccountVerifyCredentials(self, include_entities = False, skip_status = False, include_email = False):
        """
            アカウントが該当アプリを認証しているか取得
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('verify_credentials.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getAccountRemoveProfileBanner(self):
        """
            バナー削除
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('remove_profile_banner.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postAccountSettings(self, 
            sleep_time_enabled = None, start_sleep_time = None, end_sleep_time = None, 
            time_zone = None, trend_location_woeid = None, lang = None):
        """
            設定更新
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('settings.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postAccountUpdateProfile(self, 
            name = None, url = None, location = None, 
            description = None, include_entities = False, skip_status = None):
        """
            プロフィール更新
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('update_profile.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postAccountUpdateProfileBanner(self, 
            banner, 
            width = None, height = None, 
            offset_left = None, offset_top = None):
        """
            プロフィールバナー更新
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('update_profile_banner.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postAccountUpdateProfileImage(self, 
            image, 
            include_entities = False, skip_status = False):
        """
            プロフィール画像更新
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('update_profile_image.json')
        res = session.post(url, params = payloads)
        return res.json()
    
