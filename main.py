import sys

# TODO: implement per the problem description.
# Commands you must handle:
#   <scenario description line> -> output one of RAFT|PAXOS|BFT|GOSSIP|NONE

SCENARIO_TO_PROTOCOL = {
    "3-node etcd cluster": "RAFT",
    "Internal Google service replicating metadata": "PAXOS",
    "Distributed ledger across mutually-untrusted parties": "BFT",
    "Service mesh discovering 1000s of nodes": "GOSSIP",
    "A single-node application": "NONE",
    "HashiCorp Consul KV store": "RAFT",
    "PostgreSQL primary with read replicas": "NONE",
    "Blockchain replication across competing miners": "BFT",
    "Kubernetes control plane state store": "RAFT",
    "Google Chubby lock service": "PAXOS",
    "Cassandra-like ring membership of 1000 nodes via gossip": "GOSSIP",
    "CockroachDB ranges": "RAFT",
    "Single-node Redis instance": "NONE",
}

state = "follower"
term = 0
voted_for = "none"
node = None

for raw in sys.stdin:
    line = raw.strip()
    if not line:
        continue

    parts = line.split()
    cmd = parts[0]
    if cmd == "INIT":
        state = "follower"
        term = 0
        voted_for = "none"
        node = parts[1]
    elif cmd == "STATUS":
        print(f"state={state} term={term} voted_for={voted_for}")
    elif cmd == "BECOME_CANDIDATE":
        state = "candidate"
        term += 1
        voted_for = node
    elif cmd == "BECOME_LEADER":
        if state == "candidate":
            state = "leader"
            voted_for = node
    elif cmd == "BECOME_FOLLOWER":
        request_term = int(parts[1])
        if term < request_term:
            term = request_term
            state = "follower"
            voted_for = "none"
