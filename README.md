🐍 Python + DSA Adaptive Quiz App
A robust, terminal-based examination tool designed to bridge the gap between Python syntax and algorithmic logic. This application features a data-driven approach to learning, utilizing JSON persistence and an adaptive difficulty engine to challenge users based on their real-time performance.

🚀 Key Features
Dynamic Difficulty Scaling: Toggle between Easy, Medium, Hard, or Mixed modes.

Adaptive Learning Engine: An optional mode that automatically adjusts question complexity based on your success rate.

Persistent Data Storage: Full user lifecycle management via quiz_results.json, tracking cumulative scores and attempts.

Immediate Pedagogical Feedback: Real-time explanations for incorrect answers to reinforce core CS fundamentals.

Algorithmic Variety: Questions covering Big O notation, Data Structures (Linked Lists, Trees, Stacks), and Python-specific optimizations.

🛠️ System Architecture
The project follows a modular structure to ensure maintainability and separation of concerns. This architecture allows the logic to stay independent of the data, making it easy to scale.

Plaintext

Python-DSA-Quiz/
├── python_quiz.py        # Main Application Entry Point & Logic
├── quiz_results.json     # Local Database (JSON format)
├── README.md             # Project Documentation
└── .gitignore            # Version control exclusions
⚙️ Installation & Setup
1. Prerequisites
Ensure you have Python 3.8 or higher installed.

2.📥 Get the Code
Option A: No Git installed? Click the green Code button at the top of this page and select Download ZIP. Extract the files to a folder on your computer. Then run the code in your preferred code editor.

Option B: Using Git Run the following command in your terminal: git clone https://github.com/omorinsola1/mayropython.git


python python_quiz.py
📖 Usage Guide
Authentication: Enter your unique username. The system loads your historical progress automatically.

Mode Selection: Choose a fixed difficulty or activate the Adaptive Engine.

Interaction: Select the best answer for the prompt.

Review: Study the immediate feedback provided for any missed questions.

Save & Exit: Use the Quit option to ensure your session data is serialized to the local database.

📊 Performance Tracking
The application manages user data through a structured JSON schema, allowing for long-term progress monitoring and performance analytics.

🛣️ Future Roadmap
Advanced UI Layer: Transitioning from CLI to an enhanced graphical interface.

Performance Analytics: Integration of advanced scoring metrics and session timing.

Expanded Knowledge Base: Scaling the question repository to include more complex algorithmic paradigms.

🧰 Built With

Language: Python

Data Storage: JSON

Editor: Visual Studio Code 


##LICENSE
[MIT license](LICENSE)



