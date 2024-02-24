def madlib():
    noun1 = input("Noun : ")
    adj1 = input("Adjective : ")
    adj2 = input("Adjective : ")
    noun2 = input("Noun : ")
    adj3 = input("Adjective : ")
    noun3 = input("Noun : ")
    adj4 = input("Adjective : ")

    madlib = f"In the championship game against the formidable \033[3;91m{noun1}\033[0m, our team faced moments of intense \033[3;91m{adj1}\033[0m and exhilarating \033[3;91m{adj2}\033[0m. The crowd erupted with cheers as our star player executed a flawless \033[3;91m{noun2}\033[0m, securing a lead that filled us with \033[3;91m{adj3}\033[0m. Despite the opposing team's persistent \033[3;91m{noun3}\033[0m, our defense held strong, and the final whistle marked a triumphant victory. The post-game celebration echoed with laughter, cheers, and an overwhelming sense of \033[3;91m{adj4}\033[0m."

    print(madlib)