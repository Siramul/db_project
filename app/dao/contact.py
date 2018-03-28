class ContactDAO:
    def __init__(self):
        C1 = [1,2,'1,2']
        C2 = [1,3,'1,3']
        C3 = [1,4,'1,4']
        C4 = [2,1,'2,1']
        C5 = [2,3,'2,3']
        C6 = [2,4,'2,4']
        C7 = [3,1,'3,1']
        C8 = [3,2,'3,2']
        C9 = [3,4,'3,4']
        C10= [4,1,'4,1']


        self.data = []
        self.data.append(C1)
        self.data.append(C2)
        self.data.append(C3)
        self.data.append(C4)
        self.data.append(C5)
        self.data.append(C6)
        self.data.append(C7)
        self.data.append(C8)
        self.data.append(C9)
        self.data.append(C10)


    def get_all_contacts(self):
            return self.data