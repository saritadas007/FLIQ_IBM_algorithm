# FLIQ_IBM_algorithm
 Deutsch Algorithm Simulator
 # 🧠 Deutsch Algorithm – FLIQ Hackathon 2025
This repository demonstrates the **Deutsch Algorithm** using Qiskit. It tests four types of oracle functions to classify them as either **constant** or **balanced** with only one query.
This work is done as part of my participation in the FLIQ Hackathon 2025.
Although I couldn't submit the project before the deadline due to time constraints, I’m sharing my work here in the hope that it helps others who are new to quantum computing.

## 🧠 Quantum Background

- **Constant function**: returns the same output for both inputs (e.g., f(x) = 0 or f(x) = 1).
- **Balanced function**: returns different outputs for each input (e.g., f(x) = x or f(x) = NOT x).
- **Deutsch Algorithm** leverages quantum superposition and interference to distinguish these with just one oracle call.

The repository includes:

- 📓 A beginner-friendly tutorial --> Deutsch Algorithm.ipynb
      Includes:
       - Step-by-step construction of the Deutsch circuit
       - Oracle implementations and analysis
       - Results interpretation
- 🧪 A local test script file --> deutsch_test.py
       This script tests four oracle functions (constant and balanced) using Qiskit's AerSimulator to verify the Deutsch algorithm behaviour.
       **How to use**
        # Install dependencies
        
        !pip install qiskit
        !pip install pylatexenc
        !pip install qiskit-aer
        ## Run the script
        python deutsch_test.py
        ### Expected output
        Constant f(x)=0: {'0': 1000}
        Constant f(x)=1: {'0': 1000}
        Balanced f(x)=x: {'1': 1000}
        Balanced f(x)=¬x: {'1': 1000}  
        

 
