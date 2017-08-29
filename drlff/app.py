from drlff.drl import dqn
with open('/tmp/drlff.log', 'w') as f:
    f.write('state\treward\talive\n')
dqn.main()
