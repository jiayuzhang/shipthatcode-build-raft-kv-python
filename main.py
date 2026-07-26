import sys

# TODO: implement per the problem description.
# Commands you must handle:
#   <scenario description line> -> output one of RAFT|PAXOS|BFT|GOSSIP|NONE

out = []
for raw in sys.stdin:
    line = raw.strip()
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]
    # TODO: handle each command and append to `out`
    pass

print("\n".join(out))
