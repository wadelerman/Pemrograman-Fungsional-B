from ProjectBuilder import ProjectBuilder
from Project import Project

class ECommerceProjectBuilder(ProjectBuilder):
    def __init__(self):
        self.project = Project()
    
    def setName(self):
        self.project.name = "E-Commerce Web App"
        return self
    
    def setDescription(self):
        self.project.description = "E-Commerce web app with cool features!"
        return self
    
    def setFramework(self, framework):
        self.project.framework = framework
        return self
    
    def setLanguage(self, language):
        self.project.lang = language
        return self
    
    def setPattern(self, pattern):
        self.project.pattern = pattern
        return self
    
    def buildProject(self):
        self.setName()
        self.setDescription()
        
    def getProject(self):
        return self.project.getProject()