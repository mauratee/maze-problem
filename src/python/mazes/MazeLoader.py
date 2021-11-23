import sys
from collections import deque
import unittest
from pathlib import Path


class ReferenceMazeRunner:

    def run(self, start, end):
        """ Use breadth-first search to check if start and end nodes
            are connected and return the path that was traversed if connected. """

        possible_rooms = deque()
        seen = set()
        possible_rooms.append(start)
        seen.add(start)
        path = []
        

        while possible_rooms:

            room = possible_rooms.popleft()

            if room is end:
                return path

            else:
                for direction in room.exits:
                    exit_object = room.get_square(direction)
                    path.append(direction)

                    if exit_object is end:
                        return path

                    if exit_object not in seen:
                        possible_rooms.append(exit_object)
                        seen.add(exit_object)
                    else:
                        path.pop()
            


    # def run(self, start, end, seen=None, path=None):
    #     """ Use recursive depth-first search to check if start and end nodes
    #         are connected and return the path that was traversed if connected. """

    #     # Keep track of nodes we've visited and initialize empty list to track path.
    #     # Add start node to "seen" stack and check if start equals end.
    #     if not seen:
    #         seen = set()

    #     if not path:
    #         path = []

    #     seen.add(start)

    #     if start is end:
    #         return path

    #     # Iterate through adjacency list for start node and get MazeSquare 
    #     # object. Check if object is in "seen" set and if not, append direction 
    #     # to path and recursively call run method on object. If recursive call 
    #     # returns the "end" node, stop calling and return the path. Or else, 
    #     # remove the most recent direction from path list.
    #     for direction in start.exits:
    #         exit_object = start.get_square(direction)

    #         if exit_object not in seen:
                
    #             path.append(direction)
    #             call_next = self.run(exit_object, end, seen, path)

    #             if call_next:
    #                 return path
    #             else:
    #                 path.pop()


class MazeLoader:
    def __init__(self):
        self.master_list = {}

        # These lines are for use with running Unit Test Class
        # #######################
        # data_folder = Path("/home/mauratee/src/mazes-takehome/src/samples/")
        # file_to_open = data_folder / "generated100.maze"
        # f = open(file_to_open)
        
        try:
            with open(sys.argv[1], 'r') as f:
                cell_nums = int(f.readline())
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



# class Test(unittest.TestCase):

#     def setUp(self):
#         self.master_list = {}

#         data_folder = Path("/home/mauratee/src/mazes-takehome/src/samples/")
#         # file_to_open = data_folder / "simple.maze"
#         # file_to_open = data_folder / "generated100.maze"
#         # file_to_open = data_folder / "generated1000.maze"
#         # file_to_open = data_folder / "generatedLong2.maze"
#         file_to_open = data_folder / "generatedsparse.maze"
#         f = open(file_to_open)
        

#         cell_nums = int(f.readline())
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
#                 # Strip newline characters from input
#                 next_square = next_square.strip('\n')
#                 if next_square not in self.master_list:
#                     self.master_list[next_square] = MazeSquare(next_square)
#                 square.add_exit(self.master_list.get(next_square), direction)
#         start, end = f.readline().split(' ')
#         # Strip newline characters from input
#         end = end.strip('\n')

#         self.start = start
#         self.end = end

    
#     def test_ReferenceMazeRunner_simplemaze(self):
#         begin = self.master_list.get(self.start)
#         finish = self.master_list.get(self.end)
#         runner = ReferenceMazeRunner()
#         actual = runner.run(begin, finish)
#         expected = ['North', 'East']
#         self.assertEqual(actual, expected)

#     def test_ReferenceMazeRunner_generated100maze(self):
#         begin = self.master_list.get(self.start)
#         finish = self.master_list.get(self.end)
#         runner = ReferenceMazeRunner()
#         actual = runner.run(begin, finish)
#         expected = ['left', 'east', 'left', 'left', 'left', 'widdershins', 'east',
#          'east', 'east', 'east', 'east', 'south', 'north', 'left', 'left', 'spinwise',
#         'south', 'left', 'east', 'spinwise', 'left', 'east', 'east', 'left', 'left',
#         'left', 'left', 'spinwise', 'east', 'spinwise', 'left', 'left', 'spinwise',
#         'up', 'right', 'east']
#         self.assertEqual(actual, expected)

#     def test_ReferenceMazeRunner_generated1000maze(self):
#         begin = self.master_list.get(self.start)
#         finish = self.master_list.get(self.end)
#         runner = ReferenceMazeRunner()
#         actual = runner.run(begin, finish)
#         expected = ['spinwise', 'left', 'spinwise', 'ascend', 'ascend', 'slide', 'east', 
#         'south', 'left', 'east', 'forward', 'stutter', 'descend', 'left', 'slide', 
#         'ascend', 'east', 'stutter', 'left', 'outside', 'east', 'east', 'forward', 
#         'forward', 'ascend', 'descend', 'west', 'north', 'east', 'forward', 'left', 
#         'stutter', 'ascend', 'south', 'inside', 'ascend', 'north', 'spinwise', 'forward', 
#         'descend', 'outside', 'stutter', 'outside', 'stutter', 'left', 'east', 'east', 
#         'up', 'east', 'east', 'east', 'east', 'slide', 'descend', 'west', 'stutter', 
#         'widdershins', 'up', 'descend', 'descend', 'spinwise', 'slide', 'left', 'ascend', 
#         'north', 'south', 'east', 'stutter', 'inside', 'left', 'descend', 'south', 'east', 
#         'slide', 'stutter', 'east', 'east', 'descend', 'left', 'forward', 'west', 'spinwise', 
#         'forward', 'slide', 'north', 'descend', 'descend', 'north', 'stutter', 'left', 'up', 
#         'ascend', 'east', 'ascend', 'ascend', 'east', 'descend', 'west', 'descend', 'forward', 
#         'ascend', 'slide', 'spinwise', 'east', 'ascend', 'up', 'ascend', 'descend', 'outside', 
#         'south', 'ascend', 'east', 'left', 'east', 'east', 'east', 'ascend', 'east', 'descend', 
#         'west', 'outside', 'spinwise', 'east', 'stutter', 'east', 'stutter', 'spinwise', 
#         'forward', 'stutter', 'inside', 'descend', 'slide', 'east', 'left', 'ascend', 'east', 
#         'stutter', 'forward', 'ascend', 'descend', 'spinwise', 'forward', 'east', 'up', 'spinwise', 
#         'left', 'descend', 'forward', 'east', 'stutter', 'descend', 'descend', 'up', 'ascend', 
#         'slide', 'stutter', 'ascend', 'outside', 'east', 'spinwise', 'ascend', 'ascend', 'spinwise', 
#         'slide', 'spinwise', 'spinwise', 'right', 'descend', 'east', 'slide', 'forward', 'spinwise', 
#         'slide', 'spinwise', 'spinwise', 'ascend', 'south', 'outside', 'spinwise', 'left', 'east', 
#         'widdershins', 'inside', 'north', 'ascend', 'slide', 'outside', 'forward', 'ascend', 'east', 
#         'up', 'ascend', 'ascend', 'forward', 'east', 'forward', 'descend', 'ascend', 'east', 
#         'spinwise', 'outside', 'ascend', 'up', 'north', 'slide', 'descend', 'stutter', 'descend', 
#         'left', 'ascend', 'slide', 'spinwise', 'stutter', 'spinwise', 'stutter', 'east', 'north', 
#         'forward', 'outside', 'stutter', 'stutter', 'spinwise', 'ascend', 'slide', 'ascend', 'north', 
#         'ascend', 'left', 'ascend', 'slide', 'south', 'ascend', 'left', 'up', 'stutter', 'east', 
#         'left', 'north', 'slide', 'slide', 'spinwise', 'east', 'east', 'descend', 'ascend', 'descend', 
#         'spinwise', 'north', 'south', 'left', 'stutter', 'up', 'east', 'east', 'east', 'stutter', 
#         'descend', 'stutter', 'stutter', 'right', 'south', 'slide', 'inside', 'south', 'east', 'ascend', 
#         'outside', 'west', 'north', 'descend', 'east', 'north', 'spinwise', 'east', 'stutter', 'slide', 
#         'forward', 'spinwise', 'south', 'descend', 'west', 'left', 'forward', 'left', 'descend', 
#         'spinwise', 'right', 'right', 'outside', 'slide']
#         self.assertEqual(actual, expected)

#     def test_ReferenceMazeRunner_generatedlong2maze(self):
#         begin = self.master_list.get(self.start)
#         finish = self.master_list.get(self.end)
#         runner = ReferenceMazeRunner()
#         actual = runner.run(begin, finish)
#         expected = ['left', 'descend', 'east', 'right', 'spinwise', 'slide', 'ascend', 'east', 'stutter', 'descend', 'forward', 'ascend', 'descend', 'spinwise', 'east', 'descend', 'ascend', 'east', 'east', 'left', 'slide', 'descend', 'outside', 'spinwise', 'stutter', 'right', 'south', 'east', 'left', 'descend', 'east', 'spinwise', 'forward', 'spinwise', 'forward', 'east', 'forward', 'east', 'descend', 'left', 'spinwise', 'ascend', 'outside', 'ascend', 'left', 'up', 'descend', 'inside', 'ascend', 'forward', 'ascend', 'slide', 'left', 'descend', 'descend', 'right', 'slide', 'descend', 'spinwise', 'east', 'backwards', 'slide', 'east', 'south', 'slide', 'stutter', 'slide', 'spinwise', 'ascend', 'ascend', 'south', 'forward', 'left', 'inside', 'descend', 'east', 'forward', 'spinwise', 'left', 'slide', 'slide', 'left', 'south', 'east', 'left', 'ascend', 'spinwise', 'east', 'left', 'left', 'stutter', 'left', 'left', 'descend', 'east', 'descend', 'left', 'descend', 'inside', 'up', 'descend', 'outside', 'east', 'ascend', 'south', 'forward', 'ascend', 'slide', 'east', 'forward', 'east', 'east', 'slide', 'east', 'descend', 'left', 'left', 'outside', 'east', 'outside', 'east', 'spinwise', 'outside', 'descend', 'south', 'east', 'descend', 'widdershins', 'right', 'descend', 'forward', 'outside', 'ascend', 'east', 'east', 'south', 'south', 'forward', 'descend', 'widdershins', 'right', 'east', 'east', 'north', 'east', 'left', 'ascend', 'spinwise', 'left', 'west', 'spinwise', 'east', 'ascend', 'north', 'forward', 'east', 'ascend', 'forward', 'stutter', 'spinwise', 'forward', 'descend', 'spinwise', 'east', 'descend', 'south', 'stutter', 'left', 'ascend', 'ascend', 'east', 'stutter', 'stutter', 'left', 'outside', 'east', 'ascend', 'ascend', 'right', 'ascend', 'descend', 'stutter', 'left', 'spinwise', 'descend', 'south', 'ascend', 'spinwise', 'east', 'descend', 'outside', 'ascend', 'ascend', 'outside', 'north', 'descend', 'left', 'north', 'east', 'spinwise', 'descend', 'east', 'descend', 'left', 'stutter', 'west', 'stutter', 'slide', 'forward', 'east', 'east', 'spinwise', 'stutter', 'east', 'west', 'descend', 'descend', 'stutter', 'stutter', 'east', 'south', 'east', 'ascend', 'ascend', 'north', 'forward', 'east', 'spinwise', 'spinwise', 'west', 'ascend', 'east', 'descend', 'descend', 'spinwise', 'ascend', 'east', 'east', 'inside', 'inside', 'stutter', 'west', 'left', 'east', 'ascend', 'east', 'ascend', 'west', 'spinwise', 'spinwise', 'ascend', 'north', 'descend', 'widdershins', 'ascend', 'stutter', 'left', 'left', 'left', 'spinwise', 'ascend', 'stutter', 'descend', 'east', 'east', 'descend', 'descend', 'slide', 'east', 'spinwise', 'down', 'ascend', 'slide', 'spinwise', 'slide', 'left', 'spinwise', 'outside', 'ascend', 'east', 'left', 'spinwise', 'east', 'up', 'descend', 'spinwise', 'stutter', 'descend', 'east', 'backwards', 'stutter', 'up', 'north', 'left']
#         self.assertEqual(actual, expected)
    
#     def test_ReferenceMazeRunner_generatedsparsemaze(self):
#         begin = self.master_list.get(self.start)
#         finish = self.master_list.get(self.end)
#         runner = ReferenceMazeRunner()
#         actual = runner.run(begin, finish)
#         expected = ['up', 'descend', 'descend', 'south', 'ascend', 'left', 'ascend', 'ascend', 'east', 'stutter', 'descend', 'stutter', 'inside', 'left', 'south', 'forward', 'left', 'ascend', 'forward', 'south', 'left', 'spinwise', 'stutter', 'east', 'slide', 'east', 'left', 'south', 'slide', 'ascend', 'left', 'descend', 'widdershins', 'forward', 'east', 'ascend', 'spinwise', 'south', 'stutter', 'north', 'descend', 'right', 'forward', 'east', 'stutter', 'widdershins', 'slide', 'up', 'south', 'south', 'stutter', 'ascend', 'descend', 'outside', 'forward', 'stutter', 'left', 'east', 'south', 'left', 'ascend', 'forward', 'spinwise', 'stutter', 'left', 'ascend', 'east', 'ascend', 'descend', 'descend', 'forward', 'spinwise', 'east', 'spinwise', 'east', 'descend', 'stutter', 'ascend', 'descend', 'east', 'east', 'ascend', 'forward', 'spinwise', 'forward', 'south', 'left', 'ascend', 'slide', 'ascend', 'east', 'ascend', 'left', 'west', 'descend', 'east', 'slide', 'spinwise', 'descend', 'east', 'descend', 'spinwise', 'left', 'spinwise', 'forward', 'east', 'spinwise', 'forward', 'forward', 'ascend', 'outside', 'spinwise', 'east', 'east', 'forward', 'left', 'stutter', 'stutter', 'east', 'east', 'east', 'ascend', 'spinwise', 'descend', 'stutter', 'up', 'east', 'east', 'slide', 'east', 'descend', 'left', 'slide', 'up', 'south', 'up', 'stutter', 'inside', 'stutter', 'spinwise', 'east', 'stutter', 'north', 'slide', 'south', 'east', 'slide', 'east', 'east', 'east', 'left', 'south', 'descend', 'descend', 'descend', 'forward', 'down', 'south', 'stutter', 'left', 'spinwise', 'left', 'spinwise', 'ascend', 'forward', 'north', 'stutter', 'slide', 'ascend', 'east', 'left', 'descend', 'ascend', 'left', 'left', 'east', 'stutter', 'right', 'down', 'stutter', 'north', 'ascend', 'descend', 'descend', 'outside', 'north', 'spinwise', 'stutter', 'south', 'forward', 'stutter', 'north', 'north', 'stutter', 'left', 'spinwise', 'descend', 'north', 'spinwise', 'spinwise', 'slide', 'north', 'ascend', 'left', 'descend', 'ascend', 'east', 'spinwise', 'ascend', 'south', 'ascend', 'spinwise', 'left', 'spinwise', 'east', 'spinwise', 'spinwise', 'left', 'east', 'outside', 'outside', 'slide', 'east', 'slide', 'east', 'backwards', 'stutter', 'inside', 'descend', 'stutter', 'east', 'stutter', 'stutter', 'slide', 'south', 'forward', 'descend', 'forward', 'descend', 'left', 'left', 'right', 'stutter', 'east', 'slide', 'spinwise', 'left', 'east', 'east', 'south', 'ascend', 'south', 'slide', 'forward', 'forward', 'west', 'slide', 'east', 'forward', 'slide', 'descend', 'descend', 'left', 'widdershins', 'descend', 'east', 'north', 'north', 'ascend', 'left', 'stutter', 'forward', 'ascend', 'stutter', 'east', 'east', 'stutter', 'east', 'east', 'east', 'ascend', 'descend', 'forward', 'inside', 'north', 'spinwise', 'descend', 'left', 'east', 'east', 'forward', 'inside', 'forward', 'east', 'descend', 'up', 'forward', 'up', 'forward', 'down', 'north', 'descend', 'left', 'inside', 'inside', 'ascend', 'ascend', 'forward', 'north', 'up', 'ascend', 'left', 'widdershins', 'left', 'east', 'ascend', 'spinwise', 'right', 'north', 'outside', 'forward', 'north', 'north', 'ascend', 'forward', 'west', 'left', 'north', 'east', 'up', 'east', 'inside', 'north', 'slide', 'ascend', 'inside', 'inside', 'spinwise', 'spinwise', 'spinwise', 'ascend', 'down', 'slide', 'left', 'left', 'ascend', 'spinwise', 'west', 'spinwise', 'stutter', 'east', 'ascend', 'spinwise', 'descend', 'east', 'ascend', 'ascend', 'left', 'east', 'widdershins', 'slide', 'forward', 'up', 'stutter', 'east', 'slide', 'ascend', 'east', 'stutter', 'north', 'left', 'outside', 'east', 'spinwise', 'descend', 'left', 'up', 'descend', 'slide', 'spinwise', 'stutter', 'up', 'east', 'left', 'east', 'right', 'up', 'backwards', 'east', 'right', 'forward', 'up', 'slide', 'up', 'inside', 'outside', 'ascend', 'forward', 'forward', 'descend', 'east', 'left', 'spinwise', 'descend', 'backwards', 'east', 'widdershins', 'forward', 'slide', 'south', 'outside', 'widdershins', 'east', 'east', 'ascend', 'east', 'left', 'widdershins', 'slide', 'forward', 'east', 'descend', 'north', 'north', 'slide', 'outside', 'east', 'east', 'descend', 'spinwise', 'up', 'ascend', 'spinwise', 'west', 'south', 'left', 'north', 'up', 'inside', 'widdershins', 'south', 'east', 'ascend', 'south', 'widdershins', 'east', 'inside', 'descend', 'north', 'forward', 'ascend', 'south', 'east', 'ascend', 'ascend', 'left', 'ascend', 'ascend', 'spinwise', 'left', 'ascend', 'north', 'east', 'descend', 'spinwise', 'forward', 'south']
#         self.assertEqual(actual, expected)



# unittest.main(verbosity=2)


# call sample mazes in Command Line:
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/simple.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generated100.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generated1000.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLarge.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLong2.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLong.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedsparse.maze




