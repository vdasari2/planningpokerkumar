import argparse
import json
from logging import root
from numpy import tile
import requests
import time
import tkinter as tk
from cmd import Cmd
from fastapi import status
from pathlib import Path
from tkinter import *
from tkinter import messagebox


class MyPrompt(Cmd):
    def help_screen():
        help_window = Tk()
        
        #text=Text(root)
        help_window.title("Help Screen")
        help_window.configure(bg='gray')

        EOF_label = Label(help_window, text = "1. add_player - This is used to register player's to the game")
        EOF_label.grid(column = 10, row = 10)

        new_game_lbl = Label(help_window, text = "2. new_game - Used to start a new game by dealer")
        new_game_lbl.grid(column = 10, row = 20)

        add_player_label = Label(help_window, text = "3. add_issues - To add the issues for the current game")
        add_player_label.grid(column = 10, row = 30)

        current_players_lbl = Label(help_window, text = "4. current_players - Used to display the list of current players any Team Member can run")
        current_players_lbl.grid(column = 10, row = 40)

        EOF_lbl = Label(help_window, text = "5. EOF - This is used to exit from the planning poker game")
        EOF_lbl.grid(column = 10, row = 50)

        current_issue_lbl = Label(help_window, text = "6. current_issue - This is used for displaying the current issue")
        current_issue_lbl.grid(column = 10, row = 60)

        voting_system_lbl = Label(help_window, text = "7. voting_system - To see the voting system to be used in the game, a user can run this command")
        voting_system_lbl.grid(column = 10, row = 70)

        next_issue_lbl = Label(help_window, text = "8. next_issue - This is used to go to the next issue")
        next_issue_lbl.grid(column = 10, row = 80)

        previous_issue_lbl = Label(help_window, text = "9. previous_issue - This is used to go to the previous issue")
        previous_issue_lbl.grid(column = 10, row = 90)

        vote_issue_lbl = Label(help_window, text = "10. vote_issue - For voting on the current issue")
        vote_issue_lbl.grid(column = 10, row = 100)

        exit_lbl = Label(help_window, text = "11. exit - This is used to exit from the planning poker game")
        exit_lbl.grid(column = 10, row = 110)

        help_lbl = Label(help_window, text = "12. help - Each player can run help to see which commands are available and documented.")
        help_lbl.grid(column = 10, row = 120)

        user_count_lbl = Label(help_window, text = "13. user_count - This is used to show the number of players in the game")
        user_count_lbl.grid(column = 10, row = 130)

        show_report_lbl = Label(help_window, text = "14. show_report - Used to show For showing the final report on the current issue")
        show_report_lbl.grid(column = 10, row = 140)

        reset_votes_lbl = Label(help_window, text = "15. re set_votes - This is used to reset the votes of an issue")
        reset_votes_lbl.grid(column = 10, row = 150)

        remove_player_lbl = Label(help_window, text = "16. remove_player - This is used to remove player's from the game")
        remove_player_lbl.grid(column = 10, row = 160)

        current_dealer_lbl = Label(help_window, text = "17. current_dealer - This is used to display the current dealer")
        current_dealer_lbl.grid(column = 10, row = 170)

        help_window.mainloop()

    


    
    
    def start_screen():
        
        start_window = Tk()
        start_window.title("Start Screen")
        start_window.geometry('1000x600')
        start_window.configure(bg='gray')
        
        
        labe1 = LabelFrame(start_window, text = 'Welcome! This is the starting page of planning poker')
        labe1.pack(expand = 'yes', fill = 'both')

 


        def do_add_player():
            #self.username=username
            player_window=Tk()
            player_window.title("Planning poker App")
            player_window.geometry("1000x600")
            player_window.configure(bg='gray')

            def submitaddplayer(): 
                print("name",name_entry.get())
                players.append(name_entry.get())
                print(players)
                tk.messagebox.showinfo("Message",  "You have registered as a player "+name_entry.get())
                
                showNames()

            def showNames():

                for i in range(len(players)):
                    txt = tk.Text(player_window,height="1",width="20", bd=8, relief="groove",font=('arial', 15, 'bold'))
                    txt.grid(row=5,column=i)
                    txt.insert(tk.END,players[i])

            name_label = tk.Label(player_window, text = 'Player Name', fg="white", bg="orange",relief="groove", font=('arial',15, 'bold'))
            name_label.grid(row=0,column=0)

            name_entry = tk.Entry(player_window,font=('roman',15,'normal'))
            name_entry.grid(row=0,column=1)


            sub_btn=tk.Button(player_window,text = 'ADD',height="1",width="20", bd=8, font=('arial', 15, 'bold'), relief="groove", fg="green",
            bg="blue",command = submitaddplayer)
            sub_btn.grid(row=2,column=0)
            

            exit_btn1=tk.Button(player_window,text='EXIT', height="1",width="20", bd=8, font=('arial', 15, 'bold'), relief="groove", fg="red",command=quit)
            exit_btn1.grid(row=2,column=1)

            player_window.mainloop()


    
        

        def view_players():
            players_window= Tk()
            players_window.title("Current List of Players")
            players_window.geometry('1000x600')
            players_window.configure(bg='gray')
            view_players_window_label = Label (players_window, text = "List of players",font=('arial', 10, 'bold'), relief="groove", fg="green",)
            view_players_window_label.grid(row = 100, column = 100)
            
            print(players)
            a = len(players)
            et = ''
            for i in range(a):
                et = et + players[i]+'\n' 
                EOF_lbl1 = Label(players_window, text = et,font=('arial', 12, 'bold'), relief="groove", fg="green")
                EOF_lbl1.grid(column = 100, row = 300)

                print(et)
           

            btn12=Button(players_window,text = 'CLOSE',font=('arial', 12, 'bold'), relief="groove", fg="red",command=quit)
            btn12.grid(row=400,column=500)

            players_window.mainloop()


        def get_current_dealer():
 
            if len(players)!=0:
                messagebox.showinfo("Current Dealer", "The current dealer is " +players[0])

            else:

                messagebox.showinfo("Current Dealer", "Please add players ")            
        def user_count():
            z=len(players)
            user_count_players= Tk()
            user_count_players.title("Total Number of Players")
            user_count_players.geometry('1000x600')
            user_count_players.configure(bg='gray')
            view_players_window_label = Label (user_count_players, text =z,font=('arial', 10, 'bold'), relief="groove", fg="green",)
            view_players_window_label.grid(row = 100, column = 100)
            user_count_players.mainloop()         



        players=[] 
        title=[]  
        desc=[]
        addplayer=tk.StringVar()
        addvalue=tk.StringVar()
        
        btn3=Button(labe1,text = 'ADD PLAYER',font=('arial', 12, 'bold'), relief="groove", fg="green",command=do_add_player)
        btn3.grid(row=200,column=500)

        btn5=Button(labe1,text = 'VIEW CURRENT PLAYERS', font=('arial', 12, 'bold'), relief="groove", fg="green", command = view_players)
        btn5.grid(row=300,column=500)
        
        btn10=Button(labe1,text = 'DISPLAY CURRENT DEALER', font=('arial', 12, 'bold'), relief="groove", fg="green", command = get_current_dealer)
        btn10.grid(row=400,column=500)
        btn10=Button(labe1,text = 'DISPLAY CURRENT USER COUNT', font=('arial', 12, 'bold'), relief="groove", fg="green", command = user_count)
        btn10.grid(row=500,column=500)

        
        start_window.mainloop()
    
    
    prompt = 'planning_poker> '
    intro = "Welcome to a nice game of Planning Poker!\nType ? to list commands"
    root = tk.Tk()
    root.geometry('1000x600')
    root.configure(bg='gray')
    
    label_frame = LabelFrame(root, text = 'Click "START" button to start the game. Click on "HELP" button to know the commands.')
    label_frame.pack(expand = 'yes', fill = 'both')

    btn2=tk.Button(root,text='HELP', height="1",width="15", bd=8, font=('arial', 15, 'bold'), relief="groove", fg="red",command=help_screen)
    btn2.place(x = 400, y = 200)
    btn1=tk.Button(root,text='START', height="1",width="15", bd=8, font=('arial', 15, 'bold'), relief="groove", fg="green",command=start_screen)
    btn1.place(x = 200, y = 200)

    
    mainloop()

    default_config_params = {"max_retries": 5,
                             "show_timeout": 1,
                             "url": "http://localhost:8000"}
    default_keys_set = set(default_config_params.keys())

    def __init__(self, **config_params):
        super().__init__()
        self.username = None

        keys_set = set(config_params.keys())
        common_config_keys = self.default_keys_set.intersection(keys_set)
        difference_config_keys = self.default_keys_set.difference(keys_set)

        if len(difference_config_keys) == 0:
            for config_key, config_value in config_params.items():
                setattr(self, config_key, config_value)
        else:
            if len(difference_config_keys) < len(self.default_keys_set):
                print("Not all parameters found in configuration file.")
                for config_key in common_config_keys:
                    setattr(self, config_key, config_params[config_key])
            print(f"Using default value for {difference_config_keys}")
            for config_key in difference_config_keys:
                setattr(self, config_key,
                        self.default_config_params[config_key])

    def default(self, inp):
        """
        You can also use x or q to exit the game. All commands that are
        not implemented will just be printed with a notification
        message.
        """
        if inp == 'x' or inp == 'q':
            return self.do_exit()

        print(f"Haven't found this command: {inp}")

    @staticmethod
    def print_error_response(response):
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            print(f"{json.loads(response.text)['detail']}")
        elif response.status_code == status.HTTP_412_PRECONDITION_FAILED:
            print(f"{json.loads(response.text)['detail']}")
        elif response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY:
            message = json.loads(response.text)['detail'][0]['msg']
            print(f"{message.capitalize()}")
        else:
            print(f"{response.text}")

    @staticmethod
    def print_issue(response):
        crt_issue_title = response['result_message']['title']
        crt_issue_description = response['result_message']['description']
        print(f"'{crt_issue_title}' is the current issue.")
        if len(crt_issue_description) > 0:
            print(f"{crt_issue_description}")

    @staticmethod
    def parse_report(report):
        for vote_value, vote_details in report.items():
            print(f"{vote_details['vote_count']} voted for {vote_value} "
                  f"story points.\n"
                  f"{json.dumps(vote_details['voters'], indent=4)}\n")

    def get_report(self, inp):
        current_status = 'pending'
        retry_count = 0
        while current_status == 'pending' and retry_count < self.max_retries:
            response = self.send_request(method='get',
                                         route='/issue/show_results')
            if response.status_code == status.HTTP_200_OK:
                response_message = json.loads(response.text)['result_message']
                current_status = response_message['status']
                if current_status == 'done':
                    self.parse_report(response_message['report'])
            else:
                current_status = 'error'
                self.print_error_response(response)
            retry_count += 1
            time.sleep(self.show_timeout)

    def send_request(self, method, route, params=None, data=None):
        full_uri = ''.join([self.url, route])
        response = requests.request(method=method, url=full_uri,
                                    params=params, json=data)
        return response

    def do_add_player(self, username):
        """
        Add a player to the current game
        """
        current_players = []

        response = self.send_request(method='get',
                                     route='/user/show_all')

        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            current_players = response_dict['result_message']['current_users']
        else:
            self.print_error_response(response)

        if self.username and self.username in current_players:
            print(f"You already have a username in the current game: "
                  f"{self.username}")
        else:
            crt_dict = {
                'name': username
            }
            response = self.send_request(method='post',
                                         route='/user/add',
                                         data=crt_dict)
            if response.status_code == status.HTTP_200_OK:
                self.username = username
                print(f"Player {self.username} has been added to the current "
                      f"game")
            else:
                self.print_error_response(response)

    def do_current_dealer(self, inp):
        """
        Show current dealer
        """
        response = self.send_request(method='get',
                                     route='/game/get_dealer')
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            print(f"Current dealer is "
                  f"{response_dict['result_message']['current_dealer']}")
        else:
            self.print_error_response(response)

    def do_current_issue(self, inp):
        """
        Show issue that players are voting on now
        """
        response = self.send_request(method='get',
                                     route='/issue/current')
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            self.print_issue(response_dict)
        else:
            self.print_error_response(response)

    def do_current_players(self, inp):
        """
        Show players that are registered for the current game
        """
        response = self.send_request(method='get',
                                     route='/user/show_all')
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            current_users = response_dict['result_message']['current_users']
            if len(current_users) == 0:
                print("Please add players to the game")
            else:
                print(f"Currently playing Planning Poker: "
                      f"{json.dumps(current_users)}")
        else:
            self.print_error_response(response)

    def do_current_votes(self, inp):
        """
        Show if all players voted or who still has to vote
        """
        response = self.send_request(method='get',
                                     route='/issue/vote_status')
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            print(f"{response_dict['result_message']}")
        else:
            self.print_error_response(response)

    def do_exit(self):
        """
        Command for exiting planning poker game
        """

        crt_dict = {
            'name': self.username
        }

        response = self.send_request(method='post',
                                     route='/user/exit',
                                     data=crt_dict)
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            print(f"{response_dict['result_message']['user_exit_status']}")
        else:
            self.print_error_response(response)
        print(f"Buh-bye, {self.username}! And in case I don't see you again, "
              f"good afternoon, good evening and good night!")
        return True

    def do_new_game(self, inp):
        """
        Start new game
        """
        crt_dict = {
            'name': self.username
        }
        response = self.send_request(method='post',
                                     route='/game/new',
                                     data=crt_dict)
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            print(f"{response_dict['result_message']}")
        else:
            self.print_error_response(response)

    def do_next_issue(self, inp):
        """
        Jump to next issue, if there is one (i.e. the current issue
        is the last one and we can go back to programming)
        """

        crt_dict = {
            'name': self.username
        }

        response = self.send_request(method='post',
                                     route='/issue/next',
                                     data=crt_dict)
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            self.print_issue(response_dict)
        else:
            self.print_error_response(response)

    def do_previous_issue(self, inp):
        """
        Jump to previous issue, if there is one (i.e. we are not on
        the first issue)
        """

        crt_dict = {
            'name': self.username
        }

        response = self.send_request(method='post',
                                     route='/issue/previous',
                                     data=crt_dict)
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            self.print_issue(response_dict)
        else:
            self.print_error_response(response)

    def do_remove_player(self, username):
        """
        Remove a player from the current game
        """

        if len(username) < 4:
            print("Please use a more meaningful name")
        else:
            params_dict = {
                'username': username
            }
            data_dict = {
                'name': self.username
            }
            response = self.send_request(method='post',
                                         route='/user/remove',
                                         params=params_dict,
                                         data=data_dict)
            if response.status_code == status.HTTP_200_OK:
                response_dict = json.loads(response.text)
                print(f"{response_dict['result_message']}")
            else:
                self.print_error_response(response)

    def do_reset_votes(self, inp):
        """
        Reset votes on current issue
        """
        crt_dict = {
            'name': self.username
        }
        response = self.send_request(method='post',
                                     route='/issue/votes_reset',
                                     data=crt_dict)
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            print(f"{response_dict['result_message']}")
        else:
            self.print_error_response(response)

    def do_show_report(self, inp):
        """
        Show vote report for current issue
        """
        self.get_report(inp)

    def do_user_count(self, inp):
        """
        Show how many users are registered for the current game
        """
        response = self.send_request(method='get',
                                     route='/user/count')
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            user_count = response_dict['result_message']['user_count']
            if user_count == 1:
                verb = 'is'
            else:
                verb = 'are'
            print(f"Currently, there {verb} {user_count} registered "
                  f"players")
        else:
            self.print_error_response(response)

    def do_vote_issue(self, vote_value):
        """
        Vote on the current issue with the registered user here
        """
        crt_dict = {
            'name': self.username,
            'vote_value': vote_value
        }
        response = self.send_request(method='put',
                                     route='/issue/vote',
                                     data=crt_dict)
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            print(f"{response_dict['result_message']}")
        else:
            self.print_error_response(response)

    def do_voting_system(self, inp):
        """
        Show voting system for the current game
        """
        response = self.send_request(method='get',
                                     route='/game/voting_system')
        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            print(f"{response_dict['result_message']}")
        else:
            self.print_error_response(response)

    do_EOF = do_exit


if __name__ == '__main__':

    crt_config_params = {}
    config_path = Path('./configs/cli_config.json')

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", type=str,
                        help="Configuration file name")
    args = parser.parse_args()
    if args.config:
        config_path = Path(args.config)

    if config_path.exists():
        with open(config_path) as f:
            try:
                crt_config_params = json.load(f)
            except json.decoder.JSONDecodeError as je:
                print(f"Please make sure config file contains a dict in json "
                      f"format. An example can be found in "
                      f"'./configs/cli_config.json'. {je} was raised.")
    else:
        print(f"Please make sure the path {config_path} is correct and that "
              f"the file exists. Will use default configuration parameters "
              f"this time.")

    MyPrompt(**crt_config_params).cmdloop()
