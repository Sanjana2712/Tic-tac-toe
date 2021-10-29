while True:
 print("Turn to choose for", cur_player)
 print("Enter 1 for X")
 print("Enter 2 for O")
 print("Enter 3 to Quit")
 try:
 choice = int(input())
 except ValueError:
 print("Wrong Input!!! Try Again\n")
 continue
 if choice == 1:
 player_choice['X'] = cur_player
 if cur_player == player1:
 player_choice['O'] = player2
 else:
 player_choice['O'] = player1
 elif choice == 2:
 player_choice['O'] = cur_player
 if cur_player == player1:
 player_choice['X'] = player2
 else:
 player_choice['X'] = player1

 elif choice == 3:
 print("Final Scores")
 print_scoreboard(score_board)
 break
 else:
 print("Wrong Choice!!!! Try Again\n")
 winner = single_game(options[choice-1])

 if winner != 'D' :
 player_won = player_choice[winner]
 score_board[player_won] = score_board[player_won] + 1
 print_scoreboard(score_board)
 if cur_player == player1:
 cur_player = player2
 else:
 cur_player = player1
