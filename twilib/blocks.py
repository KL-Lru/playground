from base import TwiBase

class BlocksHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/blocks'

    def getBlocksIds(self, cursor = -1, stringify_ids = False):
        """
            ブロックしているユーザid 一覧
            count未指定の場合最大5000人分返ってくる、激重になる
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('ids.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getBlockslist(self, include_entities = False, cursor = -1, stringify_ids = False):
        """
            ブロックしているユーザ一覧
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('list.json')
        res = session.get(url, params = payloads)
        return res.json()

    def postBlocksCreate(self, user_id = False, screen_name = False, include_entities = False, skip_status = False):
        """
            指定ユーザをブロックする
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('create.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postBlocksDestroy(self, user_id = False, screen_name = False, include_entities = False, skip_status = False):
        """
            指定ユーザのブロックを解除する
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('destroy.json')
        res = session.post(url, params = payloads)
        return res.json()