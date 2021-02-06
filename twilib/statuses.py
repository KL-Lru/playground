from base import TwiBase

class StatusesHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/statuses'

    def getStatusesHomeTimeline(self, count = 20, 
            since_id = None, max_id = None,
            trim_user = None, exclude_replies = None, include_entities = None):
        """
            ホームタイムラインのツイートを取得
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('home_timeline.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getStatusesMentionTimeline(self, count = 20, 
            since_id = None, max_id = None,
            trim_user = None, exclude_replies = None, include_entities = None):
        """
            メンションタイムラインのツイートを取得
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('mention_timeline.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getStatusesUserTimeline(self, count = 20, 
            user_id = None, screen_name = None,
            since_id = None, max_id = None,
            trim_user = None, exclude_replies = None, include_entities = None):
        """
            ユーザタイムラインのツイートを取得
        """
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('user_timeline.json')
        res = session.get(url, params = payloads)
        return res.json()
    
    def postStatusesUpdate(self, status, 
            in_reply_to_status_id = None, auto_populate_reply_metadata = False,
            exclude_reply_user_ids = None, attachment_url = None,
            media_ids = None, possibly_sensitive = False, lat = None, long = None,
            place_id = None, display_coordinates = None, trim_user = False, 
            enable_dmcommands = False, fail_dmcommands = True, card_uri = None):
        """
            ツイートする
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('update.json')
        res = session.post(url, params = payloads)
        return res.json()
    
    def postStatusesDestroy(self, id, trim_user = None):
        """
            ツイートを削除する
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin(f'destroy/{id}.json')
        res = session.post(url, params = payloads)
        return res.json()

    def getStatusesShow(self, id, trim_user = None,
                        include_my_retweet = None, 
                        include_entities = None,
                        include_ext_alt_text = None,
                        include_card_url = None):
        """
            ツイートの詳細を取得
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin(f'show.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getStatusesLookup(self, id, trim_user = None, map = None,
                        include_entities = None,
                        include_ext_alt_text = None,
                        include_card_url = None):
        """
            ツイートの詳細を取得(複数対応)
            idはカンマ区切り
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin(f'show.json')
        res = session.get(url, params = payloads)
        return res.json()

    def postStatusesRetweet(self, id, trim_user = None):
        """
            リツイートする
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin(f'retweet/{id}.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postStatusesUnretweet(self, id, trim_user = None):
        """
            リツイート解除する
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin(f'retweet/{id}.json')
        res = session.post(url, params = payloads)
        return res.json()

    def getStatusesRetweets(self, id, count = None, trim_user = None):
        """
            対象IDツイートのリツイートを取得
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin(f'retweets/{id}.json')
        res = session.get(url, params = payloads)
        return res.json()

    def postStatusesRetweetsOfMe(self, count = None, 
                                since_id = None, max_id = None,
                                trim_user = None,
                                include_entities = None,
                                include_user_entities = None):
        """
            自身のツイートのRTを取得
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('retweets_of_me.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getStatusesRetweets(self, id, count = None, 
                            cursor = None, stringify_ids, = None):
        """
            対象IDツイートをリツイートしたUser IDを取得
        """
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('retweeters/ids.json')
        res = session.get(url, params = payloads)
        return res.json()
