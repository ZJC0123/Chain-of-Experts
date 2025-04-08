import re
import json
import os


def extract_code_from_string(input_string):
    # Match code within ```python ... ``` or ``` ... ``` blocks
    pattern = r'```(?:python)?\s*(.*?)\s*```'
    
    # Find all matches in the input string
    code_blocks = re.findall(pattern, input_string, re.DOTALL)

    if len(code_blocks) == 0:
        # print(f'Parse code error! {input_string}')
        return input_string
    elif len(code_blocks) == 1:
        return code_blocks[0]

    code_blocks = [code for code in code_blocks if 'pip' not in code]
    return '\n'.join(code_blocks)


def read_problem(dataset, problem_name):
    base_dir = 'dataset'
    if os.path.exists(os.path.join(base_dir, dataset, problem_name, 'description.txt')):
        with open(os.path.join(base_dir, dataset, problem_name, 'description.txt'), 'r', encoding='utf8') as f:
            description = f.read()
    else:
        with open(os.path.join(base_dir, dataset, problem_name, 'background.txt'), 'r', encoding='utf8') as f:
            description = f.read()
    with open(os.path.join(base_dir, dataset, problem_name, 'code_example.py'), 'r', encoding='utf8') as f:
        code_example = f.read()

    return {
        'description': description,
        'code_example': code_example
    }


def extract_code_blocks(text, code_type=None):
    """
    Extracts code blocks of a specific type (e.g., JSON or Python) or generic code blocks from the given text.

    :param text: The input text containing code blocks.
    :param code_type: The type of code to extract ('json', 'python', or None for generic code blocks).
    :return: A list of extracted code blocks as strings.
    """
    if '```' not in text:
        return text
    if code_type:
        pattern = rf"```{code_type}\s*\n(.*?)```"
    else:
        pattern = r"```\s*\n(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return [match.strip() for match in matches][0] if matches else None