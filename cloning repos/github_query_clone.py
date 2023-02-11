import git
import os
from os.path import exists

def clone_repo():
    n = 0
    with open(r"git_urls.txt", "r") as url_file:
        urls = url_file.readlines()
    for url in urls:
        url = url.strip()
        n += 1
        new_dir_name = "cloned_repo{}".format(n)
        os.mkdir(new_dir_name)
        repo = git.Repo.clone_from(url, new_dir_name)
        readme_exists = exists("{}/README.md".format(new_dir_name))
        if readme_exists:
            rampup_time = 1
        else:
            rampup_time = 0
    
        os.system(cloc)
            
clone_repo()