#!/usr/bin/env tsc
"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
exports.__esModule = true;
var fs_1 = require("fs");
var fetch = require('node-fetch');
//import fetch from 'node-fetch';
// This function grabs the license information for a github repository
function FetchGithubRepo(owner, repo) {
    return __awaiter(this, void 0, void 0, function () {
        var end, res, data, url;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    end = 'https://api.github.com/repos/' + owner + '/' + repo + '/license';
                    return [4 /*yield*/, fetch(end)];
                case 1:
                    res = _a.sent();
                    return [4 /*yield*/, res.json()];
                case 2:
                    data = _a.sent();
                    url = "https://github.com/" + owner + "/" + repo;
                    try {
                        console.log(data['license']['key'], url);
                        console.log(CheckCompatibility(data['license']['key']));
                    }
                    catch (error) {
                        console.log("N/A", url);
                        console.log(CheckCompatibility('N/A'));
                    }
                    return [2 /*return*/];
            }
        });
    });
}
// This function grabs the license information from an npmjs repository
function FetchNPMRepo(name) {
    return __awaiter(this, void 0, void 0, function () {
        var end, res, data, url;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    end = 'https://registry.npmjs.org/' + name + '';
                    return [4 /*yield*/, fetch(end)];
                case 1:
                    res = _a.sent();
                    return [4 /*yield*/, res.json()];
                case 2:
                    data = _a.sent();
                    url = "https://www.npmjs.com/package/" + name;
                    //
                    try {
                        console.log(data['license'], url);
                        console.log(CheckCompatibility(data['license']));
                    }
                    catch (error) {
                        console.log("N/A", url);
                        console.log(CheckCompatibility('N/A'));
                    }
                    return [2 /*return*/];
            }
        });
    });
}
// Regexes each link to grab either the user and name for github, or just name for npmjs
function RegexLink(textfile) {
    // read the second argument
    var txt = (0, fs_1.readFileSync)(textfile, 'ascii');
    var regex = txt.match(/(\/){1}([-.\w]+)+/ig);
    // if there are links within the text file
    if (regex) {
        for (var i = 1; i < regex.length; i = i + 3) {
            if (regex[i - 1] == '/github.com') {
                var repo_user = regex[i].slice(1);
                var repo_name = regex[i + 1].slice(1);
                FetchGithubRepo(repo_user, repo_name);
            }
            else {
                var repo_name = regex[i + 1].slice(1);
                FetchNPMRepo(repo_name);
            }
        }
    }
}
function CheckCompatibility(license) {
    // These lists of compatible and incompatible licenses are based on documents found online unger the GPL licensing information website, will be linked in readme
    // If its listed as other, that means that there is a license, but not explicitly stated within the repository and is under a readme.
    // We were not able to regex readme, so we are assuming that lgpl is compatible as it is more common than not, compatible with licenses
    var incompatible = ['afl-3.0', 'cc', 'cc0-1.0', 'cc-by-4.0', 'epl-1.0', 'epl-2.0', 'agpl-3.0', 'postgresql', 'N/A'];
    var compatible = ['artistic-2.0', 'bsl-1.0', 'bsd-2-clause', 'bsd-3-clause', 'bsd-3-clause-clear', 'mit', 'MIT', 'wtfpl', 'gpl', 'gpl-2.0', 'gpl-3.0', 'lgpl', 'lgpl-2.1', 'lgpl-3.0', 'isc', 'lppl-1.3c', 'ms-pl', 'mpl-2.0', 'osl-3.0', 'ofl-1.1', 'unlicense', 'zlib', 'ncsa', 'other', 'apache-2.0'];
    // These lists will now compared with the license passed in the parameter to see it is compatible
    var score = 0.0;
    if (compatible.includes(license)) {
        score = 1.0;
    }
    return score;
}
RegexLink(process.argv.slice(2)[0]);
