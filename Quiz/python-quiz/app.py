from flask import Flask, jsonify, render_template


app = Flask(__name__)


# In-memory quiz data converted from src/data/quizzes.ts
QUIZZES = [
    {
        "id": "javascript-basics",
        "title": "JavaScript Fundamentals",
        "description": "Test your knowledge of JavaScript basics including variables, functions, and data types.",
        "difficulty": "easy",
        "timeLimit": 30,
        "questions": [
            {
                "id": 1,
                "question": "Which of the following is used to declare a variable in JavaScript?",
                "options": ["var", "let", "const", "All of the above"],
                "correctAnswer": 3,
                "explanation": "All three keywords (var, let, const) can be used to declare variables in JavaScript, each with different scoping rules.",
            },
            {
                "id": 2,
                "question": "What does \"=== \" operator do in JavaScript?",
                "options": [
                    "Assignment",
                    "Comparison with type coercion",
                    "Strict equality comparison",
                    "Not equal",
                ],
                "correctAnswer": 2,
                "explanation": "The === operator performs strict equality comparison, checking both value and type without type coercion.",
            },
            {
                "id": 3,
                "question": "Which method is used to add an element to the end of an array?",
                "options": ["push()", "pop()", "shift()", "unshift()"],
                "correctAnswer": 0,
                "explanation": "The push() method adds one or more elements to the end of an array and returns the new length.",
            },
            {
                "id": 4,
                "question": "What is the correct way to create a function in JavaScript?",
                "options": [
                    "function myFunction() {}",
                    "create myFunction() {}",
                    "function = myFunction() {}",
                    "def myFunction() {}",
                ],
                "correctAnswer": 0,
                "explanation": "Functions in JavaScript are declared using the function keyword followed by the function name and parentheses.",
            },
            {
                "id": 5,
                "question": "Which of these is NOT a JavaScript data type?",
                "options": ["String", "Boolean", "Float", "Number"],
                "correctAnswer": 2,
                "explanation": "JavaScript has Number data type for all numeric values. There is no separate Float data type.",
            },
        ],
    },
    {
        "id": "react-advanced",
        "title": "React Advanced Concepts",
        "description": "Challenge yourself with advanced React topics including hooks, context, and performance optimization.",
        "difficulty": "hard",
        "timeLimit": 45,
        "questions": [
            {
                "id": 1,
                "question": "Which hook would you use to perform side effects in a functional component?",
                "options": ["useState", "useEffect", "useContext", "useReducer"],
                "correctAnswer": 1,
                "explanation": "useEffect is used to perform side effects like data fetching, subscriptions, or manually changing the DOM.",
            },
            {
                "id": 2,
                "question": "What is the purpose of React.memo()?",
                "options": [
                    "To memoize state values",
                    "To prevent unnecessary re-renders",
                    "To cache API responses",
                    "To optimize event handlers",
                ],
                "correctAnswer": 1,
                "explanation": "React.memo() is a higher-order component that prevents unnecessary re-renders by memoizing the component.",
            },
            {
                "id": 3,
                "question": "Which pattern is recommended for sharing state between components?",
                "options": [
                    "Props drilling",
                    "Global variables",
                    "Context API",
                    "Local storage",
                ],
                "correctAnswer": 2,
                "explanation": "Context API is the recommended React pattern for sharing state between components without prop drilling.",
            },
        ],
    },
    {
        "id": "web-fundamentals",
        "title": "Web Development Fundamentals",
        "description": "Cover the basics of HTML, CSS, and web development principles.",
        "difficulty": "medium",
        "timeLimit": 25,
        "questions": [
            {
                "id": 1,
                "question": "What does HTML stand for?",
                "options": [
                    "Hyper Text Markup Language",
                    "High Tech Modern Language",
                    "Home Tool Markup Language",
                    "Hyperlink and Text Markup Language",
                ],
                "correctAnswer": 0,
                "explanation": "HTML stands for Hyper Text Markup Language, the standard markup language for creating web pages.",
            },
            {
                "id": 2,
                "question": "Which CSS property is used to change the text color?",
                "options": ["font-color", "text-color", "color", "foreground-color"],
                "correctAnswer": 2,
                "explanation": "The color property in CSS is used to set the text color of an element.",
            },
            {
                "id": 3,
                "question": "What is the correct HTML element for the largest heading?",
                "options": ["<heading>", "<h6>", "<h1>", "<head>"],
                "correctAnswer": 2,
                "explanation": "The <h1> element represents the largest heading in HTML, with <h6> being the smallest.",
            },
            {
                "id": 4,
                "question": "Which property is used in CSS to make text bold?",
                "options": ["font-weight", "text-weight", "font-style", "text-style"],
                "correctAnswer": 0,
                "explanation": "The font-weight property is used to set how thick or thin characters in text should be displayed.",
            },
        ],
    },
]


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/quizzes")
def get_quizzes():
    return jsonify(QUIZZES)


if __name__ == "__main__":
    app.run(debug=True)


