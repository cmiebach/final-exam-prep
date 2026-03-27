import sys
import numpy as np


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python sampler.py <distribution> <n_samples> <seed>")
        print("Distributions: normal, uniform, randint")
        sys.exit(1)

    distribution = sys.argv[1]
    n_samples = int(sys.argv[2])
    seed = int(sys.argv[3])

    np.random.seed(seed)

    if distribution == "normal":
        samples = np.random.normal(0, 1, n_samples)
    elif distribution == "uniform":
        samples = np.random.uniform(0, 1, n_samples)
    elif distribution == "randint":
        samples = np.random.randint(1, 100, n_samples)
    else:
        print(f"Error: Unknown distribution '{distribution}'")
        print("Supported: normal, uniform, randint")
        sys.exit(1)

    print(f"Distribution: {distribution}")
    print(f"Samples: {n_samples} (seed={seed})")
    print(f"First 5 values: {samples[:5]}")
    print(f"Mean: {samples.mean():.4f}")
    print(f"Std:  {samples.std():.4f}")
