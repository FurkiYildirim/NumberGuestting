from random import randint
import click
from time import sleep

# Shell setting
@click.command()
@click.option('--difficult', default=1, prompt="enter difficult (1-3)",
              help='1: 0-9 between 2: 0-50 between 3: 0-100 between (default : 1)')
@click.option('--trycount', default=5, prompt="enter try amount", help='trial amount')

def Menu(difficult, trycount):
    if 3 < difficult or 0 > difficult:
        print("\ndifficult turn the default value : 1\n")
        difficult = 1
    difficultG = {
        1: (0, 9),
        2: (0, 50),
        3: (0, 100),
    }.get(difficult)

    def create_randdom_number() -> int:
        return randint(difficultG[0], difficultG[1])

    def start_again():
        while True:
            again = input("Do you want play again with same settings (y/n) (-1: exit): ")
            if again.lower() == "y":
                return True
            elif again.lower() == "n":
                return False

            elif again == -1:
                quit()
            else:
                continue

    def guess_num(real_n,try_n):
        if try_n == real_n:
            return True
        else:
            return False

    def help():
        return """
        -1 : Create new number to guess
        -2 : help
        
        """

    def Loop(trycount):
        guesnum = create_randdom_number()
        print(guesnum)
        try_again = False
        while True:
            try:
                if try_again:
                    guesnum = create_randdom_number()
                    print(guesnum)
                    try_again = False
                    continue
                TRY = int(input(f"(-2: to help) [try: {trycount}] guess number {difficultG}: "))
                if TRY == -1:
                    print("\nNew number created!\n")
                    guesnum = create_randdom_number()
                    continue

                if TRY == -2:
                    print("\n"+help()+"\n")

                else:
                    if guess_num(guesnum,TRY):
                        print("You win")
                        if start_again():
                            try_again = True
                            continue
                    else:
                        trycount -= 1
                        if trycount == 0:
                            print("You Lose")
                            sleep(1)
                            quit()

                        print(f"Try again! try amount {trycount}")

            except ValueError:
                print("\nEnter a integer please!\n")

    Loop(trycount)


Menu()
