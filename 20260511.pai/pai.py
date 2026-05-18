import math

print("计算π的近似值，使用公式 π ≈ n * sin(π/n)")
print("-" * 50)

for exponent in range(1, 11):
    n = 2 ** exponent
    pi_approx = n * math.sin(math.pi / n)
    print(f"2^{exponent} = {n:<5} | π ≈ {pi_approx:.15f}")