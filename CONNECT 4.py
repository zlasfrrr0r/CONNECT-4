#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_grid(grid):
    
    clear_output()

    print(
        '|' + grid[5] + '|' + grid[11] + '|' + grid[17] + '|' + grid[23] + '|' + grid[29] + '|' + grid[35] + '|' + grid[
            41] + '|')
    print(
        '|' + grid[4] + '|' + grid[10] + '|' + grid[16] + '|' + grid[22] + '|' + grid[28] + '|' + grid[34] + '|' + grid[
            40] + '|')
    print(
        '|' + grid[3] + '|' + grid[9] + '|' + grid[15] + '|' + grid[21] + '|' + grid[27] + '|' + grid[33] + '|' + grid[
            39] + '|')
    print(
        '|' + grid[2] + '|' + grid[8] + '|' + grid[14] + '|' + grid[20] + '|' + grid[26] + '|' + grid[32] + '|' + grid[
            38] + '|')
    print(
        '|' + grid[1] + '|' + grid[7] + '|' + grid[13] + '|' + grid[19] + '|' + grid[25] + '|' + grid[31] + '|' + grid[
            37] + '|')
    print(
        '|' + grid[0] + '|' + grid[6] + '|' + grid[12] + '|' + grid[18] + '|' + grid[24] + '|' + grid[30] + '|' + grid[
            36] + '|')


# In[2]:


def player_mark():
    mark = ''

    while mark not in ['X', 'O']:

        mark = input('Choose your mark (X or O): ')

        if mark not in ['X', 'O']:
            print('X or O ONLY')

    return mark


# In[3]:


def drop_disc(grid, mark, column):
    if column == 0:
        for row in range(6):
            if grid[row] == ' ':
                grid[row] = mark
                break
    elif column == 1:
        for row in range(6, 12):
            if grid[row] == ' ':
                grid[row] = mark
                break
    elif column == 2:
        for row in range(12, 18):
            if grid[row] == ' ':
                grid[row] = mark
                break
    elif column == 3:
        for row in range(18, 24):
            if grid[row] == ' ':
                grid[row] = mark
                break
    elif column == 4:
        for row in range(24, 30):
            if grid[row] == ' ':
                grid[row] = mark
                break
    elif column == 5:
        for row in range(30, 36):
            if grid[row] == ' ':
                grid[row] = mark
                break
    else:
        for row in range(36, 42):
            if grid[row] == ' ':
                grid[row] = mark
                break


# In[4]:


def user_column(grid):
    
    choice = ''
    
    available = False

    inrange = range(7)

    while choice not in inrange or available == False:

        choice = int(input('Choose column (0-6 left to right): '))

        if choice not in inrange:
            print('outside range.')
        else:
            if choice == 0:
                if grid[5]!=' ':
                    print('Column is full. Choose another one')
                    available = False
                else:
                    available = True
                    return choice
            elif choice == 1:
                if grid[11]!=' ':
                    print('Column is full. Choose another one')
                    available = False
                else:
                    available = True
                    return choice
            elif choice == 2:
                if grid[17]!=' ':
                    print('Column is full. Choose another one')
                    available = False
                else:
                    available = True
                    return choice
            elif choice == 3:
                if grid[23]!=' ':
                    print('Column is full. Choose another one')
                    available = False
                else:
                    available = True
                    return choice
            elif choice == 4:
                if grid[29]!=' ':
                    print('Column is full. Choose another one')
                    available = False
                else:
                    available = True
                    return choice
            elif choice == 5:
                if grid[35]!=' ':
                    print('Column is full. Choose another one')
                    available = False
                else:
                    available = True
                    return choice
            else:
                if grid[41]!=' ':
                    print('Column is full. Choose another one')
                    available = False
                else:
                    available = True
                    return choice


# In[ ]:


def check_win(grid,mark):

    def check_vertical_win(grid, mark):

        for row in range(0, 3):
            if (grid[row] == mark and
                    grid[row + 1] == mark and
                    grid[row + 2] == mark and
                    grid[row + 3] == mark):
                return True
            return False

        for row in range(6, 9):
            if (grid[row] == mark and
                    grid[row + 1] == mark and
                    grid[row + 2] == mark and
                    grid[row + 3] == mark):
                return True
            return False

        for row in range(12, 15):
            if (grid[row] == mark and
                    grid[row + 1] == mark and
                    grid[row + 2] == mark and
                    grid[row + 3] == mark):
                return True
            return False

        for row in range(18, 21):
            if (grid[row] == mark and
                    grid[row + 1] == mark and
                    grid[row + 2] == mark and
                    grid[row + 3] == mark):
                return True
            return False

        for row in range(24, 27):
            if (grid[row] == mark and
                    grid[row + 1] == mark and
                    grid[row + 2] == mark and
                    grid[row + 3] == mark):
                return True
            return False

        for row in range(30, 33):
            if (grid[row] == mark and
                    grid[row + 1] == mark and
                    grid[row + 2] == mark and
                    grid[row + 3] == mark):
                return True
            return False

        for row in range(36, 39):
            if (grid[row] == mark and
                    grid[row + 1] == mark and
                    grid[row + 2] == mark and
                    grid[row + 3] == mark):
                return True
            return False

    def check_horizontal_win(grid, mark):

        if ((grid[0] == mark and
             grid[6] == mark and
             grid[12] == mark and
             grid[18] == mark)
            or
            (grid[1] == mark and
             grid[7] == mark and
             grid[13] == mark and
             grid[19] == mark)
             or
             (grid[2] == mark and
             grid[8] == mark and
             grid[14] == mark and
             grid[20] == mark)

             or
             (grid[3] == mark and
             grid[9] == mark and
             grid[15] == mark and
             grid[21] == mark)
             or
             (grid[4] == mark and
             grid[10] == mark and
             grid[16] == mark and
             grid[22] == mark)
             or
             (grid[5] == mark and
             grid[11] == mark and
             grid[17] == mark and
             grid[23] == mark)
             or
             (grid[6] == mark and
             grid[12] == mark and
             grid[18] == mark and
             grid[24] == mark)
             or
             (grid[7] == mark and
             grid[13] == mark and
             grid[19] == mark and
             grid[25] == mark)
                or
                (grid[8] == mark and
                 grid[14] == mark and
                 grid[20] == mark and
                 grid[26] == mark)
                or
                (grid[9] == mark and
                 grid[15] == mark and
                 grid[21] == mark and
                 grid[27] == mark)
                or
                (grid[10] == mark and
                 grid[16] == mark and
                 grid[22] == mark and
                 grid[28] == mark)
                or
                (grid[11] == mark and
                 grid[17] == mark and
                 grid[23] == mark and
                 grid[29] == mark)
                or
                (grid[12] == mark and
                 grid[18] == mark and
                 grid[24] == mark and
                 grid[30] == mark)
                or
                (grid[13] == mark and
                 grid[19] == mark and
                 grid[25] == mark and
                 grid[31] == mark)
                or
                (grid[14] == mark and
                 grid[20] == mark and
                 grid[26] == mark and
                 grid[32] == mark)
                or
                (grid[15] == mark and
                 grid[21] == mark and
                 grid[27] == mark and
                 grid[33] == mark)
                or
                (grid[16] == mark and
                 grid[22] == mark and
                 grid[28] == mark and
                 grid[34] == mark)
                or
                (grid[17] == mark and
                 grid[23] == mark and
                 grid[29] == mark and
                 grid[35] == mark)
                or
                (grid[18] == mark and
                 grid[24] == mark and
                 grid[30] == mark and
                 grid[36] == mark)
                or
                (grid[19] == mark and
                 grid[25] == mark and
                 grid[31] == mark and
                 grid[37] == mark)
                or
                (grid[20] == mark and
                 grid[26] == mark and
                 grid[32] == mark and
                 grid[38] == mark)
                or
                (grid[21] == mark and
                 grid[27] == mark and
                 grid[33] == mark and
                 grid[39] == mark)
                or
                (grid[22] == mark and
                 grid[28] == mark and
                 grid[34] == mark and
                 grid[40] == mark)
                or
                (grid[23] == mark and
                 grid[29] == mark and
                 grid[35] == mark and
                 grid[41] == mark)):
            return True
        return False

    def check_diagonal_win(grid, mark):

        if ((grid[2] == mark and
            grid[9] == mark and
             grid[16] == mark and
             grid[23] == mark)
                or
                (grid[1] == mark and
                 grid[8] == mark and
                 grid[15] == mark and
                 grid[22] == mark)
                or
                (grid[8] == mark and
                 grid[15] == mark and
                 grid[22] == mark and
                 grid[29] == mark)
                or
                (grid[0] == mark and
                 grid[7] == mark and
                 grid[14] == mark and
                 grid[21] == mark)
                or
                (grid[7] == mark and
                 grid[14] == mark and
                 grid[21] == mark and
                 grid[28] == mark)
                or
                (grid[14] == mark and
                 grid[21] == mark and
                 grid[28] == mark and
                 grid[35] == mark)
                or
                (grid[6] == mark and
                 grid[13] == mark and
                 grid[20] == mark and
                 grid[27] == mark)
                or
                (grid[13] == mark and
                 grid[20] == mark and
                 grid[27] == mark and
                 grid[34] == mark)
                or
                (grid[20] == mark and
                 grid[27] == mark and
                 grid[34] == mark and
                 grid[41] == mark)
                or
                (grid[12] == mark and
                 grid[19] == mark and
                 grid[26] == mark and
                 grid[33] == mark)
                or
                (grid[19] == mark and
                 grid[26] == mark and
                 grid[33] == mark and
                 grid[40] == mark)
                or
                (grid[18] == mark and
                 grid[25] == mark and
                 grid[32] == mark and
                 grid[39] == mark)
                or
                (grid[3] == mark and
                 grid[8] == mark and
                 grid[13] == mark and
                 grid[18] == mark)
                or
                (grid[4] == mark and
                 grid[9] == mark and
                 grid[14] == mark and
                 grid[19] == mark)
                or
                (grid[9] == mark and
                 grid[14] == mark and
                 grid[19] == mark and
                 grid[24] == mark)
                or
                (grid[5] == mark and
                 grid[10] == mark and
                 grid[15] == mark and
                 grid[20] == mark)
                or
                (grid[10] == mark and
                 grid[15] == mark and
                 grid[20] == mark and
                 grid[25] == mark)
                or
                (grid[15] == mark and
                 grid[20] == mark and
                 grid[25] == mark and
                 grid[30] == mark)
                or
                (grid[11] == mark and
                 grid[16] == mark and
                 grid[21] == mark and
                 grid[26] == mark)
                or
                (grid[16] == mark and
                 grid[21] == mark and
                 grid[26] == mark and
                 grid[31] == mark)
                or
                (grid[21] == mark and
                 grid[26] == mark and
                 grid[31] == mark and
                 grid[36] == mark)
                or
                (grid[17] == mark and
                 grid[22] == mark and
                 grid[27] == mark and
                 grid[32] == mark)
                or
                (grid[22] == mark and
                 grid[27] == mark and
                 grid[32] == mark and
                 grid[37] == mark)
                or
                (grid[23] == mark and
                 grid[28] == mark and
                 grid[33] == mark and
                 grid[38] == mark)):
            return True
        return False

    if (check_vertical_win(grid, mark) == True) or (check_diagonal_win(grid, mark) == True) or (check_horizontal_win(grid, mark) == True):
        return True
    return False


# In[ ]:


def replay():

    choice = ''

    while choice not in ['Yes', 'No']:

        choice = input('Do you want to replay? (Yes/No): ')

        if choice not in ['Yes', 'No']:
            print('Yes or No only')

    if choice == 'Yes':
        return True
    else:
        print('Thanks for playing')
        return False


# In[ ]:


def connect_four():
    
    while True:

        print('Welcome to CONNECT 4')

        mygrid = [' '] * 42

        player1 = player_mark()

        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

        display_grid(mygrid)

        current_mark = player1

        game_on = True

        while game_on:

            print(f'Player {current_mark} turn')

            col = user_column(mygrid)

            drop_disc(mygrid, current_mark, col)

            display_grid(mygrid)

            if check_win(mygrid, current_mark):

                print(f'player {current_mark} won!')
                game_on = False

            elif ' ' not in mygrid:

                print('Tie!')
                game_on = False

            else:

                if current_mark == player1:
                    current_mark = player2
                else:
                    current_mark = player1

        if not replay():
            break
            
            
connect_four()

