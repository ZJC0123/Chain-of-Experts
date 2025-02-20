import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set the OPENAI_API_KEY environment variable
with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'openaikey.txt'))) as f:
    os.environ["OPENAI_API_KEY"] = f.read().strip()

from experts.code_reviewer import CodeReviewer

# Create a mock comment pool
class MockCommentPool:
    def get_current_comment_text(self):
        return "This is a mock comment."

# Create a mock feedback pool
class MockFeedbackPool:
    def get_current_comment_text(self):
        return "This is a mock feedback."

# Initialize the CodeReviewer with the "deepseek" model
code_reviewer = CodeReviewer(model="deepseek")

# Define a mock problem
mock_problem = {
    "description": "Optimize the sorting algorithm in the given code."
}

# Test the forward method
forward_output = code_reviewer.forward(mock_problem, MockCommentPool())
print("Forward Output:", forward_output)

# Test the backward method
backward_output = code_reviewer.backward(MockFeedbackPool())
print("Backward Output:", backward_output)
