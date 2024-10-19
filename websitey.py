# Sherif Abdelhay 20-10-2024

import os
import shutil
import webbrowser

#1- Create project
def create_project():
    global project_name 
    project_name = input("Enter your new project name: ")
    os.system(f"mkdir -p ../{project_name}")
    os.system(f"mkdir -p ../{project_name}/src")
    os.system(f"mkdir -p ../{project_name}/app")
    os.system(f"mkdir -p ../{project_name}/css")

    os.system(f"touch ../{project_name}/src/index.html")
    os.system(f"touch ../{project_name}/app/app.js")
    os.system(f"touch ../{project_name}/css/style.css")

# 2- Create the index.html file
def create_index_file():
    fd=open(f"../{project_name}/src/index.html","w")

    fd.write(r""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>It's working ;)</h1>
    </body>
    </html>
    """
    )
    fd.close()

# Open index.html in the browser
def open_index_file():

    os.chdir(f"../{project_name}/src")
    filename = 'file:///'+os.getcwd()+'/' + 'index.html'
    webbrowser.open_new_tab(filename)

