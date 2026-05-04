from input_module import *
from logic_module import *
from output_module import *


def main():
    score = get_score()
    grade = calculate_grade(score)
    display_result(score, grade)


main()