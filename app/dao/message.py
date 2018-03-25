class MessageDAO:
    def __init__(self):
        m1 = [1, 1, "Jean-Luc", "1987-03-25 03:47:30", 5, 0, "Make it so!", 0]
        m2 = [2, 2, "Benjamin", "1993-03-24 06:47:30", 6, 1, "It is the will of the Prophets!", 12]
        m3 = [3, 3, "James", "1966-02-25 03:50:00", 7, 2, "What does God need with a Starship?", 3]
        m4 = [1, 1, "Katherine", "1995-03-25 03:47:30", 3, 4, "We're Starfleet officers; weird is part of the job.", 5]

        self.data = []
        self.data.append(m1)
        self.data.append(m2)
        self.data.append(m3)
        self.data.append(m3)
        self.data.append(m4)

    def get_all_messages(self):
        return self.data

    def get_messages_by_id(self, mid):
        for r in self.data:
            if mid == r[0]:
                return r
            return None

    def get_messages_by_chat_id(self, cid):
        for r in self.data:
            if cid == r[1]:
                return r
            return None

    def get_messages_by_sender(self, sender):
        result = []
        for r in self.data:
            if sender == r[3]:
                result.append(r)
        return result

    def get_messages_by_timestamp(self, timestamp):
        result = []
        for r in self.data:
            if timestamp == r[4]:
                result.append(r)
        return result

    def get_messages_by_likes_dislikes(self, counter):
        for r in self.data:
            if counter == r[5]:
                return r
        return None

    def get_messages_by_reply_id(self, rid):
        for r in self.data:
            if rid == r[6]:
                return r
        return None

    def get_messages_by_content(self, text):
        for r in self.data:
            if text == r[7]:
                return r
        return None

    def get_messages_by_media_uri(self, uri):
        for r in self.data:
            if uri == r[8]:
                return r
        return None

