# Quiz Game

A simple and interactive quiz game built with Python's Tkinter library. This application displays a series of quiz questions, allows users to select answers, and provides feedback on their choices.

## Features

- **Question Display**: Shows quiz questions and associated images (if available).
- **Answer Choices**: Users can select from multiple-choice options.
- **Feedback**: Provides immediate feedback on selected answers.
- **Score Tracking**: Keeps track of the score and displays it during the quiz.
- **Responsive Design**: Adjusts window size to fit content and screen height.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Htmil/QuizGame
    ```

2. **Navigate to the project directory**:
    ```sh
    cd quiz-game
    ```

3. **Install dependencies**:
    Ensure you have Python 3 installed. Install required packages using pip:
    ```sh
    pip install pillow ttkbootstrap
    ```

4. **Prepare your quiz data**: Create a file named `quiz_data.py` in the project directory with the following format:
    ```python
    quiz_data = [
        {
            "question": "What is the capital of France?",
            "choices": ["Paris", "London", "Rome", "Berlin"],
            "answer": "Paris",
            "image": "path/to/image.jpg"  # Optional
        },
        # Add more questions as needed
    ]
    ```

5. **Prepare your images**: Place any images referenced in `quiz_data.py` in the `images` directory.

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Play the game**:
    - The application will display a question and multiple-choice answers.
    - Select an answer to receive feedback.
    - Click the "Next" button to proceed to the next question.
    - View your final score when all questions have been answered.


## Acknowledgements

- [Pillow](https://pillow.readthedocs.io/en/stable/) - For image handling.
- [TTKBootstrap](https://ttkbootstrap.readthedocs.io/en/latest/) - For the themed Tkinter widgets.
- [Building a Quiz App with Python and Tkinter | Tutorial](https://www.youtube.com/watch?v=gfV1a3ri1tk) - inspiration and codebase from tutorial.
