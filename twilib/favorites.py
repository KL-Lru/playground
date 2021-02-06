from base import TwiBase

class FavoritesHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/favorites'

    def getFavoritesList(self, count = 20, 
            user_id = None, screen_name = None,
            since_id = None, max_id = None,
            include_entities = None):
        """
            対象ユーザのFav一覧を取得
        """

        self.validateSetUser(user_id, screen_name)
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('list.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getFavoritesCreate(self, id, 
            include_entities = None):
        """
            Favる
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('create.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getFavoritesDestroy(self, id, 
            include_entities = None):
        """
            Fav取り消し
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('destroy.json')
        res = session.get(url, params = payloads)
        return res.json()