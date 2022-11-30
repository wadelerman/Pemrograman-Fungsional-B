from BlogProjectBuilder import BlogProjectBuilder
from ECommerceProjectBuilder import ECommerceProjectBuilder

builder =  ECommerceProjectBuilder()
builder.setLanguage("PHP").setFramework("Laravel").setPattern("MVC")
builder.buildProject()
print(builder.getProject())

builder = BlogProjectBuilder()
builder.setLanguage("Python").setFramework("Django").setPattern("MVT")
builder.buildProject()
print(builder.getProject())