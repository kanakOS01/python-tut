def madlib():
    adj1 = input("Adjective : ")
    adj2 = input("Adjective : ")
    place1 = input("Place (common noun) : ")
    place2 = input("Place (common noun) : ")
    adj3 = input("Adjective : ")
    adj4 = input("Adjective : ")
    
    madlib = f"The \033[3;91m{adj1}\033[0m outbreak caught everyone off guard, turning ordinary people into \033[3;91m{adj2}\033[0m creatures. As I navigated the eerily silent streets, I stumbled upon a group of survivors huddled in a \033[3;91m{place1}\033[0m. Armed with makeshift weapons, we formulated a plan to reach the supposed safe haven—a \033[3;91m{place2}\033[0m fortified against the undead. The journey was fraught with \033[3;91m{adj3}\033[0m, but our determination and teamwork saw us through, making the escape both \033[3;91m{adj4}\033[0m and thrilling."
    
    print(madlib)