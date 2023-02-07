#!/usr/bin/env ts-node
import { readFileSync } from 'fs';

// This function grabs the license information for a github repository
async function FetchGithubRepo(owner:string, repo:string) {
    const end = 'https://api.github.com/repos/' + owner + '/' + repo + '/license';
    const res = await fetch(end);
    const data = await res.json();
    try {
        console.log(data['license']['key'])
    } catch(error) {
        console.log("N/A")
    }
}

// This function grabs the license information from an npmjs repository
async function FetchNPMRepo(name:string) {
    const end = 'https://registry.npmjs.org/' + name + '';
    const res = await fetch(end);
    const data = await res.json();
    try {
        console.log(data['license'])
    } catch(error) {
        console.log("N/A")
    }
}

// Regexes each link to grab either the user and name for github, or just name for npmjs
function RegexLink() {
    const txt = readFileSync('URL_FILE.txt', 'utf-8');
    const regex =  txt.match(/(\/){1}([-.\w]+)+/ig);

    if (regex) {
        for(let i = 1; i < regex.length; i = i + 3) {
            if(regex[i-1] == '/github.com') {
                const repo_user = regex[i].slice(1)
                const repo_name = regex[i+1].slice(1)
                FetchGithubRepo(repo_user, repo_name)
            } else {
                const repo_name = regex[i+1].slice(1)
                FetchNPMRepo(repo_name)
            }
        }
    }

}

async function CheckCompatibility() {

}

RegexLink()