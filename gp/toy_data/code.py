import scipy

# Gaussian process posterior
def GP(observed_X, observed_y, X2, kernel_func):
    """
    Calculate the posterior mean and covariance matrix for y2
    based on the corresponding input X2, the observations (observed_y, observed_X), 
    and the prior kernel function.
    """
    # Kernel of the observations
    Σ11 = kernel_func(observed_X, observed_X)
    # Kernel of observations vs to-predict
    Σ12 = kernel_func(observed_X, X2)

    # Solve
    solved = scipy.linalg.solve(Σ11, Σ12, assume_a='pos').T
    # Compute posterior mean
    μ2 = solved @ observed_y  # @ means matrix multiply
    # Compute the posterior covariance
    Σ22 = kernel_func(X2, X2)
    Σ2 = Σ22 - (solved @ Σ12)
    return μ2, Σ2  # mean, covariance


def GP_multi(observed_X, observed_y,
             task_observed: int, 
             X2,
             task_predicted: int,
             kernel_func):
    """
    A multi task gaussian process

    observed_X, observed_y are assumed to come from task_observed, which is indexed with an integer

    kernel_func is a MultiKernel, #TODO add type hint later
    """
    # Kernel of the observations
    Σ11 = kernel_func(task_observed, task_observed, observed_X, observed_X)
    # Kernel of observations vs to-predict
    Σ12 = kernel_func(task_observed, task_predicted, observed_X, X2)

    # Solve
    solved = scipy.linalg.solve(Σ11, Σ12, assume_a='pos').T
    # Compute posterior mean
    μ2 = solved @ observed_y  # @ means matrix multiply
    # Compute the posterior covariance
    Σ22 = kernel_func(task_predicted, task_predicted, X2, X2)
    Σ2 = Σ22 - (solved @ Σ12)
    return μ2, Σ2  # mean, covariance