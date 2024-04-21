import os

def clearConsole():
    os.system('cls' if os.name=='nt' else 'clear')


def title():
    content = r"""
 GGGG  RRRR   AAAAA  PPPP   H   H  SSSS
G      R   R  A   A  P   P  H   H  S
G  GG  RRRR   AAAAA  PPPP   HHHHH  SSSS
G   G  R  R   A   A  P      H   H     S
 GGGG  R   R  A   A  P      H   H  SSSS

"""

    print(content)