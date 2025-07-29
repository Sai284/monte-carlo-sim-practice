# Monte Carlo Investment Simulation in Python

This project demonstrates how to use a Monte Carlo simulation to model the possible future values of an investment portfolio over time. The simulation is implemented in Python and visualizes both individual investment growth paths as well as the distribution of outcomes after a set period.

---

## What is Monte Carlo Simulation?

Monte Carlo simulation is a computational technique that uses random sampling to estimate the probable outcomes of a process. In the context of finance, it's widely used to model the uncertainty and variability of investment returns over time, helping investors understand both the range of possible outcomes and the likelihood of achieving various results.

---

## Features

- **User Console Input:** You can set the initial investment, expected return, volatility, investment horizon (years), number of simulations, and how many paths to plot.
- **Simulates Hundreds/Thousands of Investment Paths:** Each path shows a different possible investment trajectory based on random returns.
- **Visualizes Results:**
  - **Line Plot:** Shows multiple possible growth paths of your investment over time.
  - **Histogram:** Shows the distribution of final investment values after the chosen time period.
- **Info Box:** Each chart includes a key displaying the parameters used for that simulation.

---

## How to Interpret the Graphs

- **Line Plot:** Shows the variability and compounding effect of returns. The spread increases over time, demonstrating both risk and reward.
- **Histogram:** Summarizes all simulation outcomes after the investment horizon. Most results are "average," but a few rare paths can produce very high final values.

---

## How to Run

1. **Install Dependencies:**
    ```bash
    pip install numpy matplotlib
    ```
2. **Run the Script:**
    ```bash
    python monte_carlo_console.py
    ```
3. **Enter Parameters When Prompted:**
    - Initial investment
    - Years to simulate
    - Expected annual return (as decimal, e.g., 0.07 for 7%)
    - Volatility (as decimal, e.g., 0.15 for 15%)
    - Number of simulation runs
    - Number of paths to plot

4. **View the Charts:**  
    Two charts will appear:
    - Investment growth paths
    - Distribution of final values

---

## Theory Recap

- **Initial Investment:** The starting amount (e.g., $10,000).
- **Expected Return (mu):** The average annual return you expect (e.g., 7%).
- **Volatility (sigma):** The annual standard deviation of returns (e.g., 15%).
- **Simulations:** Number of possible "futures" to simulate.
- **Investment Horizon:** Number of years to project.

The simulation randomly generates a return for each year and each simulation, compounding the investment accordingly. After all runs, you can analyze the range and likelihood of possible outcomes.

---

## Customization

- **Change Parameters:** Rerun the script with different input values to see how results change.
- **View Info Box:** Each chart includes a summary of the parameters used, positioned to the side of the graph for clarity.

---

## Insights

- The simulation makes clear that **investing is uncertain**, and both risk and reward grow with time.
- Most outcomes are clustered, but a few rare scenarios can lead to very large gains.
- Monte Carlo simulation is a powerful way to visualize both the most likely and the "outlier" results.

---

## Further Ideas

- Add regular contributions or withdrawals.
- Model inflation and after-tax returns.
- Explore different distributions for returns (e.g., log-normal).
- Calculate and annotate specific percentiles or statistics on the charts.

---
