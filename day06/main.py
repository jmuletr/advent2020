def get_unique_answers(answers):
    return set(''.join(answers.split()))


def get_common_answers(answers):
    passenger = [set(passenger) for passenger in answers.split()]
    return passenger[0].intersection(*passenger[1:])


with open("input.txt") as f:
    groups = f.read().split('\n\n')

    answers_list = []
    all_group_yes_answers = []
    for group in groups:
        answers_list.append(get_unique_answers(group))
        all_group_yes_answers.append(get_common_answers(group))

    print(sum(len(group_answer) for group_answer in answers_list))
    print(sum(len(group_answer) for group_answer in all_group_yes_answers))
