import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import turtle
root=tk.Tk()
root.geometry("1000x600")
root.configure(bg='gray')

root.title("Planning poker App")
def help_screen():
        help_window = Tk()
        text=Text(root)
        help_window.title("Help Screen")

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

        reset_votes_lbl = Label(help_window, text = "15. reset_votes - This is used to reset the votes of an issue")
        reset_votes_lbl.grid(column = 10, row = 150)

        remove_player_lbl = Label(help_window, text = "16. remove_player - This is used to remove player's from the game")
        remove_player_lbl.grid(column = 10, row = 160)

        current_dealer_lbl = Label(help_window, text = "17. current_dealer - This is used to display the current dealer")
        current_dealer_lbl.grid(column = 10, row = 170)

        help_window.mainloop()
btn2=tk.Button(root,text='HELP', height="1",width="20", bd=8, font=('arial', 15, 'bold'), relief="groove", fg="yellow",command=help_screen)
btn2.grid(column = 1, row = 1)
mainloop()