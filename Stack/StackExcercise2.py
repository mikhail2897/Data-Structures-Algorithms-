'''2. Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use [Stack class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/5_Stack/5_stack.ipynb) from the tutorial.
    ```
    is_balanced("({a+b})")     --> True
    is_balanced("))((a+b}{")   --> False
    is_balanced("((a+b))")     --> True
    is_balanced("))")          --> False
    is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
    ```
'''

from StackExcercise1 import Stack
def is_match(char_1, char_2):
    match_dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    return match_dict[char_1] == char_2


def is_balanced(string):
    stack = Stack()
    for char in string:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        if char == ')' or char == ']' or char == '}':
            if stack.size() == 0:
                return False
            if not is_match(char, stack.pop()):
                return False
    return stack.size() == 0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))