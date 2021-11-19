package mazes;

import java.util.List;

public interface MazeRunner {
    /*
     * Takes a MazeSquare start and a MazeSquare end and returns a path between them
     * This is not required to be the shortest path, the emphasis should be on a reasonable time/space complexity of the function
     * The return value should be an ordered list of exits that describes a path between start and end
     */
    public List<String> run (MazeSquare start, MazeSquare end);
}
