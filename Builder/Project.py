class Project:
    def __init__(self):
        self.name = None
        self.description = None
        self.framework = None
        self.lang = None
        self.pattern = None
        
    def getProject(self):
        str = "New Project wants to be started! \n"
        str += f"Project Name: {self.name}\n"
        str += f"Project Description: {self.description}\n"
        str += f"Project Framework: {self.framework}\n"
        str += f"Project Programming Language: {self.lang}\n"
        str += f"Project Development Pattern: {self.pattern}\n"
        
        return str
    
    
        