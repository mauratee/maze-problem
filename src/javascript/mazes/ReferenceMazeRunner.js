// This ReferenceMazeRunner contains a run method that returns a hard-coded solution to simple.maze. 
// Modify or create your own version of ReferenceMazeRunner.js. 
// In your version, the run method should return a valid path when passed any solvable maze.

// You can test your implementation by changing line 1 of MazeLoader.js 
// to refer to your implementation of ReferenceMazeRunner.js and 
// then running "node src/javascript/mazes/MazeLoader.js {PATH_TO_MAZE_FILE}". 
// For example, you might run: "node src/javascript/mazes/MazeLoader.js src/samples/simple.maze" 
// to test your implementation with simple.maze.

class Runner {
    constructor() {
        this.name = 'Example Runner'
    }
    run(start, end) {
        return ["North", "East"];
    }
}

module.exports = Runner;