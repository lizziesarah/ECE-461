import requests



def getCorrectnessScore(token, owner, name) :
    #username = "lizziesarah"
    #token = "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"
    header = {'Authorization': 'Bearer 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'}

    #owner = '"' + "octocat" + '"'
    #name = '"' + "Hello-World" + '"'

    query1 = "{\n" + f"\trepository(owner: {owner}, name: {name})" + " { \n\t\tstargazerCount }}"

    # req=requests.get(url='https://api.github.com/graphql', auth=(username,token)) headers=header
    req = requests.post(url='https://api.github.com/graphql', json={'query': query1}, headers=header)
    result = req.json()

    number_of_stars = result['data']['repository']['stargazerCount']
    print(f"Number of Stars: {number_of_stars}")
    if number_of_stars > 5:
        return 1
    else:
        return 0

if __name__ == '__main__':
    score = getCorrectnessScore('lizziesarah', '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', owner='datacite', name='lupo')

