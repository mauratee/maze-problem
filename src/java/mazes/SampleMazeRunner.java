package mazes;

import java.util.Arrays;
import java.util.List;

public class SampleMazeRunner implements MazeRunner {

    /*
     This is a sample implementation that solves simple.maze
     to demonstrate the expected output format
     */
    @Override
    public List<String> run(MazeSquare start, MazeSquare end) {
        return Arrays.asList("North", "East");
    }
}
