import requests
from datetime import date

def getBusFactorScore(username, token, owner, name):
    username = "lizziesarah"
    token = "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"
    header = {'Authorization': 'Bearer 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'}

    owner = '"' + "octocat" + '"'
    name = '"' + "Hello-World" + '"'

    query1 = "{\n" + f"\trepository(owner: {owner}, name: {name})\n" + "\t{ mentionableUsers{\n\ttotalCount\n}\n}\n}"

    # req=requests.get(url='https://api.github.com/graphql', auth=(username,token)) headers=header
    req = requests.post(url='https://api.github.com/graphql', json={'query': query1}, auth=(username, token))
    result = req.json()

    numContributors = result['data']['repository']['mentionableUsers']['totalCount']
    if numContributors >= 5:
        score = 1
    else:
        score = numContributors / 5
    #print(f"Number of contributors: {numContributors}")
    #print(f"Bus Factor: {score}")
    return score

def getCorrectnessScore(username, token, owner, name) :
    #username = "lizziesarah"
    #token = "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"
    header = {'Authorization': 'Bearer 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'}

    #owner = '"' + "octocat" + '"'
    #name = '"' + "Hello-World" + '"'

    query1 = "{\n" + f"\trepository(owner: {owner}, name: {name})" + " { \n\t\tstargazerCount }}"

    # req=requests.get(url='https://api.github.com/graphql', auth=(username,token)) headers=header
    req = requests.post(url='https://api.github.com/graphql', json={'query': query1}, auth=(username, token))
    result = req.json()

    number_of_stars = result['data']['repository']['stargazerCount']
    print(f"Number of Stars: {number_of_stars}")
    if number_of_stars > 5:
        return 1
    else:
        return 0

def getResponsiveMaintainersScore(username, token, owner, name):
    #username = "lizziesarah"
    #token = "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"
    # header = {'Authorization': f'Bearer {token}'}

    owner = '"' + f"{owner}" + '"'
    name = '"' + f"{name}" + '"'
    master = '"' + "master" + '"'

    # create github timestamp of last year's date
    todaysDateDateTime = date.today()
    lastyear = todaysDateDateTime.year - 1
    # format time stamp accordingly as a string
    gts = ""
    if todaysDateDateTime.day < 10 and todaysDateDateTime.month < 10:
        gts = '"' + str(lastyear) + "-0" + str(todaysDateDateTime.month) + "-0" + str(
            todaysDateDateTime.day) + "T01:01:00Z" + '"'
    if todaysDateDateTime.day < 10 and todaysDateDateTime.month > 10:
        gts = '"' + str(lastyear) + "-" + str(todaysDateDateTime.month) + "-0" + str(
            todaysDateDateTime.day) + "T01:01:00Z" + '"'
    if todaysDateDateTime.day > 10 and todaysDateDateTime.month < 10:
        gts = '"' + str(lastyear) + "-0" + str(todaysDateDateTime.month) + "-" + str(
            todaysDateDateTime.day) + "T01:01:00Z" + '"'

    query1 = "{\n" + f"\trepository(owner: {owner}, name: {name})" + " { \n" + "\t ref(qualifiedName:" + f" {master})" + " { " + "\n\t\ttarget { \n\t\t ... on Commit {\n\t" + f"history(since:{gts})" + "{" + "\n\t\ttotalCount}}}}}\n\t\t}"

    req = requests.post(url='https://api.github.com/graphql', json={'query': query1}, auth=(username, token))
    result = req.json()
    numCommits = result['data']['repository']['ref']['target']['history']['totalCount']
    rm_score = 0
    if numCommits > 1:
        rm_score = 1
    # print(f"Number of commits since {todaysDateDateTime}: {numCommits}")
    #print(f"Responsive Maintainers: {rm_score}")
    return(rm_score)