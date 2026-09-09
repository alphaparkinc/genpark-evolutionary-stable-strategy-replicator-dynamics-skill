"""MCP Server for Replicator Dynamics Skill."""
import json
import sys
from client import ReplicatorDynamics

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "simulate_replicator_dynamics",
                            "description": "Simulate evolutionary replicator dynamics trajectory",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "payoff_matrix": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    },
                                    "initial_distribution": {
                                        "type": "array",
                                        "items": {"type": "number"}
                                    },
                                    "steps": {"type": "integer"}
                                },
                                "required": ["payoff_matrix", "initial_distribution"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                out = ReplicatorDynamics.simulate(
                    payoff_matrix=args["payoff_matrix"],
                    initial_distribution=args["initial_distribution"],
                    steps=args.get("steps", 250)
                )
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(out)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
