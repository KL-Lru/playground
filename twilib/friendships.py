from base import TwiBase

class FriendshipsHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/friendsships'

    def getFriendshipsIncoming(self, 
            cursor = -1, stringify_ids = False):
        """
            フォローリクエストを送ってきているユーザid一覧を取得
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('incoming.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getFriendshipsOutgoing(self, 
            cursor = -1, stringify_ids = False):
        """
            フォローリクエストを送っているユーザid一覧を取得
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('outgoing.json')
        res = session.get(url, params = payloads)
        return res.json()


    def getFriendshipsLookUp(self, user_id = None, screen_name = None):
        """
            対象ユーザとの関係性を取得
            複数指定可能
        """

        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('loopup.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getFriendshipsShow(self, 
            source_id = None, source_name = None,
            target_id = None, target_name = None):
        """
            対象二人のユーザの関係性を取得
        """

        self.validateSetUser(source_id, source_name)
        self.validateSetUser(target_id, target_name)
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('show.json')
        res = session.get(url, params = payloads)
        return res.json()


    def getFriendshipsNoRetweetsIds(self, stringify_ids = False):
        """
            RT非表示設定をしているユーザid一覧を取得
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('no_retweet/ids.json')
        res = session.get(url, params = payloads)
        return res.json()

    def postFriendshipsCreate(self, user_id = None, screen_name = None, follow = None):
        """
            フォローする
            followは通知を行うか否かのフラグ
        """

        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('create.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postFriendshipsCreate(self, user_id = None, screen_name = None):
        """
            フォロー解除
        """

        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('destroy.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postFriendshipsUpdate(self, user_id = None, screen_name = None, device = None, retweets = None):
        """
            通知とRT表示の設定更新
        """

        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('update.json')
        res = session.post(url, params = payloads)
        return res.json()

