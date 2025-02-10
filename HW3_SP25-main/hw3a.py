from numericalMethods import GPDF, Probability, Secant
#chatgpt

def probability_input(c, mean, stDev, onesided, GT):
    """
    Utilizes GPDF. probability and, secant functions from hw 2 to determin
    probability from user input
    Parameters:
        c : The cutoff value.
        mean : Mean (μ) of the normal distribution.
        stDev : Standard deviation (σ).
        onesided : If True, compute a one-sided probability.
        GT : If True, compute P(X > c), otherwise P(X < c).
    """
    if onesided:
        return Probability(GPDF, (mean, stDev), c, GT=GT)
    else:
        tail = Probability(GPDF, (mean, stDev), c, GT=True)
        central_prob = 1 - 2 * tail  # P(μ-(c-μ) < x < μ+(c-μ))
        return central_prob if not GT else 1 - central_prob


def main():
#initial inputs
    side = (input("c or p:")) #input that determines weather looking for c or p
    mean = float(input("input mean:"))
    stDev = float(input("input stDev:"))


    prob_types = {
        1: ("P(X < c | μ,σ)", True, False),
        2: ("P(X > c | μ,σ)", True, True),
        3: ("P(μ-(c-μ) < X < μ+(c-μ) | μ, σ)", False, False),
        4: ("P(μ-(c-μ) > X > μ+(c-μ) | μ, σ)", False, True)}
#looking for c
    if side == "c":
        c = float(input("Enter value of c: "))
        print("Select probability type:")
        for key, value in prob_types.items():
            print(f"{key}. {value[0]}")
        prob_option = int(input("Enter 1, 2, 3, or 4: "))

        if prob_option in prob_types:
            probability = probability_input(c, mean, stDev, onesided=prob_types[prob_option][1],
                                            GT=prob_types[prob_option][2])
            print(f"Computed Probability: {probability:.6f}")
        else:
            print("Invalid option.")
#looking for probability
    elif side == "p":
        probability = float(input("Enter desired probability P: "))
        print("Select probability type:")
        for key, value in prob_types.items():
            print(f"{key}. {value[0]}")
        prob_option = int(input("Enter 1, 2, 3, or 4: "))

        if prob_option in prob_types:
            c_func = lambda c: probability_input(c, mean, stDev, onesided=prob_types[prob_option][1],
                                                 GT=prob_types[prob_option][2])
            c_value, iterations = Secant(lambda c: c_func(c) - probability, mean, mean + stDev)
            print(f"Computed value of c: {c_value:.6f} (Converged in {iterations} iterations)")
        else:
            print("Invalid option.")

    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()






