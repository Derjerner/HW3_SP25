import math
#chatgpt

#t-distribution probability func
def t_pdf(t, m):

    factor = math.gamma((m + 1) / 2)
    denom = math.sqrt(m * math.pi) * math.gamma(m / 2)
    return (factor / denom) * (1 + (t ** 2) / m) ** (-(m + 1) / 2)

#Simpsons 1/3 rule
def simpsons_rule(func, a, b, m, n=100):

    if n % 2 == 1:
        n += 1  # Ensure even
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [func(t, m) for t in x]

    integral = (h / 3) * (
                y[0] + 4 * sum(y[i] for i in range(1, n, 2)) + 2 * sum(y[i] for i in range(2, n - 1, 2)) + y[n])
    return integral


def t_distribution_cdf(t, m):
    #computes total probability
    return 0.5 + simpsons_rule(t_pdf, 0, t, m)


def main():

    # Fixed test cases
    degrees_of_freedom = [7, 11, 15]
    user_m = int(input("Enter degrees of freedom (m): "))
    degrees_of_freedom.append(user_m)

    # Ask the user for three z-values
    z_values = []
    for i in range(3):
        z = float(input(f"Enter z-value {i + 1}: "))
        z_values.append(z)

    print("\nComputing probabilities...\n")
    print(f"{'Degrees of Freedom':<20}{'Z-Value':<10}{'Computed Probability':<20}")
    print("=" * 50)

    # Compute probabilities for each degree of freedom and z-value
    for m in degrees_of_freedom:
        for z in z_values:
            probability = t_distribution_cdf(z, m)
            print(f"{m:<20}{z:<10.3f}{probability:<20.6f}")


if __name__ == "__main__":
    main()
