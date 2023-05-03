# Date: 2023 04 25
# Purpose: Write some Markov Chain Monte Carlo Algorithms for practice


import numpy as np
import pymc3 as pm
import matplotlib.pyplot as plt


def main():
    # Define the model using PyMC3 syntax
    with pm.Model() as model:
        # Define prior distribution for the parameter of interest
        theta = pm.Beta('theta', alpha=1, beta=1)

    # Define likelihood function
        y = pm.Bernoulli('y', p=theta, observed=[0, 1, 0, 0, 1])

    # Generate MCMC samples
        trace = pm.sample(1000, chains=4)

    # Plot the posterior distribution of the parameter
    pm.plot_posterior(trace, var_names=['theta'])
    pm.traceplot(trace, var_names=['theta'])

    # Show the plots
    plt.show()

if __name__ == "__main__" :
    print("Welcome to the study of Markov Chain")
    main()