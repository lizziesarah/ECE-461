#!/usr/bin/env tsc
import { readFileSync } from 'fs';
const fetch = require('node-fetch')

// This function grabs the license information for a github repository
async function FetchGithubRepo(owner:string, repo:string) {
    const end = 'https://api.github.com/repos/' + owner + '/' + repo + '/license';
    const res = await fetch(end);
    const data = await res.json();
    const url = "https://github.com/" + owner + "/" + repo
    try {
        console.log(data['license']['key'], url)
        console.log(CheckCompatibility(data['license']['key']))
    } catch(error) {
        console.log("N/A", url)
        console.log(CheckCompatibility('N/A'))
    }
}

// This function grabs the license information from an npmjs repository
async function FetchNPMRepo(name:string) {
    //
    const end = 'https://registry.npmjs.org/' + name + '';
    const res = await fetch(end);
    const data = await res.json();
    const url = "https://www.npmjs.com/package/" + name

    //
    try {
        console.log(data['license'], url);
        console.log(CheckCompatibility(data['license']))
    } catch(error) {
        console.log("N/A", url)
        console.log(CheckCompatibility('N/A'))
    }
}

// Regexes each link to grab either the user and name for github, or just name for npmjs
function RegexLink(textfile:string) {

    // read the second argument
    const txt = readFileSync(textfile, 'utf-8');

    // This code takes the string of ascii encoded url_file and converts it into an array of numbers, which then converts each of those characters to utf-8 format
    var ascii = txt.split(' ').map(Number);
    const converted_txt = String.fromCharCode(...ascii)

    // regex links to get github or npm, name, and repo
    const regex =  converted_txt.match(/(\/){1}([-.\w]+)+/ig);

    // if there are links within the text file
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

function CheckCompatibility(license:string) {

    // These lists of compatible and incompatible licenses are based on documents found online unger the GPL licensing information website, will be linked in readme
    // If its listed as other, that means that there is a license, but not explicitly stated within the repository and is under a readme.
    // We were not able to regex readme, so we are assuming that lgpl is compatible as it is more common than not, compatible with licenses
    let incompatible: Array<string> = ['afl-3.0', 'cc', 'cc0-1.0', 'cc-by-4.0', 'epl-1.0', 'epl-2.0', 'agpl-3.0', 'postgresql', 'N/A']
    let compatible: Array<string> = ['artistic-2.0', 'bsl-1.0', 'bsd-2-clause', 'bsd-3-clause', 'bsd-3-clause-clear', 'mit', 'MIT', 'wtfpl', 'gpl', 'gpl-2.0', 'gpl-3.0', 'lgpl', 'lgpl-2.1', 'lgpl-3.0', 'isc', 'lppl-1.3c', 'ms-pl', 'mpl-2.0', 'osl-3.0', 'ofl-1.1', 'unlicense', 'zlib', 'ncsa', 'other', 'apache-2.0']
    // These lists will now compared with the license passed in the parameter to see it is compatible
    let score = 0.0
    if (compatible.includes(license)) {
        score = 1.0
    }
    return score
}

RegexLink(process.argv.slice(2)[0])