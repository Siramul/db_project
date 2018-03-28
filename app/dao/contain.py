class ContainDAO:
    def __init__(self, u_id):
        # Row Description [chat_id , message_id ]
        c1 = [1, 4]
        c2 = [2, 5]
        c3 = [3, 3]
        c4 = [4, 2]
        c5 = [5, 1]
        c6 = [1, 6]
        c7 = [1, 7]
        c8 = [2, 8]

        self.u_id = u_id
        self.data = [c1, c2, c3, c4, c5, c6, c7, c8]

    # No handler or route needed. Only for chat implementation purposes.
    def remove_all_content_from_chat(self, c_id):
        for r in self.data:
            if r[0] == c_id:
                self.remove(r)
            return True
        return False

    def get_all_id_message_contained_in_chat(self,c_id):
        all_message_id = []
        for r in self.data:
            if r[0] == c_id:
                all_message_id.append(r[1])
        return all_message_id
