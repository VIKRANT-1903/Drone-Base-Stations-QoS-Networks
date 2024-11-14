# Drone-Base-Stations-QoS-Networks
Project Title: Cloud Computing: Placing Multiple Drone Base Stations in Hotspots - Enhancing User QoS with Drone-Assisted Networks

Team Members:
- Vikrant Kumar - 221CS163
- Aryan Kundu - 221CS210
- Harsh Gupta - 221CS126
- Rahul - 221CS141

---

Project Overview:
This project explores the deployment of Drone Base Stations (DBSs) in hotspot areas to improve Quality of Service (QoS) for users in high-density locations. The focus is on enhancing connectivity and addressing network congestion through drone-assisted networks. Edge and cloud computing are integrated to handle computational loads, maintain energy efficiency, and minimize costs.

Contents:
1. Introduction
   - Overview of drone-assisted networks and the role of DBSs in improving connectivity and QoS.
   - Description of challenges such as energy efficiency, cost constraints, and QoS requirements in dynamic hotspots.

2. Core Concepts
   - Drone Assisted Networks and Base Stations: How DBSs serve as relay nodes for Line-of-Sight (LoS) connections, enhancing data transmission and reducing network congestion.
   - Edge and Cloud Computing Integration: Importance of localized processing and broader computational support for QoS maintenance.

3. Challenges
   - High Energy Consumption: Strategies for optimizing energy usage and exploring sustainable energy sources.
   - Latency and SLA Compliance: Balancing energy efficiency with Service Level Agreement (SLA) compliance.
   - Dynamic Hotspot Conditions: Adaptive algorithms for DBS repositioning in response to fluctuating demand.

4. High-Level Working of the AMUSE Algorithm
   - Explanation of the AMUSE algorithm’s steps for optimizing DBS deployment in high-demand areas, including initial deployment, user coverage analysis, iterative DBS addition, dynamic placement optimization, and QoS verification.

5. Workflow Diagram
   - Visual representation of the DBS deployment process, from user data collection to final evaluation.

6. C++ Code Implementation
   - C++ code for deploying and managing DBSs using the AMUSE algorithm.

7. Output
   - Display of user and DBS locations generated through the algorithm in a Jupyter Notebook environment.

---

How to Use:
1. Setup:
   - Clone the repository to your local machine.
   - Ensure all dependencies for C++ and Jupyter Notebooks are installed.

2. Run the Code:
   - Open the `main.cpp` file to execute the DBS deployment algorithm.
   - Use Jupyter Notebook to visualize user and DBS locations and the hotspot data processed.

3. View Workflow:
   - The Workflow Diagram is located in the project directory and illustrates each step of the AMUSE algorithm deployment process.

4. Output Analysis:
   - Review the output data in the `output` directory to analyze the effectiveness of DBS placement as per the algorithm.

---

Additional Notes:
- Energy Optimization Techniques: Power management methods for DBSs.
- QoS Verification: Periodic validation ensures users receive adequate coverage and QoS compliance.

Future Work:
- Enhanced Real-Time Adaptation: Improvements in dynamic DBS repositioning based on real-time changes in user demand.
- Integration with More Sustainable Energy Solutions: Expanding to include solar-powered DBS solutions.

