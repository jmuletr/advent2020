class CurrentState:
    position = 0
    acc = 0
    last_acc = 0
    used_instructions = set()

    def reset(self):
        self.acc = 0
        self.position = 0
        self.last_acc = 0
        self.used_instructions = set()


def run_instruction(current_state, instruction):
    op, arg = instruction
    current_state.last_acc = current_state.acc
    if op == "acc":
        current_state.acc += int(arg)
        current_state.position += 1
    if op == "jmp":
        current_state.position += int(arg)
    if op == "nop":
        current_state.position += 1


def get_first_repeated_acc(data):
    current_state = CurrentState()
    while current_state.position < len(data):
        run_instruction(current_state, data[current_state.position])
        if current_state.position not in current_state.used_instructions:
            current_state.used_instructions.add(current_state.position)
        else:
            return current_state.last_acc


def execute_all_code(current_state, data):
    while current_state.position <= len(data):
        if current_state.position == len(data):
            return current_state.acc
        else:
            run_instruction(current_state, data[current_state.position])
            if current_state.position in current_state.used_instructions:
                break
            else:
                current_state.used_instructions.add(current_state.position)


def get_last_operation(data):
    current_state = CurrentState()
    for i, (op, arg) in enumerate(data):
        current_state.reset()
        data_edit = data.copy()
        if op == "jmp":
            data_edit[i] = ("nop", arg)
        elif op == "nop":
            data_edit[i] = ("jmp", arg)
        else:
            continue

        result = execute_all_code(current_state, data_edit)
        if result is not None:
            return result


with open("input.txt") as f:
    lines = [(i.split()[0].strip(), i.split()[1].strip()) for i in f.readlines()]
    print(get_first_repeated_acc(lines))
    print(get_last_operation(lines))
