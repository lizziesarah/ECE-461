from github import Github
import git
import os
from dotenv import load_dotenv
load_dotenv()

g = Github(os.getenv('GITHUB_TOKEN'))

def query_github():
    n = 0
    with open(r"url_file.txt", "r") as url_file:
        urls = url_file.readlines()
    for url in urls:
        url = url.strip()
        n += 1
        new_dir_name = "cloned_repo{}".format(n)
        os.mkdir(new_dir_name)
        repo = git.Repo.clone_from(url, new_dir_name)

query_github()