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

out = []
for raw in sys.stdin:
    line = raw.strip()
    if not line:
        continue
    out.append(SCENARIO_TO_PROTOCOL[line])

print("\n".join(out))
