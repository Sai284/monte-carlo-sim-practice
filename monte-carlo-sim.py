import numpy as np
import matplotlib.pyplot as plt

def get_float(prompt, default):
  try:
    return float(input(f"{prompt} (default {default}): ") or default)
  except ValueError:
    print("Please enter a valid number.")
    return get_float(prompt, default)
  
def get_int(prompt, default):
  try:
    return int(input(f"{prompt} (default {default}): ") or default)
  except ValueError:
    print("Please enter a valid integer.")
    return get_int(prompt, default)

def main():
  initial_investment = get_float("Enter the initial investment amount", 10000)
  years = get_int("Enter number of years to simulate", 30) # Time horizon
  mu = get_float("Enter expected average annual return (eg. 0.07 for 7%)", 0.07)  # Expected annual return
  sigma = get_float("Enter annual volatility (0.15 for 15%)", 0.15) # Volatility or stdev of returns
  simulations = get_int("Enter number of simulations to run", 10000)
  plot_paths = get_int("Enter number of paths to plot (0 for none)", 100) 

  results = np.zeros((simulations, years + 1))
  results[:, 0] = initial_investment

  for sim in range(simulations):
    for year in range(1, years + 1):
      random_return = np.random.normal(mu, sigma)
      results[sim, year] = results[sim, year - 1] * np.exp(random_return)

  param_text = (
    f"Initial investment: ${initial_investment:,.0f}\n"
    f"Years: {years}\n"
    f"Expected annual return: {mu*100:.2f}%\n"
    f"Volatility (standard deviation): {sigma*100:.2f}%\n"
    f"Simulations: {simulations}\n"
    f"Paths plotted: {plot_paths}"
)


  plt.figure(figsize=(10, 5))
  for i in range(plot_paths, simulations):
    plt.plot(results[i], color='blue', alpha=0.2)
  plt.title('Monte Carlo Simulation of Investment Growth')
  plt.xlabel('Years')
  plt.ylabel('Investment Value ($)')
  plt.grid(True)

  ax = plt.gca()
  plt.subplots_adjust(right=0.75)
  ax.text(
    1.02, 0.95, param_text,
    transform=ax.transAxes,
    fontsize=10,
    va='top', ha='left',
    bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5')
  )

  plt.show()

  plt.figure(figsize=(10,5))
  plt.hist(results[:, -1], bins=100, color='skyblue')
  plt.title('Distribution of Investment Value After {} Years'.format(years))
  plt.xlabel('Investment Value ($)')
  plt.ylabel('Frequency')
  plt.grid(True)
  plt.show()

  median = np.median(results[:, -1])
  percentile_10 = np.percentile(results[:, -1], 10)
  percentile_90 = np.percentile(results[:, -1], 90)

  print(f"Median final value: ${median:,.2f}")
  print(f"10th percentile: ${percentile_10:,.2f}")
  print(f"90th percentile: ${percentile_90:,.2f}")

if __name__ == "__main__":
  main()