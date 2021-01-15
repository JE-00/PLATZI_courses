
def calcular_bayes(prior_A, prob_B_dado_A, prob_B):
    return (prior_A * prob_B_dado_A) / prob_B


if __name__ == '__main__':
    prob_H = 1/100000
    prob_E_dado_H = 1
    prob_E_dado_h = 10/99999
    prob_h = 1 - prob_H  # Representa ¬H

    prob_E = (prob_E_dado_H * prob_H) + (prob_E_dado_h * prob_h)

    prob_H_dado_E = calcular_bayes(prob_H, prob_E_dado_h, prob_E)

    print(prob_H_dado_E)
