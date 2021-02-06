from base import TwiBase

class UsersHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/users'

    def getUsersLookUp(self, user_id = None, screen_name = None, include_entities = False, tweet_mode = None):
        """
            特定のユーザのユーザオブジェクトを取得
        """

        self.validateSetUser(user_id, screen_name)
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('lookup.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getUsersSearch(self, q, page = None, count = None, include_entities = False):
        """
            ユーザを検索する
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('search.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getUsersShow(self, user_id = None, screen_name = None, include_entities = False):
        """
            ユーザ詳細取得
        """

        self.validateSetUser(user_id, screen_name)
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('show.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getUsersProfileBanner(self, user_id = None, screen_name = None):
        """
            特定のユーザのバナー取得
        """

        self.validateSetUser(user_id, screen_name)
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('profile_banner.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getUsersReportSpam(self, user_id = None, screen_name = None, perform_block = True):
        """
            特定のユーザのスパム報告
        """

        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('report_spam.json')
        res = session.get(url, params = payloads)
        return res.json()
