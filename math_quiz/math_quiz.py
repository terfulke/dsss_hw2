import random


def generate_integer(min, max):
    """
    Generate random integer.

    Parameters
    -----------
    min : int
        The minimum value generated intiger will have.
    max : int or float
        The value to which the integer will be generated but will never reach.

    Raises
    ------
    TypeError
        If either min or max is not an integer.

    Returns
    -------
    int
        Randomly generated integer within the interval [min, max).

    """
    # error handling in case max or min is not an integer
    if not isinstance(min, int) or not isinstance(max, int):
        raise TypeError("Both min and max must be integers.")

    return random.randint(min, max)


def generate_operator():
    """
    Generate operator.

    Parameters
    ----------
    None

    Returns
    -------
    string
        Randomly generated string '+', '-', or '*' defining the operator.
    """
    return random.choice(['+', '-', '*'])


def math_example_result(number1, number2, operator):
    """
    Evaluate example.

    Parameters
    -----------
    number1 : int
        The first number in the math example.
    number2 : int
        The second number in the math example
    operator : string
        String for implifying addition ('+'), difference ('-') or multiplication ('*').


    Returns
    -------
    tuple
        A tuple containing:
            - str : The math ecample as a string (for example: "3 + 4").
            - int : The result of the evaluated expression.
    """

    if number2 < 0:
        # if the number2 is smaller than 0, we need to add brackets for precision in example
        generated_example = f"{number1} {operator} ({number2})"
    else:
        generated_example = f"{number1} {operator} {number2}"
    
    if operator == '+':             # addition
        result = number1 + number2  
    elif operator == '-':           # difference
        result = number1 - number2
    else:                           # multiplication
        result = number1 * number2
    return generated_example, result


def math_quiz():
    """
    Run a math quiz game where the user solves 10 math problems.

    The quiz consists of:
        - 10 randomly generated problems with integer operands between -10 and 10.
        - Random operators for each problem (addition, difference or multiplication).

    At the end, the user is shown their final score out of the total number of questions.

    Parameters
    ----------
    None

    Prints
    ------
        The quiz prints the quiz introduction, math example, feedback on the answer (correct or incorrect), 
        and the final score.

    Notes
    -----
    This function assumes the existence of helper functions:
        `generate_integer(max, min)`
        `generate_operator()`
        `math_example_result(number1, number2, operator)`
    """

    score = 0               
    num_of_problems = 10   

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_of_problems):
        number1 = generate_integer(-10, 10)
        number2 = generate_integer(-10, 10)
        operator = generate_operator()

        PROBLEM, ANSWER = math_example_result(number1, number2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1                              # adding up the score in case of correct answer
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{num_of_problems}")

if __name__ == "__main__":
    math_quiz()
