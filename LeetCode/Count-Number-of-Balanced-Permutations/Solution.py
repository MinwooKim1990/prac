from collections import Counter, defaultdict

class Solution:
  def countBalancedPermutations(self, num: str) -> int:
    MOD = 10**9 + 7

    n_total = len(num)
    digits_int = [int(d) for d in num]
    
    total_sum = sum(digits_int)
    if total_sum % 2 != 0:
        return 0
    
    target_sum_even = total_sum // 2
    
    len_even_slots = (n_total + 1) // 2
    len_odd_slots = n_total // 2

    digit_freq_map = Counter(digits_int)
    distinct_sorted_digits_with_freq = sorted(digit_freq_map.items())

    max_fact_arg = n_total 

    fact = [1] * (max_fact_arg + 1)
    inv_fact = [1] * (max_fact_arg + 1)
    for i in range(1, max_fact_arg + 1):
        fact[i] = (fact[i-1] * i) % MOD
    
    inv_fact[max_fact_arg] = pow(fact[max_fact_arg], MOD - 2, MOD)
    for i in range(max_fact_arg - 1, -1, -1): 
        inv_fact[i] = (inv_fact[i+1] * (i+1)) % MOD
    
    dp_prev = defaultdict(int)
    dp_prev[(0, 0, 0)] = 1 

    for digit_val, total_freq_of_current_digit in distinct_sorted_digits_with_freq:
        dp_next = defaultdict(int)
        for (k_e, s_e, k_o), prev_dp_val in dp_prev.items():
            if prev_dp_val == 0:
                continue

            for num_curr_for_even in range(total_freq_of_current_digit + 1):
                num_curr_for_odd = total_freq_of_current_digit - num_curr_for_even

                new_k_e = k_e + num_curr_for_even
                new_s_e = s_e + num_curr_for_even * digit_val
                new_k_o = k_o + num_curr_for_odd

                if new_k_e <= len_even_slots and \
                   new_s_e <= target_sum_even and \
                   new_k_o <= len_odd_slots:

                    term_contribution = (prev_dp_val * inv_fact[num_curr_for_even]) % MOD
                    term_contribution = (term_contribution * inv_fact[num_curr_for_odd]) % MOD
                    
                    dp_next[(new_k_e, new_s_e, new_k_o)] = \
                        (dp_next[(new_k_e, new_s_e, new_k_o)] + term_contribution) % MOD
        dp_prev = dp_next

    velunexorai = dp_prev.get((len_even_slots, target_sum_even, len_odd_slots), 0)
    
    ans = (velunexorai * fact[len_even_slots]) % MOD
    ans = (ans * fact[len_odd_slots]) % MOD
    
    return ans