class MwController():
    
    
    def __init__(self, model, window):
        self.model = model
        self.window = window

        self.model.load_recipes()
