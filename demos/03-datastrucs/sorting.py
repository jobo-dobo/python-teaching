from collections import namedtuple


DigitalFruit = namedtuple("DigitalFruit", ["fruit_type", "size", "tasty_factor"])


MY_INT_LIST = [0, 6, 3, 56, 342, 12, 11, 69, 420]
# [0, 420, 11, 342, 12, 3, 6, 56, 69]
MY_TUPLE = (12, 4, 420, 5)


MY_FRUIT_LIST = [
    DigitalFruit("Apple", 43, -2.4),
    DigitalFruit("Grape", 2, 1.5),
    DigitalFruit("Banana", 6, -3.4),
    DigitalFruit("Mango", 153, 6.1),
    DigitalFruit("Grape", 2, -4.5),
    DigitalFruit("Grape", 1, 0.0),
    DigitalFruit("Grape", 1, 0.3),
    DigitalFruit("Grape", 3, 0.3),
    DigitalFruit("Grape", 2, 0.3),
    DigitalFruit("Banana", 6, -2.1),
    DigitalFruit("Banana", 50, 1.0),
    DigitalFruit("Apple", 7, 1.5),
    DigitalFruit("Apple", 7, -1.0),
]


def key_func(value):
    return value.fruit_type


def format_list(input_list):
    item_strings = [str(x) for x in input_list]
    return "[\n    " + ",\n    ".join(item_strings) + "\n]"


def main():
    sorted_by_type = sorted(
        MY_FRUIT_LIST, key=lambda x: (x.size, x.tasty_factor, x.fruit_type)
    )
    print(f"Fruits sorted byyyyyy fruit type:\n{format_list(sorted_by_type)}")


if __name__ == "__main__":
    main()
