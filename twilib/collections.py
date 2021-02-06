from base import TwiBase
import json
class CollectionsHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/collections'

    def getCollectionsEntries(self, id, count = None, max_position = None, min_position = None):
        """
            コレクション内のツイートを取得
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('entries.json')
        res = session.get(url, params = payloads)
        return res.json()
    
    def getCollectionsList(self, user_id = None, screen_name = None , tweet_id = None, count = None, cursor = None):
        """
            コレクションの一覧を取得
        """
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('list.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getCollectionsShow(self, id):
        """
            コレクション内の情報を取得
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('show.json')
        res = session.get(url, params = payloads)
        return res.json()

    def postCollectionsCreate(self, name, description = None, url = None, timeline_order = None):
        """
            コレクション作成
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('create.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postCollectionsUpdate(self, id, name = None, description = None, url = None):
        """
            コレクション更新
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('updata.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postCollectionsDestroy(self, id):
        """
            コレクション削除
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('destroy.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postCollectionsEntriesAdd(self, id, tweet_id, relative_to = None, above = True):
        """
            コレクションにツイートを追加
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('entries/add.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postCollectionsEntriesCurate(self, id, changes):
        """
            コレクションの一括操作
            送信はjsonをbodyに入れて送る
            changesにはop(操作)とtweet_idを入れたdictのlistを入力
            
        """
        body = self.makePayloads(locals())
        payloads = {}
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('entries/curate.json')
        res = session.post(url, params = payloads, body = json.dumps(body))
        return res.json()

    def postCollectionsEntriesMove(self, id, tweet_id, relative_to = None, above = True):
        """
            コレクションのツイートの位置を変更
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('entries/move.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postCollectionsEntriesRemove(self, id, tweet_id):
        """
            コレクションのツイートを削除
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('entries/remove.json')
        res = session.post(url, params = payloads)
        return res.json()
