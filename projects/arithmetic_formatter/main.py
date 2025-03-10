def arithmetic_arranger(problems, show_answers=False):
    top_line = []
    middle_line = []
    dash_line = []
    result_line = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        for problem in problems:
            parts = problem.split(' ')
            operand_1 = parts[0]
            operator = parts[1]
            operand_2 = parts[2]
            if operator != '+' and operator != '-':
                return "Error: Operator must be '+' or '-'."
            if not operand_1.isdigit() or not operand_2.isdigit():
                return 'Error: Numbers must only contain digits.'
            int(operand_1)
            int(operand_2)
            if len(operand_1) > 4 or len(operand_2) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            width = max(len(operand_1), len(operand_2)) + 2
            top_line.append(operand_1.rjust(width))
            middle_line.append(operator + operand_2.rjust(width - 1))
            dash_line.append('-' * width)
            # For the result
            if operator == '+':
                result = str(int(operand_1) + int(operand_2))
            elif operator == '-':
                result = str(int(operand_1) - int(operand_2))
            result_line.append(result.rjust(width))

    arranged_problems = '    '.join(top_line) + '\n' + '    '.join(middle_line) + '\n' + '    '.join(dash_line)
    if show_answers:
        arranged_problems += '\n' + '    '.join(result_line)
    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')