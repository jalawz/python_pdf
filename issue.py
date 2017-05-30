class Issue(object):

    def __init__(self, title, points, desc):
        self.title = title
        self.points = points
        self.desc = desc


    @staticmethod
    def get_all_issues(*issues):
        list = []
        for issue in issues:
            list.append(issue)
        return list