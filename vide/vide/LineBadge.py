class LineBadge(object):
    def __init__(self, mark, description="", fg_color=None, bg_color=None):
       self._mark = mark
       self._description = description
       self._fg_color = fg_color
       self._bg_color = bg_color

    def mark(self):
        return self._mark

    def bgColor(self):
        return self._bg_color

    def description(self):
        return self._description
