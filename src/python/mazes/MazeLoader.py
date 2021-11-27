import sys
from collections import deque
import unittest
from pathlib import Path
# Change Python recursion limit to accomodate more recursive calls
import sys
sys.setrecursionlimit(10000)

# Import built-in memoization
import functools


class ReferenceMazeRunner:

    # I wrote this algorithm and began to write unit tests based on this algorithm before
    # I realized the generatedLarge.maze file errors out because it is a recursive algorithm.
    # I've been travelling the last few days and am short on time but would otherwise have
    # completed the breadth-first-search algorithm below to run the generatedLarge.maze file
    # and completed the test suite below.

    ##############
    # Memoization function: TypeError: unhashable type: 'set'
    # def memoize(f):
    #     cache = {}

    #     def helper(*args):
    #         if args in cache:
    #             return cache[args]
    #         result = f(*args)
    #         cache[args] = result
    #         return result

    #     return helper

    # @functools.lru_cache(maxsize = 1000)
    def run(self, start, end, seen=None, path=None):
        """ Use recursive depth-first search to check if start and end nodes
            are connected and return the path that was traversed if connected. """

        # Keep track of nodes we've visited and initialize empty list to track path.
        # Add start node to "seen" stack and check if start equals end.
        if not seen:
            seen = set()

        if not path:
            path = []

        seen.add(start)

        if start is end:
            return path

        # Iterate through adjacency list for start node and get MazeSquare 
        # object. Check if object is in "seen" set and if not, append direction 
        # to path and recursively call run method on object. If recursive call 
        # returns the "end" node, stop calling and return the path. Or else, 
        # remove the most recent direction from path list.
        for direction in start.exits:
            exit_object = start.get_square(direction)

            if exit_object not in seen:
                
                path.append(direction)
                call_next = self.run(exit_object, end, seen, path)

                if call_next:
                    return path
                else:
                    path.pop()
    #########################
    # Call memoization function
    # run = memoize(run)

    # This algorithm was written after I realized the generatedLarge.maze file was not running
    # through the recursive DFS algo without errors. This is incomplete but if I had more time
    # I would implement this algorithm for the generatedLarge.maze file
    # def run(self, start, end):
    #     """ Use breadth-first search to check if start and end nodes
    #         are connected and return the path that was traversed if connected. """

    #     possible_rooms = deque()
    #     seen = set()
    #     possible_rooms.append(start)
    #     seen.add(start)
    #     path = []
        

    #     # print(f"\nroom is {room} (first object in possible_rooms queue)\n")

    #     while possible_rooms:
    #         print(f"^^^^^^^^THIS IS THE START OF THE WHILE LOOP^^^^^^^^^^^^^^")
    #         print(f"\npossible rooms queue is {possible_rooms}")


    #         # if room not in seen:

    #         #     seen[room] = prev

    #         #     if room is end:

    #         #         path = []
    #         #         print(f"\nreturning path: {path} - {room} is {end}")

    #         #         while room is not None:
    #         #             path.append(room)
    #         #             room = seen[room]

    #         #         return path[::-1]
                
    #         #     else:
    #         #         possible_rooms += [(room.get_square(direction), room) for direction in room.exits.keys()]


    #         print(f">>>>> We are in the else block >>>>>")
    #         # print(f"\nroom is {room}\n")
    #         # print(f"\nroom.exits is {room.exits}")
    #         room = possible_rooms.popleft()

    #         if room is end:
    #             print(f"\nreturning room: {room} is {end}")
    #             return room
    #         # possible_rooms.append(room)
    #         seen.add(room)

    #         for direction in room.exits:

    #             print(f"\n>>>>> We are in the for loop >>>>>")
    #             print(f"\ndirection is {direction}")

    #             # path.append(direction)
    #             exit_object = room.get_square(direction)

    #             print(f"exit_object is {exit_object}")

    #             # if exit_object is end:

    #             #     print(f"\nIn else block -> for loop -> if stmt returning path: {path} - {exit_object} is {end}")
    #             #     return path

    #             if exit_object not in seen:

    #                 print(f"\n<<<<< We are in the if stmt (not in seen) <<<<<<")
    #                 print(f"exit_object is {exit_object}")
    #                 print(f"Seen is {seen}")

                    
    #                 possible_rooms.append(exit_object)

    #                 # print(f"\nWe just appended {direction} to path. Path is now: {path}")
    #                 # print(f"\nWe just appended {exit_object} to possible_rooms. Possible_rooms is now: {possible_rooms}")
    #                 # print(f"\nWe just appended {exit_object} to seen. Seen is now: {seen}")

    #             # else:
                    
    #             #     if path:
    #             #         print(f"\n<<<<< We are in the else stmt (after not in seen) <<<<<<")
    #             #         print(f"\nWe just removed {direction} from path. Path is now: {path}")

    #             #         path.pop()


class MazeLoader:
    def __init__(self):
        self.master_list = {}
        
        try:
            with open(file_to_open) as f:
            # with open(sys.argv[1], 'r') as f:
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

# MazeLoader()



class Test(unittest.TestCase):

    def setUp(self):
        self.master_list = {}

        # data_folder = Path("/home/mauratee/src/mazes-takehome/src/samples/")
        # # file_to_open = data_folder / "simple.maze"
        # # file_to_open = data_folder / "generated100.maze"
        # # file_to_open = data_folder / "generated1000.maze"
        # # file_to_open = data_folder / "generatedLong2.maze"
        # file_to_open = data_folder / "generatedsparse.maze"
        f = open(file_to_open)
        

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

        self.start = start
        self.end = end

    
    def test_ReferenceMazeRunner_simplemaze(self):
        begin = self.master_list.get(self.start)
        finish = self.master_list.get(self.end)
        runner = ReferenceMazeRunner()
        actual = runner.run(begin, finish)
        expected = ['North', 'East']
        self.assertEqual(actual, expected)

    def test_ReferenceMazeRunner_generated100maze(self):
        begin = self.master_list.get(self.start)
        finish = self.master_list.get(self.end)
        runner = ReferenceMazeRunner()
        actual = runner.run(begin, finish)
        expected = ['left', 'east', 'left', 'left', 'left', 'widdershins', 'east',
         'east', 'east', 'east', 'east', 'south', 'north', 'left', 'left', 'spinwise',
        'south', 'left', 'east', 'spinwise', 'left', 'east', 'east', 'left', 'left',
        'left', 'left', 'spinwise', 'east', 'spinwise', 'left', 'left', 'spinwise',
        'up', 'right', 'east']
        self.assertEqual(actual, expected)

    def test_ReferenceMazeRunner_generated1000maze(self):
        begin = self.master_list.get(self.start)
        finish = self.master_list.get(self.end)
        runner = ReferenceMazeRunner()
        actual = runner.run(begin, finish)
        expected = ['spinwise', 'left', 'spinwise', 'ascend', 'ascend', 'slide', 'east', 
        'south', 'left', 'east', 'forward', 'stutter', 'descend', 'left', 'slide', 
        'ascend', 'east', 'stutter', 'left', 'outside', 'east', 'east', 'forward', 
        'forward', 'ascend', 'descend', 'west', 'north', 'east', 'forward', 'left', 
        'stutter', 'ascend', 'south', 'inside', 'ascend', 'north', 'spinwise', 'forward', 
        'descend', 'outside', 'stutter', 'outside', 'stutter', 'left', 'east', 'east', 
        'up', 'east', 'east', 'east', 'east', 'slide', 'descend', 'west', 'stutter', 
        'widdershins', 'up', 'descend', 'descend', 'spinwise', 'slide', 'left', 'ascend', 
        'north', 'south', 'east', 'stutter', 'inside', 'left', 'descend', 'south', 'east', 
        'slide', 'stutter', 'east', 'east', 'descend', 'left', 'forward', 'west', 'spinwise', 
        'forward', 'slide', 'north', 'descend', 'descend', 'north', 'stutter', 'left', 'up', 
        'ascend', 'east', 'ascend', 'ascend', 'east', 'descend', 'west', 'descend', 'forward', 
        'ascend', 'slide', 'spinwise', 'east', 'ascend', 'up', 'ascend', 'descend', 'outside', 
        'south', 'ascend', 'east', 'left', 'east', 'east', 'east', 'ascend', 'east', 'descend', 
        'west', 'outside', 'spinwise', 'east', 'stutter', 'east', 'stutter', 'spinwise', 
        'forward', 'stutter', 'inside', 'descend', 'slide', 'east', 'left', 'ascend', 'east', 
        'stutter', 'forward', 'ascend', 'descend', 'spinwise', 'forward', 'east', 'up', 'spinwise', 
        'left', 'descend', 'forward', 'east', 'stutter', 'descend', 'descend', 'up', 'ascend', 
        'slide', 'stutter', 'ascend', 'outside', 'east', 'spinwise', 'ascend', 'ascend', 'spinwise', 
        'slide', 'spinwise', 'spinwise', 'right', 'descend', 'east', 'slide', 'forward', 'spinwise', 
        'slide', 'spinwise', 'spinwise', 'ascend', 'south', 'outside', 'spinwise', 'left', 'east', 
        'widdershins', 'inside', 'north', 'ascend', 'slide', 'outside', 'forward', 'ascend', 'east', 
        'up', 'ascend', 'ascend', 'forward', 'east', 'forward', 'descend', 'ascend', 'east', 
        'spinwise', 'outside', 'ascend', 'up', 'north', 'slide', 'descend', 'stutter', 'descend', 
        'left', 'ascend', 'slide', 'spinwise', 'stutter', 'spinwise', 'stutter', 'east', 'north', 
        'forward', 'outside', 'stutter', 'stutter', 'spinwise', 'ascend', 'slide', 'ascend', 'north', 
        'ascend', 'left', 'ascend', 'slide', 'south', 'ascend', 'left', 'up', 'stutter', 'east', 
        'left', 'north', 'slide', 'slide', 'spinwise', 'east', 'east', 'descend', 'ascend', 'descend', 
        'spinwise', 'north', 'south', 'left', 'stutter', 'up', 'east', 'east', 'east', 'stutter', 
        'descend', 'stutter', 'stutter', 'right', 'south', 'slide', 'inside', 'south', 'east', 'ascend', 
        'outside', 'west', 'north', 'descend', 'east', 'north', 'spinwise', 'east', 'stutter', 'slide', 
        'forward', 'spinwise', 'south', 'descend', 'west', 'left', 'forward', 'left', 'descend', 
        'spinwise', 'right', 'right', 'outside', 'slide']
        self.assertEqual(actual, expected)

    def test_ReferenceMazeRunner_generatedlong2maze(self):
        begin = self.master_list.get(self.start)
        finish = self.master_list.get(self.end)
        runner = ReferenceMazeRunner()
        actual = runner.run(begin, finish)
        expected = ['left', 'descend', 'east', 'right', 'spinwise', 'slide', 'ascend', 'east', 'stutter', 'descend', 'forward', 'ascend', 'descend', 'spinwise', 'east', 'descend', 'ascend', 'east', 'east', 'left', 'slide', 'descend', 'outside', 'spinwise', 'stutter', 'right', 'south', 'east', 'left', 'descend', 'east', 'spinwise', 'forward', 'spinwise', 'forward', 'east', 'forward', 'east', 'descend', 'left', 'spinwise', 'ascend', 'outside', 'ascend', 'left', 'up', 'descend', 'inside', 'ascend', 'forward', 'ascend', 'slide', 'left', 'descend', 'descend', 'right', 'slide', 'descend', 'spinwise', 'east', 'backwards', 'slide', 'east', 'south', 'slide', 'stutter', 'slide', 'spinwise', 'ascend', 'ascend', 'south', 'forward', 'left', 'inside', 'descend', 'east', 'forward', 'spinwise', 'left', 'slide', 'slide', 'left', 'south', 'east', 'left', 'ascend', 'spinwise', 'east', 'left', 'left', 'stutter', 'left', 'left', 'descend', 'east', 'descend', 'left', 'descend', 'inside', 'up', 'descend', 'outside', 'east', 'ascend', 'south', 'forward', 'ascend', 'slide', 'east', 'forward', 'east', 'east', 'slide', 'east', 'descend', 'left', 'left', 'outside', 'east', 'outside', 'east', 'spinwise', 'outside', 'descend', 'south', 'east', 'descend', 'widdershins', 'right', 'descend', 'forward', 'outside', 'ascend', 'east', 'east', 'south', 'south', 'forward', 'descend', 'widdershins', 'right', 'east', 'east', 'north', 'east', 'left', 'ascend', 'spinwise', 'left', 'west', 'spinwise', 'east', 'ascend', 'north', 'forward', 'east', 'ascend', 'forward', 'stutter', 'spinwise', 'forward', 'descend', 'spinwise', 'east', 'descend', 'south', 'stutter', 'left', 'ascend', 'ascend', 'east', 'stutter', 'stutter', 'left', 'outside', 'east', 'ascend', 'ascend', 'right', 'ascend', 'descend', 'stutter', 'left', 'spinwise', 'descend', 'south', 'ascend', 'spinwise', 'east', 'descend', 'outside', 'ascend', 'ascend', 'outside', 'north', 'descend', 'left', 'north', 'east', 'spinwise', 'descend', 'east', 'descend', 'left', 'stutter', 'west', 'stutter', 'slide', 'forward', 'east', 'east', 'spinwise', 'stutter', 'east', 'west', 'descend', 'descend', 'stutter', 'stutter', 'east', 'south', 'east', 'ascend', 'ascend', 'north', 'forward', 'east', 'spinwise', 'spinwise', 'west', 'ascend', 'east', 'descend', 'descend', 'spinwise', 'ascend', 'east', 'east', 'inside', 'inside', 'stutter', 'west', 'left', 'east', 'ascend', 'east', 'ascend', 'west', 'spinwise', 'spinwise', 'ascend', 'north', 'descend', 'widdershins', 'ascend', 'stutter', 'left', 'left', 'left', 'spinwise', 'ascend', 'stutter', 'descend', 'east', 'east', 'descend', 'descend', 'slide', 'east', 'spinwise', 'down', 'ascend', 'slide', 'spinwise', 'slide', 'left', 'spinwise', 'outside', 'ascend', 'east', 'left', 'spinwise', 'east', 'up', 'descend', 'spinwise', 'stutter', 'descend', 'east', 'backwards', 'stutter', 'up', 'north', 'left']
        self.assertEqual(actual, expected)
    
    def test_ReferenceMazeRunner_generatedsparsemaze(self):
        begin = self.master_list.get(self.start)
        finish = self.master_list.get(self.end)
        runner = ReferenceMazeRunner()
        actual = runner.run(begin, finish)
        expected = ['up', 'descend', 'descend', 'south', 'ascend', 'left', 'ascend', 'ascend', 'east', 'stutter', 'descend', 'stutter', 'inside', 'left', 'south', 'forward', 'left', 'ascend', 'forward', 'south', 'left', 'spinwise', 'stutter', 'east', 'slide', 'east', 'left', 'south', 'slide', 'ascend', 'left', 'descend', 'widdershins', 'forward', 'east', 'ascend', 'spinwise', 'south', 'stutter', 'north', 'descend', 'right', 'forward', 'east', 'stutter', 'widdershins', 'slide', 'up', 'south', 'south', 'stutter', 'ascend', 'descend', 'outside', 'forward', 'stutter', 'left', 'east', 'south', 'left', 'ascend', 'forward', 'spinwise', 'stutter', 'left', 'ascend', 'east', 'ascend', 'descend', 'descend', 'forward', 'spinwise', 'east', 'spinwise', 'east', 'descend', 'stutter', 'ascend', 'descend', 'east', 'east', 'ascend', 'forward', 'spinwise', 'forward', 'south', 'left', 'ascend', 'slide', 'ascend', 'east', 'ascend', 'left', 'west', 'descend', 'east', 'slide', 'spinwise', 'descend', 'east', 'descend', 'spinwise', 'left', 'spinwise', 'forward', 'east', 'spinwise', 'forward', 'forward', 'ascend', 'outside', 'spinwise', 'east', 'east', 'forward', 'left', 'stutter', 'stutter', 'east', 'east', 'east', 'ascend', 'spinwise', 'descend', 'stutter', 'up', 'east', 'east', 'slide', 'east', 'descend', 'left', 'slide', 'up', 'south', 'up', 'stutter', 'inside', 'stutter', 'spinwise', 'east', 'stutter', 'north', 'slide', 'south', 'east', 'slide', 'east', 'east', 'east', 'left', 'south', 'descend', 'descend', 'descend', 'forward', 'down', 'south', 'stutter', 'left', 'spinwise', 'left', 'spinwise', 'ascend', 'forward', 'north', 'stutter', 'slide', 'ascend', 'east', 'left', 'descend', 'ascend', 'left', 'left', 'east', 'stutter', 'right', 'down', 'stutter', 'north', 'ascend', 'descend', 'descend', 'outside', 'north', 'spinwise', 'stutter', 'south', 'forward', 'stutter', 'north', 'north', 'stutter', 'left', 'spinwise', 'descend', 'north', 'spinwise', 'spinwise', 'slide', 'north', 'ascend', 'left', 'descend', 'ascend', 'east', 'spinwise', 'ascend', 'south', 'ascend', 'spinwise', 'left', 'spinwise', 'east', 'spinwise', 'spinwise', 'left', 'east', 'outside', 'outside', 'slide', 'east', 'slide', 'east', 'backwards', 'stutter', 'inside', 'descend', 'stutter', 'east', 'stutter', 'stutter', 'slide', 'south', 'forward', 'descend', 'forward', 'descend', 'left', 'left', 'right', 'stutter', 'east', 'slide', 'spinwise', 'left', 'east', 'east', 'south', 'ascend', 'south', 'slide', 'forward', 'forward', 'west', 'slide', 'east', 'forward', 'slide', 'descend', 'descend', 'left', 'widdershins', 'descend', 'east', 'north', 'north', 'ascend', 'left', 'stutter', 'forward', 'ascend', 'stutter', 'east', 'east', 'stutter', 'east', 'east', 'east', 'ascend', 'descend', 'forward', 'inside', 'north', 'spinwise', 'descend', 'left', 'east', 'east', 'forward', 'inside', 'forward', 'east', 'descend', 'up', 'forward', 'up', 'forward', 'down', 'north', 'descend', 'left', 'inside', 'inside', 'ascend', 'ascend', 'forward', 'north', 'up', 'ascend', 'left', 'widdershins', 'left', 'east', 'ascend', 'spinwise', 'right', 'north', 'outside', 'forward', 'north', 'north', 'ascend', 'forward', 'west', 'left', 'north', 'east', 'up', 'east', 'inside', 'north', 'slide', 'ascend', 'inside', 'inside', 'spinwise', 'spinwise', 'spinwise', 'ascend', 'down', 'slide', 'left', 'left', 'ascend', 'spinwise', 'west', 'spinwise', 'stutter', 'east', 'ascend', 'spinwise', 'descend', 'east', 'ascend', 'ascend', 'left', 'east', 'widdershins', 'slide', 'forward', 'up', 'stutter', 'east', 'slide', 'ascend', 'east', 'stutter', 'north', 'left', 'outside', 'east', 'spinwise', 'descend', 'left', 'up', 'descend', 'slide', 'spinwise', 'stutter', 'up', 'east', 'left', 'east', 'right', 'up', 'backwards', 'east', 'right', 'forward', 'up', 'slide', 'up', 'inside', 'outside', 'ascend', 'forward', 'forward', 'descend', 'east', 'left', 'spinwise', 'descend', 'backwards', 'east', 'widdershins', 'forward', 'slide', 'south', 'outside', 'widdershins', 'east', 'east', 'ascend', 'east', 'left', 'widdershins', 'slide', 'forward', 'east', 'descend', 'north', 'north', 'slide', 'outside', 'east', 'east', 'descend', 'spinwise', 'up', 'ascend', 'spinwise', 'west', 'south', 'left', 'north', 'up', 'inside', 'widdershins', 'south', 'east', 'ascend', 'south', 'widdershins', 'east', 'inside', 'descend', 'north', 'forward', 'ascend', 'south', 'east', 'ascend', 'ascend', 'left', 'ascend', 'ascend', 'spinwise', 'left', 'ascend', 'north', 'east', 'descend', 'spinwise', 'forward', 'south']
        self.assertEqual(actual, expected)

    def test_ReferenceMazeRunner_generatedLargemaze(self):
        begin = self.master_list.get(self.start)
        finish = self.master_list.get(self.end)
        runner = ReferenceMazeRunner()
        actual = runner.run(begin, finish)
        expected = ['ascend', 'east', 'east', 'east', 'east', 'left', 'east', 'east', 'descend', 'south', 'east', 'stutter', 'stutter', 'forward', 'east', 'left', 'left', 'ascend', 'descend', 'left', 'east', 'spinwise', 'slide', 'forward', 'east', 'descend', 'forward', 'ascend', 'ascend', 'left', 'descend', 'left', 'descend', 'left', 'forward', 'slide', 'east', 'up', 'left', 'descend', 'east', 'stutter', 'east', 'north', 'ascend', 'east', 'east', 'east', 'spinwise', 'east', 'descend', 'stutter', 'descend', 'east', 'ascend', 'ascend', 'ascend', 'forward', 'slide', 'ascend', 'east', 'left', 'slide', 'descend', 'right', 'ascend', 'slide', 'slide', 'spinwise', 'ascend', 'east', 'descend', 'stutter', 'ascend', 'ascend', 'east', 'east', 'forward', 'stutter', 'up', 'forward', 'ascend', 'descend', 'slide', 'east', 'descend', 'spinwise', 'east', 'inside', 'stutter', 'spinwise', 'descend', 'south', 'ascend', 'left', 'up', 'east', 'spinwise', 'east', 'east', 'descend', 'spinwise', 'east', 'east', 'inside', 'north', 'east', 'left', 'left', 'ascend', 'east', 'outside', 'ascend', 'east', 'descend', 'east', 'east', 'descend', 'spinwise', 'south', 'left', 'descend', 'east', 'east', 'east', 'left', 'ascend', 'up', 'ascend', 'east', 'forward', 'spinwise', 'south', 'forward', 'left', 'spinwise', 'stutter', 'ascend', 'descend', 'spinwise', 'slide', 'spinwise', 'spinwise', 'left', 'stutter', 'forward', 'forward', 'ascend', 'ascend', 'left', 'ascend', 'east', 'ascend', 'outside', 'slide', 'east', 'stutter', 'east', 'east', 'ascend', 'descend', 'stutter', 'slide', 'slide', 'spinwise', 'ascend', 'left', 'ascend', 'east', 'ascend', 'spinwise', 'spinwise', 'descend', 'south', 'spinwise', 'left', 'ascend', 'slide', 'ascend', 'spinwise', 'spinwise', 'ascend', 'up', 'spinwise', 'descend', 'south', 'descend', 'east', 'descend', 'slide', 'stutter', 'left', 'left', 'slide', 'spinwise', 'east', 'descend', 'descend', 'ascend', 'outside', 'west', 'left', 'ascend', 'ascend', 'stutter', 'forward', 'spinwise', 'east', 'descend', 'slide', 'east', 'east', 'south', 'inside', 'east', 'descend', 'descend', 'east', 'forward', 'east', 'left', 'spinwise', 'south', 'spinwise', 'left', 'ascend', 'descend', 'north', 'east', 'forward', 'left', 'left', 'east', 'ascend', 'spinwise', 'slide', 'south', 'inside', 'slide', 'left', 'east', 'ascend', 'ascend', 'stutter', 'slide', 'descend', 'east', 'forward', 'south', 'south', 'east', 'forward', 'forward', 'slide', 'forward', 'stutter', 'forward', 'descend', 'south', 'slide', 'north', 'ascend', 'east', 'descend', 'widdershins', 'spinwise', 'ascend', 'stutter', 'ascend', 'descend', 'stutter', 'right', 'spinwise', 'descend', 'descend', 'west', 'left', 'ascend', 'up', 'left', 'outside', 'spinwise', 'east', 'east', 'ascend', 'north', 'east', 'descend', 'descend', 'descend', 'spinwise', 'ascend', 'descend', 'descend', 'descend', 'ascend', 'west', 'south', 'stutter', 'spinwise', 'spinwise', 'spinwise', 'spinwise', 'ascend', 'spinwise', 'ascend', 'ascend', 'descend', 'left', 'descend', 'east', 'left', 'ascend', 'east', 'ascend', 'forward', 'ascend', 'east', 'up', 'spinwise', 'south', 'east', 'forward', 'spinwise', 'north', 'east', 'descend', 'east', 'descend', 'descend', 'left', 'east', 'east', 'descend', 'descend', 'spinwise', 'left', 'east', 'spinwise', 'spinwise', 'descend', 'spinwise', 'spinwise', 'east', 'stutter', 'up', 'left', 'stutter', 'ascend', 'stutter', 'ascend', 'east', 'north', 'forward', 'left', 'descend', 'descend', 'east', 'east', 'east', 'descend', 'north', 'descend', 'left', 'east', 'ascend', 'east', 'east', 'outside', 'forward', 'stutter', 'left', 'left', 'ascend', 'spinwise', 'west', 'stutter', 'south', 'outside', 'stutter', 'slide', 'stutter', 'descend', 'descend', 'left', 'stutter', 'outside', 'left', 'up', 'forward', 'left', 'north', 'east', 'east', 'north', 'stutter', 'spinwise', 'east', 'east', 'slide', 'left', 'descend', 'left', 'south', 'forward', 'forward', 'down', 'slide', 'east', 'descend', 'slide', 'left', 'north', 'east', 'stutter', 'descend', 'south', 'stutter', 'north', 'east', 'ascend', 'north', 'east', 'ascend', 'up', 'east', 'descend', 'slide', 'stutter', 'east', 'south', 'spinwise', 'spinwise', 'forward', 'spinwise', 'outside', 'left', 'spinwise', 'descend', 'spinwise', 'left', 'south', 'backwards', 'east', 'east', 'descend', 'east', 'east', 'spinwise', 'descend', 'descend', 'forward', 'descend', 'east', 'left', 'ascend', 'north', 'forward', 'widdershins', 'south', 'slide', 'east', 'east', 'descend', 'left', 'forward', 'stutter', 'east', 'north', 'east', 'descend', 'left', 'descend', 'slide', 'east', 'inside', 'ascend', 'east', 'descend', 'left', 'spinwise', 'east', 'east', 'east', 'south', 'forward', 'north', 'right', 'ascend', 'east', 'descend', 'up', 'left', 'left', 'east', 'descend', 'forward', 'left', 'east', 'outside', 'south', 'descend', 'up', 'spinwise', 'east', 'stutter', 'east', 'ascend', 'east', 'east', 'east', 'left', 'left', 'east', 'stutter', 'east', 'descend', 'west', 'ascend', 'forward', 'east', 'up', 'descend', 'descend', 'spinwise', 'south', 'spinwise', 'left', 'forward', 'forward', 'left', 'outside', 'left',
        'descend', 'south', 'slide', 'south', 'east', 'slide', 'east', 'north', 'descend', 'outside', 'left', 'forward', 'east', 'ascend', 'outside', 'stutter', 'north', 'descend', 'left', 'ascend', 'ascend', 'east', 'inside', 'descend', 'left', 'east', 'spinwise', 'spinwise', 'spinwise', 'ascend', 'forward', 'stutter', 'ascend', 'descend', 'spinwise', 'ascend', 'south', 'backwards', 'east', 'descend', 'stutter', 'descend', 'ascend', 'east', 'ascend', 'east', 'ascend', 'descend', 'descend', 'north', 'forward', 'east', 'spinwise', 'spinwise', 'up', 'south', 'south', 'south', 'east', 'ascend', 'left', 'ascend', 'east', 'left', 'left', 'south', 'ascend', 'stutter', 'ascend', 'south', 'descend', 'east', 'spinwise', 'east', 'east', 'ascend', 'ascend', 'descend', 'descend', 'spinwise', 'south', 'descend', 'spinwise', 'spinwise', 'east', 'slide', 'descend', 'east', 'descend', 'slide', 'left', 'descend', 'inside', 'east', 'up', 'ascend', 'spinwise', 'descend', 'ascend', 'slide', 'ascend', 'stutter', 'ascend', 'up', 'ascend', 'ascend', 'east', 'inside', 'left', 'descend', 'stutter', 'up', 'south', 'east', 'outside', 'slide', 'east', 'south', 'slide', 'up', 'north', 'east', 'ascend', 'east', 'left', 'spinwise', 'north', 'east', 'east', 'left', 'south', 'stutter', 'south', 'descend', 'ascend', 'east', 'east', 'north', 'spinwise', 'east', 'descend', 'spinwise', 'descend', 'descend', 'stutter', 'north', 'stutter', 'slide', 'east', 'stutter', 'stutter', 'descend', 'east', 'up', 'north', 'ascend', 'outside', 'left', 'ascend', 'spinwise', 'slide', 'east', 'ascend', 'up', 'ascend', 'ascend', 'ascend', 'ascend', 'ascend', 'spinwise', 'stutter', 'left', 'east', 'descend', 'descend', 'slide', 'ascend', 'east', 'ascend', 'ascend', 'spinwise', 'stutter', 'descend', 'east', 'descend', 'outside', 'ascend', 'slide', 'outside', 'north', 'spinwise', 'left', 'ascend', 'east', 'spinwise', 'left', 'forward', 'north', 'spinwise', 'left', 'spinwise', 'spinwise', 'east', 'forward', 'spinwise', 'east', 'descend', 'spinwise', 'outside', 'east', 'spinwise', 'north', 'descend', 'slide', 'north', 'east', 'spinwise', 'forward', 'south', 'stutter', 'east', 'spinwise', 'north', 'west', 'left', 'left', 'forward', 'ascend', 'left', 'ascend', 'forward', 'stutter', 'ascend', 'spinwise', 'ascend', 'descend', 'backwards', 'east', 'spinwise', 'descend', 'stutter', 'left', 'descend', 'ascend', 'east', 'stutter', 'left', 'up', 'east', 'east', 'descend', 'ascend', 'east', 'left', 'ascend', 'spinwise', 'descend', 'slide', 'outside', 'outside', 'spinwise', 'south', 'outside', 'ascend', 'spinwise', 'spinwise', 'stutter', 'descend', 'right', 'forward', 'east', 'east', 'forward', 'ascend', 'north', 'stutter', 'descend', 'ascend', 'forward', 'spinwise', 'east', 'east', 'east', 'outside', 'slide', 'forward', 'up', 'descend', 'east', 'left', 'stutter', 'forward', 'ascend', 'south', 'ascend', 'left', 'right', 'slide', 'stutter', 'descend', 'left', 'ascend', 'forward', 'ascend', 'north', 'left', 'left', 'descend', 'outside', 'slide', 'forward', 'stutter', 'outside', 'descend', 'east', 'left', 'forward', 'inside', 'spinwise', 'south', 'ascend', 'inside', 'spinwise', 'left', 'east', 'ascend', 'descend', 'left', 'south', 'widdershins', 'spinwise', 'left', 'left', 'descend', 'up', 'ascend', 'ascend', 'forward', 'descend', 'east', 'ascend', 'south', 'ascend', 'stutter', 'east', 'stutter', 'north', 'descend', 'north', 'spinwise', 'east', 'slide', 'widdershins', 'south', 'outside', 'slide', 'spinwise', 'inside', 'spinwise', 'ascend', 'ascend', 'east', 'stutter', 'ascend', 'ascend', 'left', 'ascend', 'slide', 'left', 'south', 'down', 'west', 'up', 'east', 'east', 'descend', 'ascend', 'outside', 'forward', 'descend', 'descend', 'south', 'north', 'ascend', 'left', 'left', 'descend', 'spinwise', 'slide', 'stutter', 'east', 'left', 'ascend', 'descend', 'south', 'forward', 'left', 'south', 'spinwise', 'inside', 'up', 'south', 'north', 'left', 'outside', 'west', 'slide', 'spinwise', 'ascend', 'spinwise', 'descend', 'east', 'east', 'forward', 'ascend', 'left', 'north', 'descend', 'descend', 'descend', 'stutter', 'east', 'south', 'descend', 'inside', 'stutter', 'left', 'ascend', 'east', 'forward', 'left', 'spinwise', 'left', 'ascend', 'spinwise', 'ascend', 'forward', 'ascend', 'widdershins', 'ascend', 'south', 'stutter', 'forward', 'stutter', 'ascend', 'spinwise', 'descend', 'left', 'spinwise', 'east', 'forward', 'spinwise', 'left', 'outside', 'inside', 'descend', 'left', 'spinwise', 'ascend', 'ascend', 'north', 'descend', 'stutter', 'east', 'left', 'left', 'east', 'descend', 'stutter', 'north', 'descend', 'east', 'ascend', 'forward', 'descend', 'forward', 'descend', 'forward', 'spinwise', 'descend', 'inside', 'ascend', 'stutter', 'up', 'stutter', 'left', 'east', 'descend', 'ascend', 'east', 'spinwise', 'right', 'east', 'stutter', 'ascend', 'ascend', 'east', 'outside', 'descend', 'ascend', 'ascend', 'slide', 'spinwise', 'spinwise', 'east', 'ascend', 'north', 'left', 'east', 'left', 'east', 'slide', 'east', 'slide', 'ascend', 'spinwise', 'left', 'descend', 'east', 'inside', 'ascend', 'left', 'east', 'descend', 'north', 'left', 'descend', 'inside', 'east', 'stutter', 'forward', 'west', 'west', 'ascend', 'ascend', 'outside', 'descend', 'left', 'ascend', 'south', 'descend', 'spinwise', 'spinwise', 'spinwise', 'inside', 'ascend', 'left', 'east', 'east', 'ascend', 'east', 'slide', 'forward', 'up', 'descend', 'spinwise', 'ascend', 'south', 'east', 'east', 'east', 'left', 'descend', 'slide', 'east', 'south', 'stutter', 'descend', 'slide', 'descend', 'east', 'slide', 'east', 'south', 'forward', 'spinwise', 'stutter', 'slide', 'forward', 'spinwise', 'ascend', 'spinwise', 'forward', 'ascend', 'ascend', 'spinwise', 'spinwise', 'east', 'left', 'ascend', 'up', 'descend', 'west', 'left', 'descend', 'outside', 'ascend', 'east', 'slide', 'east', 'stutter', 'ascend', 'east', 'east', 'left', 'ascend', 'slide', 'south', 'spinwise', 'ascend', 'ascend', 'widdershins', 'backwards', 'north', 'right', 'north', 'descend', 'south', 'descend', 'south', 'east', 'outside', 'descend', 'forward', 'east', 'left', 'east', 'spinwise', 'east', 'east', 'descend', 'spinwise', 'spinwise', 'forward', 'east', 'east', 'spinwise', 'outside', 'ascend', 'ascend', 'spinwise', 'forward', 'spinwise', 'ascend', 'descend', 'east', 'descend', 'widdershins', 'outside', 'ascend', 'east', 'left', 'south', 'ascend', 'north', 'left', 'forward', 'east', 'north', 'west', 'descend', 'stutter', 'south', 'forward', 'ascend', 'ascend', 'ascend', 'spinwise', 'left', 'descend', 'east', 'descend', 'down', 'descend', 'spinwise', 'ascend', 'forward', 'outside', 'ascend', 'descend', 'forward', 'north', 'east', 'east', 'left', 'east', 'forward', 'descend', 'up', 'inside', 'east', 'inside', 'ascend', 'descend', 'spinwise', 'spinwise', 'east', 'north', 'ascend', 'west', 'outside', 'west', 'stutter', 'ascend', 'ascend', 'ascend', 'inside', 'slide', 'spinwise', 'spinwise', 'spinwise', 'north', 'south', 'forward', 'stutter', 'ascend', 'descend', 'stutter', 'descend', 'outside', 'stutter', 'south', 'forward', 'east', 'slide', 'left', 'stutter', 'slide', 'spinwise', 'left', 'north', 'forward',
        'slide', 'slide', 'east', 'descend', 'ascend', 'north', 'ascend', 'ascend', 'descend', 'descend', 'up', 'spinwise', 'east', 'forward', 'east', 'ascend', 'forward', 'east', 'east', 'east', 'forward', 'inside', 'left', 'ascend', 'stutter', 'descend', 'east', 'ascend', 'ascend', 'south', 'east', 'east', 'forward', 'spinwise', 'left', 'down', 'stutter', 'slide', 'left', 'descend', 'widdershins', 'slide', 'ascend', 'left', 'slide', 'descend', 'inside', 'descend', 'forward', 'spinwise', 'ascend', 'south', 'ascend', 'forward', 'north', 'south', 'slide', 'forward', 'spinwise', 'east', 'left', 'ascend', 'descend', 'spinwise', 'left', 'stutter', 'descend', 'descend', 'up', 'south', 'forward', 'stutter', 'east', 'inside', 'forward', 'east', 'left', 'slide', 'east', 'outside', 'east', 'stutter', 'left', 'left', 'left', 'east', 'ascend', 'ascend', 'stutter', 'north', 'north', 'ascend', 'stutter', 'forward', 'spinwise', 'slide', 'ascend', 'slide', 'left', 'north', 'east', 'east', 'ascend', 'spinwise', 'left', 'east', 'widdershins', 'descend', 'east', 'slide', 'east', 'east', 'east', 'east', 'ascend', 'outside', 'stutter', 'east', 'forward', 'ascend', 'stutter', 'descend', 'east', 'slide', 'ascend', 'ascend', 'up', 'descend', 'widdershins', 'forward', 'left', 'spinwise', 'ascend', 'slide', 'inside', 'east', 'east', 'forward', 'east', 'ascend', 'left', 'east', 'east', 'east', 'spinwise', 'ascend', 'descend', 'east', 'left', 'slide', 'inside', 'descend', 'left', 'descend', 'stutter', 'inside', 'stutter', 'descend', 'east', 'north', 'up', 'ascend', 'north', 'outside', 'ascend', 'east', 'east', 'left', 'ascend', 'west', 'forward', 'spinwise', 'east', 'left', 'stutter', 'north', 'descend', 'forward', 'slide', 'ascend', 'ascend', 'ascend', 'descend', 'widdershins', 'widdershins', 'east', 'left', 'spinwise', 'slide', 'left', 'spinwise', 'left', 'descend', 'spinwise', 'east', 'south', 'left', 'outside', 'right', 'south', 'descend', 'north', 'slide', 'east', 'outside', 'ascend', 'stutter', 'down', 'ascend', 'south', 'left', 'east', 'descend', 'spinwise', 'ascend', 'slide', 'west', 'forward', 'stutter', 'slide', 'east', 'up', 'left', 'north', 'forward', 'stutter', 'descend', 'spinwise', 'spinwise', 'outside', 'stutter', 'inside', 'descend', 'descend', 'slide', 'descend', 'forward', 'ascend', 'north', 'descend', 'up', 'descend', 'north', 'ascend', 'east', 'forward', 'spinwise', 'descend', 'south', 'forward', 'east', 'outside', 'left', 'ascend', 'south', 'descend', 'east', 'north', 'spinwise', 'left', 'ascend', 'stutter', 'descend', 'spinwise', 'ascend', 'slide', 'slide', 'south', 'east', 'left', 'slide', 'east', 'descend', 'east', 'stutter', 'south', 'up', 'left', 'ascend', 'descend', 'descend', 'ascend', 'north', 'left', 'spinwise', 'spinwise', 'descend', 'east', 'descend', 'south', 'ascend', 'forward', 'stutter', 'forward', 'forward', 'slide', 'ascend', 'slide', 'east', 'slide', 'left', 'east', 'spinwise', 'west', 'west', 'down', 'east', 'stutter', 'outside', 'descend', 'inside', 'left', 'east', 'left', 'forward', 'descend', 'descend', 'forward', 'ascend', 'inside', 'stutter', 'ascend', 'outside', 'east', 'ascend', 'spinwise', 'descend', 'left', 'south', 'south', 'inside', 'descend', 'ascend', 'south', 'west', 'outside', 'descend', 'north', 'south', 'forward', 'east', 'ascend', 'forward', 'stutter', 'ascend', 'spinwise', 'west', 'north', 'south', 'east', 'left', 'descend', 'east', 'east', 'left', 'ascend', 'left', 'slide', 'slide', 'east', 'ascend', 'east', 'stutter', 'descend', 'east', 'left', 'slide', 'east', 'stutter', 'outside', 'forward', 'east', 'east', 'ascend', 'ascend', 'spinwise', 'stutter', 'ascend', 'ascend', 'ascend', 'left', 'east', 'ascend', 'east', 'slide', 'slide', 'forward', 'east', 'outside', 'descend', 'east', 'ascend', 'up', 'ascend', 'east', 'right', 'left', 'north', 'slide', 'ascend', 'south', 'ascend', 'ascend', 'inside', 'ascend', 'north', 'down', 'west', 'inside', 'left', 'south', 'stutter', 'ascend', 'west', 'ascend', 'ascend', 'outside', 'inside', 'ascend', 'ascend', 'descend', 'left', 'descend', 'east', 'spinwise', 'stutter', 'ascend', 'east', 'spinwise', 'east', 'ascend', 'spinwise', 'ascend', 'ascend', 'descend', 'east', 'east', 'ascend', 'south', 'south', 'east', 'east', 'east', 'east', 'forward', 'ascend', 'east', 'ascend', 'outside', 'left', 'forward', 'forward', 'north', 'north', 'ascend', 'east', 'forward', 'up', 'forward', 'east', 'east', 'east', 'left', 'east', 'inside', 'east', 'up', 'spinwise', 'left', 'descend', 'east', 'slide', 'up', 'left', 'north', 'descend', 'north', 'south', 'stutter', 'east', 'descend', 'descend', 'slide', 'ascend', 'up', 'spinwise', 'forward', 'left', 'east', 'outside', 'slide', 'descend', 'north', 'north', 'spinwise', 'stutter', 'left', 'spinwise', 'slide', 'ascend', 'ascend', 'ascend', 'east', 'south', 'east', 'forward', 'descend', 'left', 'stutter', 'forward', 'outside', 'slide', 'north', 'east', 'left', 'spinwise', 'forward', 'ascend', 'forward', 'ascend', 'stutter', 'widdershins', 'down', 'left', 'slide', 'descend', 'descend', 'spinwise', 'east', 'descend', 'spinwise', 'forward', 'ascend', 'slide', 'south', 'widdershins', 'north', 'descend', 'east', 'ascend', 'left', 'forward', 'south', 'descend', 'ascend', 'east', 'slide', 'north', 'ascend', 'spinwise', 'spinwise', 'east', 'ascend', 'east', 'slide', 'ascend', 'forward', 'spinwise', 'forward', 'slide', 'ascend', 'east', 'ascend', 'left', 'ascend', 'left', 'descend', 'right', 'ascend', 'spinwise', 'left', 'spinwise', 'spinwise', 'stutter', 'left', 'inside', 'spinwise', 'spinwise', 'spinwise', 'ascend', 'stutter', 'forward', 'stutter', 'ascend', 'left', 'east', 'spinwise', 'ascend', 'west', 'outside', 'descend', 'forward', 'ascend', 'left', 'stutter', 'left', 'descend', 'right', 'widdershins', 'up', 'east', 'slide', 'ascend', 'slide', 'descend', 'descend', 'left', 'spinwise', 'widdershins', 'outside', 'left', 'stutter', 'descend', 'slide', 'ascend', 'left', 'ascend', 'slide', 'stutter', 'north', 'spinwise', 'spinwise', 'left', 'left', 'east', 'ascend', 'east', 'spinwise', 'up', 'descend', 'spinwise', 'ascend', 'spinwise', 'north', 'left', 'stutter', 'left', 'east', 'spinwise', 'forward', 'descend', 'descend', 'slide', 'outside', 'slide', 'south', 'slide', 'east', 'ascend', 'descend', 'left', 'slide', 'east', 'spinwise', 'east', 'ascend', 'ascend', 'left', 'inside', 'inside', 'east', 'east', 'south', 'up', 'left', 'stutter', 'descend', 'left', 'descend', 'left', 'left', 'descend', 'inside', 'ascend', 'right', 'east', 'left', 'left', 'ascend', 'east', 'outside', 'east', 'east', 'up', 'left', 'left', 'ascend', 'spinwise', 'east', 'east', 'ascend', 'east', 'stutter', 'left', 'east', 'left', 'spinwise', 'spinwise', 'ascend', 'forward', 'ascend', 'south', 'left', 'forward', 'spinwise', 'north', 'descend', 'outside', 'descend', 'north', 'descend', 'ascend', 'left', 'slide', 'east', 'left', 'stutter', 'east', 'stutter', 'forward', 'east', 'descend', 'forward', 'ascend', 'ascend', 'east', 'down', 'up', 'east', 'east', 'stutter', 'north', 'west', 'left', 'left', 'north', 'spinwise', 'east', 'ascend', 'inside', 'north', 'forward', 'ascend', 'north', 'slide', 'slide', 'east', 'slide', 'left', 'descend', 'east', 'east', 'descend', 'spinwise', 'east', 'outside', 'ascend', 'east', 'east', 'east', 'stutter', 'ascend', 'descend', 'inside', 'left', 'stutter', 'ascend', 'descend', 'right', 'spinwise', 'left', 'east', 'north', 'slide', 'stutter', 'slide', 'descend', 'descend', 'forward', 'ascend', 'east', 'forward', 'forward', 'forward', 'ascend', 'descend', 'east', 'east', 'left', 'ascend', 'slide', 'south', 'outside', 'south', 'ascend', 'ascend', 'left', 'up', 'slide', 'spinwise', 'north', 'spinwise', 'inside', 'spinwise', 'ascend', 'east', 'inside', 'left', 'north', 'forward', 'spinwise', 'east', 'forward', 'north', 'ascend', 'stutter', 'ascend', 'up', 'forward', 'up', 'forward', 'forward', 'ascend', 'east', 'descend', 'left', 'east', 'ascend', 'backwards', 'east', 'east', 'inside', 'descend', 'right', 'north', 'descend', 'up', 'spinwise', 'spinwise', 'ascend', 'east', 'ascend', 'left', 'descend', 'left', 'descend', 'spinwise', 'spinwise', 'down', 'descend',
        'left', 'left', 'spinwise', 'slide', 'left', 'stutter', 'descend', 'west', 'east', 'left', 'east', 'forward', 'stutter', 'spinwise', 'east', 'east', 'forward', 'east', 'ascend', 'ascend', 'descend', 'widdershins', 'widdershins', 'east', 'east', 'left', 'spinwise', 'east', 'east', 'left', 'left', 'east', 'stutter', 'east', 'east', 'forward', 'ascend', 'left', 'up', 'north', 'east', 'east', 'forward', 'descend', 'north', 'east', 'left', 'ascend', 'widdershins', 'outside', 'spinwise', 'spinwise', 'forward', 'spinwise', 'east', 'descend', 'up', 'descend', 'descend', 'forward', 'outside', 'left', 'east', 'forward', 'north', 'forward', 'east', 'left', 'east', 'east', 'ascend', 'spinwise', 'spinwise', 'east', 'ascend', 'south', 'spinwise', 'ascend', 'ascend', 'down', 'east', 'descend', 'stutter', 'backwards', 'ascend', 'inside', 'east', 'stutter', 'down', 'stutter', 'stutter', 'up', 'ascend', 'north', 'ascend', 'spinwise', 'spinwise', 'outside', 'descend', 'west', 'inside', 'left', 'outside', 'ascend', 'stutter', 'up', 'ascend', 'left', 'west', 'south', 'outside', 'ascend', 'left', 'descend', 'west', 'spinwise', 'ascend', 'east', 'left', 'inside', 'descend', 'east', 'descend', 'spinwise', 'ascend', 'descend', 'up', 'up', 'ascend', 'outside', 'east', 'ascend', 'spinwise', 'left', 'north', 'ascend', 'left', 'left', 'east', 'west', 'left', 'ascend', 'ascend', 'east', 'south', 'stutter', 'spinwise', 'stutter', 'east', 'spinwise', 'east', 'descend', 'forward', 'descend', 'east', 'east', 'outside', 'north', 'slide', 'spinwise', 'forward', 'ascend', 'east', 'east', 'left', 'outside', 'east', 'left', 'east', 'up', 'left', 'ascend', 'left', 'stutter', 'descend', 'outside', 'stutter', 'east', 'descend', 'stutter', 'ascend', 'ascend', 'forward', 'forward', 'spinwise', 'left', 'spinwise', 'east', 'east', 'south', 'forward', 'east', 'east', 'slide', 'east', 'slide', 'left', 'inside', 'south', 'spinwise', 'east', 'ascend', 'ascend', 'stutter', 'north', 'slide', 'ascend', 'left', 'forward', 'east', 'forward', 'spinwise', 'ascend', 'south', 'north', 'inside', 'east', 'south', 'north', 'slide', 'slide', 'east', 'south', 'spinwise', 'slide', 'descend', 'ascend', 'up', 'east', 'stutter', 'stutter', 'spinwise', 'north', 'stutter', 'south', 'east', 'down', 'south', 'south', 'ascend', 'left', 'forward', 'slide', 'east', 'outside', 'stutter', 'descend', 'east', 'slide', 'spinwise', 'ascend', 'east', 'descend', 'left', 'stutter', 'descend', 'spinwise', 'ascend', 'slide', 'ascend', 'east', 'slide', 'outside', 'ascend', 'east', 'south', 'ascend', 'ascend', 'ascend', 'ascend', 'descend', 'east', 'forward', 'outside', 'slide', 'up', 'descend', 'descend', 'north', 'left', 'ascend', 'stutter', 'forward', 'spinwise', 'ascend', 'ascend', 'up', 'east', 'descend', 'descend', 'outside', 'stutter', 'east', 'left', 'stutter', 'widdershins', 'east', 'ascend', 'spinwise', 'forward', 'descend', 'east', 'stutter', 'inside', 'south', 'spinwise', 'left', 'slide', 'south', 'ascend', 'ascend', 'up', 'west', 'east', 'forward', 'south', 'slide', 'ascend', 'east', 'east', 'east', 'spinwise', 'spinwise', 'north', 'descend', 'ascend', 'east', 'up', 'forward', 'stutter', 'forward', 'forward', 'stutter', 'stutter', 'east', 'ascend', 'descend', 'slide', 'up', 'spinwise', 'descend', 'stutter', 'left', 'left', 'spinwise', 'stutter', 'spinwise', 'outside', 'backwards', 'up', 'spinwise', 'forward', 'stutter', 'east', 'north', 'forward', 'east', 'east', 'west', 'spinwise', 'stutter', 'widdershins', 'slide', 'east', 'forward', 'ascend', 'descend', 'left', 'spinwise', 'east', 'spinwise', 'slide', 'slide', 'east', 'spinwise', 'east', 'east', 'inside', 'left', 'forward', 'east', 'outside', 'ascend', 'east', 'left', 'up', 'forward', 'spinwise', 'outside', 'spinwise', 'descend', 'spinwise', 'north', 'up', 'descend', 'outside', 'up', 'left', 'north', 'descend', 'east', 'descend', 'widdershins', 'east', 'ascend', 'west', 'spinwise', 'descend', 'spinwise', 'ascend', 'stutter', 'ascend', 'ascend', 'inside', 'forward', 'spinwise', 'forward', 'forward', 'north', 'descend', 'east', 'east', 'east', 'outside', 'slide', 'slide', 'descend', 'descend', 'east', 'outside', 'slide', 'south', 'south', 'ascend', 'north', 'stutter', 'descend', 'stutter', 'north', 'spinwise', 'spinwise', 'left', 'slide', 'east', 'ascend', 'spinwise', 'east', 'slide', 'east', 'left', 'left', 'south', 'left', 'inside', 'east', 'forward', 'left', 'north', 'north', 'left', 'stutter', 'south', 'left', 'spinwise', 'west', 'left', 'ascend', 'slide', 'east', 'spinwise', 'slide', 'east', 'stutter', 'spinwise', 'stutter', 'widdershins', 'up', 'forward', 'spinwise', 'descend', 'slide', 'left', 'west', 'stutter', 'spinwise', 'spinwise', 'up', 'spinwise', 'south', 'east', 'descend', 'east', 'spinwise', 'stutter', 'inside', 'ascend', 'east', 'inside', 'north', 'spinwise', 'north', 'descend', 'spinwise', 'outside', 'east', 'spinwise', 'east', 'ascend', 'ascend', 'east', 'east', 'stutter', 'left', 'up', 'descend', 'spinwise', 'descend', 'south', 'slide', 'down', 'left', 'stutter', 'ascend', 'west', 'north', 'north', 'left', 'ascend', 'stutter', 'spinwise', 'up', 'up', 'spinwise', 'ascend', 'south', 'right', 'outside', 'west', 'inside', 'east', 'east', 'stutter', 'forward', 'ascend', 'left', 'ascend', 'descend', 'forward', 'descend', 'forward', 'north', 'forward', 'descend', 'stutter', 'south', 'inside', 'spinwise', 'stutter', 'east', 'east', 'left', 'left', 'north', 'spinwise', 'left', 'ascend', 'left', 'north', 'descend', 'forward', 'east', 'ascend', 'ascend', 'ascend', 'descend', 'left', 'west', 'descend', 'spinwise', 'east', 'spinwise', 'right', 'forward', 'outside', 'forward', 'ascend', 'east', 'spinwise', 'east', 'east', 'descend', 'east', 'ascend', 'spinwise', 'stutter', 'north', 'ascend', 'descend', 'forward', 'stutter', 'inside', 'slide', 'ascend', 'forward', 'forward', 'ascend', 'east', 'ascend', 'north', 'descend', 'south', 'north', 'stutter', 'spinwise', 'slide', 'north', 'left', 'ascend', 'east', 'up', 'east', 'east', 'ascend', 'ascend', 'left', 'north', 'slide', 'south', 'spinwise', 'west', 'east', 'east', 'east', 'south', 'ascend', 'ascend', 'ascend', 'east', 'left', 'east', 'spinwise', 'spinwise', 'forward', 'north', 'east', 'slide', 'east', 'slide', 'east', 'east', 'inside', 'forward', 'north', 'east', 'descend', 'north', 'up', 'widdershins', 'forward', 'spinwise', 'left', 'slide', 'east', 'east', 'forward', 'slide', 'ascend', 'left', 'ascend', 'outside', 'forward', 'ascend', 'ascend', 'spinwise', 'left', 'east', 'slide', 'spinwise', 'ascend', 'left', 'east', 'slide', 'descend', 'spinwise', 'up', 'east', 'ascend', 'south', 'descend', 'west', 'slide', 'north', 'spinwise', 'outside', 'spinwise', 'ascend', 'north', 'north', 'left', 'north', 'east', 'spinwise', 'left', 'backwards', 'south', 'left', 'left', 'forward', 'stutter', 'descend', 'down', 'outside', 'slide', 'stutter', 'ascend', 'east', 'spinwise', 'ascend', 'north', 'left', 'north', 'descend', 'spinwise', 'slide', 'slide', 'ascend', 'inside', 'left', 'west', 'ascend', 'stutter', 'descend', 'spinwise', 'ascend', 'left', 'descend', 'descend', 'spinwise', 'slide', 'ascend', 'west', 'north', 'west', 'north', 'west', 'left', 'east', 'ascend', 'south', 'widdershins', 'spinwise', 'slide', 'east', 'spinwise', 'descend', 'slide', 'descend', 'east', 'slide', 'stutter', 'spinwise', 'ascend', 'west', 'outside', 'widdershins', 'east', 'stutter', 'left', 'spinwise', 'left', 'ascend', 'inside', 'down', 'east', 'left', 'descend', 'slide', 'up', 'spinwise', 'ascend', 'backwards', 'east', 'stutter', 'spinwise', 'up', 'ascend', 'north', 'widdershins', 'ascend', 'north', 'south', 'stutter', 'north', 'left', 'east', 'descend', 'outside', 'descend', 'slide', 'spinwise', 'widdershins', 'backwards', 'ascend', 'spinwise', 'west', 'north', 'north', 'left', 'widdershins', 'north', 'ascend', 'slide', 'descend', 'spinwise', 'left', 'spinwise', 'forward', 'widdershins', 'up', 'down', 'north', 'east', 'east', 'north', 'south', 'forward', 'stutter', 'east', 'south', 'ascend', 'descend', 'right', 'ascend', 'spinwise', 'stutter', 'south', 'up', 'left', 'forward', 'east', 'slide', 'spinwise', 'spinwise', 'stutter', 'north', 'spinwise', 'down', 'descend', 'descend', 'slide', 'descend', 'left', 'north', 'north', 'left', 'forward', 'stutter', 'ascend', 'ascend', 'slide', 'inside', 'spinwise', 'south', 'east', 'slide', 'south', 'stutter', 'west', 'left', 'left', 'stutter', 'descend', 'east', 'descend', 'east', 'left', 'slide', 'left', 'east', 'east', 'east', 'stutter', 'descend', 'left', 'left', 'spinwise', 'right', 'ascend', 'stutter', 'east', 'up', 'ascend', 'outside', 'stutter', 'ascend', 'east', 'up', 'east', 'ascend', 'north', 'north', 'ascend', 'spinwise', 'ascend', 'north', 'east', 'left', 'descend', 'forward', 'forward', 'slide', 'outside', 'right', 'outside', 'descend', 'east', 'left', 'ascend', 'widdershins', 'ascend', 'up', 'forward', 'outside', 'spinwise', 'east', 'east', 'east', 'stutter', 'left', 'left', 'south', 'spinwise', 'forward', 'up', 'ascend', 'north', 'left', 'east', 'left', 'forward', 'slide', 'inside', 'forward', 'stutter', 'spinwise', 'east', 'descend', 'outside', 'left', 'slide', 'north', 'north', 'left',
        'spinwise', 'west', 'right', 'east', 'ascend', 'slide', 'left', 'spinwise', 'outside', 'east', 'ascend', 'forward', 'outside', 'north', 'east', 'ascend', 'descend', 'spinwise', 'east', 'inside', 'left', 'ascend', 'ascend', 'east', 'south', 'descend', 'stutter', 'backwards', 'south', 'up', 'up', 'spinwise', 'ascend', 'ascend', 'left', 'up', 'slide', 'ascend', 'east', 'south', 'outside', 'south', 'left', 'slide', 'stutter', 'down', 'ascend', 'forward', 'up', 'descend', 'west', 'slide', 'ascend', 'ascend', 'slide', 'slide', 'up', 'backwards', 'descend', 'stutter', 'up', 'ascend', 'left', 'ascend', 'forward', 'east', 'east', 'left', 'east', 'backwards', 'stutter', 'left', 'east', 'east', 'slide', 'east', 'north', 'forward', 'ascend', 'north', 'spinwise', 'forward', 'descend', 'outside', 'descend', 'east', 'stutter', 'left', 'south', 'east', 'descend', 'right', 'spinwise', 'east', 'stutter', 'forward', 'north', 'descend', 'slide', 'forward', 'slide', 'backwards', 'ascend', 'stutter', 'right', 'stutter', 'down', 'ascend', 'stutter', 'spinwise', 'slide', 'up', 'spinwise', 'east', 'ascend', 'ascend', 'ascend', 'backwards', 'descend', 'spinwise', 'slide', 'stutter', 'south', 'east', 'stutter', 'ascend', 'east', 'descend', 'left', 'forward', 'slide', 'descend', 'descend', 'spinwise', 'right', 'left', 'forward', 'spinwise', 'ascend', 'widdershins', 'right', 'forward', 'up', 'ascend', 'left', 'left', 'east', 'left', 'outside', 'left', 'forward', 'descend', 'slide', 'spinwise', 'spinwise', 'descend', 'forward', 'stutter', 'ascend', 'north', 'left', 'backwards', 'inside', 'east', 'descend', 'west', 'descend', 'ascend', 'east', 'forward', 'left', 'east', 'left', 'up', 'descend', 'slide', 'descend', 'forward', 'slide', 'south', 'ascend', 'spinwise', 'stutter', 'down', 'outside', 'left', 'descend', 'forward', 'spinwise', 'left', 'outside', 'backwards', 'backwards', 'spinwise', 'spinwise', 'up', 'slide', 'ascend', 'spinwise', 'ascend', 'widdershins', 'forward', 'ascend', 'spinwise', 'descend', 'descend', 'widdershins', 'widdershins', 'slide', 'south', 'right', 'stutter', 'stutter', 'south', 'outside', 'forward', 'spinwise', 'descend', 'north', 'south', 'stutter', 'ascend', 'slide', 'left', 'ascend', 'slide', 'up', 'forward', 'spinwise', 'spinwise', 'slide', 'spinwise', 'descend', 'left', 'descend', 'up', 'east', 'stutter', 'spinwise', 'forward', 'left', 'left', 'east', 'outside', 'north', 'east', 'south', 'left', 'east', 'east', 'ascend', 'ascend', 'stutter', 'north', 'forward', 'ascend', 'backwards', 'up', 'left', 'south', 'slide', 'ascend', 'ascend', 'descend', 'forward', 'stutter', 'ascend', 'slide', 'forward', 'forward', 'ascend', 'backwards', 'ascend', 'east', 'slide', 'slide', 'widdershins', 'east', 'south', 'spinwise', 'west', 'up', 'stutter', 'ascend', 'east', 'slide', 'ascend', 'widdershins', 'inside', 'ascend', 'east', 'forward', 'left', 'ascend', 'south', 'left', 'backwards', 'spinwise', 'slide', 'north', 'spinwise', 'inside', 'left', 'south', 'ascend', 'descend', 'backwards', 'spinwise', 'spinwise', 'forward', 'south', 'ascend', 'left', 'slide', 'spinwise', 'left', 'ascend', 'descend', 'left', 'forward', 'ascend', 'left', 'east', 'east', 'east', 'spinwise', 'east', 'south', 'south', 'spinwise', 'spinwise', 'north', 'east', 'ascend', 'descend', 'left', 'ascend', 'forward', 'up', 'widdershins', 'south', 'west', 'slide', 'spinwise', 'right', 'forward', 'south', 'up', 'ascend', 'right', 'spinwise', 'east', 'slide', 'inside', 'left', 'forward', 'outside', 'left', 'stutter', 'north', 'forward', 'east', 'east', 'forward', 'right', 'west', 'ascend', 'ascend', 'ascend', 'east', 'south', 'descend', 'down', 'inside', 'east', 'descend', 'stutter', 'forward', 'descend', 'ascend', 'descend', 'spinwise', 'forward', 'ascend', 'east', 'east', 'ascend', 'descend', 'east', 'forward', 'spinwise', 'spinwise', 'ascend', 'ascend', 'descend', 'forward', 'north', 'outside', 'east', 'east', 'north', 'inside', 'left', 'spinwise', 'left', 'descend', 'left', 'slide', 'ascend', 'outside', 'south', 'west', 'east', 'left', 'descend', 'spinwise', 'ascend', 'east', 'descend', 'east', 'up', 'east', 'descend', 'east', 'east', 'inside', 'forward', 'north', 'ascend', 'slide', 'left', 'forward', 'east', 'descend', 'inside', 'slide', 'left', 'ascend', 'south', 'east', 'left', 'east', 'south', 'spinwise', 'stutter', 'east', 'up', 'left', 'ascend', 'left', 'east', 'inside', 'spinwise', 'descend', 'left', 'ascend', 'ascend', 'slide', 'slide', 'up', 'spinwise', 'ascend', 'left', 'spinwise', 'stutter', 'stutter', 'left', 'widdershins', 'inside', 'left', 'left', 'left', 'inside', 'east', 'spinwise', 'descend', 'descend', 'slide', 'right', 'north', 'inside', 'descend', 'slide', 'right', 'stutter', 'inside', 'up', 'inside', 'descend', 'outside', 'outside', 'ascend', 'spinwise', 'ascend', 'up', 'spinwise', 'east', 'forward', 'east', 'spinwise', 'left', 'east', 'spinwise', 'ascend', 'left', 'spinwise', 'east', 'ascend', 'spinwise', 'stutter', 'ascend', 'east', 'forward', 'ascend', 'east', 'east', 'spinwise', 'east', 'south', 'down', 'descend', 'widdershins', 'inside', 'ascend',
            'south', 'up', 'east', 'east', 'forward', 'north', 'forward', 'left', 'descend', 'descend', 'right', 'west', 'slide', 'north', 'east', 'left', 'right', 'left', 'east', 'ascend', 'left', 'left', 'spinwise', 'ascend', 'up', 'spinwise', 'north', 'ascend', 'stutter', 'east', 'spinwise', 'north', 'forward', 'inside', 'ascend', 'right', 'forward', 'up', 'forward', 'south', 'right', 'ascend', 'ascend', 'east', 'forward', 'up', 'ascend', 'stutter', 'inside', 'forward', 'south', 'descend', 'left', 'spinwise', 'left', 'east', 'spinwise', 'east', 'ascend', 'inside', 'east', 'slide', 'up', 'south', 'ascend', 'spinwise', 'slide', 'east', 'east', 'left', 'left', 'spinwise', 'spinwise', 'backwards', 'east', 'ascend', 'south', 'outside', 'ascend', 'ascend', 'spinwise', 'stutter', 'descend', 'backwards', 'slide', 'east', 'forward', 'south', 'spinwise', 'spinwise', 'spinwise', 'south', 'descend', 'forward', 'north', 'ascend', 'stutter', 'south', 'stutter', 'south', 'stutter', 'east', 'ascend', 'slide', 'slide', 'inside', 'forward', 'stutter', 'south', 'slide', 'descend', 'forward', 'east', 'ascend', 'descend', 'left', 'east', 'ascend', 'forward', 'left', 'south', 'slide', 'up', 'north', 'left', 'east', 'spinwise', 'ascend', 'east', 'inside', 'right', 'ascend', 'forward', 'left', 'spinwise', 'descend', 'forward', 'forward', 'spinwise', 'outside', 'left', 'descend', 'inside', 'spinwise', 'left', 'left', 'ascend', 'up', 'south', 'left', 'spinwise', 'left', 'slide', 'east', 'ascend', 'spinwise', 'descend', 'forward', 'outside', 'south', 'ascend', 'slide', 'east', 'north', 'ascend', 'stutter', 'east', 'ascend', 'slide', 'ascend', 'right', 'descend', 'west', 'north', 'forward', 'slide', 'inside', 'north', 'left', 'descend', 'slide', 'left', 'north', 'spinwise', 'left', 'widdershins', 'forward', 'south', 'descend', 'north', 'ascend', 'north', 'ascend', 'east', 'left', 'forward', 'up', 'widdershins', 'widdershins', 'stutter', 'spinwise', 'up', 'spinwise', 'descend', 'descend', 'east', 'ascend', 'slide', 'forward', 'stutter', 'stutter', 'east', 'ascend', 'descend', 'up', 'left', 'inside', 'inside', 'stutter', 'stutter', 'south', 'ascend', 'backwards', 'east', 'left', 'east', 'east', 'outside', 'widdershins', 'backwards', 'south', 'spinwise', 'spinwise', 'left', 'left', 'east', 'ascend', 'slide', 'left', 'east', 'descend', 'backwards', 'stutter', 'north', 'descend', 'descend', 'left', 'stutter', 'widdershins', 'ascend', 'ascend', 'descend', 'stutter', 'right', 'stutter', 'ascend', 'descend', 'left', 'ascend', 'left', 'forward', 'east', 'forward', 'east', 'outside', 'stutter', 'south', 'ascend', 'forward', 'ascend', 'stutter', 'forward', 'west', 'descend', 'east', 'east', 'inside', 'slide', 'stutter', 'ascend', 'north', 'south', 'spinwise', 'inside', 'slide', 'slide', 'backwards', 'right', 'ascend', 'outside', 'east', 'up', 'slide', 'west', 'south', 'inside', 'south', 'spinwise', 'slide', 'north', 'left', 'east', 'descend', 'west', 'left', 'outside', 'ascend', 'west', 'slide', 'descend', 'outside', 'ascend', 'widdershins', 'spinwise', 'inside', 'right', 'right', 'forward', 'spinwise', 'up', 'descend', 'inside', 'left', 'east', 'east', 'south', 'ascend', 'outside', 'ascend', 'left', 'forward', 'north', 'stutter', 'forward', 'slide', 'left', 'slide', 'forward', 'up', 'slide', 'forward', 'stutter', 'stutter', 'stutter', 'descend', 'stutter', 'forward', 'descend', 'south', 'left', 'descend', 'north', 'north', 'ascend', 'left', 'forward', 'outside', 'stutter', 'inside', 'ascend', 'inside', 'east', 'stutter', 'spinwise', 'ascend', 'inside', 'ascend', 'north', 'spinwise', 'descend', 'up', 'north', 'north', 'east', 'up', 'right', 'spinwise', 'slide', 'spinwise', 'south', 'north', 'north', 'forward', 'descend', 'stutter', 'outside', 'ascend', 'east', 'left', 'spinwise', 'east', 'left', 'ascend', 'spinwise', 'north', 'ascend', 'spinwise', 'left', 'inside', 'down', 'east', 'ascend', 'east', 'inside', 'widdershins', 'ascend', 'slide', 'east', 'spinwise', 'north', 'spinwise', 'slide', 'widdershins', 'forward', 'inside', 'spinwise', 'slide', 'ascend', 'spinwise', 'ascend', 'forward', 'spinwise', 'east', 'up', 'ascend', 'descend', 'north', 'forward', 'left', 'spinwise', 'spinwise', 'outside', 'down', 'outside', 'stutter', 'ascend', 'spinwise', 'east', 'forward', 'forward', 'up', 'ascend', 'forward', 'east', 'west', 'up', 'south', 'backwards', 'left', 'forward', 'left', 'ascend', 'stutter', 'stutter', 'left', 'spinwise', 'north', 'ascend', 'outside', 'ascend', 'ascend', 'east', 'right', 'east', 'down', 'east', 'south', 'left', 'west', 'slide', 'right', 'south', 'ascend', 'east', 'spinwise', 'stutter', 'outside', 'left', 'spinwise', 'forward', 'descend', 'north', 'left', 'east', 'spinwise', 'spinwise', 'north', 'spinwise', 'east', 'ascend', 'left', 'descend', 'east', 'north', 'ascend', 'left', 'spinwise', 'descend', 'forward', 'left', 'backwards', 'left', 'east', 'forward', 'ascend', 'right', 'slide', 'ascend', 'ascend', 'ascend', 'slide', 'descend', 'south', 'spinwise', 'descend', 'left', 'ascend', 'outside', 'stutter', 'outside', 'spinwise', 'forward', 'ascend', 'outside', 'left', 'descend', 'east', 'ascend', 'spinwise', 'south', 'east', 'slide', 'spinwise', 'right', 'left', 'slide', 'left', 'spinwise', 'outside', 'forward', 'ascend', 'descend', 'spinwise', 'inside', 'up', 'north', 'widdershins', 'forward', 'ascend', 'east', 'inside', 'east', 'stutter', 'south', 'east', 'slide', 'left', 'backwards', 'ascend', 'stutter', 'spinwise', 'stutter', 'spinwise', 'outside', 'descend', 'left', 'stutter', 'north', 'spinwise', 'east', 'left', 'east', 'ascend', 'slide', 'outside', 'west', 'left', 'ascend', 'forward', 'slide', 'spinwise', 'left', 'ascend', 'descend', 'stutter', 'left', 'forward', 'inside', 'forward', 'east', 'slide', 'spinwise', 'slide', 'slide', 'east', 'east', 'right', 'ascend', 'spinwise', 'west', 'west', 'east', 'outside', 'descend', 'east', 'spinwise', 'ascend', 'east', 'ascend', 'forward', 'spinwise', 'forward', 'forward', 'east', 'ascend', 'up', 'forward', 'stutter', 'backwards', 'left', 'forward', 'descend', 'ascend', 'north', 'outside', 'south', 'outside', 'north', 'north', 'inside', 'south', 'spinwise', 'left', 'spinwise', 'spinwise', 'slide', 'north', 'outside', 'left', 'east', 'south', 'left', 'east', 'slide', 'descend', 'forward', 'left', 'right', 'west', 'spinwise', 'up', 'left', 'west', 'south', 'outside', 'up', 'east', 'ascend', 'outside', 'east', 'backwards', 'slide', 'ascend', 'forward', 'down', 'outside', 'north', 'ascend', 'ascend', 'east', 'north', 'stutter', 'spinwise', 'up', 'inside', 'left', 'east', 'forward', 'descend', 'spinwise', 'left', 'ascend', 'spinwise', 'east', 'east', 'left', 'forward', 'forward', 'descend', 'slide', 'ascend', 'up', 'descend', 'spinwise', 'ascend', 'inside', 'ascend', 'slide', 'east', 'south', 'up', 'backwards', 'east', 'ascend', 'east', 'left', 'outside', 'spinwise', 'up', 'north', 'slide', 'down', 'forward', 'forward', 'down', 'spinwise', 'descend', 'descend', 'south', 'ascend', 'up', 'widdershins', 'stutter', 'up', 'north', 'north']
        self.assertEqual(actual, expected)

# unittest.main(verbosity=2)

if __name__ == "__main__":
    data_folder = Path("/home/mauratee/src/mazes-takehome/src/samples/")
    file_to_open = data_folder / "simple.maze"
    # file_to_open = data_folder / "generated100.maze"
    # file_to_open = data_folder / "generated1000.maze"
    # file_to_open = data_folder / "generatedLong2.maze"
    # file_to_open = data_folder / "generatedsparse.maze"

    MazeLoader()

    unittest.main(verbosity=2)



# call sample mazes in Command Line:
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/simple.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generated100.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generated1000.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLarge.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLong2.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedLong.maze
# python3 MazeLoader.py /home/mauratee/src/mazes-takehome/src/samples/generatedsparse.maze




