import json
import random
import os
from datetime import datetime
# =====================
python_questions = [
    # Easy: 1–10
    {"id":1, "subject":"python","difficulty":"easy","question":"What is Python?","options":["A snake","A programming language","A car","A fruit"],"answer":"A programming language","explanation":"Python is a high-level programming language."},
    {"id":2, "subject":"python","difficulty":"easy","question":"Which symbol is used for comments in Python?","options":["//","/* */","#","<>"],"answer":"#","explanation":"The '#' symbol is used for single-line comments in Python."},
    {"id":3, "subject":"python","difficulty":"easy","question":"What does the len() function do?","options":["Counts items","Adds numbers","Deletes items","Prints text"],"answer":"Counts items","explanation":"len() returns the number of items in an object."},
    {"id":4, "subject":"python","difficulty":"easy","question":"Which of these is a valid Python variable name?","options":["1var","var_name","var-name","var name"],"answer":"var_name","explanation":"Variable names cannot start with a number or contain spaces or hyphens."},
    {"id":5, "subject":"python","difficulty":"easy","question":"What is the output of print(2 + 3 * 4)?","options":["20","14","24","None"],"answer":"14","explanation":"Python follows operator precedence: 3*4=12, then 2+12=14."},
    {"id":6, "subject":"python","difficulty":"easy","question":"Which data type is immutable in Python?","options":["List","Dictionary","Tuple","Set"],"answer":"Tuple","explanation":"Tuples cannot be changed after creation; lists, dicts, and sets are mutable."},
    {"id":7, "subject":"python","difficulty":"easy","question":"How do you start a for loop in Python?","options":["for i in range(5):","for(i=0;i<5;i)","for i=1 to 5","foreach i in range"],"answer":"for i in range(5):","explanation":"Python uses 'for variable in iterable:' syntax."},
    {"id":8, "subject":"python","difficulty":"easy","question":"What does the 'break' statement do?","options":["Exits the loop","Skips iteration","Repeats the loop","Stops the program"],"answer":"Exits the loop","explanation":"The 'break' statement immediately terminates the loop."},
    {"id":9, "subject":"python","difficulty":"easy","question":"Which keyword is used to define a function in Python?","options":["function","def","fun","define"],"answer":"def","explanation":"Functions are defined using 'def' keyword."},
    {"id":10, "subject":"python","difficulty":"easy","question":"How do you check the type of a variable?","options":["type(var)","check(var)","var.type()","var.class"],"answer":"type(var)","explanation":"The type() function returns the data type of a variable."},

    # Medium: 11–20
    {"id":11, "subject":"python","difficulty":"medium","question":"Which method adds an element to the end of a list?","options":["append()","insert()","add()","extend()"],"answer":"append()","explanation":"list.append(x) adds x at the end of the list."},
    {"id":12, "subject":"python","difficulty":"medium","question":"What is the output of 'Hello'[::-1]?","options":["Hello","olleH","H","Error"],"answer":"olleH","explanation":"The slicing [::-1] reverses the string."},
    {"id":13, "subject":"python","difficulty":"medium","question":"Which of these is a mutable data type?","options":["String","Tuple","List","Integer"],"answer":"List","explanation":"Lists can be changed after creation; strings, tuples, and integers cannot."},
    {"id":14, "subject":"python","difficulty":"medium","question":"What is the output of bool('False')?","options":["False","True","0","Error"],"answer":"True","explanation":"Non-empty strings are True in Python, even if the content is 'False'."},
    {"id":15, "subject":"python","difficulty":"medium","question":"Which operator is used for floor division?","options":["/","//","%","**"],"answer":"//","explanation":"The // operator divides and returns the integer part only."},{"id":16, "subject":"python","difficulty":"medium","question":"How do you handle exceptions in Python?","options":["try-except","catch","error-handling","do-except"],"answer":"try-except","explanation":"Python uses try-except blocks for exception handling."},
    {"id":17, "subject":"python","difficulty":"medium","question":"Which of these creates a set in Python?","options":["{}","[]","()","set()"],"answer":"set()","explanation":"set() creates a set; {} creates a dict unless empty."},
    {"id":18, "subject":"python","difficulty":"medium","question":"What is the difference between '==' and 'is'?","options":["No difference","'==' compares values, 'is' compares identities","'==' compares types, 'is' compares values","'==' is faster than 'is'"],"answer":"'==' compares values, 'is' compares identities","explanation":"'==' checks value equality, 'is' checks if objects are the same in memory."},
    {"id":19, "subject":"python","difficulty":"medium","question":"Which function converts a string to lowercase?","options":["str.lower()","str.upcase()","str.toLower()","lower()"],"answer":"str.lower()","explanation":"The str.lower() method returns the lowercase version of the string."},
    {"id":20, "subject":"python","difficulty":"medium","question":"How can you remove whitespace from both ends of a string?","options":["strip()","trim()","remove()","clean()"],"answer":"strip()","explanation":"The strip() method removes leading and trailing whitespace."},

    # Hard: 21–30
    {"id":21, "subject":"python","difficulty":"hard","question":"Which of these is a Python comprehension?","options":["[x for x in range(5)]","for x in range(5):","while x<5:","list(x)"],"answer":"[x for x in range(5)]","explanation":"List comprehensions provide a concise way to create lists."},
    {"id":22, "subject":"python","difficulty":"hard","question":"What is a Python generator?","options":["A function returning list","A function returning iterator","A variable type","A module"],"answer":"A function returning iterator","explanation":"Generators yield items lazily using 'yield' keyword."},
    {"id":23, "subject":"python","difficulty":"hard","question":"Which module allows you to work with regular expressions?","options":["re","regex","expr","pyregex"],"answer":"re","explanation":"The 're' module handles regular expressions in Python."},
    {"id":24, "subject":"python","difficulty":"hard","question":"What does the 'with' statement do?","options":["Handles exceptions","Simplifies file handling","Loops over items","Creates class"],"answer":"Simplifies file handling","explanation":"The 'with' statement is used for context management (like files)."},
    {"id":25, "subject":"python","difficulty":"hard","question":"What is the output of 0.1 + 0.2 == 0.3?","options":["True","False","Error","0.3"],"answer":"False","explanation":"Floating point arithmetic is not exact in Python."},
    {"id":26, "subject":"python","difficulty":"hard","question":"Which function is used to get the ASCII code of a character?","options":["ord()","ascii()","chr()","code()"],"answer":"ord()","explanation":"ord() returns the Unicode/ASCII code of a character."},
    {"id":27, "subject":"python","difficulty":"hard","question":"What is the difference between deep copy and shallow copy?","options":["No difference","Deep copies objects recursively, shallow copies references","Shallow copies recursively, deep copies references","Deep copy is faster"],"answer":"Deep copies objects recursively, shallow copies references","explanation":"Deep copy duplicates objects, shallow copy duplicates references."},
    {"id":28, "subject":"python","difficulty":"hard","question":"Which keyword is used to create a class?","options":["class","def","object","struct"],"answer":"class","explanation":"Classes are defined using 'class' keyword."},{"id":29, "subject":"python","difficulty":"hard","question":"What is the purpose of init method?","options":["Destructor","Initializer/Constructor","Class variable","Private method"],"answer":"Initializer/Constructor","explanation":"init is called when an object is created to initialize it."},
    {"id":30, "subject":"python","difficulty":"hard","question":"Which of these is NOT a Python data structure?","options":["List","Stack","Dictionary","Tuple"],"answer":"Stack","explanation":"Stack is a data structure concept, not a built-in Python type."},

 
    {"id":31,"subject":"python","difficulty":"easy","question":"What is the output of print((2 + 3) * 4)?","options":["14","20","24","None"],"answer":"20","explanation":"Brackets have priority: (2+3)=5, then 5*4=20."},
    {"id":32,"subject":"python","difficulty":"easy","question":"What does the % operator do?","options":["Division","Floor division","Returns remainder","Exponent"],"answer":"Returns remainder","explanation":"The % operator returns the remainder after division."},
    {"id":33,"subject":"python","difficulty":"easy","question":"What is the output of 9 // 2?","options":["4","4.5","5","Error"],"answer":"4","explanation":"Floor division returns the integer part only."},
    {"id":34,"subject":"python","difficulty":"easy","question":"What is the output of len('Hi there')?","options":["7","8","9","Error"],"answer":"8","explanation":"Spaces are counted in string length."},
    {"id":35,"subject":"python","difficulty":"easy","question":"Which function adds an element to the end of a list?","options":["add()","append()","insert()","extend()"],"answer":"append()","explanation":"append() adds one element to the end of a list."},
    {"id":36,"subject":"python","difficulty":"easy","question":"What does the input() function do?","options":["Prints output","Takes user input","Stops program","Converts data"],"answer":"Takes user input","explanation":"input() collects data entered by the user."},
    {"id":37,"subject":"python","difficulty":"easy","question":"What is the output of min([3, 1, 5])?","options":["1","3","5","Error"],"answer":"1","explanation":"min() returns the smallest value."},
    {"id":38,"subject":"python","difficulty":"easy","question":"What is the output of max([2, 8, 4])?","options":["2","4","8","Error"],"answer":"8","explanation":"max() returns the largest value."},
    {"id":39,"subject":"python","difficulty":"easy","question":"What keyword is used to repeat code multiple times?","options":["repeat","loop","for","run"],"answer":"for","explanation":"for loops are used for iteration."},
    {"id":40,"subject":"python","difficulty":"easy","question":"What does the in keyword check?","options":["Index","Membership","Length","Type"],"answer":"Membership","explanation":"'in' checks if a value exists in a sequence."},

    # Medium: 41–50
    {"id":41,"subject":"python","difficulty":"medium","question":"What is the output of 'Hello World'[5]?","options":["W","o","space","Error"],"answer":"space","explanation":"Index 5 refers to the space character."},
    {"id":42,"subject":"python","difficulty":"medium","question":"What does the find() function return if the value is not found?","options":["-1","0","None","Error"],"answer":"-1","explanation":"find() returns -1 when the substring is not found."},
    {"id":43,"subject":"python","difficulty":"medium","question":"What does insert(1, 'A') do in a list?","options":["Adds at end","Adds at index 1","Replaces value","Deletes element"],"answer":"Adds at index 1","explanation":"insert(index, value) adds at a specific position."},
    {"id":44,"subject":"python","difficulty":"medium","question":"What does pop() do in a list?","options":["Adds element","Removes last element","Clears list","Sorts list"],"answer":"Removes last element","explanation":"pop() removes and returns the last element by default."},
    {"id":45,"subject":"python","difficulty":"medium","question":"What is the output of sum([1, 2, 3])?","options":["5","6","7","Error"],"answer":"6","explanation":"sum() adds all elements in the list."},
    {"id":46,"subject":"python","difficulty":"medium","question":"What does range(3) produce?","options":["1,2,3","0,1,2","0,1,2,3","Error"],"answer":"0,1,2","explanation":"range(3) starts at 0 and stops before 3."},
    {"id":47,"subject":"python","difficulty":"medium","question":"What does remove(3) do in a list?","options":["Removes index 3","Removes value 3","Deletes list","Raises error always"],"answer":"Removes value 3","explanation":"remove() deletes the first occurrence of the value."},
    {"id":48,"subject":"python","difficulty":"medium","question":"What is the output of len([1, 2, 3, 4])?","options":["3","4","5","Error"],"answer":"4","explanation":"len() counts the number of elements."},
    {"id":49,"subject":"python","difficulty":"medium","question":"What does sort() do to a list?","options":["Reverses list","Sorts list","Deletes duplicates","Returns new list"],"answer":"Sorts list","explanation":"sort() arranges elements in ascending order."},
    {"id":50,"subject":"python","difficulty":"medium","question":"What does reverse() do?","options":["Sorts list","Reverses order","Deletes list","Creates copy"],"answer":"Reverses order","explanation":"reverse() changes the list order."},

    # Hard: 51–60
    {"id":51,"subject":"python","difficulty":"hard","question":"What is the output of (10 + 2) // (2 * 3)?","options":["2","3","4","Error"],"answer":"2","explanation":"Brackets first: (10+2)=12, (2*3)=6, 12//6=2."},
    {"id":52,"subject":"python","difficulty":"hard","question":"What is the output of 'Data Science'[4]?","options":["S","space","a","Error"],"answer":"space","explanation":"Index 4 refers to the space character."},
    {"id":53,"subject":"python","difficulty":"hard","question":"What happens if pop(1) is used?","options":["Removes first item","Removes item at index 1","Deletes list","Error"],"answer":"Removes item at index 1","explanation":"pop(index) removes element at that index."},
    {"id":54,"subject":"python","difficulty":"hard","question":"Which condition stops a while loop from running infinitely?","options":["break","False condition","continue","pass"],"answer":"False condition","explanation":"A while loop stops when its condition becomes False."},
    {"id":55,"subject":"python","difficulty":"hard","question":"What does while True do?","options":["Stops loop","Runs once","Runs infinitely","Error"],"answer":"Runs infinitely","explanation":"while True runs forever unless stopped."},
    {"id":56,"subject":"python","difficulty":"hard","question":"Which keyword can be used to stop a loop immediately?","options":["stop","end","break","exit"],"answer":"break","explanation":"break exits the loop instantly."},
    {"id":57,"subject":"python","difficulty":"hard","question":"What is the output of 17 % 5?","options":["2","3","4","5"],"answer":"2","explanation":"17 divided by 5 leaves remainder 2."},
    {"id":58,"subject":"python","difficulty":"hard","question":"What is the output of list(range(2, 7, 2))?","options":["[2,4,6]","[2,3,4,5,6]","[2,5]","Error"],"answer":"[2,4,6]","explanation":"range(start, stop, step) skips by step."},
    {"id":59,"subject":"python","difficulty":"hard","question":"What does input() return by default?","options":["Integer","Float","String","Boolean"],"answer":"String","explanation":"input() always returns a string unless converted."},
    {"id":60,"subject":"python","difficulty":"hard","question":"What is the output of len('A B C')?","options":["3","4","5","Error"],"answer":"5","explanation":"Spaces are counted in string length."}
    
]
new_python_set = [
    # Easy (65-70)
    {"id":65, "subject":"python","difficulty":"easy","question":"What is the correct way to create a list in Python?","options":["list = (1, 2)","list = [1, 2]","list = {1, 2}","list = <1, 2>"],"answer":"[1, 2]","explanation":"Lists are defined using square brackets []."},
    {"id":66, "subject":"python","difficulty":"easy","question":"Which function is used to convert a string to an integer?","options":["str()","int()","float()","convert()"],"answer":"int()","explanation":"The int() function parses a string into an integer if possible."},
    {"id":67, "subject":"python","difficulty":"easy","question":"What does the '*' operator do when used with a string and an integer (e.g., 'A' * 3)?","options":["Error","Adds 3 to A","Repeats the string 3 times","Square of the string"],"answer":"Repeats the string 3 times","explanation":"String multiplication repeats the string $n$ times."},
    {"id":68, "subject":"python","difficulty":"easy","question":"How do you add a comment that spans multiple lines?","options":["// Comment //","# Comment #","''' Comment '''","/* Comment */"],"answer":"''' Comment '''","explanation":"Triple quotes (''' or \"\"\") are used for multi-line strings/comments."},
    {"id":69, "subject":"python","difficulty":"easy","question":"Which method removes all items from a list?","options":["delete()","remove()","clear()","pop()"],"answer":"clear()","explanation":"list.clear() empties the entire list."},
    {"id":70, "subject":"python","difficulty":"easy","question":"What is the default value of a function that does not return anything?","options":["0","False","None","Error"],"answer":"None","explanation":"Python functions return None by default if no return statement is reached."},

    # Medium (71-77)
    {"id":71, "subject":"python","difficulty":"medium","question":"What is the output of print(0.1 + 0.2 == 0.3)?","options":["True","False","None","Error"],"answer":"False","explanation":"Floating-point precision issues make 0.1 + 0.2 slightly different from 0.3."},
    {"id":72, "subject":"python","difficulty":"medium","question":"How can you merge two dictionaries in Python 3.9+?","options":["dict1 + dict2","dict1.join(dict2)","dict1 | dict2","merge(dict1, dict2)"],"answer":"dict1 | dict2","explanation":"The union operator | was introduced for dictionaries in Python 3.9."},
    {"id":73, "subject":"python","difficulty":"medium","question":"What does 'self' represent in a class method?","options":["The class itself","The parent class","The instance of the object","A private variable"],"answer":"The instance of the object","explanation":"'self' refers to the specific object created from the class."},
    {"id":74, "subject":"python","difficulty":"medium","question":"Which of these is used to skip the current iteration of a loop?","options":["break","pass","skip","continue"],"answer":"continue","explanation":"continue jumps to the next cycle of the loop, skipping remaining code in current cycle."},
    {"id":75, "subject":"python","difficulty":"medium","question":"What is the purpose of the 'pass' statement?","options":["To skip an error","A placeholder for future code","To exit a function","To ignore a loop"],"answer":"A placeholder for future code","explanation":"'pass' is a null operation used where syntax requires a statement."},
    {"id":76, "subject":"python","difficulty":"medium","question":"Which built-in function can sort a list without modifying the original?","options":["list.sort()","sorted()","arrange()","order()"],"answer":"sorted()","explanation":"sorted() returns a new list, while list.sort() modifies the original list in place."},
    {"id":77, "subject":"python","difficulty":"medium","question":"What does the 'range(1, 10, 2)' function generate?","options":["1, 3, 5, 7, 9","1, 2, 3, ..., 10","2, 4, 6, 8, 10","1, 10, 2"],"answer":"1, 3, 5, 7, 9","explanation":"It starts at 1, stops before 10, with a step of 2."},

    # Hard (78-84)
    {"id":78, "subject":"python","difficulty":"hard","question":"What is a 'decorator' in Python?","options":["A GUI tool","A function that modifies another function","A class attribute","A type of loop"],"answer":"A function that modifies another function","explanation":"Decorators wrap a function to extend its behavior without changing its source code."},
    {"id":79, "subject":"python","difficulty":"hard","question":"How do you handle multiple exceptions in a single except block?","options":["except TypeError, ValueError:","except (TypeError, ValueError):","except TypeError | ValueError:","except all:"],"answer":"except (TypeError, ValueError):","explanation":"Multiple exceptions must be passed as a tuple."},
    {"id":80, "subject":"python","difficulty":"hard","question":"What is the difference between __str__ and __repr__?","options":["No difference","__str__ is for users, __repr__ is for developers","__repr__ is for users, __str__ is for developers","__str__ is only for strings"],"answer":"__str__ is for users, __repr__ is for developers","explanation":"__str__ is 'informal/readable', __repr__ is 'official/unambiguous' for debugging."},
    {"id":81, "subject":"python","difficulty":"hard","question":"What is 'Monkey Patching' in Python?","options":["A way to sort lists","Dynamic replacement of attributes at runtime","A method of testing","Using AI to write code"],"answer":"Dynamic replacement of attributes at runtime","explanation":"It refers to changing code behavior at runtime (e.g., swapping a method in a module)."},
    {"id":82, "subject":"python","difficulty":"hard","question":"Which module is used for deep copying objects?","options":["copy","clone","os","sys"],"answer":"copy","explanation":"The 'copy' module provides the deepcopy() function for nested objects."},
    {"id":83, "subject":"python","difficulty":"hard","question":"What is the output of print(list(map(lambda x: x*2, [1, 2, 3])))?","options":["[1, 2, 3]","[2, 4, 6]","[1, 4, 9]","Error"],"answer":"[2, 4, 6]","explanation":"The map function applies the lambda (multiply by 2) to every item in the list."},
    {"id":84, "subject":"python","difficulty":"hard","question":"What does the '__init__.py' file do in a directory?","options":["Speeds up the code","Deletes old data","Treats the directory as a package","Initializes the computer"],"answer":"Treats the directory as a package","explanation":"It allows you to import modules from that folder like a Python package."}
]
python_questions.extend(new_python_set)
dsa_questions = [
    # Easy: 1–4
    {"id":1,"subject":"dsa","difficulty":"easy","question":"What is a stack?","options":["FIFO","LIFO","Random","Sorted"],"answer":"LIFO","explanation":"Stack follows Last In First Out."},
    {"id":2,"subject":"dsa","difficulty":"easy","question":"What is a queue?","options":["FIFO","LIFO","Random","Sorted"],"answer":"FIFO","explanation":"Queue follows First In First Out."},
    {"id":3,"subject":"dsa","difficulty":"easy","question":"Which data structure uses keys and values?","options":["List","Dictionary","Set","Tuple"],"answer":"Dictionary","explanation":"Dictionaries store key-value pairs."},
    {"id":4,"subject":"dsa","difficulty":"easy","question":"Which data structure allows duplicates?","options":["Set","List","Dictionary","Queue"],"answer":"List","explanation":"Lists allow duplicates; sets do not."},

    # Medium: 5–7
    {"id":5,"subject":"dsa","difficulty":"medium","question":"What is the time complexity of binary search?","options":["O(n)","O(log n)","O(n^2)","O(1)"],"answer":"O(log n)","explanation":"Binary search splits the array each step, giving log n complexity."},
    {"id":6,"subject":"dsa","difficulty":"medium","question":"Which data structure is used in BFS traversal?","options":["Stack","Queue","Tree","Graph"],"answer":"Queue","explanation":"Breadth-First Search uses a queue."},
    {"id":7,"subject":"dsa","difficulty":"medium","question":"Which operation removes from a stack?","options":["Push","Pop","Insert","Delete"],"answer":"Pop","explanation":"Pop removes the top element from the stack."},

    # Hard: 8–10
    {"id":8,"subject":"dsa","difficulty":"hard","question":"What is the height of a balanced binary tree with n nodes?","options":["O(n)","O(log n)","O(1)","O(n^2)"],"answer":"O(log n)","explanation":"Height is logarithmic in a balanced binary tree."},
    {"id":9,"subject":"dsa","difficulty":"hard","question":"Which algorithm is used for shortest path in a graph?","options":["DFS","BFS","Dijkstra","Bubble sort"],"answer":"Dijkstra","explanation":"Dijkstra's algorithm finds the shortest path in weighted graphs."},
    {"id":10,"subject":"dsa","difficulty":"hard","question":"Which data structure is used in recursion?","options":["Queue","Stack","Heap","Array"],"answer":"Stack","explanation":"Recursion uses the call stack internally."}
]
new_dsa_set = [
    # Medium (11-15)
    {"id":11,"subject":"dsa","difficulty":"medium","question":"What is the time complexity of searching for an element in a sorted array using Binary Search?","options":["O(n)","O(log n)","O(n^2)","O(1)"],"answer":"O(log n)","explanation":"Binary Search halves the search space at each step, making it logarithmic."},
    {"id":12,"subject":"dsa","difficulty":"medium","question":"Which data structure is best for implementing a 'Back' button in a browser?","options":["Queue","Linked List","Stack","Hash Map"],"answer":"Stack","explanation":"A Stack uses Last-In-First-Out (LIFO) logic, perfect for reversing navigation steps."},
    {"id":13,"subject":"dsa","difficulty":"medium","question":"What is the space complexity of an array of size 'n'?","options":["O(1)","O(n)","O(log n)","O(n^2)"],"answer":"O(n)","explanation":"An array requires memory proportional to the number of elements it holds."},
    {"id":14,"subject":"dsa","difficulty":"medium","question":"Which sorting algorithm is known for its 'Divide and Conquer' approach?","options":["Bubble Sort","Selection Sort","Merge Sort","Insertion Sort"],"answer":"Merge Sort","explanation":"Merge Sort recursively divides the list into halves and merges them back in order."},
    {"id":15,"subject":"dsa","difficulty":"medium","question":"In a Linked List, what does a node typically contain?","options":["Data only","Pointer only","Data and a pointer to the next node","An index number"],"answer":"Data and a pointer to the next node","explanation":"Each node stores its value and the memory address of the next node in the sequence."},

    # Hard (16-20)
    {"id":16,"subject":"dsa","difficulty":"hard","question":"What is the worst-case time complexity of Quick Sort?","options":["O(n log n)","O(n)","O(n^2)","O(1)"],"answer":"O(n^2)","explanation":"If the pivot is always the smallest or largest element, Quick Sort degrades to quadratic time."},
    {"id":17,"subject":"dsa","difficulty":"hard","question":"Which data structure uses a Hash Function to map keys to values?","options":["Binary Tree","Hash Table / Dictionary","Stack","Queue"],"answer":"Hash Table / Dictionary","explanation":"Hash Tables use a function to compute an index into an array of buckets or slots."},
    {"id":18,"subject":"dsa","difficulty":"hard","question":"What is the time complexity of inserting an element at the beginning of a Python list?","options":["O(1)","O(n)","O(log n)","O(n^2)"],"answer":"O(n)","explanation":"Since all other elements must be shifted one position to the right, it takes linear time."},
    {"id":19,"subject":"dsa","difficulty":"hard","question":"What is a 'Circular Queue'?","options":["A queue that only accepts zeros","A queue where the last position is connected back to the first","A queue that never ends","A stack disguised as a queue"],"answer":"A queue where the last position is connected back to the first","explanation":"Circular Queues use memory more efficiently by reusing empty spaces at the front."},
    {"id":20,"subject":"dsa","difficulty":"hard","question":"Which traversal of a Binary Search Tree (BST) produces sorted output?","options":["Pre-order","In-order","Post-order","Level-order"],"answer":"In-order","explanation":"In-order traversal visits nodes in the order: Left, Root, Right, which results in sorted values for a BST."}
]
dsa_questions.extend(new_dsa_set)
# ==========================================================
# 2. THE LOGIC ENGINE (Functions)
# ==========================================================

def load_results():
    if not os.path.exists("quiz_results.json"):
        return {}
    try:
        with open("quiz_results.json", "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_results(results):
    with open("quiz_results.json", "w") as file:
        json.dump(results, file, indent=4)

def get_grade(percentage):
    if percentage >= 90: return "A"
    if percentage >= 80: return "B"
    if percentage >= 70: return "C"
    if percentage >= 60: return "D"
    return "F"

def get_user_title(total_correct):
    """Assigns a rank based on cumulative correct answers."""
    if total_correct >= 100: return "🧙 Python Wizard"
    elif total_correct >= 50: return "🛡️ Senior Coder"
    elif total_correct >= 25: return "⚔️ Intermediate Scripter"
    elif total_correct >= 10: return "🌱 Novice"
    else: return "🌑 Initiate"

def get_study_recommendation(username):
    """Analyzes practice history to give the user advice."""
    results = load_results()
    user_data = results.get(username, {})
    
    # Collect all practice attempts
    all_practice = []
    for subject in ["Python", "DSA"]:
        attempts = user_data.get(subject, [])
        all_practice.extend([a for a in attempts if a.get("mode") == "PRACTICE"])

    if not all_practice:
        return "💡 Tip: Try a few 'Practice Mode' rounds to get your first recommendation!"

    # Get the average of the last 3 practice rounds
    recent_practice = all_practice[-3:]
    avg_recent = sum(a["percentage"] for a in recent_practice) / len(recent_practice)

    if avg_recent >= 80:
        return "🚀 Recommendation: Your practice scores are excellent! You are ready for a HARD Test."
    elif avg_recent >= 50:
        return "📈 Recommendation: You're doing well. Keep practicing MEDIUM until you hit 80%."
    else:
        return "📚 Recommendation: Focus on EASY practice rounds to strengthen your basics."

def select_questions(subject, difficulty, answered_ids, all_questions):
    if difficulty != "mixed":
        pool = [q for q in all_questions if q["difficulty"] == difficulty]
    else:
        pool = all_questions
    
    # We only filter out repeats for TEST mode; Practice can repeat.
    available = [q for q in pool if q["id"] not in answered_ids]
    
    if not available: return None
    num_to_pick = min(len(available), 5)
    return random.sample(available, num_to_pick)

def run_quiz(username, subject, questions_list, practice=False):
    mode_label = "PRACTICE" if practice else "TEST"
    print(f"\n--- {subject} Quiz: {mode_label} Mode ---")
    
    results = load_results()
    if username not in results:
        results[username] = {"Python": [], "DSA": [], "progress": {}}
    
    results[username].setdefault("progress", {})
    results[username]["progress"].setdefault(subject, {"answered_ids": [], "total_answered": 0})
    answered_ids = results[username]["progress"][subject]["answered_ids"]

    print("Choose difficulty:\n1. Easy\n2. Medium\n3. Hard\n4. Mixed")
    diff_choice = input("Enter choice (1-4): ").strip()
    diff_map = {"1": "easy", "2": "medium", "3": "hard", "4": "mixed"}
    difficulty = diff_map.get(diff_choice, "mixed")

    # If it's practice, we don't care about answered_ids (allow repeats)
    current_answered_ids = [] if practice else answered_ids
    selected = select_questions(subject, difficulty, current_answered_ids, questions_list)
    
    if not selected:
        print("⚠️ No new questions available! Try a different difficulty.")
        return

    score = 0
    for q in selected:
        print(f"\nQ: {q['question']}")
        for i, opt in enumerate(q["options"], 1):
            print(f"{i}. {opt}")
        try:
            user_input = int(input("Your answer: "))
            if q["options"][user_input-1] == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct: {q['answer']}\n💡 {q['explanation']}")
        except:
            print("Invalid input. Skipped.")

        if not practice:
            if q["id"] not in answered_ids:
                answered_ids.append(q["id"])

    # Saving Logic
    percentage = (score / len(selected)) * 100
    attempt = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "mode": mode_label,
        "difficulty": difficulty,
        "score": f"{score}/{len(selected)}",
        "percentage": round(percentage, 2),
        "grade": get_grade(percentage)
    }
    
    results[username][subject].append(attempt)
    if not practice:
        results[username]["progress"][subject]["total_answered"] += len(selected)
        print(f"\n✅ Official Test Saved!")
    else:
        print(f"\n📝 Practice Session Recorded!")
    
    save_results(results)

def show_leaderboard():
    results = load_results()
    leaderboard = []
    for user, data in results.items():
        # Only count TEST mode scores for the leaderboard
        all_att = [a for s in ["Python", "DSA"] for a in data.get(s, []) if a.get("mode") == "TEST"]
        if all_att:
            avg = sum(a["percentage"] for a in all_att) / len(all_att)
            # Rank title is based on TOTAL correct answers (Test + Practice)
            total_correct = 0
            for s in ["Python", "DSA"]:
                for a in data.get(s, []):
                    total_correct += int(str(a["score"]).split('/')[0])
            
            leaderboard.append((user, round(avg, 2), get_user_title(total_correct)))
    
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    print("\n🏆 ======= GLOBAL LEADERBOARD =======")
    print(f"{'Rank':<5} {'Username':<15} {'Avg %':<10} {'Title'}")
    print("-" * 65)
    for r, (u, s, t) in enumerate(leaderboard, 1):
        print(f"{r:<5} {u:<15} {s}%      {t}")

def show_topic_kings():
    results = load_results()
    python_stats, dsa_stats = [], []
    for user, data in results.items():
        # Only count Official Tests for "Kings"
        py = [a["percentage"] for a in data.get("Python", []) if a.get("mode") == "TEST"]
        dsa = [a["percentage"] for a in data.get("DSA", []) if a.get("mode") == "TEST"]
        if py: python_stats.append((user, round(sum(py)/len(py), 2)))
        if dsa: dsa_stats.append((user, round(sum(dsa)/len(dsa), 2)))

    print("\n👑 ======= TOPIC KINGS =======")
    if python_stats:
        python_stats.sort(key=lambda x: x[1], reverse=True)
        print(f"🐍 Python Expert: {python_stats[0][0]} ({python_stats[0][1]}%)")
    if dsa_stats:
        dsa_stats.sort(key=lambda x: x[1], reverse=True)
        print(f"🌳 DSA Master:    {dsa_stats[0][0]} ({dsa_stats[0][1]}%)")
    print("-" * 35)

# ==========================================================
# 3. MAIN MENU
# ==========================================================

def main():
    print("=== Python & DSA Quiz System ===")
    username = input("Enter Username: ").strip()
    
    while True:
        print("\n===== Main Menu =====")
        print("1. Start Python Quiz (Test Mode)")
        print("2. Start DSA Quiz (Test Mode)")
        print("3. Practice Python (Saves to History)")
        print("4. Practice DSA (Saves to History)")
        print("5. View My Advisor & Performance")
        print("6. Show Leaderboards")
        print("7. Quit")

        choice = input("Choice (1-7): ")
        if choice == "1": run_quiz(username, "Python", python_questions)
        elif choice == "2": run_quiz(username, "DSA", dsa_questions)
        elif choice == "3": run_quiz(username, "Python", python_questions, True)
        elif choice == "4": run_quiz(username, "DSA", dsa_questions, True)
        elif choice == "5":
            print("\n--- Your Study Recommendation ---")
            print(get_study_recommendation(username))
            print("-" * 40)
            user_data = load_results().get(username, "No data found.")
            print(json.dumps(user_data, indent=4))
        elif choice == "6":
            show_leaderboard()
            show_topic_kings()
        elif choice == "7":
            print("👋 Goodbye!"); break
        else:
        # This catches letters, symbols, or wrong numbers
           print("!!! Invalid entry. Please type 1 or 2. !!!")    

if __name__ == "__main__":
    main()