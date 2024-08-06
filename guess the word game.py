import random
import csv
word_list= []
csv_file= open('guess.csv',mode = 'r')
word_reader= csv.reader(l.upper() for l in csv_file)

for row in word_reader:
    
    word_list += row


print("""
 ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba,  
a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    ""  
8b       88 88       88 8PP"""""""  `"Y8ba,   `"Y8ba,   
"8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I  
 `"YbbdP"Y8  `"YbbdP'Y8  `"Ybbd8"' `"YbbdP"' `"YbbdP"'  
 aa,    ,88                                             
  "Y8bbdP"      


 """)


choose_word= random.choice(word_list)
word = ""
for i in range(len(choose_word)):    
    if i % 2 == 0:
        word += choose_word[i]
    else:
        word += "_"
print("\n" + word)     

#NOW to we program it to be displayed as a game
chances = 5
game_over = False
correct_letter = []
correct_letter += word

print(f"""lives remaining ❤️   {chances}/5""")

while not game_over:
    guess = input("\nGuess a letter: ").upper()




    display=""
    

    
    for letter in choose_word:
            if letter == guess:
                display += letter
                correct_letter.append(guess)
            elif letter in correct_letter:
                 display += letter
            else:
                display += "_"

                
    
    if guess not in choose_word:
        chances -= 1


    print(display) 
    print(f"""lives remaining ❤️   {chances}/5""")




   

    if display == choose_word:
            game_over = True
            print("""
                                                  ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //           .--------.
              ,-.//          .: : :  :___`.
              `--'         .'!!:::::  \\_\ `.
                      : . /%O!!::::::::\\_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  /\\ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.   hjw
                  
                  
                 
                  
                  
                                                           _ _ 
 _   _  ___  _   _  __      _____  _ __ | | |
| | | |/ _ \| | | | \ \ /\ / / _ \| '_ \| | |
| |_| | (_) | |_| |  \ V  V / (_) | | | |_|_|
 \__, |\___/ \__,_|   \_/\_/ \___/|_| |_(_|_)
 |___/                                       
                   """)
            
    elif chances == 0:
         game_over = True
         print(f"""Your word WAS : {choose_word}
               
$$$$$$$$\ $$$$$$$\ $$\     $$\        $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\ $$\ $$\ 
\__$$  __|$$  __$$\\$$\   $$  |      $$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |$$ |$$ |
   $$ |   $$ |  $$ |\$$\ $$  /       $$ /  $$ |$$ /  \__|$$ /  $$ |  $$ |  $$$$\ $$ |$$ |$$ |
   $$ |   $$$$$$$  | \$$$$  /        $$$$$$$$ |$$ |$$$$\ $$$$$$$$ |  $$ |  $$ $$\$$ |$$ |$$ |
   $$ |   $$  __$$<   \$$  /         $$  __$$ |$$ |\_$$ |$$  __$$ |  $$ |  $$ \$$$$ |\__|\__|
   $$ |   $$ |  $$ |   $$ |          $$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |  $$ |\$$$ |        
   $$ |   $$ |  $$ |   $$ |          $$ |  $$ |\$$$$$$  |$$ |  $$ |$$$$$$\ $$ | \$$ |$$\ $$\ 
   \__|   \__|  \__|   \__|          \__|  \__| \______/ \__|  \__|\______|\__|  \__|\__|\__|
                                                                                             
                                                                                             
                                                                                             
""")
        

            




