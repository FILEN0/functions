def comentario(string:str,pattern:str="█",width:int = 112):
    string = string.replace("é","e").replace("É","E")
    string = string.replace("ã","a").replace("Ã","A")
    string = string.replace("ó","o").replace("É","E")
    string = string.replace("é","e").replace("É","E")
    string = string.replace("é","e").replace("É","E")
    try:
        pattern = pattern[0]
    except:
        pattern = "█"
    LINE = ["","","","",""]
    ASCII = """"""   

    
    ASCII += """ !"#$%&'()"""
    LINE[0] += "     " + "██   " + "██ ██" + " █ █ " + " ████" + "██  █" + "███  " + "██   " + "   ██" + "██   " 
    LINE[1] += "     " + "██   " + "██ ██" + "█████" + "█ █  " + "   █ " + " ██  " + "██   " + "  ██ " + " ██  " 
    LINE[2] += "     " + "██   " + "     " + " █ █ " + " ███ " + "  █  " + "█ █ █" + "     " + "  ██ " + " ██  " 
    LINE[3] += "     " + "     " + "     " + "█████" + "  █ █" + " █   " + "█  █ " + "     " + "  ██ " + " ██  " 
    LINE[4] += "     " + "██   " + "     " + " █ █ " + "████ " + "█  ██" + " ██ █" + "     " + "   ██" + "██   " 
    
    ASCII += """*+,-./0123"""
    LINE[0] += "█ █  " + "     " + "     " + "     " + "     " + "   ██" + "█████" + "  █  " + "█████" + "█████" 
    LINE[1] += " █   " + "  █  " + "     " + "     " + "     " + "  ██ " + "█   █" + " ██  " + "    █" + "    █" 
    LINE[2] += "█ █  " + "█████" + "     " + "█████" + "     " + "  █  " + "█ █ █" + "  █  " + "█████" + "█████" 
    LINE[3] += "     " + "  █  " + " ██  " + "     " + "     " + " ██  " + "█   █" + "  █  " + "█    " + "    █" 
    LINE[4] += "     " + "     " + "██   " + "     " + "██   " + "██   " + "█████" + "█████" + "█████" + "█████"
    
    ASCII += """456789:;<="""
    LINE[0] += "█   █" + "█████" + "█████" + "█████" + "█████" + "█████" + "     " + "     " + "   ██" + "     " 
    LINE[1] += "█   █" + "█    " + "█    " + "    █" + "█   █" + "█   █" + "██   " + " ██  " + "  ██ " + "█████" 
    LINE[2] += "█████" + "█████" + "█████" + "    █" + "█████" + "█████" + "     " + "     " + " ██  " + "     " 
    LINE[3] += "    █" + "    █" + "█   █" + "    █" + "█   █" + "    █" + "██   " + " ██  " + "  ██ " + "█████" 
    LINE[4] += "    █" + "█████" + "█████" + "    █" + "█████" + "█████" + "     " + "██   " + "   ██" + "     " 
    ASCII += """>?@ABCDEFG"""
    LINE[0] += "██   " + "█████" + " ███ " + "█████" + "████ " + "█████" + "████ " + "█████" + "█████" + "█████" 
    LINE[1] += " ██  " + "██ ██" + "█ █ █" + "█   █" + "█   █" + "█    " + "█   █" + "█    " + "█    " + "█    " 
    LINE[2] += "  ██ " + "   ██" + "██  █" + "█████" + "████ " + "█    " + "█   █" + "█████" + "█████" + "█ ███" 
    LINE[3] += " ██  " + "     " + "█ ██ " + "█   █" + "█   █" + "█    " + "█   █" + "█    " + "█    " + "█   █" 
    LINE[4] += "██   " + "   ██" + " ████" + "█   █" + "████ " + "█████" + "████ " + "█████" + "█    " + "█████" 
 
    ASCII += """HIJKLMNOPQ"""
    LINE[0] += "█   █" + "███  " + "    █" + "█   █" + "█    " + "█   █" + "█   █" + "█████" + "█████" + "█████" 
    LINE[1] += "█   █" + " █   " + "    █" + "█  █ " + "█    " + "██ ██" + "██  █" + "█   █" + "█   █" + "█   █" 
    LINE[2] += "█████" + " █   " + "    █" + "███  " + "█    " + "█ █ █" + "█ █ █" + "█   █" + "█████" + "█ █ █" 
    LINE[3] += "█   █" + " █   " + "█   █" + "█  █ " + "█    " + "█   █" + "█  ██" + "█   █" + "█    " + "█  █ " 
    LINE[4] += "█   █" + "███  " + " ███ " + "█   █" + "█████" + "█   █" + "█   █" + "█████" + "█    " + "███ █" 
 
    ASCII += """RSTUVWXYZ["""
    LINE[0] += "█████" + " ████" + "█████" + "█   █" + "█   █" + "█   █" + "█   █" + "█   █" + "█████" + "  ███" 
    LINE[1] += "█   █" + "██   " + "  █  " + "█   █" + "█   █" + "█   █" + " █ █ " + " █ █ " + "   █ " + "  ██ " 
    LINE[2] += "█████" + " ███ " + "  █  " + "█   █" + "█   █" + "█ █ █" + "  █  " + "  █  " + "  █  " + "  ██ " 
    LINE[3] += "█  █ " + "   ██" + "  █  " + "█   █" + " █ █ " + "██ ██" + " █ █ " + "  █  " + " █   " + "  ██ " 
    LINE[4] += "█   █" + "████ " + "  █  " + "█████" + "  █  " + "█   █" + "█   █" + "  █  " + "█████" + "  ███" 
 
    ASCII += """\\]^_`abcde"""
    LINE[0] += "██   " + "███  " + "  █  " + "     " + " ██  " + "     " + "█    " + "     " + "   █ " + "     " 
    LINE[1] += " ██  " + " ██  " + " █ █ " + "     " + "  ██ " + "     " + "█    " + "     " + "   █ " + " ███ " 
    LINE[2] += "  █  " + " ██  " + "█   █" + "     " + "     " + " ███ " + "███  " + " ███ " + " ███ " + "█ █  " 
    LINE[3] += "  ██ " + " ██  " + "     " + "     " + "     " + "█  █ " + "█  █ " + "█    " + "█  █ " + "██   " 
    LINE[4] += "   ██" + "███  " + "     " + "█████" + "     " + " ███ " + "███  " + " ███ " + " ███ " + " ███ " 

    ASCII += """fghijklmno"""
    LINE[0] += "  █  " + " ██  " + "█    " + "     " + "     " + "█    " + "     " + "     " + "     " + "     " 
    LINE[1] += " █   " + "█  █ " + "█    " + " █   " + " ██  " + "█  █ " + "██   " + "     " + "     " + "     " 
    LINE[2] += "███  " + " ██  " + "███  " + "     " + "  █  " + "█ █  " + " █   " + "██ █ " + "███  " + " ██  " 
    LINE[3] += " █   " + "█    " + "█  █ " + " █   " + "█ █  " + "███  " + " █   " + "█ █ █" + "█  █ " + "█  █ " 
    LINE[4] += " █   " + " ███ " + "█  █ " + "███  " + " █   " + "█  █ " + " ██  " + "█ █ █" + "█  █ " + " ██  " 
  
    ASCII += """pqrstuvwxy"""
    LINE[0] += "     " + "     " + "     " + "     " + " █   " + "     " + "     " + "     " + "     " + "     " 
    LINE[1] += " ██  " + " ██  " + "     " + " ██  " + "███  " + "     " + "     " + "     " + "     " + "█  █ " 
    LINE[2] += "█  █ " + "█  █ " + "█ ██ " + "██   " + " █   " + "█  █ " + "█ █  " + "█ █ █" + "█ █  " + " █ █ " 
    LINE[3] += "███  " + " ███ " + "██   " + "  █  " + " █   " + "█  █ " + "█ █  " + "█ █ █" + " █   " + "  ██ " 
    LINE[4] += "█    " + "   █ " + "█    " + "██   " + "  █  " + " ███ " + " █   " + " █ █ " + "█ █  " + "███  " 
 
    ASCII += """z{|}~"""
    LINE[0] += "     " + "   ██" + "  █  " + "██   " + "     "
    LINE[1] += "████ " + "   █ " + "  █  " + " █   " + " █   "
    LINE[2] += "  █  " + "  ██ " + "  █  " + "  █  " + "█ █ █"
    LINE[3] += " █   " + "   █ " + "  █  " + " █   " + "   █ "
    LINE[4] += "████ " + "   ██" + "  █  " + "██   " + "     "

    CHAR = []
    INDENT = (width-(len(string)*6))//2
    for s in string:
        CHAR.append(ASCII.index(s))

    COMMENT = [INDENT*" ",INDENT*" ",INDENT*" ",INDENT*" ",INDENT*" "]    
    for C in CHAR:
        COMMENT[0] += LINE[0][C*5:C*5+5:].replace("█",pattern) + " "
        COMMENT[1] += LINE[1][C*5:C*5+5:].replace("█",pattern) + " "
        COMMENT[2] += LINE[2][C*5:C*5+5:].replace("█",pattern) + " "
        COMMENT[3] += LINE[3][C*5:C*5+5:].replace("█",pattern) + " "
        COMMENT[4] += LINE[4][C*5:C*5+5:].replace("█",pattern) + " "
    
    print(f'"""\n{COMMENT[0]}\n{COMMENT[1]}\n{COMMENT[2]}\n{COMMENT[3]}\n{COMMENT[4]}\n"""')