import requests

username = "lizziesarah"
token = "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"
header = {'Authorization': 'Bearer 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'}

owner = '"' + "octocat" + '"'
name = '"' + "Hello-World" + '"'

query1 = "{\n" + f"\trepository(owner: {owner}, name: {name})\n" + "\t{ mentionableUsers{\n\ttotalCount\n}\n}\n}"

#req=requests.get(url='https://api.github.com/graphql', auth=(username,token)) headers=header
req = requests.post(url='https://api.github.com/graphql', json={'query': query1}, auth=(username,token))
result = req.json()

numContributors = result['data']['repository']['mentionableUsers']['totalCount']
score = 0
if numContributors >= 5:
    score = 1
else:
    score = numContributors / 5
print(f"Number of contributors: {numContributors}")
print(f"Bus Factor: {score}")

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
