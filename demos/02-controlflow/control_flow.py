from random import randrange
import click


@click.command("main")
@click.argument("startindex", type=click.INT)
@click.argument("endindex", type=click.INT)
@click.argument("numrandom", type=click.INT, default=1)
def main(startindex, endindex, numrandom):

    if startindex < endindex:
        print("This is so good right now!!!! :3")
    elif startindex > endindex:
        print("THIS IS A TRAVESTY >:((")
    else:
        print("I don't know at all ¯\_(ツ)_/¯")

    # for i in range(startindex, endindex):
    #     print(i)
    #     print(get_number_comment(i))

    for _ in range(numrandom):
        print("""--------------------------------
HERE IS A RANDOM VALUE NOW!!!!!
--------------------------------"""
        )
        i = randrange(startindex, endindex)
        print(i)
        print(get_number_comment(i))
    
    do_crazy_shit(endindex, startindex)
    
def get_number_comment(intval):
    if intval == 2:
        return "me too"
    elif intval == 4:
        return "NOT A FAN"
    elif intval == 11:
        return "so cool"
    elif intval == 13:
        return "I HATE THIS NUMBER"
    elif intval == 69:
        return "nice"
    else:
        return "nothin here to see"

def do_crazy_shit(pee_value, poop_value):
    print("pee" * pee_value)
    print("poo" * poop_value + "p")
    if pee_value >= poop_value:
        print("i peed myself")


if __name__ == "__main__":
    main()

