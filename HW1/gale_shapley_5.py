import random
def gale_shapley(m_prefs, w_prefs):
    m_pointers = [0 for m in range(len(m_prefs))]
    w_matches = {w : None for w in range(len(w_prefs))}
    all_males = set([i for i in range(0, len(m_prefs))])
    engaged = set()
    matches = []
    m_g, w_g = 0, 0 
    while engaged != all_males:
        for male in m_prefs:
            if male in engaged:
                continue
            highest_w = m_prefs[male][m_pointers[male]]
            if not w_matches[highest_w]:
                w_matches[highest_w] = (male, w_prefs[highest_w].index(male))
                engaged.add(male)
            else:
                if w_matches[highest_w][1] > w_prefs[highest_w].index(male):
                    engaged.remove(w_matches[highest_w][0])
                    w_matches[highest_w] = (male, w_prefs[highest_w].index(male))
                    engaged.add(male)
            m_pointers[male] += 1
    for female, male in w_matches.items():
        matches.append((male[0], female))

    # Debug:
    # print(f'male: {w_matches}')
    # print(f'result matching: {matches}')

    # Calculate the goodness of males and females:
    n, m_total, f_total = len(m_prefs), 0, 0
    for m_i, f_i in matches:
        m_total += m_prefs[m_i].index(f_i) + 1
        f_total += w_prefs[f_i].index(m_i) + 1
    return n, m_total / n, f_total / n

def create_preferences(n):
    m_prefs, w_prefs = {m : [w_i for w_i in range(n)] for m in range(n)}, {w : [m_i for m_i in range(n)] for w in range(n)}
    for m_w in range(n):
        random.shuffle(m_prefs[m_w])
        random.shuffle(w_prefs[m_w])
    return m_prefs, w_prefs

if __name__ == '__main__':
    for n in range(1, 1001):
        m_prefs, w_prefs = create_preferences(n)
        res = gale_shapley(m_prefs, w_prefs)
        print(f'{[res[0], res[1], res[2]]}')