def check_valid_range(pass_v, defer_v, fail_v):
    valid_range = (0, 20, 40, 60, 80, 100, 120)
    if pass_v not in valid_range or \
        defer_v not in valid_range or \
        fail_v not in valid_range:
        print('Range error')
        return False
    return True

def check_total(pass_v, defer_v, fail_v):
    if pass_v + defer_v + fail_v != 120:
        print('Total incorrect')
        return False
    return True

def main():
    pass_v = None
    defer_v = None
    fail_v = None

    try:
        pass_v = int(input('Pass: '))
        defer_v = int(input('Defer: '))
        fail_v = int(input('Fail: '))
    except ValueError:
        print('Integers required')
        exit(1)

    if not check_valid_range(pass_v, defer_v, fail_v):
        exit(2)

    if not check_total(pass_v, defer_v, fail_v):
        exit(3)

    if pass_v == 120:
        print('Progress')
    elif pass_v == 100:
        print('Progress - module trailer')
    elif pass_v == 80 or pass_v == 60 or \
        (pass_v == 60 and defer_v >= 20) or (pass_v == 20 and defer_v >= 40) or \
        (pass_v == 0 and defer_v >= 60) or (pass_v == 40 and fail_v <= 60):
        print('Do not progress - module retriever')
    elif fail_v >= 80:
        print('Exclude')

main()
