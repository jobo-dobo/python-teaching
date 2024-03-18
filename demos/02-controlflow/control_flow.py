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
        print(r"I don't know at all ¯\_(ツ)_/¯")

    # for i in range(startindex, endindex):
    #     print(i)
    #     print(get_number_comment(i))

    for _ in range(numrandom):
        print(
            """--------------------------------
HERE IS A RANDOM VALUE NOW!!!!!
--------------------------------"""
        )
        i = randrange(startindex, endindex)
        print(i)
        print(get_number_comment(i))

    do_crazy_shit(endindex, startindex)


def get_number_comment(intval: str) -> int:
    """Get a comment corresponding with a provided int value

    args:
        - intval (int): input integer value

    returns:
        str: comment corresponding to value
    """
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
    """Print pee a number of times and poo a number of times

    args:
        - pee_value (int): number of pee to print
        - poo_value (int): number poo to print
    """
    print("pee" * pee_value)
    print("poo" * poop_value + "p")
    if pee_value >= poop_value:
        print("i peed myself")


if __name__ == "__main__":
    main()
