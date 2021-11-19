package mazes;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class MazeLoader {

    public static void main(String[] args) {

        List<MazeRunner> runners = new LinkedList<>(); // The list of implementations to test
        runners.add(new SampleMazeRunner());

        File f = new File(args[0]); // Get the maze file from the first command line argument
        if (!f.exists() || !f.canRead()) { // Make sure it's real and we can read from it
            System.err.println("Cannot read from file " + args[0]);
        }
        try {
            // This will be the list of all of the rooms in the maze
            Map<String, MazeSquareInternal> masterList = new HashMap<>();
            BufferedReader br = new BufferedReader(new FileReader(f)); // Set up to read from the file
            int cells = Integer.parseInt(br.readLine()); // The count of rooms in the maze
            for (int i = 0; i < cells; i++) { // For each of the cell lines
                String line = br.readLine();
                String[] parts = line.split(" ", 2); // Split by spaces, to separate the identifier from the exits
                String identifier = parts[0];
                if (!masterList.containsKey(identifier)) { // If we haven't seen this room yet, add it to the master list
                    masterList.put(identifier, new MazeSquareInternal(identifier));
                }
                MazeSquareInternal cell = masterList.get(identifier); // Get the room we are reading from the master list
                String[] exits = parts[1].split(","); // parse out the exits for this room
                for (String exit : exits) { // For each of the exits
                    String[] dirid = exit.split(":"); // Split the exit pair into the direction and the room it leads to
                    if (!masterList.containsKey(dirid[1])) { // Add the destination room to the master list if it doesn't already exist
                        masterList.put(dirid[1], new MazeSquareInternal(dirid[1]));
                    }
                    cell.addExit(masterList.get(dirid[1]), dirid[0]); // Add the link to the room we are currently reading
                }

            }
            String[] startEnd = br.readLine().split(" "); // Split the final line into the start and end rooms
            for (MazeRunner runner : runners) { // For each of the implementations we are testing
                // Run the implementation and get the list of steps it takes
                List<String> result = runner.run(masterList.get(startEnd[0]), masterList.get(startEnd[1]));
                MazeSquare current = masterList.get(startEnd[0]); // Get the starting room
                for (String step : result) { // retrace the path that it gave
                    System.out.println(current.getName() + ", going " + step);
                    current = current.get(step);
                    if (current == null) {
                        System.err.println("Invalid path returned");
                        break;
                    }
                }
                // Check to see if we ended up in the right place or not
                System.out.println(runner.getClass().getSimpleName() + ": returned "
                        + (masterList.get(startEnd[1]).equals(current) ? "valid" : "invalid") +
                        " path");
            }


        } catch (ArrayIndexOutOfBoundsException e) { // Some part of the parsing didn't go properly
            System.err.println("Format Error: Missing expected part of cell definition");
        } catch (NumberFormatException e) { // The first line wasn't a number
            System.err.println("Format error: First line should be the number of cells in the maze");
        } catch (IOException e) { // Some other read error
            System.err.println("IO Exception reading from maze file");
        }

    }

    // This is the implementation of the MazeSquare that provides an additional method to add an exit
    // We need it to build the maze, in contrast to the MazeRunners that only need to be able to read from
    // the MazeSquare
    private static class MazeSquareInternal implements MazeSquare {

        private final Map<String, MazeSquare> exits = new HashMap<>();
        private final String name;

        public MazeSquareInternal(String name) {
            this.name = name;
        }

        public void addExit(MazeSquare other, String exitName) {
            exits.put(exitName, other);
        }

        @Override
        public String getName() {
            return name;
        }

        @Override
        public List<String> getExits() {
            return new ArrayList<>(exits.keySet());
        }

        @Override
        public MazeSquare get(String direction) {
            return exits.get(direction);
        }
    }
}
