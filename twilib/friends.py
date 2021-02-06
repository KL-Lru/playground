from base import TwiBase

class FriendsHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/friends'

    def getFriendsIds(self, user_id = None, screen_name = None, cursor = -1, stringify_ids = False, count = None):
        """
            特定のユーザのフォローのid 一覧を取得
            count未指定の場合最大5000人分返ってくる、激重になる
        """

        self.validateSetUser(user_id, screen_name)
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('ids.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getFriendsList(self, user_id = None, screen_name = None, 
                    cursor = -1, skip_status = False, include_user_entities = False, count = 20):
        """
            特定のユーザのフォローの一覧を取得
        """

        self.validateSetUser(user_id, screen_name)
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('ids.json')
        res = session.get(url, params = payloads)
        return res.json()