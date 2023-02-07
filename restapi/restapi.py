# Access token: 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
import requests
import os
import re

license_score = 0.0

# Implements regex to grab the owner and repo name from a github link.
def Grab_Credentials(link):
    comp = re.findall(r"(\/){1}([\w\-]+)", link)
    owner = comp[1][1]
    repo = comp[2][1]
    return owner, repo

def Get_Repo_License(link):
    token = os.getenv('GITHUB_TOKEN', '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')
    owner, repo = Grab_Credentials(link)
    query_url = f"https://api.github.com/repos/{owner}/{repo}/license"
    
    params = {
        "state": "open",
    }
    headers = {'Authorization': f'token {token}'}
    
    r = requests.get(query_url, headers=headers, params=params)
    json_form = r.json()
    
    try:
        license = json_form['license']['key']
        print(license)
    except KeyError as ke:
        print('This repository does not have a license')
        
def main():
    link = input()
    if link[8] == 'w':
        pass
    else:
        Get_Repo_License(link)
    
    
if __name__ == "__main__":
    main()
    

 