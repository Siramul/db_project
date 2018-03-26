from app.dao import message


class Chat:
    def __init__(self, u_id):
        #Row Description [c_id, c_name, c_manager, c_members,]
        C1 = [1, 'Ejecutivos del Jangueo', 1, [1,3,46,752]]
        C2 = [2, 'Plan Fiscal', 2, [2,3,46,752]]
        C3 = [3, 'UPRM gana la LAI', 3, [2,3,46,752]]
        C4 = [4, 'ICOM, los mejores!', 4, [2,3,4,752]]
        C5 = [5, 'Las mujeres al poder', 5, [2,3,46,752,5]]

        self.u_id = u_id
        self.data = [C1, C2, C3, C4, C5]

    # Handler and Route DONE
    def get_all_chats(self):
        return self.data

    # Handler and Route DONE
    def get_chat_managed(self):
        chats = []

        for r in self.data:
            if self.u_id == r[2]:
                chats.append(r)

        return chats

    #Handler and Route DONE
    def create_chat(self, name):
        new_chat = [len(self.data), name, self.u_id]
        self.data.append(new_chat)

        return self.data[-1] == new_chat

    # Handler and Route DONE
    def add_contact_to_chat(self, c_id, u_id):
        chat = None
        for r in self.data:
            if c_id == r[0] and self.u_id == r[2]:
                chat = r
                if u_id not in r[3]:
                    r[3].append(u_id)
                    return True

        return False

    #TODO: Handler and Route
    def remove_user_from_chat(self,c_id,u_id):
        for r in self.data:
            if self.u_id == r[2] and c_id == r[0] and u_id in r[3]:
                r[3].remove(u_id)
                return True
        return False

    # TODO: Handler and Route
    def remove_chat(self,c_id):
        message.remove_all_message_from_chat(self,c_id)
        for r in self.data:
            if self.u_id == r[2] and c_id == r[0]:
                self.data.remove(r)
                return True

        return False