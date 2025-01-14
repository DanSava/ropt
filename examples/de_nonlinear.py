"""Differential evaluation optimization example.

This example uses the differential evolution method to solve a discrete
problem with a linear constraint, implemented as a non-linear constraint.
"""

from typing import Any, Dict, Tuple

import numpy as np
from numpy.typing import NDArray

from ropt.enums import ConstraintType, VariableType
from ropt.evaluator import EvaluatorContext, EvaluatorResult
from ropt.results import FunctionResults, Results
from ropt.workflow import BasicWorkflow

CONFIG: Dict[str, Any] = {
    "variables": {
        "initial_values": 2 * [0.0],
        "types": VariableType.INTEGER,
        "lower_bounds": [0.0, 0.0],
        "upper_bounds": [10.0, 10.0],
    },
    "optimizer": {
        "method": "differential_evolution",
        "options": {"seed": 3},
        "max_functions": 100,
        "parallel": True,
    },
    "nonlinear_constraints": {
        "types": [ConstraintType.LE],
        "rhs_values": [10.0],
    },
}


def function(variables: NDArray[np.float64], _: EvaluatorContext) -> EvaluatorResult:
    """Evaluate the function.

    Args:
        variables: The variables to evaluate
        context:   Evaluator context

    Returns:
        Calculated objectives and constraints.
    """
    x = variables[:, 0]
    y = variables[:, 1]
    objectives = -np.array(np.minimum(3 * x, y), ndmin=2).T
    constraints = np.array(x + y, ndmin=2).T
    return EvaluatorResult(objectives=objectives, constraints=constraints)


def report(results: Tuple[Results, ...]) -> None:
    """Report results of an evaluation.

    Args:
        results: Results from an evaluation
    """
    for item in results:
        if isinstance(item, FunctionResults) and item.functions is not None:
            print(f"result: {item.result_id}")
            print(f"  variables: {item.evaluations.variables}")
            print(f"  objective: {item.functions.weighted_objective}\n")


def run_optimization() -> None:
    """Run the optimization."""
    optimal_result = BasicWorkflow(CONFIG, function, callback=report).run().results
    assert optimal_result is not None
    assert optimal_result.functions is not None
    assert np.all(optimal_result.evaluations.variables == [3, 7])
    print(f"BEST RESULT: {optimal_result.result_id}")
    print(f"  variables: {optimal_result.evaluations.variables}")
    print(f"  objective: {optimal_result.functions.weighted_objective}\n")


def main() -> None:
    """Main function."""
    run_optimization()


if __name__ == "__main__":
    main()
