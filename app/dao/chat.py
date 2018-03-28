from app.dao import contain
from app.dao import message


class ChatDAO:
    def __init__(self):
        #Row Description [c_id, c_name, c_manager]
        c1 = [1, 'Kill me', 1]
        c2 = [2, 'Plan Fiscal', 2]
        c3 = [3, 'UPRM gana la LAI', 3]
        c4 = [4, 'ICOM, los mejores!', 4]

        self.data = []
        self.data.append(c1)
        self.data.append(c2)
        self.data.append(c3)
        self.data.append(c4)

    # Handler and Route DONE
    def get_all_chats(self):
        return self.data

    def get_chat_by_chat_id(self, cid):
        for r in self.data:
            if cid == r[0]:
                return r
            print(r, cid)
            return None

    def get_chat_by_chat_manager(self, cmanager):
        for r in self.data:
            if cmanager == r[2]:
                return r
        return None

    def get_chat_by_chat_name(self, cname):
        for r in self.data:
            if cname == r[1]:
                return r
        return None
