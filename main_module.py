from input_module import *
from logic_module import *
from output_module import *


def main():
    score = input_module.get_score()
    grade = logic_module.calculate_grade(score)
    output_module.display_result(score, grade)


main()