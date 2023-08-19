def gale_shapley(m_prefs, w_prefs):
    m_pointers = [0 for m in range(len(m_prefs))]
    w_matches = {w : None for w in range(len(w_prefs))}
    all_males = set([i for i in range(0, len(m_prefs))])
    engaged = set()
    matches = []
    while engaged != all_males:
        for male in m_prefs:
            if male in engaged:
                continue
            # Propose to the most preferable female on their list
            highest_w = m_prefs[male][m_pointers[male]]
            m_pointers[male] += 1
            print(f'male {male} proposes to female {highest_w}')
            # Female will have to decide to either accept or reject the current offer made to them
            if not w_matches[highest_w]:
                w_matches[highest_w] = (male, w_prefs[highest_w].index(male))
                engaged.add(male)
                print(f'--> male {male}\'s proposal is accepted')
            else:
                if w_matches[highest_w][1] > w_prefs[highest_w].index(male):
                    engaged.remove(w_matches[highest_w][0])
                    print(f'--> female {highest_w} rejects male {w_matches[highest_w][0]}')
                    w_matches[highest_w] = (male, w_prefs[highest_w].index(male))
                    print(f'--> female {highest_w} accepts male {w_matches[highest_w][0]}\'s proposal')
                    engaged.add(male)
                else:
                    print(f'--> male {male}\'s proposal is rejected')
    for w, m in w_matches.items():
        matches.append((m[0], w))
    return matches

def stable_matching_1(men_prefs, women_prefs):
    single_men = set(men_prefs.keys())
    matches = {}
    while single_men:
        man = single_men.pop()
        for woman in men_prefs[man]:
            if woman not in matches:
                matches[woman] = man
                break
            else:
                current_match = matches[woman]
                if women_prefs[woman].index(man) < women_prefs[woman].index(current_match):
                    matches[woman] = man
                    single_men.add(current_match)
                    break
    return matches

if __name__ == '__main__':

    m_prefs_1 = {0: [2, 1, 3, 0],
                 1: [0, 1, 3, 2],
                 2: [0, 1, 2, 3],
                 3: [0, 1, 2, 3]}

    w_prefs_1 = {0: [0, 2, 1, 3],
                 1: [2, 0, 3, 1],
                 2: [3, 2, 1, 0],
                 3: [2, 3, 1, 0]}

    # m_prefs_2 = {0: [2, 0, 1],
    #              1: [2, 0, 1],
    #              2: [2, 1, 0]}

    # w_prefs_2 = {0: [2, 0, 1],
    #              1: [0, 2, 1],
    #              2: [2, 0, 1]}

    # Each male that is not engaged will propose to the female that is highest on their list
    # The female being proposed to will need to:
    #   - Accept the offer if it is their first offer
    #   - Reject if this is a worse offer than their current offer
    #   - Accept if this is better than their current offer, and reject their previous offer

    stable_matches_1 = gale_shapley(m_prefs_1, w_prefs_1)
    print(f'Result Matching: {stable_matches_1}')
    # print()
    # stable_matches_2 = gale_shapley(m_prefs_2, w_prefs_2)
    # print(f'Result Matching: {stable_matches_2}')
