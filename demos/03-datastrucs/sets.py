import click


@click.command()
@click.argument("set1")
@click.argument("set2")
def operate_sets(set1,set2):
    print("hi")
    # validate/convert to sets
    set1 = set(set1)
    set2 = set(set2)
    print(
        f"""set1: {set1!s}
set2: {set2!s}

"""
    )

    # union, intersect, difference
    union_set = set1 | set2
    intersect_set = set1 & set2
    diff_set = set1 - set2
    diff_rev_set = set2 - set1
    print(
        f"""union set1 | set2:
    {union_set!s}

intersection set1 & set2:
    {intersect_set!s}
    
diff_set set1 - set2:
    {diff_set!s}

diff_set set2 - set1:
    {diff_rev_set!s}
    
    """
    )


if __name__ == "__main__":
    operate_sets()
