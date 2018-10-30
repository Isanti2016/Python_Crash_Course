import json

# ~ filename = "username.json"
# ~ try:
    # ~ with open(filename, 'r') as f_obj:
        # ~ username = json.load(f_obj)
# ~ except FileNotFoundError:
    # ~ username = input("What is your name?")
    # ~ with open(filename,'w') as f_obj:
        # ~ json.dump(username, f_obj)
        # ~ print("we'll remember you when you come back," + username + "!")
# ~ else:
    # ~ print("wecome back," + username + "!")


def get_stored_usernaem(filename):
    """读取用户信息"""
    try:
        with open(filename, 'r') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
        
def get_new_username(filename):
    """提示用户输入信息"""
    username = input("What is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
    
def greet_user(filename):
    """问候用户"""
    username = get_stored_usernaem(filename)

    if username:
        message = "Your name is " + username + "?"
        message += "\ninput 'yes' or 'no'\n"
        user_answer = input( message)
        if user_answer == 'yes':
            print("Welcome back, " + username + "!")
        elif user_answer == 'no':
            username = get_new_username(filename)
            print("We'll remember you when you come back," + username + "!")
    else:
        username = get_new_username(filename)
        print("We'll remember you when you come back," + username + "!")
        
filename = "username.json"
greet_user(filename)
