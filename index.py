import typer
import git
import pandas as pd
import os
import glob
import json
import requests
import subprocess
from github import Github


# Variable to store access token
token = ""

# Directory to store the repositories
directory = "Repo Files"
path = os.path.join('./', directory)

# Creating the folder of repos
if(not os.path.exists(path)):
    os.mkdir(path)
    
# Creating output file
output = open("output.csv", "w")
output.write("name,repo,version,version_satisfied,update_pr")

app = typer.Typer()


links = []
@app.command()
def hello(filename:str, dependency: str, update: bool = True):

    print(f"Opening {filename}")
    dataframe = pd.read_csv(filename)
    print('Successfully opened file')
    print(f"Checking dependency {dependency}\n")
    
    
    # Traversing through all cloned repo files in the folder
    for i in range(len(dataframe)):
        l = dataframe.iloc[i,1].split('/')          # Obtaining repo name via link
        if l[-1] not in os.listdir(path):   
            git.Git(path).clone(dataframe.iloc[i,1])
            
        links.append(dataframe.iloc[i,1])           # Storing repo names for future usage
    
    for file in os.listdir(path):
        loc = path + '\\' + file
        file1 = loc + '\\' + 'package.json'
        
        i, version = 0, "0"
        with open(file1, "r") as f:              
            my_dict = json.load(f)                          # Opening the package.json files in read mode for checking dependency versions
            depname, reqversion = dependency.split("@") 
            if(depname in my_dict['dependencies'].keys()):  # Case to monitor if the dependency is present or not in the project
                version = my_dict['dependencies'][depname]
                version = version[1:]
                
            text = file + ',' + links[i] + ',' + version + ',' + str(version >= reqversion).lower()
            output.write('\n'+text)                         # Writing to output file
            
            if(update and (version < reqversion)):          # Case of when dependency version requirement is not met
                print("\n" + file + " does not meet requirement.. Updating...")
                subprocess.call('npm i ' + depname + '@' + reqversion, cwd=loc, shell=True)     # Call npm to update dependency version
                print("\nUpdation carried out successfully... Now proceeding with creation and addition of new branch to repo...")
                
                
                branch_name = 'updated-branch'              # Updated branch name
                subprocess.call('git branch ' + branch_name, cwd=loc, shell=True)
                subprocess.call('git checkout ' + branch_name, cwd=loc, shell=True)
                subprocess.call('git add .', cwd=loc, shell=True)
                subprocess.call('git commit -m \"changed ' + depname + ' version\"' , cwd=loc, shell=True)
                subprocess.call('git push origin ' + branch_name, cwd = loc, shell=True)        # Pushing new branch onto repo
               
                
                print("\nNew branch successfully created and added. Proceeding to creation of Pull request..")
                client = Github(token)
                user = client.get_user()
                username = user.login
                repo = client.get_repo(username + "/" + file)                                   # Obtaining main repo
                stdout = subprocess.check_output('git branch -a'.split(), cwd=loc, shell=True )
                branches = stdout.decode()
                branch_list = [b.strip('* ') for b in branches.splitlines()]

                title = "Dependencies"
             
                if "main" in branch_list:
                    base = "main"
                else:
                    base = "master"
                body = "Changed " + depname + " Version to " + reqversion + " from " + version
                pr = repo.create_pull(title=title, body=body, head=branch_name, base=base)      # Create pull request
                
                pull_link = "," + "https://github.com/" + username + "/" + file + "/pull/" + str(pr.number)                          
                print("\nPull request created with link " + pull_link[1:])
                output.write(pull_link)                                                         # Add pull request link to output file


                print('Processing of file ' + file + ' successful!!\n')
                
            i += 1
            
    output.close()
        
    
if __name__ == "__main__":
    token = input('Please enter your personal access token: ')
    app()