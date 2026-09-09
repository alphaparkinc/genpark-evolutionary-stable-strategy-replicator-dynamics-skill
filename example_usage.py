"""Example usage for Replicator Dynamics Skill."""
from client import ReplicatorDynamics

def main():
    print("Executing Replicator Dynamics Simulation...")
    # Hawk-Dove game: Hawk=0, Dove=1
    hawk_dove = [
        [-1.0, 2.0],
        [0.0, 1.0]
    ]
    res = ReplicatorDynamics.simulate(hawk_dove, [0.9, 0.1], steps=250, dt=0.05)
    dist = res["final_population_distribution"]
    print("Final Strategy Distribution (Hawk, Dove):", dist)
    assert abs(dist[0] - 0.5) < 0.05, f"Expected ~0.50 Hawk, got {dist[0]}"
    print("Replicator Dynamics verified successfully!")

if __name__ == "__main__":
    main()
