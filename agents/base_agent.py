class BaseAgent:
    def __init__(self, name):
        self.name = name

    def rewrite(self, input_text):
        raise NotImplementedError

    def feedback(self, feedback_text):
        pass
