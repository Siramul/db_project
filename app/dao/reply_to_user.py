class ReplyDAO:
    def __init__(self):
        r1 = [1, 1]
        r2 = [2, 2]
        r3 = [3, 3]
        r4 = [4, 4]

        self.data = []
        self.data.append(r1)
        self.data.append(r2)
        self.data.append(r3)
        self.data.append(r4)

    def get_all_replies(self):
        return self.data

    def get_replies_by_uid(self, uid):
        for r in self.data:
            if uid == r[0]:
                return r
        return None

    def get_replies_by_mid(self, mid):
        for r in self.data:
            if mid == r[1]:
                return r
        return None

    def get_replies_by_uid_and_mid(self, uid, mid):
        for r in self.data:
            if uid == r[0]:
                if mid == r[1]:
                    return r
                return None
        return None
