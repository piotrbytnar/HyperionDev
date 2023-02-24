# SE T26 - TASK #1

#=====importing libraries===========

from datetime import date
import os

#=======FUNCTIONS DEFINITIONS========

#New user registration

def reg_user():
    u_name = []
    passwords = []

    with open('user.txt', 'r') as login_det:
        
        for lines in login_det:
            log_list = lines.strip()
            log_list = log_list.split(', ')

            u_name.append(log_list[0])

    new_u_name = input('Type in your username: ').lower()

    while new_u_name in u_name:
        print('This username is already taken!')
        new_u_name = input('Type in your username, again: ').lower()

    new_u_password = input('Type in your password: ')
    new_u_pass_conf = input('Confirm your password: ')

    if new_u_password != new_u_pass_conf:
        print('This passwords do not match!')
        new_u_password = input('Type in your password: ')
        new_u_pass_conf = input('Confirm your password: ')

    else:
        login_det = open("user.txt", 'a')
        login_det.write(f'\n{new_u_name}, {new_u_password}')
        login_det.close()
    login_det.close()
    print('Your input is complete, what do you want to do now?\n')

# TASK ADDITION

def add_task():
    print('The following mode will promt you for the entry of the new tasks')
    nt_uname = input('Who does the task - enter username: ').lower()
    task_n = input('What is the task title: ').lower()
    task_d = input('What is the task about: ').lower()
    task_cd = date.today()
    print('What is the deadline?')
    task_dd = input('Year - yyyy: ') + input('Month - mm: ') + input('Day - dd: ')
    task_dd_check = task_dd.isdigit()
    task_dd_len = len(task_dd)
    task_stat = 'no'

    while task_dd_len != 8 or task_dd_check != True:
        print('The format you input is incorrect, make sure to provide numbers in the format as specified') #further input fail proofing will be required, eg:
                                                                                                            #by year month and day. Or input of the callendar module in GUI.
        task_dd = input('Year - yyyy: ') + input('Month - mm: ') + input('Day - dd: ')
        task_dd_check = task_dd.isdigit()
        task_dd_len = len(str(task_dd))
    else: 

        tasks_dd_yyyy = task_dd[0:4]
        tasks_dd_mm = task_dd[4:6]
        task_dd_dd = task_dd[6:]
        task_dd_format = f'{tasks_dd_yyyy}-{tasks_dd_mm}-{task_dd_dd}'

        tasks_add = open("tasks.txt", 'a')
        tasks_add.write(f'\n{nt_uname}, {task_n}, {task_d}, {task_cd}, {task_dd_format}, {task_stat}')
        tasks_add.close()
        print('Your input is complete, what do you want to do now?\n')

# TASK VIEWER

def view_all():
    tasks_read = open('tasks.txt', 'r')
    tasks = tasks_read.readlines()

    for pos, line in enumerate(tasks, 1):
        split_lines = line.split(', ')

        format = f'═══════════ ◄ {pos} ► ═══════════\n'
        format += '\n'
        format += f'Username:    {split_lines[0]}\n'
        format += f'Task:        {split_lines[1]}\n'
        format += f'Description: {split_lines[2]}\n'
        format += f'Start Date:  {split_lines[3]}\n'
        format += f'Deadline:    {split_lines[4]}\n'
        format += f'Completed?:  {split_lines[5]}\n' 
        format += '\n'
        print(format)
    tasks_read.close()
    print('These are the tasks, what do you want to do now?\n')

#USER TASKS VIEWER

def view_mine():

    tasks_read = open('tasks.txt', 'r')
    tasks = tasks_read.readlines()
    n = 0
    mine_tasks = {}   
    for line in tasks:              
        split_lines = line.split(', ')
        split_lines = [y.replace('\n', '') for y in split_lines]
        if split_lines[0] == name_check:
            n += 1           
            mine_tasks[n] = split_lines   
            format = f'════════◄ {n} ►══════════════\n'                
            format += '\n'
            format += f'Username:    {split_lines[0]}\n'
            format += f'Task:        {split_lines[1]}\n'
            format += f'Description: {split_lines[2]}\n'
            format += f'Start Date:  {split_lines[3]}\n'
            format += f'Deadline:    {split_lines[4]}\n'
            format += f'Completed?:  {split_lines[5]}'
            format += '\n'
            print(format)
                             
    tasks_read.close()    
    print('These are your tasks, what do you want to do now?\n')
    return mine_tasks

#REPORTS GENERATOR

def gen_rep_tasks():
    
    with open('tasks.txt', 'r') as tasks:
        tasks = tasks.readlines()
        tasks = [y.replace('\n', '') for y in tasks]
        tasks_list = []
        for line in tasks:
            spl_file = line.strip('')
            spl_file = line.split(', ')
            tasks_list.append(spl_file)

        tasks_num = len(tasks_list)
        
        yes_n = 0
        no_n = 0
        over_n = 0
        for pos in range(0,tasks_num):
            if tasks_list[pos][5] == 'yes':
                yes_n += 1
            if tasks_list[pos][5] == 'no':
                no_n += 1
            if tasks_list[pos][4] < str(date.today()):
                over_n += 1 
            else:
                continue

    inc_per = no_n / tasks_num * 100 
    over_per = over_n / tasks_num * 100 
    with open('tasks_overview.txt', 'w', encoding='utf-8') as tasks_overview:
        tasks_overview.write(f'''
                ╠ TAKS OVERVIEW REPORT ╣

NUMBER OF TASKS           ║             {tasks_num}
COMPLETED TASKS           ║             {yes_n}
REMAINING TASKS           ║             {no_n}
OVERDUE TASKS             ║             {over_n}
INCOMPLETE [%]            ║             {round(inc_per, 1)}%
OVERDUE [%]               ║             {round(over_per, 1)}%
''')
    return [tasks_num, tasks_list]

def gen_rep_user():

    tasks_num, tasks_list = gen_rep_tasks()
    
    with open('user.txt', 'r') as users:
        users = users.readlines()
        users = [y.replace('\n', '') for y in users]
        users_list = []
        
        for line in users:
            uspl_file = line.strip('')
            uspl_file = line.split(', ')
            users_list.append(uspl_file[0])
        users_num = len(users_list)
       
    per_user_dic = {} 
    pos = 0
    for user in range(0, len(users_list)):
        per_user_dic[users_list[user]]= [] 

    for tasks in range(0, tasks_num):
        if tasks_list[tasks][0] == users_list[pos]:
            per_user_dic[users_list[pos]] += [tasks_list[tasks]]
        else:
            pos += 1
            per_user_dic[users_list[pos]] += [tasks_list[tasks]]
   
    users_overview = open('users_overview.txt', 'w', encoding='utf-8') 
    users_overview.write(f'''
                        ╠ USERS OVERVIEW REPORT ╣

        NUMBER OF USERS            ║              {users_num}
        NUMBER OF TASKS            ║              {tasks_num}
        ''')    
     
    keys_list = list(per_user_dic.keys())
    for users in range(0,len(keys_list)):
        user = keys_list[users]
        user_upp = f'{user}'.upper()
        num_task = len(per_user_dic.get(user))
        dic_tasks = per_user_dic.get(user)
        perc_tot = round(num_task / tasks_num * 100, 1)
        
        yes_n = 0
        no_n = 0
        over_n = 0
        for pos in range(0, num_task):
            if dic_tasks[pos][5] == 'yes':
                yes_n += 1
            if dic_tasks[pos][5] == 'no':
                no_n += 1
            if dic_tasks[pos][4] < str(date.today()):
                over_n += 1 
            else:
                continue

        inc_per = no_n / num_task * 100 
        over_per = over_n / num_task * 100 

        users_overview.write(f'''\n
        {user_upp}
        NUMBER OF TASKS ASSIGNED TO THE USER                - {num_task}
        PERCENTAGE OF THE TOTAL TASKS ASSIGNED TO THE USER  - {perc_tot}%
        USER's COMPLETION PERCENTAGE                        - {100 - inc_per}%
        USER's INCOMPLETION PERCENTAGE                      - {inc_per}%
        USER's OVERDUE TASKS PERCENTAGE                     - {over_per}%                     
        ''')
    
    users_overview.close()

#STATISTICS DISPLAY

def dis_stat():
    to = 'tasks_overview.txt'
    uo = 'users_overview.txt'
    to_chck = os.path.exists(to)
    uo_chck = os.path.exists(uo)

    if to_chck == True and uo_chck == True:
        tasks = open('tasks_overview.txt', 'r', encoding='utf-8')
        taskss = [y.replace('\n', '') for y in tasks]
        for line in taskss:
            print(line)
        tasks.close()
    
        users = open('users_overview.txt', 'r', encoding='utf-8')
        userss = [y.replace('\n', '') for y in users]
        for line in userss:
            print(line)
        users.close()
                

    else:
        gen_rep_tasks()
        gen_rep_user()
        
        tasks = open('tasks_overview.txt', 'r', encoding='utf-8')
        taskss = [y.replace('\n', '') for y in tasks]
        for line in taskss:
            print(line)
        tasks.close()
    
        users = open('users_overview.txt', 'r', encoding='utf-8')
        userss = [y.replace('\n', '') for y in users]
        for line in userss:
            print(line)
        users.close()

#====Login Section====

    '''Softwere introduces itself to user and prompts for login.
    It then opens the username text file and evaluates the existing data and compars it with the user input.
    If incorrect input the user is prompted for retry.
    Following correct input the program continous to menu.
    '''

print('\n WELCOME TO THE TASKS MANAGEMENT SOFTWARE \nPlease provide your credentials to log in.')

u_name = []
passwords = []

with open('user.txt', 'r') as login_det:
    line_data = login_det.readlines()

     
    for line in line_data:
        spl_l_dat = line.strip('')
        spl_l_dat = line.split(', ')
 
        u_name.append(spl_l_dat[0])
        passwords.append(spl_l_dat[1].replace('\n', ''))

login_det.close()

name_check = input('Type in your username: ')
pass_check = input('Type in your password: ')
while True:
    
    if name_check in u_name: break      
    while name_check not in u_name:
        print('You have provided an incorrect username!')
        name_check = input('Type in your username, again: ')

    nam_pos = u_name.index(name_check)  

    if pass_check in passwords[nam_pos]: break
    while pass_check not in passwords[nam_pos]:
        print('You have provided an incorrect password!')
        pass_check = input('Type in your password, again: ')

#====Menu Section====
''' Softwere prompts for input and lower case it. 
    If input is correct the further lines of code are being used depending on the selction
    Otherwise the program promts for reinput
'''
while True:
    if name_check != 'admin':
        menu = input('''\nPlease select one of the following options, by typing below:
    r  - Registering a user
    a  - Adding a task
    va - View all tasks
    vm - view my task
    e  - Exit
    ''').lower()
    if name_check == 'admin':
        menu = input('''\nPlease select one of the following options, by typing below:
    r  - Registering a user
    a  - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - display statistics
    e  - Exit
    ''').lower()

#====Registration Section====

    ''' Softwere reads from the file and compares input with the existing
        If existing it prompts for new input otherwise it registers the user
    '''
    if menu == 'r':
        reg_user()
        
#====Task Addition Section====

        ''' Softwere prompts user for input and writes it in the file.
            Software fromats the data input to match the format of the data module and the required output.
        '''       
    elif menu == 'a':
        add_task()
    
#====Tasks List Section====

        ''' Softwere reads the content of the file and prints out its content
        '''

    elif menu == 'va':
        view_all()

#====User Tasks List Section====

        ''' Softwere reads the content of the file and prints out its content 
            Only the user assign content is being shown.
        '''

    elif menu == 'vm':
        view_mine()
        tasks = view_mine()
        while True:

            options = int(input(f''' YOU HAVE THE FOLLOWING OPTIONS:
            ○ To change the task description or the completion status, choose the number of the task you want to change between 1 and {len(tasks)}
            ○ To return to the main menu, type -1
            '''))
            if options == -1: break
            
            elif options >= 1 and options <= (len(tasks)):
                
                while True:
                    stat_des_op = input(f'''
                To change the task completion status, type in YES or NO 
                To change the task description or the username, type in EDIT

                (Note: Completed tasks cannot be edited. To edit a complited task
                you will need to first change the status of the completion to "NO")
                ''').lower()                        
                    if stat_des_op == 'yes' or stat_des_op == 'no':
                        stat_chg = tasks[options]
                        stat_chg[5] = stat_des_op
                        break
                        
                    elif stat_des_op == 'edit':
                        stat_chg = tasks[options]
                        if stat_chg[5] == 'yes':
                            print('You cannot change the completed task')
                            break
                        else:
                            while True:
                                name_o_des = (input(f'''
                TYPE:
                1 - to change the username
                2 - to change the description
                '''))
                                if name_o_des == '1':
                                    stat_chg = tasks[options]
                                    stat_chg[0] = input('New Username:')
                                    break
                                
                                elif name_o_des == '2':
                                    stat_chg = tasks[options]
                                    stat_chg[2] = input('New description:')
                                    break
                                else:
                                    print('Incorrect Input - 1 or 2 valid only.')
                                    continue
                                                            
                    else: 
                        print('Wrong input, try again!: ')
                                                
            else:
                print(f'You have provided wrong input\n Make sure to either type in (-1) or a whole number between 1 and {len(tasks)}')

        #replace the changed parts in txt

        with open('tasks.txt', 'r') as file_update:
            file = file_update.readlines()
            file = [y.replace('\n', '') for y in file]
            file_list = []
            for line in file:
                spl_file = line.strip('')
                spl_file = line.split(', ')
                file_list.append(spl_file)
        
        n = 0
        d_n = 1
        for pos in file_list:
            if file_list[n][0] == name_check:
                file_list[n] = tasks[d_n]
                n += 1
                d_n += 1
                
            else:
                n += 1
        
        with open('tasks.txt', 'w') as file_update:        
            for pos in file_list:
                pos = ', '.join(pos)
                file_update.write(f'{pos}\n')    

#====Generate Reports====
    
    elif menu == 'gr':
        gen_rep_tasks()
        gen_rep_user()

#====Display Statistics===
    
    elif menu == 'ds':
        dis_stat()  


#====END====  

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")