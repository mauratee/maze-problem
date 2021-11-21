import sys
# use Python's built-in queue structure
from collections import deque

# This ReferenceMazeRunner class contains a run method that returns a hard-coded solution to simple.maze. 
# Modify or create your own version of the ReferenceMazeRunner class. 
# In your version, the run method should return a valid path when passed any solvable maze.
# If you create your own version of ReferenceMazeRunner, make sure to replace the ReferenceMazeRunner call on line 40 with your own class

# To test your program run "python src/python/mazes/MazeLoader.py {PATH_TO_MAZE_FILE}" from the root of the mazes-takehome directory
# For example, you might run: "python src/python/mazes/MazeLoader.py src/samples/simple.maze"
# to test your implementation with simple.maze

# Mock submission that will return valid path for simple.maze
class ReferenceMazeRunner:
    # def __init__(self):
    #     # dictionary of all node names paired with the corresponding node object
    #     self.master_list = {}
        
        # try:
        #     with open(sys.argv[1], 'r') as f:
        #         cell_nums = int(f.readline())
        #         print(f"cell_nums = {cell_nums}")
        #         for _ in range(cell_nums):
        #             curr_line = f.readline()
        #             parts = curr_line.split(' ', 2)
        #             name = parts[0]
        #             if name not in self.master_list:
        #                 self.master_list[name] = MazeSquare(name)
        #             square = self.master_list.get(name)
        #             exits = parts[1].split(',')
        #             for exit in exits:
        #                 direction, next_square = exit.split(':')
        #                 if next_square not in self.master_list:
        #                     # print("!"* 10)
        #                     # print(f"next_square = {next_square}")
        #                     next_square = next_square.strip('\n')
        #                     # print("!"* 10)
        #                     # print(f"we stripped the newline?! next_square = {next_square}")
        #                     self.master_list[next_square] = MazeSquare(next_square)
        #                 square.add_exit(self.master_list.get(next_square), direction)
        #         start, end = f.readline().split(' ')
        #         end = end.strip('\n')
        #         # print(f"start = {start}")
        #         # print(f"end = {end}")

        #         # print(self.master_list)
        #         # print(self.master_list.keys())
        #         # print(len(self.master_list.keys()))

        # except FileNotFoundError:
        #     print('Location of maze file was not found')
        # except IOError:
        #     print('IO Exception reading from maze file')

    #############################################################
    # || Original try, except block with '\n' newline characters ||
    
        # try:
        #     with open(sys.argv[1], 'r') as f:
        #         cell_nums = int(f.readline())
        #         for _ in range(cell_nums):
        #             curr_line = f.readline()
        #             parts = curr_line.split(' ', 2)
        #             name = parts[0]
        #             # print(f"we're in ReferenceMazeRunner init function. name = {name}")
        #             # Strip trailing new line characters
        #             name.replace("\n", "")
        #             # name = name.strip("\n")
        #             if name not in self.master_list:
        #                 # print(f"name = {name}")
        #                 self.master_list[name] = MazeSquare(name)
        #             square = self.master_list.get(name)
        #             exits = parts[1].split(',')
        #             for exit in exits:
        #                 direction, next_square = exit.split(':')
        #                 if next_square not in self.master_list:
        #                     self.master_list[next_square] = MazeSquare(next_square)
        #                 square.add_exit(self.master_list.get(next_square), direction)
        #         start, end = f.readline().split(' ')
        #         # print(self.master_list)
        #         # print(self.master_list.keys())
        #         # print(len(self.master_list.keys()))

        # except FileNotFoundError:
        #     print('Location of maze file was not found')
        # except IOError:
        #     print('IO Exception reading from maze file')

    #############################################################


    # def run(self, start, end):
    #     """ Use breadth-first search to check if start and end nodes
    #         are connected and return path if connected. """
        
    #     # print(f"in run function. start = {start}")

    #     # Track room nodes to visit using Queue and seen room nodes
    #     # using Set.
    #     possible_rooms = deque()
    #     seen = set()
    #     # Add start node to Queue and Set
    #     possible_rooms.append(start)
    #     seen.add(start)
    #     # print(seen)
    #     # print(possible_rooms)
    #     path = []

    #     while possible_rooms:
    #         room = possible_rooms.popleft()
    #         print(room.name)
    #         if room is end:
    #             return path
    #         else:
    #             print("*"*20)
    #             print(f"room.exits = {room.exits}")
    #             print(f"room.exits.keys = {room.exits.keys()}")
    #             # print(f"room.exits,values = {room.exits.values()}")
    #             for exit in set(room.exits.values()) - seen:
    #                 # print("*"*20)
    #                 # print(f"exit = {type(exit)}")
    #                 possible_rooms.append(exit)
    #                 seen.add(exit)


    def run(self, start, end, seen=None, path=None):
        """ Use recursive depth-first search to check if start and end nodes
            are connected and return path if connected. """

        print(f"We're in ReferenceRunner.run, very beginning: start =  {start}")
        print(f"We're in ReferenceRunner.run, very beginning: start.exits =  {start.exits}")
        print(f"We're in ReferenceRunner.run, very beginning: end =  {end}")

        if not seen:
            seen = set()

        if not path:
            path = []

        if start is end:
            # path.append(start.exits)
            print(f"\nreturning path - {start.name} is {end.name}")
            print(path)
            return path
        
        seen.add(start)
        print(f"adding, {start.name}")
        print(f"{start.name}'s exits are {start.exits}")

        for direction in start.exits:
        # for exit in start.exits.values():
            print(direction)
            exit_object = start.get_square(direction)
            if exit_object not in seen:
                print(direction)
                path.append(direction)
                print(
                    f"calling method on {start.name}'s exit {exit_object.name}"
                )
                print(f"{exit_object.name}'s exits are {exit_object.exits}")
                if self.run(exit_object, end, seen, path):
                    # print(exit)
                    # path.append(exit)
                    print(f"\nreturning path from checking {exit_object.name}")
                    return path




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
                        print("!"* 10)
                        print(f"next_square = {next_square}")
                        next_square = next_square.strip('\n')
                        print("!"* 10)
                        print(f"we stripped the newline?! next_square = {next_square}")
                        if next_square not in self.master_list:
                            # print("!"* 10)
                            # print(f"next_square = {next_square}")
                            # next_square = next_square.strip('\n')
                            # print("!"* 10)
                            # print(f"we stripped the newline?! next_square = {next_square}")
                            self.master_list[next_square] = MazeSquare(next_square)
                        square.add_exit(self.master_list.get(next_square), direction)
                start, end = f.readline().split(' ')
                end = end.strip('\n')
                print(f"start = {start}")
                print(f"end = {end}")

                # print(f"We're in MazeLoader init function")
                print(self.master_list)
                print(self.master_list.keys())
                print(len(self.master_list.keys()))
                current = self.master_list.get(start)
                print(f"current = {current}")
                # Change the implemenation of ReferenceMazeRunner, or replace it with your class here
                ##############################################
                runner = ReferenceMazeRunner()
                # print(f"we're in MazeLoader, runner = {runner}")
                print(f"we're in MazeLoader, self.master_list.get(start) = {self.master_list.get(start)}")
                print(f"we're in MazeLoader, self.master_list.get(end) = {self.master_list.get(end)}")
                result = runner.run(self.master_list.get(start), self.master_list.get(end))
                print(f"we're in MazeLoader, result = {result}")
                for step in result:
                    print(f"we're in MazeLoader, step = {step}")
                    current = current.get_square(step)
                    print(f"we're in MazeLoader, current = {current}")
                    print(f"type of current = {type(current)}")
                    if current == None:
                        print('Invalid path returned')
                        break
                ################################################
                # runners = [ReferenceMazeRunner()]
                # print(f"we're in MazeLoader, runners = {runners}")
                # for runner in runners:
                #     print(f"start = {start}")
                #     print(f"type of start = {type(start)}")
                #     print(f"end = {end}")
                #     print(f"type of end = {type(end)}")
                #     print(f"we're in MazeLoader, self.master_list.get(start) = {self.master_list.get(start)}")
                #     print(f"we're in MazeLoader, self.master_list.get(end) = {self.master_list.get(end)}")
                #     # print(f"we're in MazeLoader, self.master_list.get('n1') = {self.master_list.get('n1')}")
                #     result = runner.run(self.master_list.get(start), self.master_list.get(end))
                #     print(f"we're in MazeLoader, result = {result}")
                #     for step in result:
                #         print(f"we're in MazeLoader, step = {step}")
                #         current = current.get_square(step)
                #         if current == None:
                #             print('Invalid path returned')
                #             break
                ####################################################
                # print(f"we're in MazeLoader, current = {current}")
                # print(f"type of current = {type(current)}")
                # print(f"we're in MazeLoader, end = {end}")
                # print(f"type of end = {type(end)}")
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

    def __repr__(self):
        """Human-friendly representation of MazeSquare object"""
        return f"<MazeSquare: {self.name}>"                       

MazeLoader()

# call sample mazes in Command Line:
# PASSING:
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/simple.maze

# HAS ERRORS:
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generated100.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generated1000.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLarge.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLong.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLong2.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedsparse.maze