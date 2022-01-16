import random  # import random module


def play():
    # get user to key in r, p or s
    user = input("What's your choice? 'r' for rock,'p' for paper,'s' for scissors\n")
    # convert the letters to lowercase
    user = user.lower()
    # computer will randomly choose r , p or s
    computer = random.choice(['r', 'p', 's'])

    if user == computer:  # if user and computer input is same. E.g. User choose r and computer choose r
        return "You and the computer have both chosen {}. It's a tie.".format(computer)

    # r > s, s > p, p > r
    if is_win(user, computer):  # if user beat computer and won, call the is_win function
        return "You have chosen {} and the computer has chosen {}. You won! :)".format(user, computer)
    # if user lose to computer
    return "You have chosen {} and the computer has chosen {}. You lost. :(".format(user, computer)


def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True
    return False


if __name__ == '__main__':
    print(play())
    
    