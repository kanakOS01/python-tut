def madlib():
    adj1 = input("Adjective : ")
    adj2 = input("Adjective : ")
    noun1 = input("Noun : ")
    noun2 = input("Noun : ")
    adj3 = input("Adjective : ")
    adj4 = input("Adjective : ")
    noun3 = input("Noun : ")
    noun4 = input("Noun : ")
    adj5 = input("Adjective : ")

    madlib = f"As the \033[3;91m{adj1}\033[0m exams loomed closer, a wave of \033[3;91m{adj2}\033[0m set in. My study sessions became a marathon of \033[3;91m{noun1}\033[0m and \033[3;91m{noun2}\033[0m, with textbooks becoming my constant companions. The night before the exam, I pulled an \033[3;91m{adj3}\033[0m to review essential concepts, fueled by a combination of \033[3;91m{adj4}\033[0m and \033[3;91m{noun3}\033[0m. As I entered the exam hall, a mix of nervousness and determination fueled my focus. The questions, though challenging, became an opportunity to showcase months of \033[3;91m{noun4}\033[0m and dedication, and I emerged from the exam room with a sense of accomplishment and \033[3;91m{adj5}\033[0m."
    
    print(madlib)