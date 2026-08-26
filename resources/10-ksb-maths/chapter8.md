# **Chapter 8: Real Numbers — Study Guide**

---

## **I. Core Concepts & Algebraic Principles**

### **1. Euclid’s Division Lemma**

- **Theorem 8.1:** Given positive integers \\(a\\) and \\(b\\), there exist unique integers \\(q\\) and \\(r\\) satisfying:
  \\[a = bq + r, \quad 0 \le r < b\\]
  Here, \\(q\\) is the **quotient** and \\(r\\) is the **remainder**. This lemma is a formal restatement of the long division process.

---

### **2. Euclid’s Division Algorithm**

- This is a technique used to compute the **Highest Common Factor (HCF)** of two positive integers. The HCF of positive integers \\(a\\) and \\(b\\) is the largest positive integer \\(d\\) that divides both \\(a\\) and \\(b\\).
- **Procedure:** To find the HCF of two positive integers \\(c\\) and \\(d\\) (where \\(c > d\\)):
  - **Step 1:** Apply Euclid's division lemma to find \\(q\\) and \\(r\\) such that \\(c = dq + r, \ 0 \le r < d\\).
  - **Step 2:** If \\(r = 0\\), then \\(d\\) is the HCF. If \\(r \neq 0\\), apply the division lemma to \\(d\\) and \\(r\\).
  - **Step 3:** Repeat this process until the remainder is zero. The divisor at this stage is the required HCF.

---

### **3. The Fundamental Theorem of Arithmetic**

- **Theorem 8.2:** Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur.
- **Standard Form:** When we express a composite number \\(x\\) as a product of prime factors sorted in ascending order (\\(p_1 \le p_2 \le \dots \le p_n\\)), the prime factorisation is entirely unique:
  \\[x = p_1^{a_1} \cdot p_2^{a_2} \dots p_n^{a_n}\\]

#### **Geometric Flow: Prime Factorisation Tree of 32760 (Theorem 8.2 Visualisation)**

The prime factorisation of \\(32760\\) can be systematically found using a factor tree:
\\[32760 = 2^3 \times 3^2 \times 5 \times 7 \times 13\\]

```xml
<svg width="500" height="460" viewBox="0 0 500 460" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .node-composite { fill: #fff; stroke: #0f172a; stroke-width: 2; }
    .node-prime { fill: #f0fdf4; stroke: #16a34a; stroke-width: 2.5; }
    .tree-branch { stroke: #64748b; stroke-width: 1.5; fill: none; }
    .text-val { font-family: 'Consolas', monospace; font-size: 13px; fill: #0f172a; text-anchor: middle; font-weight: bold; }
    .label-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; text-anchor: middle; }
  </style>

  <!-- Title -->
  <text x="250" y="25" class="label-title">Factor Tree of 32760</text>

  <!-- Level 1 (32760) -->
  <line x1="120" y1="45" x2="70" y2="95" class="tree-branch" />
  <line x1="120" y1="45" x2="170" y2="95" class="tree-branch" />
  <circle cx="120" cy="45" r="22" class="node-composite" />
  <text x="120" y="49" class="text-val">32760</text>

  <!-- Level 2 (2 & 16380) -->
  <line x1="170" y1="95" x2="120" y2="145" class="tree-branch" />
  <line x1="170" y1="95" x2="220" y2="145" class="tree-branch" />
  <circle cx="70" cy="95" r="18" class="node-prime" />
  <text x="70" y="99" class="text-val" style="fill:#16a34a;">2</text>
  <circle cx="170" cy="95" r="22" class="node-composite" />
  <text x="170" y="99" class="text-val">16380</text>

  <!-- Level 3 (2 & 8190) -->
  <line x1="220" y1="145" x2="170" y2="195" class="tree-branch" />
  <line x1="220" y1="145" x2="270" y2="195" class="tree-branch" />
  <circle cx="120" cy="145" r="18" class="node-prime" />
  <text x="120" y="149" class="text-val" style="fill:#16a34a;">2</text>
  <circle cx="220" cy="145" r="20" class="node-composite" />
  <text x="220" y="149" class="text-val">8190</text>

  <!-- Level 4 (2 & 4095) -->
  <line x1="270" y1="195" x2="220" y2="245" class="tree-branch" />
  <line x1="270" y1="195" x2="320" y2="245" class="tree-branch" />
  <circle cx="170" cy="195" r="18" class="node-prime" />
  <text x="170" y="199" class="text-val" style="fill:#16a34a;">2</text>
  <circle cx="270" cy="195" r="20" class="node-composite" />
  <text x="270" y="199" class="text-val">4095</text>

  <!-- Level 5 (3 & 1365) -->
  <line x1="320" y1="245" x2="270" y2="295" class="tree-branch" />
  <line x1="320" y1="245" x2="370" y2="295" class="tree-branch" />
  <circle cx="220" cy="245" r="18" class="node-prime" />
  <text x="220" y="249" class="text-val" style="fill:#16a34a;">3</text>
  <circle cx="320" cy="245" r="20" class="node-composite" />
  <text x="320" y="249" class="text-val">1365</text>

  <!-- Level 6 (3 & 455) -->
  <line x1="370" y1="295" x2="320" y2="345" class="tree-branch" />
  <line x1="370" y1="295" x2="420" y2="345" class="tree-branch" />
  <circle cx="270" cy="295" r="18" class="node-prime" />
  <text x="270" y="299" class="text-val" style="fill:#16a34a;">3</text>
  <circle cx="370" cy="295" r="20" class="node-composite" />
  <text x="370" y="299" class="text-val">455</text>

  <!-- Level 7 (5 & 91) -->
  <line x1="420" y1="345" x2="370" y2="395" class="tree-branch" />
  <line x1="420" y1="345" x2="470" y2="395" class="tree-branch" />
  <circle cx="320" cy="345" r="18" class="node-prime" />
  <text x="320" y="349" class="text-val" style="fill:#16a34a;">5</text>
  <circle cx="420" cy="345" r="18" class="node-composite" />
  <text x="420" y="349" class="text-val">91</text>

  <!-- Level 8 (7 & 13) -->
  <circle cx="370" cy="395" r="18" class="node-prime" />
  <text x="370" y="399" class="text-val" style="fill:#16a34a;">7</text>
  <circle cx="470" cy="395" r="18" class="node-prime" />
  <text x="470" y="399" class="text-val" style="fill:#16a34a;">13</text>
</svg>
```

---

### **4. HCF and LCM of Numbers (Using Prime Factorisation)**

- **Highest Common Factor (HCF):** The product of the **smallest power** of each common prime factor in the numbers.
- **Least Common Multiple (LCM):** The product of the **greatest power** of each prime factor involved in the numbers.
- **The Product Formula:** For any two positive integers \\(a\\) and \\(b\\):
  \\[\text{HCF}(a, b) \times \text{LCM}(a, b) = a \times b\\]
  _Note: This relationship does not hold true for three or more numbers._

---

### **5. Revisiting Irrational Numbers & Proof by Contradiction**

- **Theorem 8.3:** Let \\(p\\) be a prime number. If \\(p\\) divides \\(a^2\\), then \\(p\\) divides \\(a\\), where \\(a\\) is a positive integer.
- **Proof by Contradiction:** To prove a number is irrational, we assume the opposite (that it is rational of the form \\(a/b\\), where \\(a\\) and \\(b\\) are coprime integers) and deduce a logical contradiction, showing our initial assumption must be incorrect.

---

### **6. Rational Numbers and their Decimal Expansions**

Let \\(x = \frac{p}{q}\\) be a rational number such that \\(p\\) and \\(q\\) are coprimes:

- **Terminating Decimal Expansion (Theorem 8.5 & 8.6):** \\(x\\) has a terminating decimal expansion if and only if the prime factorisation of \\(q\\) is of the form **\\(2^n 5^m\\)**, where \\(n, m\\) are non-negative integers.
- **Non-Terminating Repeating (Recurring) Decimal Expansion (Theorem 8.7):** \\(x\\) has a non-terminating repeating decimal expansion if the prime factorisation of \\(q\\) is **not** of the form \\(2^n 5^m\\).

---

## **II. Example Problems (with Step-by-Step Solutions)**

### **Example 1**

**Problem:** Use Euclid's division algorithm to find the HCF of \\(4052\\) and \\(12576\\).

- **Solution:**
  - Since \\(12576 > 4052\\), apply the division lemma:
    \\[12576 = 4052 \times 3 + 420\\]
  - Since the remainder \\(420 \neq 0\\), apply the lemma to \\(4052\\) and \\(420\\):
    \\[4052 = 420 \times 9 + 272\\]
  - Since \\(272 \neq 0\\), apply the lemma to \\(420\\) and \\(272\\):
    \\[420 = 272 \times 1 + 148\\]
  - Since \\(148 \neq 0\\), apply the lemma to \\(272\\) and \\(148\\):
    \\[272 = 148 \times 1 + 124\\]
  - Since \\(124 \neq 0\\), apply the lemma to \\(148\\) and \\(124\\):
    \\[148 = 124 \times 1 + 24\\]
  - Since \\(24 \neq 0\\), apply the lemma to \\(124\\) and \\(24\\):
    \\[124 = 24 \times 5 + 4\\]
  - Since \\(4 \neq 0\\), apply the lemma to \\(24\\) and \\(4\\):
    \\[24 = 4 \times 6 + 0\\]
  - The remainder has become zero. The divisor at this stage is \\(4\\).
  - **Answer:** The HCF of \\(12576\\) and \\(4052\\) is **\\(4\\)**.

---

### **Example 2**

**Problem:** Show that every positive even integer is of the form \\(2q\\), and that every positive odd integer is of the form \\(2q+1\\), where \\(q\\) is some integer.

- **Solution:**
  - Let \\(a\\) be any positive integer and \\(b = 2\\).
  - By Euclid's division lemma, \\(a = 2q + r\\) for some integer \\(q \ge 0\\), where \\(0 \le r < 2\\).
  - The possible values for the remainder \\(r\\) are \\(0\\) and \\(1\\).
  - If \\(r = 0\\), then \\(a = 2q\\), which is divisible by \\(2\\) and thus represents an **even integer**.
  - If \\(r = 1\\), then \\(a = 2q + 1\\), which is not divisible by \\(2\\) and thus represents an **odd integer**.

---

### **Example 3**

**Problem:** Show that any positive odd integer is of the form \\(4q+1\\) or \\(4q+3\\), where \\(q\\) is some integer.

- **Solution:**
  - Let \\(a\\) be a positive odd integer. Apply Euclid's lemma with \\(b = 4\\).
  - Since \\(0 \le r < 4\\), the possible remainders are \\(r = 0, 1, 2, 3\\).
  - Thus, \\(a\\) can be written as \\(4q\\), \\(4q+1\\), \\(4q+2\\), or \\(4q+3\\).
  - However, since \\(a\\) is given to be an **odd integer**, it cannot be \\(4q\\) or \\(4q+2\\) because both of these are divisible by \\(2\\) (i.e., \\(4q = 2(2q)\\) and \\(4q+2 = 2(2q+1)\\)).
  - Therefore, any positive odd integer must be of the form **\\(4q+1\\)** or **\\(4q+3\\)**.

---

### **Example 4**

**Problem:** A sweetseller has \\(420\\) kaju barfis and \\(130\\) badam barfis. She wants to stack them in such a way that each stack has the same number, and they take up the least area of the tray. What is the maximum number of barfis that can be placed in each stack for this purpose?

- **Solution:**
  - To find the maximum number of barfis per stack (using the least area), we need to find the HCF of \\(420\\) and \\(130\\).
  - Applying Euclid’s division algorithm:
    \\[420 = 130 \times 3 + 30\\]
    \\[130 = 30 \times 4 + 10\\]
    \\[30 = 10 \times 3 + 0\\]
  - The HCF is \\(10\\).
  - **Answer:** The sweetseller can make stacks of **\\(10\\)** for both kinds of barfi.

---

### **Example 5**

**Problem:** Consider the numbers \\(4^n\\), where \\(n\\) is a natural number. Check whether there is any value of \\(n\\) for which \\(4^n\\) ends with the digit zero.

- **Solution:**
  - For a number to end with the digit \\(0\\), its prime factorisation must contain the prime factor \\(5\\) (since it must be divisible by \\(2 \times 5 = 10\\)).
  - The prime factorisation of \\(4^n\\) is:
    \\[4^n = (2^2)^n = 2^{2n}\\]
  - The only prime factor in the factorisation of \\(4^n\\) is \\(2\\).
  - By the uniqueness of the Fundamental Theorem of Arithmetic, no other prime factor (specifically \\(5\\)) can appear in the prime factorisation of \\(4^n\\).
  - **Answer:** There is no natural number \\(n\\) for which \\(4^n\\) ends with the digit zero.

---

### **Example 6**

**Problem:** Find the HCF and LCM of \\(6\\) and \\(20\\) by the prime factorisation method.

- **Solution:**
  - Prime factorisation:
    \\[6 = 2^1 \times 3^1\\]
    \\[20 = 2^2 \times 5^1\\]
  - \\(\text{HCF}(6, 20) = 2^1 = 2\\) (Product of the smallest power of each common prime factor).
  - \\(\text{LCM}(6, 20) = 2^2 \times 3^1 \times 5^1 = 4 \times 3 \times 5 = 60\\) (Product of the greatest power of each prime factor involved).

---

### **Example 7**

**Problem:** Find the HCF of \\(96\\) and \\(404\\) by the prime factorisation method. Hence, find their LCM.

- **Solution:**
  - Prime factorisation:
    \\[96 = 2^5 \times 3^1\\]
    \\[404 = 2^2 \times 101^1\\]
  - \\(\text{HCF}(96, 404) = 2^2 = 4\\).
  - Using the product formula \\(\text{LCM}(a, b) = \frac{a \times b}{\text{HCF}(a, b)}\\):
    \\[\text{LCM}(96, 404) = \frac{96 \times 404}{4} = 96 \times 101 = 9696\\]
  - **Answer:** \\(\text{HCF} = 4\\), \\(\text{LCM} = 9696\\).

---

### **Example 8**

**Problem:** Find the HCF and LCM of \\(6\\), \\(72\\), and \\(120\\) using the prime factorisation method.

- **Solution:**
  - Prime factorisation:
    \\[6 = 2^1 \times 3^1\\]
    \\[72 = 2^3 \times 3^2\\]
    \\[120 = 2^3 \times 3^1 \times 5^1\\]
  - The common prime factors are \\(2\\) and \\(3\\). Their lowest powers are \\(2^1\\) and \\(3^1\\).
    \\[\text{HCF}(6, 72, 120) = 2^1 \times 3^1 = 6 \quad.\\]
  - The highest powers of all prime factors involved (\\(2\\), \\(3\\), \\(5\\)) are \\(2^3\\), \\(3^2\\), and \\(5^1\\).
    \\[\text{LCM}(6, 72, 120) = 2^3 \times 3^2 \times 5^1 = 8 \times 9 \times 5 = 360 \quad.\\]

---

### **Example 9**

**Problem:** Prove that \\(\sqrt{3}\\) is irrational.

- **Solution:**
  - Assume to the contrary that \\(\sqrt{3}\\) is rational.
  - Thus, we can find coprime integers \\(a\\) and \\(b\\) (\\(b \neq 0\\)) such that:
    \\[\sqrt{3} = \frac{a}{b}\\]
  - Squaring both sides and rearranging:
    \\[3b^2 = a^2 \quad \text{--- (Eq. 1)}\\]
  - Therefore, \\(a^2\\) is divisible by \\(3\\). By Theorem 8.3, \\(a\\) must also be divisible by \\(3\\).
  - Let \\(a = 3c\\) for some integer \\(c\\). Substitute this into (Eq. 1):
    \\[3b^2 = (3c)^2 = 9c^2 \implies b^2 = 3c^2\\]
  - This implies \\(b^2\\) is divisible by \\(3\\), and so \\(b\\) is also divisible by \\(3\\) (Theorem 8.3).
  - Hence, \\(a\\) and \\(b\\) have \\(3\\) as a common factor, which contradicts the fact that \\(a\\) and \\(b\\) are coprimes (having no common factor other than \\(1\\)).
  - This contradiction shows our assumption was false. Thus, **\\(\sqrt{3}\\) is irrational**.

---

### **Example 10**

**Problem:** Show that \\(5 - \sqrt{3}\\) is irrational.

- **Solution:**
  - Assume to the contrary that \\(5 - \sqrt{3}\\) is rational.
  - Then, we can find coprime integers \\(a\\) and \\(b\\) (\\(b \neq 0\\)) such that:
    \\[5 - \sqrt{3} = \frac{a}{b}\\]
  - Rearranging the terms:
    \\[\sqrt{3} = 5 - \frac{a}{b} = \frac{5b - a}{b}\\]
  - Since \\(a\\) and \\(b\\) are integers, the RHS expression \\(\frac{5b - a}{b}\\) is rational. This implies that \\(\sqrt{3}\\) is rational, which contradicts the established fact that \\(\sqrt{3}\\) is irrational.
  - Thus, the assumption was wrong. **\\(5 - \sqrt{3}\\) is irrational**.

---

### **Example 11**

**Problem:** Show that \\(3\sqrt{2}\\) is irrational.

- **Solution:**
  - Assume to the contrary that \\(3\sqrt{2}\\) is rational.
  - Thus, we can find coprime integers \\(a\\) and \\(b\\) (\\(b \neq 0\\)) such that:
    \\[3\sqrt{2} = \frac{a}{b}\\]
  - Rearranging the terms:
    \\[\sqrt{2} = \frac{a}{3b}\\]
  - Since \\(3\\), \\(a\\), and \\(b\\) are integers, \\(\frac{a}{3b}\\) is rational. This implies \\(\sqrt{2}\\) is rational, which contradicts the fact that \\(\sqrt{2}\\) is irrational.
  - Therefore, **\\(3\sqrt{2}\\) is irrational**.

---

## **III. Exercises**

### **EXERCISE 8.1**

1.  Use Euclid's division algorithm to find the HCF of:
    (i) \\(135\\) and \\(225\\)
    (ii) \\(196\\) and \\(38220\\)
    (iii) \\(867\\) and \\(255\\)
2.  Show that any positive odd integer is of the form \\(6q+1\\), or \\(6q+3\\), or \\(6q+5\\), where \\(q\\) is some integer.
3.  An army contingent of \\(616\\) members is to march behind an army band of \\(32\\) members in a parade. The two groups are to march in the same number of columns. What is the maximum number of columns in which they can march?
4.  Use Euclid's division lemma to show that the square of any positive integer is either of the form \\(3m\\) or \\(3m+1\\) for some integer \\(m\\).
5.  Use Euclid's division lemma to show that the cube of any positive integer is of the form \\(9m, 9m+1\\) or \\(9m+8\\).

---

### **EXERCISE 8.2**

1.  Express each number as a product of its prime factors:
    (i) \\(140\\) \quad (ii) \\(156\\) \quad (iii) \\(3825\\) \quad (iv) \\(5005\\) \quad (v) \\(7429\\)
2.  Find the LCM and HCF of the following pairs of integers and verify that \\(\text{LCM} \times \text{HCF} = \text{product of the two numbers}\\):
    (i) \\(26\\) and \\(91\\) \quad (ii) \\(510\\) and \\(92\\) \quad (iii) \\(336\\) and \\(54\\)
3.  Find the LCM and HCF of the following integers by applying the prime factorisation method:
    (i) \\(12, 15\\) and \\(21\\) \quad (ii) \\(17, 23\\) and \\(29\\) \quad (iii) \\(8, 9\\) and \\(25\\)
4.  Given that \\(\text{HCF}(306, 657) = 9\\), find \\(\text{LCM}(306, 657)\\).
5.  Check whether \\(6^n\\) can end with the digit \\(0\\) for any natural number \\(n\\).
6.  Explain why \\(7 \times 11 \times 13 + 13\\) and \\(7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 + 5\\) are composite numbers.
7.  There is a circular path around a sports field. Sonia takes \\(18\\) minutes to drive one round of the field, while Ravi takes \\(12\\) minutes for the same. Suppose they both start at the same point and at the same time, and go in the same direction. After how many minutes will they meet again at the starting point?

---

### **EXERCISE 8.3**

1.  Prove that \\(\sqrt{5}\\) is irrational.
2.  Prove that \\(3+2\sqrt{5}\\) is irrational.
3.  Prove that the following are irrationals:
    (i) \\(\frac{1}{\sqrt{2}}\\) \quad (ii) \\(7\sqrt{5}\\) \quad (iii) \\(6+\sqrt{2}\\)

---

### **EXERCISE 8.4**

1.  Without actually performing the long division, state whether the following rational numbers will have a terminating decimal expansion or a non-terminating repeating decimal expansion:
    (i) \\(\frac{13}{3125}\\) \quad (ii) \\(\frac{17}{8}\\) \quad (iii) \\(\frac{64}{455}\\) \quad (iv) \\(\frac{15}{1600}\\) \quad (v) \\(\frac{29}{343}\\) \quad (vi) \\(\frac{23}{2^3 5^2}\\) \quad (vii) \\(\frac{129}{2^2 5^7 7^5}\\) \quad (viii) \\(\frac{6}{15}\\) \quad (ix) \\(\frac{35}{50}\\) \quad (x) \\(\frac{77}{210}\\)
2.  Write down the decimal expansions of those rational numbers in Question 1 above which have terminating decimal expansions.
3.  The following real numbers have decimal expansions as given below. In each case, decide whether they are rational or not. If they are rational, and of the form \\(\frac{p}{q}\\), what can you say about the prime factors of \\(q\\)?
    (i) \\(43.123456789\\)
    (ii) \\(0.120120012000120000\dots\\)
    (iii) \\(43.\overline{123456789}\\)

---

📐 I can construct an interactive Python-based HCF/LCM solver or write a clean PDF reference document containing all these proof structures (such as prime factor trees and contradiction steps). What would you like to build next?
