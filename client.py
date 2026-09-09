"""
Autonomous Agent Evolutionary Stable Strategy Replicator Dynamics Skill
Pure Python Standard Library implementation.
"""
from typing import List, Dict, Any

class ReplicatorDynamics:
    """
    Replicator Dynamics ODE numerical solver for evolutionary game theory.
    """
    @staticmethod
    def simulate(payoff_matrix: List[List[float]], initial_distribution: List[float], 
                 steps: int = 250, dt: float = 0.05) -> Dict[str, Any]:
        n = len(initial_distribution)
        x = list(initial_distribution)
        trajectory = [list(x)]

        for _ in range(steps):
            Ax = [sum(payoff_matrix[i][j] * x[j] for j in range(n)) for i in range(n)]
            avg_fitness = sum(x[i] * Ax[i] for i in range(n))
            dx = [x[i] * (Ax[i] - avg_fitness) * dt for i in range(n)]
            x = [max(0.0, x[i] + dx[i]) for i in range(n)]
            tot = sum(x)
            if tot > 1e-12:
                x = [val / tot for val in x]
            trajectory.append(list(x))

        return {
            "final_population_distribution": [round(v, 4) for v in x],
            "trajectory_steps": len(trajectory)
        }
