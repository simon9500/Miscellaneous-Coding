def conditional_roulette_probs(history):
    """

    Example:
    conditional_roulette_probs([1, 3, 1, 5, 1])
    > {1: {3: 0.5, 5: 0.5},
       3: {1: 1.0},
       5: {1: 1.0}
      }
    """
    dict = {}

    for i in range(len(history) - 1):
        n1 = history[i]
        n2 = history[i + 1]
        dict[n1] = {}
        if dict[n1]:
            dict[n1][n2] = 0.
            dict[n1][n2] += 1.
            print "non-empty"
        else:
            dict[n1] = {}
            dict[n1][n2] = 0.
            dict[n1][n2] += 1.
            print "empty"
        print n1, n2, dict[n1][n2]
        print dict


    for n1, n2 in dict.items():
        total = len(dict[n1])
        for key in n2:
            num_appearances = dict[n1][key]
            dict[n1][key] = num_appearances / total

    return dict

conditional_roulette_probs([1, 3, 1, 5, 1])