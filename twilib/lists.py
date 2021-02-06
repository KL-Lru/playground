from base import TwiBase

class ListHundler(TwiBase):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        super().__init__()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = 'https://api.twitter.com/1.1/lists'

    def getList(self, user_id = None, screen_name = None, reverse = None):
        """
            特定ユーザの管理しているリスト + 保存しているリスト
            最大100件まで(全てを探すならownershipsかsubscriptionを使う)
        """
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('list.json')
        res = session.get(url, params = payloads)
        return res.json()
        
    def getMembers(self, list_id = None, 
                        slug = None, owner_screen_name = None, owner_id = None,
                        count = 20, include_entities = False, skip_status = None):
        """
            特定のリストに含まれるメンバ一覧
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('members.json')
        res = session.get(url, params = payloads)
        return res.json()
    
    def getMembersShow(self, list_id = None, user_id = None, screen_name = None,
                        slug = None, owner_screen_name = None, owner_id = None,
                        include_entities = False, skip_status = None):
        """
            特定ユーザが特定のリストに含まれるかのチェック
        """

        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('members/show.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getMemberships(self, user_id = None, screen_name = None,
                        count = 20, cursor = None, filter_to_owned_lists = None):
        """
            特定ユーザの含まれるリスト一覧
        """

        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('membersships.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getOwnerships(self, user_id = None, screen_name = None,
                        count = 20, cursor = None):
        """
            特定ユーザの管理しているリスト一覧
        """
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('ownerships.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getShow(self, list_id = None, 
                        slug = None, owner_screen_name = None, owner_id = None):
        """
            特定のリストの情報
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('show.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getStatuses(self, list_id = None, 
                        slug = None, owner_screen_name = None, owner_id = None,
                        since_id = None, max_id = None, count = 20,
                        include_entities = False, include_rts = False):
        """
            特定のリストのTimeline
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('statuses.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getSubscribers(self, list_id = None, 
                        slug = None, owner_screen_name = None, owner_id = None,
                        cursor = None, count = 20,
                        include_entities = False, skip_status = None):
        """
            特定のリストを保存しているユーザ一覧
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('subscribers.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getSubscribersShow(self, list_id = None, user_id = None, screen_name = None,
                        slug = None, owner_screen_name = None, owner_id = None,
                        include_entities = False, skip_status = None):
        """
            特定ユーザが特定のリストを保存しているかのチェック
        """

        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('subscribers/show.json')
        res = session.get(url, params = payloads)
        return res.json()

    def getSubscriptions(self, user_id = None, screen_name = None,
                        count = 20, cursor = None):
        """
            特定ユーザの保存しているリスト一覧
        """
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('subscription.json')
        res = session.get(url, params = payloads)
        return res.json()

    def postCreate(self, name, mode = None,
                    description = None):
        """
            リスト作成
        """

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('create.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postDestroy(self, list_id = None, 
                        slug = None, owner_screen_name = None, owner_id = None):
        """
            リスト削除
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('destroy.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postMembersCreate(self, list_id = None, user_id = None, screen_name = None,
                        slug = None, owner_screen_name = None, owner_id = None):
        """
            リストにメンバー追加
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('members/create.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postMembersCreateAll(self, list_id = None, user_id = None, screen_name = None,
                        slug = None, owner_screen_name = None, owner_id = None):
        """
            リストにメンバー(多人数指定)
            指定はuser_id, screen_nameのどちらかにカンマ区切り
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('members/create_all.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postMembersDestroy(self, list_id = None, user_id = None, screen_name = None,
                        slug = None, owner_screen_name = None, owner_id = None):
        """
            リストからメンバー削除
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('members/destroy.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postMembersDestroyAll(self, list_id = None, user_id = None, screen_name = None,
                        slug = None, owner_screen_name = None, owner_id = None):
        """
            リストからメンバー削除(多人数指定)
            指定はuser_id, screen_nameのどちらかにカンマ区切り
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('members/destroy_all.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postSubscribersCreate(self, list_id = None, 
                        slug = None, owner_screen_name = None, owner_id = None):
        """
            リスト保存
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('subscribers/create.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postSubscribersDestroy(self, list_id = None, 
                        slug = None, owner_screen_name = None, owner_id = None):
        """
            リスト保存解除
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('subscribers/destroy.json')
        res = session.post(url, params = payloads)
        return res.json()

    def postUpdate(self, list_id = None, 
                        slug = None, owner_screen_name = None, owner_id = None,
                        name = None, mode = None, description = None):
        """
            リスト内容更新
        """
        self.validateSpecifiedList(list_id, slug, owner_screen_name, owner_id)
        self.validateSetUser(user_id, screen_name)

        payloads = self.makePayloads(locals())
        session = self.oauth1AuthorizedSession()
        url = self.urlJoin('update.json')
        res = session.post(url, params = payloads)
        return res.json()
