# ECE 461 Project

Our project for ECE 461 (Software Engineering) is to help ACME Corporation's software architects by providing infrastructure services for implementing new Node.js-based services easily. We use npm (the package manager for Node.js) with certain requirements shown below. The main product of our project is a command-line interface that ACME service engineering teams can use to help them choose their modules. It should "not be super slow", according to the customer.

## Project Requirements

Executable file in the root directory of your project called "run" that includes
- “./run install”
    - Installs any dependencies in userland
    - Should exit 0 on success
- “./run build”
    - Completes any compilation needed
    - Should exit 0 on success
- "./run URL_FILE", where URL_FILE is the  location of a file consisting of an ASCII-encoded newline-delimited set of URLs.
    - This invocation should produce NDJSON output; Each row should include the fields:
        - “URL”
        - “NetScore”
        - “RampUp”
        - “Correctness”
        - “BusFactor”
        - “ResponsiveMaintainer”
        - “License”.
    - Each score should be in the range [0,1] where 0 indicates total failure and 1
indicates perfection. The specific operationalizations are up to you, but you must
provide rationales as part of your documentation.
    - The “NetScore” should be calculated as [0,1] as well, as a weighted sum. You
should choose the weights based on Sarah’s priorities, and explain your choice.
    - Should exit 0 on success

## Getting Started

ACME Corporation currently offers its web service product directly via a REST API. However, they want a licensed version of the web service that its customers can self deploy. This means it needs to be open-sourced so it can be easily adaptable to their needs (ACME uses GNU Lesser Public License v2.1 for all open-source software so it must be compatible). 

### Requirements for npm packackages

The packages chosen have the main goal of a “low ramp-up time” for the future engineers. Therefore they have to follow the below requirements
- the package is correct
- the maintainers will be responsive to fix any bugs that are blocking ACME’s teams
- the open-source module has enough maintainers to continue to apply critical fixes such as a security patch. [highest priority]

It should be noted that more requirements for the npm packages could be added at a later time, so the design should be able to accommodate adding new aspects.

### Installing

A step by step series of examples that tell you how to get a development
environment running

Download any software application that has a command-line interface

    i.e. terminal, VSCode, eclipse

Run the module on the command-line to determine the score of the module

    write command ehre

End with an example of getting some data out of the system or using it
for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Sample Tests

Explain what these tests test and why

    Give an example

### Style test

Checks if the best practices and the right coding style has been used.

    Give an example

## Deployment

Add additional notes to deploy this on a live system

## Built With

  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used
    for the Code of Conduct
  - [Creative Commons](https://creativecommons.org/) - Used to choose
    the license

## Authors

  - **Elizabeth McNaughton** - 
    [lizziesarah](https://github.com/lizziesarah)
  - **Aiden Goen** - 
    [Agoen](https://github.com/Agoen)
  - **Kaylee Smith** - 
    [kaylee-smith](https://github.com/kaylee-smith)
  - **Collin Sell** - 
    [collinsell](https://github.com/collinsell)

## License

Node.js is available under the MIT license. Node.js also includes external libraries that are available under a variety of licenses. See LICENSE for the full license text.

## Acknowledgments

  - Hat tip to anyone whose code is used
  - Inspiration
  - etc
