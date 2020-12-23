def get_strings(city):
    cidade = ""
    for let in city.lower():
        if let not in cidade and let != " ":
            cnt = city.lower().count(let)
            cidade += f"{let.lower()}:{cnt * '*'},"

    return cidade[:-1]

#Better way
"""from collections import Counter


def get_strings(city):
    return ",".join(f"{char}:{'*'*count}" for char, count in Counter(city.replace(" ", "").lower()).items())"""