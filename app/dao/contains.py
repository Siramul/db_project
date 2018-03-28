
class Contains:
    def __init__(self, u_id):
        # Row Description [chat_id , message_id ]
        C1 = [1 , 4]
        C2 = [2 , 5]
        C3 = [3 , 3]
        C4 = [4 , 2]
        C5 = [5 , 1]
        C6 = [1, 6]
        C7 = [1, 7]
        C8 = [2, 8]

        self.u_id = u_id
        self.data = [C1, C2, C3, C4, C5, C6, C7, C8]

    #No handler or route needed. Only for chat implementation purposes.
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



