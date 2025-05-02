class SpyGetJpyOfTheDayViewImpl:
    def __init__(self):
        self.called = 0

    def generate_view(self, view_model):
        self.called += 1
