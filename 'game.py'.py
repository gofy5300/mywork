# coding: utf-8
play=True 

while play:
    game()
    print('.....')
    again=input('play again?')
    if again=='no':
        play=False
get_ipython().run_line_magic('save', "'game.py' 132 133")
