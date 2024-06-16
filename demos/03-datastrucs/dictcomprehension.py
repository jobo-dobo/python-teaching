BIG_DICT = {
    "dict": 2020202020202020,
    "yyyeeeee": 333,
    "why": 2,
    "nice": 69,
    "blazin'": 420,
    "blaze-maxing": 420,
    "weed-pilled": 420,
    "onioncore": -13,
}


def invert_dict(input_dict, exclude_keys=set()):
    """Returns a dict that reverses keys and
    values of the input dict
    Assumes that values are unique, otherwise
    the last key containing a value is what is
    inverted and put into the result.

    args:
        - input_dict (dict)
        - exclude_keys (set): optional set of keys
            from input_dict to ignore

    returns:
        dict: inverted dict
    """
    output_dict = {v: k for k, v in input_dict.items() if k not in exclude_keys}
    sampler_ctr = 0
    for k in input_dict:
        if sampler_ctr % 3 == 0:
            exclude_keys.add(k)
        sampler_ctr += 1
    return output_dict


def main():
    print(BIG_DICT)
    print(invert_dict(BIG_DICT))
    print(invert_dict(BIG_DICT, exclude_keys={"onioncore", "weed-pilled"}))
    print(invert_dict(BIG_DICT))


if __name__ == "__main__":
    main()
