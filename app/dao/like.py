
class LikeDAO:
    def __init__(self):
        c1 = [1, 10, 'true', '1, 10']
        c2 = [1, 3, 'false', '1, 3']
        c3 = [1, 4, 'true', '1, 4']
        c4 = [2, 1, 'false', '2,1']

        self.data = []
        self.data.append(c1)
        self.data.append(c2)
        self.data.append(c3)
        self.data.append(c4)

    def get_all_likes(self):
            return self.data
