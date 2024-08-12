def arithmetic_arranger(problems, display_answers=False):
    # Check for too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    operators = []
    second_operands = []
    answers = []
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            continue  # This shouldn't happen with well-formed input.

        first_operand, operator, second_operand = parts
        
        # Validate the operator
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        # Validate the numbers
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate the answer if needed
        if display_answers:
            if operator == '+':
                answer = str(int(first_operand) + int(second_operand))
            else:  # operator == '-'
                answer = str(int(first_operand) - int(second_operand))
            answers.append(answer)

        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)

    arranged_problems = []
    
    # Format the problems
    first_line = []
    second_line = []
    dashes = []
    answer_line = []

    for i in range(len(problems)):
        first = first_operands[i]
        operator = operators[i]
        second = second_operands[i]

        length = max(len(first), len(second)) + 2  # Two spaces for the operator and space

        first_line.append(first.rjust(length))
        second_line.append(operator + ' ' + second.rjust(length - 2))
        dashes.append('-' * length)
        
        if display_answers:
            answer_line.append(answers[i].rjust(length))

    arranged_problems.append('    '.join(first_line))
    arranged_problems.append('    '.join(second_line))
    arranged_problems.append('    '.join(dashes))
    if display_answers:
        arranged_problems.append('    '.join(answer_line))

    return '\n'.join(arranged_problems)

# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
