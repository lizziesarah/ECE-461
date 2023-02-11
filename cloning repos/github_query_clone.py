from github import Github
import git
import os
import sys
from dotenv import load_dotenv
from os.path import exists
load_dotenv()

g = Github(os.getenv('GITHUB_TOKEN'))

def clone_repo():
    n = 0
    with open(r"url_file.txt", "r") as url_file:
        urls = url_file.readlines()
    for url in urls:
        url = url.strip()
        n += 1
        new_dir_name = "cloned_repo{}".format(n)
        os.mkdir(new_dir_name)
        url_split = url.split('/')
        print(url_split)
        if url_split[2] == 'github.com':
            repo = git.Repo.clone_from(url, new_dir_name)
            readme_exists = exists("{}/README.md".format(new_dir_name))
        else:
            registry_name = url_split[4]
            query = registry_name + '+in:readme+in:description'
            repos = g.search_repositories(query, 'stars', 'desc')
            for repo in repos:
                split = repo.clone_url.split('/')
                print(repo.clone_url)
                if split[4] == registry_name:
                    print(repo.clone_url)
                    break
    
    sys.print('cloc', registry_name)
