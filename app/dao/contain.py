class ContainDAO:
    def __init__(self):
        # Row Description [chat_id , message_id ]
        c1 = [1, 4]
        c2 = [2, 5]
        c3 = [3, 3]
        c4 = [4, 2]
        c5 = [5, 1]
        c6 = [1, 6]
        c7 = [1, 7]
        c8 = [2, 8]

        self.data = []
        self.data.append(c1)
        self.data.append(c2)
        self.data.append(c3)
        self.data.append(c4)
        self.data.append(c5)
        self.data.append(c6)
        self.data.append(c7)
        self.data.append(c8)

    def get_all_messages_contained_in_chat_by_message_id(self, mid):
        for r in self.data:
            if mid == r[1]:
                return r
            return None

    def get_all_id_message_contained_in_chat(self,c_id):
        all_message_id = []
        for r in self.data:
            if r[0] == c_id:
                all_message_id.append(r[1])
        return all_message_id
