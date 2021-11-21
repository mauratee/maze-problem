import sys


class ReferenceMazeRunner:

    def run(self, start, end, seen=None, path=None):
        """ Use recursive depth-first search to check if start and end nodes
            are connected and return the path that was traversed if connected. """

        if not seen:
            seen = set()

        if not path:
            path = []

        seen.add(start)

        if start is end:
            return path


        for direction in start.exits:
            exit_object = start.get_square(direction)
            if exit_object not in seen:
                call_next = self.run(exit_object, end, seen, path)
                if call_next:
                    return path
                # If not traversing further down, remove most recent direction from path
                else:
                    path.pop()


class MazeLoader:
    def __init__(self):
        self.master_list = {}
        
        try:
            with open(sys.argv[1], 'r') as f:
                cell_nums = int(f.readline())
                print(f"cell_nums = {cell_nums}")
                for _ in range(cell_nums):
                    curr_line = f.readline()
                    parts = curr_line.split(' ', 2)
                    name = parts[0]
                    if name not in self.master_list:
                        self.master_list[name] = MazeSquare(name)
                    square = self.master_list.get(name)
                    exits = parts[1].split(',')
                    for exit in exits:
                        direction, next_square = exit.split(':')
                        # Strip newline characters from input
                        next_square = next_square.strip('\n')
                        if next_square not in self.master_list:
                            self.master_list[next_square] = MazeSquare(next_square)
                        square.add_exit(self.master_list.get(next_square), direction)
                start, end = f.readline().split(' ')
                # Strip newline characters from input
                end = end.strip('\n')
                current = self.master_list.get(start)
                # Simplify call to ReferenceMazeRunner class
                runner = ReferenceMazeRunner()
                result = runner.run(self.master_list.get(start), self.master_list.get(end))
                for step in result:
                    current = current.get_square(step)
                    if current == None:
                        print('Invalid path returned')
                        break
                print('Returned ' + ('valid' if self.master_list.get(end).get_name() == current.get_name() else 'invalid') + ' path')
        except FileNotFoundError:
            print('Location of maze file was not found')
        except IOError:
            print('IO Exception reading from maze file')


class MazeSquare:
    def __init__(self, name):
        self.name = name
        self.exits = {}
        
    def add_exit(self, square, direction):                            
        self.exits[direction] = square
    
    def get_name(self):
        return self.name
    
    def get_exists(self):
        return self.exits.keys()
                    
    def get_square(self, direction):
        return self.exits.get(direction, None) 

    # Add repr method for more readable output of MazeSquare objects
    def __repr__(self):
        """Human-friendly representation of MazeSquare object"""
        return f"<MazeSquare: {self.name}>"                       

MazeLoader()

# call sample mazes in Command Line:
# PASSING:
# assert:
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/simple.maze
# expect: Returned valid path
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generated100.maze
# expect: Returned valid path
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generated1000.maze
# expect: Returned valid path
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLarge.maze
# expect: Returned valid path
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLong2.maze
# expect: Returned valid path
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLong.maze
# expect: Returned valid path
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedsparse.maze
# expect: Returned valid path


# HAS ERRORS:
# None!!
