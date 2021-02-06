from base import TwiBase

class SavedSearchHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/saved_search'

    def getSavedSearchList(self):
        """
            保存した検索条件一覧を取得
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('list.json')
        res = session.get(url, params = payloads)
        return res.json()
    
    def getSavedSearchShow(self, id):
        """
            保存した検索条件を取得
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin(f'list/{id}.json')
        res = session.get(url, params = payloads)
        return res.json()

    def postSavedSearchCreate(self, query):
        """
            検索条件の保存
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('create.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postSavedSearchDestroy(self, id):
        """
            保存された検索条件の削除
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin(f'destroy/{id}.json')
        res = session.post(url, params = payloads)
        return res.json()

