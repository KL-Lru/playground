from base import TwiBase

class MutesHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/mutes/users'

    def getMutesIds(self, cursor = -1, stringify_ids = False):
        """
            ミュートしているユーザid 一覧
            count未指定の場合最大5000人分返ってくる、激重になる
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('ids.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getMuteslist(self, include_entities = False, cursor = -1, stringify_ids = False):
        """
            ミュートしているユーザ一覧
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('list.json')
        res = session.get(url, params = payloads)
        return res.json()

    def postMutesCreate(self, user_id = False, screen_name = False, include_entities = False, skip_status = False):
        """
            指定ユーザをミュートする
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('create.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postMutesDestroy(self, user_id = False, screen_name = False, include_entities = False, skip_status = False):
        """
            指定ユーザのミュートを解除する
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('destroy.json')
        res = session.post(url, params = payloads)
        return res.json()