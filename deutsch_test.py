
"""
Deutsch Algorithm Test Script
-----------------------------
This script tests four oracle functions (constant and balanced) using
Qiskit's AerSimulator to verify the Deutsch algorithm behavior.

Expected Output:
- '0': for constant functions
- '1': for balanced functions

Author: Sarita Das
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# ------------------------------------
# Oracle Definitions
# ------------------------------------

def oracle_constant_0(qc):
    # f(x) = 0 → do nothing
    pass

def oracle_constant_1(qc):
    # f(x) = 1 → flip the output qubit
    qc.x(1)

def oracle_balanced_identity(qc):
    # f(x) = x → apply CNOT gate
    qc.cx(0, 1)

def oracle_balanced_not(qc):
    # f(x) = NOT x → flip output, then CNOT
    qc.x(1)
    qc.cx(0, 1)

# ------------------------------------
# Deutsch Algorithm
# ------------------------------------

def run_deutsch(oracle_func):
    qc = QuantumCircuit(2, 1)

    # Initialize output qubit to |1⟩
    qc.x(1)
    qc.h([0, 1])

    # Apply oracle
    oracle_func(qc)

    # Final Hadamard and measurement
    qc.h(0)
    qc.measure(0, 0)

    # Simulate the circuit
    simulator = AerSimulator()
    transpiled_qc = transpile(qc, simulator)
    job = simulator.run(transpiled_qc, shots=1000)
    result = job.result()
    counts = result.get_counts()

    return counts

# ------------------------------------
# Main Test Execution
# ------------------------------------

def main():
    oracle_list = [
        ("Constant f(x)=0", oracle_constant_0),
        ("Constant f(x)=1", oracle_constant_1),
        ("Balanced f(x)=x", oracle_balanced_identity),
        ("Balanced f(x)=¬x", oracle_balanced_not),
    ]

    for label, oracle in oracle_list:
        counts = run_deutsch(oracle)
        print(f"{label}: {counts}")

if __name__ == "__main__":
    main()
 