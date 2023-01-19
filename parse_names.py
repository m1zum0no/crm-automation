def log_names(order_entry):
    with open('names.py', 'a') as output:
        output.write(':'.join(order_entry) + '\n')


def parse_name(lst):
    order_entry = lst[:2]
    full_name = lst[2].split(' ')
    if len(full_name) == 1:
        order_entry.append(*full_name)
    else:
        order_entry.append(full_name[1])
    log_names(order_entry)


def log_orders():
    with open('orders.py', 'r') as input:
        for line in input.readlines():
            lst = list(line.split(':'))
            parse_name(lst)


log_orders()