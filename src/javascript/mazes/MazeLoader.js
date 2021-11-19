const Runner = require('./ReferenceMazeRunner.js'); // candidate's file here
const fs = require("fs");

class MazeLoader {
    constructor() {
        const files = process.argv;
        let mazeFile;
        try {
            mazeFile = fs.readFileSync(files[2]).toString();
        } catch(error) {
            console.log("Cannot read from file " + files[2] + "Error: " + error);
        }
        try {
            const mazeFileLines = mazeFile.split("\n");
            this.mazeSize = parseInt(mazeFileLines[0]);
            this.mazeSquares = {};
            const startEnd = mazeFileLines[mazeFileLines.length-1].split(" ");
            this.mazeStart = startEnd[0];
            this.mazeEnd = startEnd[1];

            for (let i=1; i <= this.mazeSize; i++) {
                let [name, exitInfo] = mazeFileLines[i].split(" ");
                let exitsList = exitInfo.split(",");
                if (!this.mazeSquares[name]) {
                    this.mazeSquares[name] = new MazeSquare(name);
                }
                for (let exit of exitsList) {
                    let [exitDirection, nextMazeSquareName] = exit.split(":");
                    let nextMazeSquare = this.mazeSquares[nextMazeSquareName];
                    if (!nextMazeSquare) {
                        this.mazeSquares[nextMazeSquareName] = new MazeSquare(nextMazeSquareName);
                    }
                    this.mazeSquares[name].addExit(exitDirection, this.mazeSquares[nextMazeSquareName])
                }
            }

            let runner = new Runner();
            let result = runner.run(this.mazeSquares[this.mazeStart], this.mazeSquares[this.mazeEnd]);
            let current = this.mazeSquares[this.mazeStart];
            for (let direction of result) {
                current = current.getNextMazeSquare(direction);
                if (!current) {
                    console.log("Invalid path returned");
                    break;
                }
            }

            console.log(runner.constructor.name + ": returned "
                            + ((this.mazeSquares[this.mazeEnd].getName() === current.getName()) ? "valid" : "invalid") +
                            " path");
        } catch(error) {
            console.log("An error occurred: " + error);
        }
    }
}

/* MazeSquare structure:
    {
        name: nameOfSquare,
        exits: {
            north: livingRoom (instance of Mazesquare),
            east: kitchen (instance of Mazesquare)
        }
    }
*/

class MazeSquare {
    constructor(name) {
        this.name = name,
        this.exits = {}
    }

    addExit(exitDirection, mazeSquare) {
        this.exits[exitDirection] = mazeSquare;
    }

    getName() {
        return this.name;
    }

    getExits() {
        return Object.keys(this.exits);
    }

    // gets the next mazeSquare or returns null if the direction leads to a dead end
    getNextMazeSquare(direction) {
        return this.exits[direction];
    }
}

new MazeLoader();