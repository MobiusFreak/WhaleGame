class BaseGame(object):
    def init(self, App):
        self.app = App

    def draw(self, screen):
        pass

    def update(self, t):
        return True

    def exit(self):
        pass

