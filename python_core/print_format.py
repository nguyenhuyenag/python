kill_count = 9
agent_name = 'James Bond'

# old ways
print("%s has killed %d enemies" % (agent_name, kill_count))

print('{} has killed {} enemies'.format(agent_name, kill_count))
print('{name} has killed {kill} enemies'.format(name=agent_name, kill=kill_count))

# f-strings way
print(f'{agent_name} has killed {kill_count} enemies')
