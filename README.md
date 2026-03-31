Algorithm:

1) Start Program
2)Initialize GUI window with title, buttons, labels, and scoreboard.
3)Set current player = X and scores = 0.
4$Display empty 3×3 grid buttons.
5)Wait for Player Click on a button:
If button is empty:
Fill it with the current player symbol (X or O).
Change text color based on player.
Check for winner:
If winner exists:
Highlight winning combination.
Update score.
Show message box with winner.
Disable all buttons.
Else, check for draw:
If all buttons filled and no winner:
Show message box “Draw”.
Disable buttons.
Switch player (X ↔ O) and update turn label.
Else, ignore click (invalid move).
6)Restart Button Clicked:
Reset all buttons to empty and normal state.
Reset turn to X (scores remain).
7)Repeat steps 5–6 until program is closed.
8)End Program
