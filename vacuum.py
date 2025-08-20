states = [
    ('A', 'dirty', 'dirty'),
    ('A', 'dirty', 'clean'),
    ('A', 'clean', 'dirty'),
    ('A', 'clean', 'clean'),
    ('B', 'dirty', 'dirty'),
    ('B', 'dirty', 'clean'),
    ('B', 'clean', 'dirty'),
    ('B', 'clean', 'clean'),
]

def vacuum_world(states):
    for state in states:
        position, a_status, b_status = state
        actions = []
        current = position
        if current == 'A':
            if a_status == 'dirty':
                actions.append('Clean')
                a_status = 'clean'
            actions.append('Move Right')
            current = 'B'
            if b_status == 'dirty':
                actions.append('Clean')
                b_status = 'clean'
        else:
            if b_status == 'dirty':
                actions.append('Clean')
                b_status = 'clean'
            actions.append('Move Left')
            current = 'A'
            if a_status == 'dirty':
                actions.append('Clean')
                a_status = 'clean'
        print(f"Initial State: {state}, Actions: {actions}")

vacuum_world(states)
