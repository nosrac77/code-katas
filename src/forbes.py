"""Module containing Forbes challenge function."""


def forbes_sort(file_name):
    """Function that takes in a JSON file and returns two values."""
    forbes_dict = {}

    with open(file_name) as f:
        for line in f.readlines():
            if 'name' in line:
                temp_name = line.strip('"name": ').strip().strip(",")
                forbes_dict[temp_name[:len(temp_name) - 1]] = []
            if 'age' in line and 'Larry Page' not in line:
                age_num = int(line.strip('"age: ""').strip(chr(10)).strip(','))
                if age_num < 80 and age_num > 1:
                    forbes_dict[temp_name[:len(temp_name) - 1]].append(age_num)
            if 'net_worth' in line:
                print(line)
                net_worth = int(line.strip().strip('"net_worth (USD)": ').strip(','))
                forbes_dict[temp_name[:len(temp_name) - 1]].append(net_worth)
        print(forbes_dict)


if __name__ == '__main__':

    forbes_sort('src/forbes.json')
