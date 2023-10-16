def print_format():
    str = "I want to pay {2} dollars for {0} pieces of item {1}."
    print(str.format(3, 576, 10.5))

    kill_count = 9
    agent_name = 'James Bond'

    # Old ways
    print("%s has killed %d enemies" % (agent_name, kill_count))

    print('{} has killed {} enemies'.format(agent_name, kill_count))
    print('{name} has killed {kill} enemies'.format(name=agent_name, kill=kill_count))

    # f-strings way
    print(f"{agent_name} has killed {kill_count} enemies")


def print_parameters():
    # print('words', 'with', 'commas', 'in', 'between', sep=', ')
    print("11", "12", "2023", sep="/")      # 29/01/2022
    print("name", "domain.com", sep="@")    # name@domain.com
    pokemon_list = ['Pikachu', 'Abra', 'Charmander']
    print(*pokemon_list, sep=', ', end='')


# print_format()
print_parameters()
