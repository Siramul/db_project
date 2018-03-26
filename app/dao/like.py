
class LikeDAO:
    def __init__(self):
        C1 = [1,10,'true','1,10']
        C2 = [1,3,'false','1,3']
        C3 = [1,4,'true','1,4']
        C4 = [2,1,'false','2,1']



        self.data = []
        self.data.append(C1)
        self.data.append(C2)
        self.data.append(C3)
        self.data.append(C4)



    def get_all_likes(self):
            return self.data
