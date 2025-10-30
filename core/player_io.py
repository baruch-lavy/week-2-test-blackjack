def is_valid_action(action:str,length):
    striped_action = action.strip()
    input_list = striped_action.split()
    if len(input_list) > length:
        return False , f'not valid, more them {length} option'
    if len(input_list) < length:
        print(input_list)
        return False , f'not valid, less them {length} option'
    elif len(input_list) == length:
            for str in input_list:
                try:
                    item = int(str)
                    return False , 'you have to enter str'
                except ValueError as e:
                    if action.lower() == 'h' or action.lower() == 's':
                        return True , action
                    else:
                        return False , 'you have to enter h or s'

def ask_player_action() -> str:
    is_asking = True
    while is_asking:
        user_action = input('enter your action please (h or s): ')
        is_valid = is_valid_action(user_action,1)
        if is_valid[0] == True:
            is_asking = False
        print(is_valid[1])
    return user_action.upper()
    
