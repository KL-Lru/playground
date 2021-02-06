from base import TwiBase
import json
class CustomProfilesHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/custom_profiles'

    def getCustomProfiles(self, id):
        """
            カスタムプロファイルの詳細取得
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin(f'{id}.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getCustomProfilesList(self, count = None, cursor = None):
        """
            カスタムプロファイルの一覧取得
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('list.json')
        res = session.get(url, params = payloads)
        return res.json()

    def postCustomProfilesNew(self, name, avater_media_id):
        """
            カスタムプロファイルの詳細取得
            TODO fix
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin(f'{id}.json')
        res = session.post(url, params = payloads)
        return res.json()

    def deleteCustomProfiles(self, id):
        """
            カスタムプロファイルの削除
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('destroy.json')
        res = session.post(url, params = payloads)
        return res.json()
