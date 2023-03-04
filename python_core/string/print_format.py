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
