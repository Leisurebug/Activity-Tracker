class Activity:
    
    def __init__(self, name, category, time) -> None:
        self.none = None
        self.name = name
        self.category = category
        self.time = float(time) 
        
    def __repr__(self):
        return f"<Activity: {self.name}, {self.category}, {self.time:.2f}hrs>"