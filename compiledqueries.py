import requests
from datetime import date

# https://github.com/octocat/Hello-World

def readFile(urlfile):
    owners_and_names = {}
    file_pointer = open(urlfile, "r")

    for line in file_pointer.readlines():
        owner = ""
        name = ""
        # its a github file
        i=19
        if line[8] == 'g':
            while line[i] != '/':
                owner += line[i]
                i+=1
            name = line[i+1:]



        owners_and_names[owner] = name.strip('\n')
        return owners_and_names


def getBusFactorScore(username, token, owner, name, outfile):
    #username = "lizziesarah"
    #token = "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"
    header = {'Authorization': 'Bearer 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'}

    owner = '"' + f"{owner}" + '"'
    name = '"' + f"{name}" + '"'

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
    outfile_pointer = open(outfile, "a")
    outfile_pointer.write(f'\n\t'+'{'+f'\n\t\tBus Factor: {score}\n'+'\t}')
    outfile_pointer.close()
    return score

def getCorrectnessScore(username, token, owner, name, outfile) :
    #username = "lizziesarah"
    #token = "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"
    header = {'Authorization': 'Bearer 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'}

    owner = '"' + f"{owner}" + '"'
    name = '"' + f"{name}" + '"'

    query1 = "{\n" + f"\trepository(owner: {owner}, name: {name})" + " { \n\t\tstargazerCount }}"

    # req=requests.get(url='https://api.github.com/graphql', auth=(username,token)) headers=header
    req = requests.post(url='https://api.github.com/graphql', json={'query': query1}, auth=(username, token))
    result = req.json()

    number_of_stars = result['data']['repository']['stargazerCount']

    score = 0
    if number_of_stars > 5:
        score=1
        outfile_pointer = open(outfile, "a")
        outfile_pointer.write(f'\n\t'+'{'+f'\n\t\tCorrectness: {score}\n'+'\t}')
        outfile_pointer.close()
        return 1
    else:
        outfile_pointer = open(outfile, "a")
        outfile_pointer.write(f'\n\t'+'{'+f'\n\t\tCorrectness: {score}\n'+'\t}')
        outfile_pointer.close()
        return 0

def getResponsiveMaintainersScore(username, token, owner, name, outfile):
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
    if todaysDateDateTime.day < 10 and todaysDateDateTime.month >= 10:
        gts = '"' + str(lastyear) + "-" + str(todaysDateDateTime.month) + "-0" + str(
            todaysDateDateTime.day) + "T01:01:00Z" + '"'
    if todaysDateDateTime.day >= 10 and todaysDateDateTime.month < 10:
        gts = '"' + str(lastyear) + "-0" + str(todaysDateDateTime.month) + "-" + str(
            todaysDateDateTime.day) + "T01:01:00Z" + '"'
    if todaysDateDateTime.day >= 10 and todaysDateDateTime.month >= 10:
        gts = '"' + str(lastyear) + "-" + str(todaysDateDateTime.month) + "-" + str(
            todaysDateDateTime.day) + "T01:01:00Z" + '"'

    query1 = "{\n" + f"\trepository(owner: {owner}, name: {name})" + " { \n" + "\t ref(qualifiedName:" + f" {master})" + " { " + "\n\t\ttarget { \n\t\t ... on Commit {\n\t" + f"history(since:{gts})" + "{" + "\n\t\ttotalCount}}}}}\n\t\t}"

    req = requests.post(url='https://api.github.com/graphql', json={'query': query1}, auth=(username, token))
    result = req.json()

    numCommits = result['data']['repository']['ref']['target']['history']['totalCount']
    rm_score = 0
    if numCommits > 1:
        rm_score = 1
    outfile_pointer = open(outfile, "a")
    outfile_pointer.write(f'\n\t'+'{'+f'\n\t\tResponsive Maintainers: {rm_score}\n'+'\t}')
    outfile_pointer.close()
    #print(f"Responsive Maintainers: {rm_score}")
    return(rm_score)

def finalScore(bf, lc, cr, ru, rm, outfile):
    score = (bf*4+lc*4+cr*3+ru*2+rm*1) /14
    outfile_pointer = open(outfile, "a")
    outfile_pointer.write(f'\n\t'+'{'+f'\t\tTotal Score: {score}\n'+'\t}'+'\n]')
    outfile_pointer.close()
    return score


if __name__ == '__main__':
    owners_and_names = {}
    owners_and_names = readFile(urlfile='urlfile_actual.txt')
    for owner in owners_and_names:
        getCorrectnessScore(username='lizziesarah', token='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', owner=owner, name=owners_and_names[owner], outfile='outfile.txt')
        getResponsiveMaintainersScore(username='lizziesarah', token='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', owner=owner, name=owners_and_names[owner], outfile='outfile.txt')
        getBusFactorScore(username='lizziesarah', token='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', owner=owner, name=owners_and_names[owner], outfile='outfile.txt')



