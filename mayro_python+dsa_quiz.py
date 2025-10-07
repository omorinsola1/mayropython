import json
import random
import os

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
    {"id":30, "subject":"python","difficulty":"hard","question":"Which of these is NOT a Python data structure?","options":["List","Stack","Dictionary","Tuple"],"answer":"Stack","explanation":"Stack is a data structure concept, not a built-in Python type."}
]

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

import json
import random
import os
from datetime import datetime

def load_results():
    if os.path.exists("quiz_results.json"):
        with open("quiz_results.json", "r") as f:
            return json.load(f)
    return {}

def save_results(results):
    with open("quiz_results.json", "w") as f:
        json.dump(results, f, indent=4)

def get_grade(percentage):
    if percentage >= 85:
        return "Excellent"
    elif percentage >= 70:
        return "Very Good"
    elif percentage >= 50:
        return "Good"
    else:
        return "Needs Improvement"

def select_questions(subject, difficulty, answered_ids, questions, num=5):
    available = []
    for q in questions:
        if not all(k in q for k in ("id","subject","difficulty","question","options","answer","explanation")):
            continue
        if q["subject"].lower() != subject.lower():
            continue
        if difficulty.lower() != "mixed" and q["difficulty"].lower() != difficulty.lower():
            continue
        if q["id"] not in answered_ids:
            available.append(q)
    if not available:
        return []
    return random.sample(available, min(num, len(available)))
def run_quiz(username, subject, questions, practice=False):
    mode = "Practice Mode" if practice else "Test Mode"
    print(f"\nStarting {subject} Quiz for {username} ({mode})...\n")

    results = load_results()

    # Initialize user progress properly
    if username not in results:
        results[username] = {"Python": [], "DSA": [], "progress": {}}
    results[username].setdefault(subject, [])
    results[username].setdefault("progress", {})
    results[username]["progress"].setdefault(subject, {"answered_ids": [], "total_answered": 0})

    answered_ids = results[username]["progress"][subject]["answered_ids"]

    # ----- Number-based difficulty selection -----
    print("Choose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Mixed")
    diff_choice = input("Enter choice (1-4): ").strip()
    diff_map = {"1": "easy", "2": "medium", "3": "hard", "4": "mixed"}
    difficulty = diff_map.get(diff_choice, "mixed")  # default to mixed

    # Select questions
    quiz_questions = select_questions(subject, difficulty, answered_ids, questions)
    if not quiz_questions:
        print("⚠️ No new questions available in this category.")
        return

    score = 0
    wrong_answers = []

    for q in quiz_questions:
        print("\n" + q["question"])
        for i,opt in enumerate(q["options"],1):
            print(f"{i}. {opt}")

        try:
            ans = int(input("Your answer: "))
            if q["options"][ans-1] == q["answer"]:
                print("✅ Correct!")
                if not practice:
                    score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
                print(f"💡 Explanation: {q['explanation']}")
                if not practice:
                    wrong_answers.append(q.get("concept",""))
        except (ValueError, IndexError):
            print("Invalid choice, skipping...")

        # Track answered questions
        if not practice and q["id"] not in answered_ids:
            answered_ids.append(q["id"])

    if practice:
        print("\nPractice session finished! (No scores recorded)")
        return

    total = len(quiz_questions)
    percentage = (score / total) * 100
    grade = get_grade(percentage)

    # Save attempt
    attempt = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "difficulty": difficulty,
        "score": score,
        "total": total,
        "percentage": round(percentage,2),
        "grade": grade,
        "answered_questions": [q["id"] for q in quiz_questions]
    }

    results[username][subject].append(attempt)
    results[username]["progress"][subject]["total_answered"] += total
    save_results(results)

    # Summary
    print(f"\n--- Quiz Summary ---")
    print(f"Score: {score}/{total} → {percentage:.2f}% → Grade: {grade}")
    if wrong_answers:
        print("\nReview your mistakes:")
        for qid in wrong_answers:
            print(f"- {qid}")

def main():
    results = load_results()

    username = input("Enter your username: ").strip()
    if username in results:
        print(f"👋 Welcome back, {username}!")
    else:
        print(f"✨ Welcome, {username}! Let's get started.")
        results[username] = {"Python": [], "DSA": [], "progress": {}}
        save_results(results)

    while True:
        print("\n===== Main Menu =====")
        print("1. Start Python Quiz (Test Mode)")
        print("2. Start DSA Quiz (Test Mode)")
        print("3. Practice Python (No scores saved)")
        print("4. Practice DSA (No scores saved)")
        print("5. View Past Performance")
        print("6. Quit")

        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            run_quiz(username, "Python", python_questions, practice=False)
        elif choice == "2":
            run_quiz(username, "DSA", dsa_questions, practice=False)
        elif choice == "3":
            run_quiz(username, "Python", python_questions, practice=True)
        elif choice == "4":
            run_quiz(username, "DSA", dsa_questions, practice=True)
        elif choice == "5":
            past = results.get(username, {"Python": [], "DSA": []})
            print(f"\n📊 Past Performance for {username}:")
            print(json.dumps(past, indent=4))
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-6.")

if __name__ == "__main__":
    main()
    