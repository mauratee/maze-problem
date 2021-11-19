package mazes;


import java.util.List;

public interface MazeSquare {
    // Returns the name of this square, which will be unique
    public String getName();
    // Returns all inputs that getExits() will not return null for
    public List<String> getExits();
    // Returns the MazeSquare in the indicated direction from this square, or null if there is no exit that way
    public MazeSquare get(String direction);
}
