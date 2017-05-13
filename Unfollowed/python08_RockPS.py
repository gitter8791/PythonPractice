#RPS

print ('Two player rps game\n')

Player1 = input ('Player 1 enter r/p/s:')
Player2 = input ('Player 2 enter r/p/s:')

if Player1 == Player2:
	print ('Tie')
elif Player1 == 'r' and Player2 == 's':
	print ('Palyer 1 wins')
elif Player1 =='p' and Player2 =='r':
	print ('Palyer 1 wins')
elif Player1 =='s' and Player2 =='p':
	print ('Palyer 1 wins')
else: print ('Player 2 wins!')

