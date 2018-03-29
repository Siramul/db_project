
class LikeDAO:
    def __init__(self):
        c1 = [1, 10, 'true', '1, 10']
        c2 = [1, 3, 'false', '1, 3']
        c3 = [1, 4, 'true', '1, 4']
        c4 = [2, 1, 'false', '2, 1']

        self.data = []
        self.data.append(c1)
        self.data.append(c2)
        self.data.append(c3)
        self.data.append(c4)

    def get_all_likes_dislikes(self):
            return self.data

    def get_likes_by_user_id(self, uid):
        for r in self.data:
            if uid == r[0]:
                return r
            return None

    def get_likes_by_message_id(self, mid):
        for r in self.data:
            if mid == r[0]:
                return r
            return None

    def get_like_dislike_by_pk(self, pk):
        for r in self.data:
            if pk == r[3]:
                return r
            return None

