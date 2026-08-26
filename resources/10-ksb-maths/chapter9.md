# **Chapter 9: Polynomials — Study Guide**

---

## **I. Core Concepts & Geometrical Principles**

### **1. Introduction to Polynomials & Degrees**

- **Definition:** If \\(p(x)\\) is a polynomial in the variable \\(x\\), the highest power of \\(x\\) in \\(p(x)\\) is defined as the **degree of the polynomial**.
- **Non-Polynomial Expressions:** Mathematical expressions such as \\(\frac{1}{x-1}\\), \\(\sqrt{x}+2\\), and \\(\frac{1}{x^2+2x+3}\\) are **not** polynomials.
- **Classification by Degree:**
  - **Linear Polynomial:** A polynomial of **degree 1**. Examples include \\(2x-3\\), \\(\sqrt{3}x+5\\), \\(y+\sqrt{2}\\), \\(3z+4\\), and \\(\frac{2}{3}u+1\\).
  - **Quadratic Polynomial:** A polynomial of **degree 2**. The word "quadratic" is derived from **_"quadrate"_**, meaning "square". Examples include \\(2x^2+3x-\frac{2}{5}\\), \\(y^2-2\\), and \\(4z^2+\frac{1}{7}\\). The general form is:
    \\[ax^2 + bx + c \quad (a, b, c \in \mathbb{R}, \ a \neq 0) \quad \text{}\\]
  - **Cubic Polynomial:** A polynomial of **degree 3**. Examples include \\(2-x^3\\), \\(x^3\\), and \\(3x^3-2x^2+x-1\\). The general form is:
    \\[ax^3 + bx^2 + cx + d \quad (a, b, c, d \in \mathbb{R}, \ a \neq 0) \quad \text{}\\]

---

### **2. Value and Zeroes of a Polynomial**

- **Value of a Polynomial:** If \\(p(x)\\) is a polynomial in \\(x\\), and \\(k\\) is any real number, the value obtained by replacing \\(x\\) by \\(k\\) in \\(p(x)\\) is denoted as **\\(p(k)\\)**.
- **Zero of a Polynomial:** A real number \\(k\\) is said to be a **zero** of a polynomial \\(p(x)\\) if:
  \\[p(k) = 0 \quad \text{}\\]
- **Linear Zero:** The unique zero of the general linear polynomial \\(ax+b\\) is related directly to its coefficients:
  \\[k = -\frac{b}{a} = \frac{-(\text{Constant term})}{\text{Coefficient of } x} \quad \text{}\\]

---

### **3. Geometrical Meaning of the Zeroes of a Polynomial**

Geometrically, the zeroes of any polynomial \\(p(x)\\) are precisely the **x-coordinates of the points where the graph of \\(y = p(x)\\) intersects the x-axis**.

#### **A. Linear Polynomial Graph (\\(y = 2x+3\\))**

The graph of a linear equation \\(y = ax+b\\) is a straight line that intersects the x-axis at exactly one point, namely \\((\frac{-b}{a}, 0)\\).

```xml
<svg width="400" height="280" viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .grid { stroke: #cbd5e1; stroke-width: 0.5; }
    .axis { stroke: #0f172a; stroke-width: 2; }
    .line-eq { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; fill: #334155; }
    .lbl-bold { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
    .pt-highlight { fill: #ef4444; stroke: #ffffff; stroke-width: 1.5; }
  </style>

  <!-- Background Grid -->
  <path d="M 50,40 L 50,240 M 100,40 L 100,240 M 150,40 L 150,240 M 200,40 L 200,240 M 250,40 L 250,240 M 300,40 L 300,240 M 350,40 L 350,240" class="grid"/>
  <path d="M 40,50 L 360,50 M 40,100 L 360,100 M 40,150 L 360,150 M 40,200 L 360,200 M 40,240 L 360,240" class="grid"/>

  <!-- Axis Lines -->
  <line x1="200" y1="20" x2="200" y2="250" class="axis"/> <!-- y-axis -->
  <line x1="30" y1="150" x2="370" y2="150" class="axis"/> <!-- x-axis -->

  <!-- Axis labels -->
  <text x="375" y="155" class="lbl-bold">X</text>
  <text x="195" y="15" class="lbl-bold">Y</text>
  <text x="185" y="165" class="lbl">O</text>

  <!-- Line y = 2x + 3 -->
  <line x1="125" y1="210" x2="230" y2="0" class="line-eq"/>
  <text x="240" y="30" class="lbl-bold" style="fill:#0284c7;">y = 2x + 3</text>

  <!-- Intersection point at (-1.5, 0) -->
  <circle cx="155" cy="150" r="5" class="pt-highlight"/>
  <text x="105" y="140" class="lbl-bold" style="fill:#ef4444;">(-3/2, 0)</text>
</svg>
```

#### **B. Quadratic Polynomial Graph (\\(y = x^2 - 3x - 4\\))**

The graph of \\(y = ax^2 + bx + c\\) is a symmetric U-shaped curve called a **parabola**. It opens **upward** (\\(\cup\\)) if \\(a > 0\\), and **downward** (\\(\cap\\)) if \\(a < 0\\).

```xml
<svg width="400" height="280" viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .grid { stroke: #cbd5e1; stroke-width: 0.5; }
    .axis { stroke: #0f172a; stroke-width: 2; }
    .curve { stroke: #8b5cf6; stroke-width: 2.5; fill: none; }
    .lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; fill: #334155; }
    .lbl-bold { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
    .pt-highlight { fill: #ef4444; stroke: #ffffff; stroke-width: 1.5; }
  </style>

  <!-- Grid -->
  <path d="M 50,40 L 50,240 M 100,40 L 100,240 M 150,40 L 150,240 M 200,40 L 200,240 M 250,40 L 250,240 M 300,40 L 300,240 M 350,40 L 350,240" class="grid"/>
  <path d="M 40,50 L 360,50 M 40,100 L 360,100 M 40,120 L 360,120 M 40,150 L 360,150 M 40,200 L 360,200" class="grid"/>

  <!-- Axis Lines (Origin at 200, 120) -->
  <line x1="200" y1="20" x2="200" y2="250" class="axis"/>
  <line x1="30" y1="120" x2="370" y2="120" class="axis"/>

  <!-- Labels -->
  <text x="375" y="125" class="lbl-bold">X</text>
  <text x="195" y="15" class="lbl-bold">Y</text>
  <text x="185" y="135" class="lbl">O</text>

  <!-- Parabola path -->
  <path d="M 160,0 C 170,80 190,180 230,245 C 270,180 290,80 300,0" class="curve"/>
  <text x="280" y="40" class="lbl-bold" style="fill:#8b5cf6;">y = x² - 3x - 4</text>

  <!-- Zeroes at x = -1 (180, 120) and x = 4 (280, 120) -->
  <circle cx="180" cy="120" r="5" class="pt-highlight"/>
  <circle cx="280" cy="120" r="5" class="pt-highlight"/>
  <text x="145" y="110" class="lbl-bold" style="fill:#ef4444;">(-1, 0)</text>
  <text x="285" y="110" class="lbl-bold" style="fill:#ef4444;">(4, 0)</text>
</svg>
```

#### **C. Three Cases of Quadratic Parabolas**

The number of real zeroes for a quadratic equation \\(ax^2 + bx + c = 0\\) is determined by the intersection of the parabola with the x-axis:

```xml
<svg width="600" height="200" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .axis { stroke: #64748b; stroke-width: 1.5; }
    .p-curve { stroke: #0284c7; stroke-width: 2; fill: none; }
    .dot-node { fill: #ef4444; }
    .box-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; text-anchor: middle; }
    .box-desc { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #64748b; text-anchor: middle; }
  </style>

  <!-- Panel 1: Case (i) - 2 Distinct Points -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="180" height="150" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <line x1="15" y1="80" x2="165" y2="80" class="axis"/>
    <path d="M 30,20 C 50,110 130,110 150,20" class="p-curve"/>
    <circle cx="43" cy="80" r="4" class="dot-node"/>
    <circle cx="137" cy="80" r="4" class="dot-node"/>
    <text x="90" y="115" class="box-title">Case (i)</text>
    <text x="90" y="132" class="box-desc">Two Distinct Zeroes</text>
  </g>

  <!-- Panel 2: Case (ii) - 1 Touch Point -->
  <g transform="translate(210, 10)">
    <rect x="0" y="0" width="180" height="150" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <line x1="15" y1="80" x2="165" y2="80" class="axis"/>
    <path d="M 30,20 C 50,80 130,80 150,20" class="p-curve" style="stroke:#10b981;"/>
    <circle cx="90" cy="80" r="4" class="dot-node" style="fill:#ef4444;"/>
    <text x="90" y="115" class="box-title" style="fill:#10b981;">Case (ii)</text>
    <text x="90" y="132" class="box-desc">One Zero (Coincident)</text>
  </g>

  <!-- Panel 3: Case (iii) - No Intersections -->
  <g transform="translate(410, 10)">
    <rect x="0" y="0" width="180" height="150" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <line x1="15" y1="80" x2="165" y2="80" class="axis"/>
    <path d="M 30,20 C 50,45 130,45 150,20" class="p-curve" style="stroke:#f59e0b;"/>
    <text x="90" y="115" class="box-title" style="fill:#f59e0b;">Case (iii)</text>
    <text x="90" y="132" class="box-desc">No Real Zeroes</text>
  </g>
</svg>
```

#### **D. Cubic Polynomial Graph (\\(y = x^3 - 4x\\))**

Cubic curves have at most **three** real zeroes since a polynomial of degree \\(n\\) intersects the x-axis at a maximum of \\(n\\) points.

```xml
<svg width="400" height="280" viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .grid { stroke: #cbd5e1; stroke-width: 0.5; }
    .axis { stroke: #0f172a; stroke-width: 2; }
    .cubic-curve { stroke: #ec4899; stroke-width: 2.5; fill: none; }
    .lbl-bold { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
    .pt-highlight { fill: #3b82f6; stroke: #ffffff; stroke-width: 1.5; }
  </style>

  <!-- Grid -->
  <path d="M 50,40 L 50,240 M 100,40 L 100,240 M 150,40 L 150,240 M 200,40 L 200,240 M 250,40 L 250,240 M 300,40 L 300,240 M 350,40 L 350,240" class="grid"/>
  <path d="M 40,50 L 360,50 M 40,100 L 360,100 M 40,120 L 360,120 M 40,150 L 360,150 M 40,200 L 360,200" class="grid"/>

  <!-- Axis Lines (Origin at 200, 120) -->
  <line x1="200" y1="20" x2="200" y2="250" class="axis"/>
  <line x1="30" y1="120" x2="370" y2="120" class="axis"/>

  <!-- Labels -->
  <text x="375" y="125" class="lbl-bold">X</text>
  <text x="195" y="15" class="lbl-bold">Y</text>

  <!-- Cubic Curve: y = x³ - 4x -->
  <!-- Zeroes at x = -2 (150, 120), x = 0 (200, 120), x = 2 (250, 120) -->
  <path d="M 142,230 C 145,150 160,40 200,120 C 240,200 255,90 258,10" class="cubic-curve"/>
  <text x="265" y="30" class="lbl-bold" style="fill:#ec4899;">y = x³ - 4x</text>

  <!-- Zero Dots -->
  <circle cx="150" cy="120" r="5" class="pt-highlight"/>
  <circle cx="200" cy="120" r="5" class="pt-highlight"/>
  <circle cx="250" cy="120" r="5" class="pt-highlight"/>
  <text x="135" y="110" class="lbl-bold" style="fill:#3b82f6;">-2</text>
  <text x="192" y="110" class="lbl-bold" style="fill:#3b82f6;">0</text>
  <text x="255" y="110" class="lbl-bold" style="fill:#3b82f6;">2</text>
</svg>
```

---

## **II. Algebraic Relationships between Zeroes and Coefficients**

### **1. Quadratic Polynomials**

If \\(\alpha\\) and \\(\beta\\) are the zeroes of the quadratic polynomial \\(p(x) = ax^2 + bx + c\\) (\\(a \neq 0\\)):

- **Sum of Zeroes:**
  \\[\alpha + \beta = -\frac{b}{a} = \frac{-(\text{Coefficient of } x)}{\text{Coefficient of } x^2} \quad \text{}\\]
- **Product of Zeroes:**
  \\[\alpha\beta = \frac{c}{a} = \frac{\text{Constant term}}{\text{Coefficient of } x^2} \quad \text{}\\]
- **Equation Formulation:** A quadratic polynomial with sum \\(S\\) and product \\(P\\) of its zeroes is represented as:
  \\[k(x^2 - Sx + P) \quad (k \text{ is a constant}) \quad \text{}\\]

---

### **2. Cubic Polynomials**

If \\(\alpha, \beta,\\) and \\(\gamma\\) are the zeroes of the cubic polynomial \\(p(x) = ax^3 + bx^2 + cx + d\\) (\\(a \neq 0\\)):

- **Sum of Zeroes:**
  \\[\alpha + \beta + \gamma = -\frac{b}{a} = \frac{-(\text{Coefficient of } x^2)}{\text{Coefficient of } x^3} \quad \text{}\\]
- **Sum of Products taken two at a time:**
  \\[\alpha\beta + \beta\gamma + \gamma\alpha = \frac{c}{a} = \frac{\text{Coefficient of } x}{\text{Coefficient of } x^3} \quad \text{}\\]
- **Product of Zeroes:**
  \\[\alpha\beta\gamma = -\frac{d}{a} = \frac{-(\text{Constant term})}{\text{Coefficient of } x^3} \quad \text{}\\]

---

## **III. Division Algorithm for Polynomials**

If \\(p(x)\\) and \\(g(x)\\) are any two polynomials where \\(g(x) \neq 0\\), then we can find polynomials \\(q(x)\\) and \\(r(x)\\) such that:
\\[p(x) = g(x) \times q(x) + r(x) \quad \text{}\\]
where either \\(r(x) = 0\\) or the \\(\text{degree of } r(x) < \text{degree of } g(x)\\).

---

## **IV. Textbook Examples (with Step-by-Step Solutions)**

### **Example 1**

**Problem:** Find the number of zeroes of \\(p(x)\\) for each of the given graphs in Fig 9.9:

1.  Linear line intersecting x-axis once.
2.  Parabola intersecting x-axis twice.
3.  Sinuous curve intersecting x-axis three times.

- **Solutions:**
  1.  **1 zero**, as the graph intersects the x-axis at one point only.
  2.  **2 zeroes**, as the graph intersects the x-axis at two points.
  3.  **3 zeroes**, as the graph intersects the x-axis at three points.

---

### **Example 2**

**Problem:** Find the zeroes of the quadratic polynomial \\(x^2+7x+10\\) and verify the relationship between zeroes and coefficients.

- **Solution:**
  - Find the factorised terms by splitting the middle term:
    \\[x^2 + 7x + 10 = (x+2)(x+5) \quad \text{}\\]
  - Equate to zero to find the zeroes: \\(x = -2\\) or \\(x = -5\\).
  - Verification:
    - **Sum of zeroes:** \\(-2 + (-5) = -7 = -\frac{7}{1} = -\frac{b}{a}\\) (Verified).
    - **Product of zeroes:** \\((-2) \times (-5) = 10 = \frac{10}{1} = \frac{c}{a}\\) (Verified).

---

### **Example 3**

**Problem:** Find the zeroes of the polynomial \\(x^2-3\\) and verify the relationship with coefficients.

- **Solution:**
  - Factorise using \\(a^2 - b^2 = (a-b)(a+b)\\):
    \\[x^2 - 3 = (x-\sqrt{3})(x+\sqrt{3}) \quad \text{}\\]
  - Zeroes are \\(\sqrt{3}\\) and \\(-\sqrt{3}\\).
  - Verification:
    - **Sum:** \\(\sqrt{3} + (-\sqrt{3}) = 0 = -\frac{0}{1} = -\frac{b}{a}\\) (Verified).
    - **Product:** \\((\sqrt{3}) \times (-\sqrt{3}) = -3 = \frac{-3}{1} = \frac{c}{a}\\) (Verified).

---

### **Example 4**

**Problem:** Find a quadratic polynomial, the sum and product of whose zeroes are \\(-3\\) and \\(2\\), respectively.

- **Solution:**
  - Let the polynomial be \\(ax^2 + bx + c\\) with zeroes \\(\alpha, \beta\\).
    \\[\alpha + \beta = -3 = -\frac{b}{a} \quad \text{and} \quad \alpha\beta = 2 = \frac{c}{a} \quad \text{}\\]
  - If \\(a = 1\\), then \\(b = 3\\) and \\(c = 2\\).
  - **Answer:** The quadratic polynomial is \\(x^2 + 3x + 2\\).

---

### **Example 5**

**Problem:** Verify that \\(3, -1,\\) and \\(-\frac{1}{3}\\) are the zeroes of the cubic polynomial \\(p(x) = 3x^3 - 5x^2 - 11x - 3\\) and verify coefficient relationships.

- **Solution:**
  - _Step 1:_ Substitute values to confirm they evaluate to zero:
    - \\(p(3) = 3(3)^3 - 5(3)^2 - 11(3) - 3 = 81 - 45 - 33 - 3 = 0\\).
    - \\(p(-1) = 3(-1)^3 - 5(-1)^2 - 11(-1) - 3 = -3 - 5 + 11 - 3 = 0\\).
    - \\(p(-\frac{1}{3}) = 3(-\frac{1}{27}) - 5(\frac{1}{9}) - 11(-\frac{1}{3}) - 3 = -\frac{1}{9} - \frac{5}{9} + \frac{11}{3} - 3 = 0\\).
  - _Step 2:_ Let \\(\alpha = 3, \beta = -1, \gamma = -\frac{1}{3}\\).
    - **Sum of zeroes:** \\(\alpha + \beta + \gamma = 3 - 1 - \frac{1}{3} = \frac{5}{3} = -\frac{b}{a}\\).
    - **Sum of products:** \\(\alpha\beta + \beta\gamma + \gamma\alpha = 3(-1) + (-1)(-\frac{1}{3}) + (-\frac{1}{3})(3) = -3 + \frac{1}{3} - 1 = -\frac{11}{3} = \frac{c}{a}\\).
    - **Product:** \\(\alpha\beta\gamma = 3 \times (-1) \times (-\frac{1}{3}) = 1 = -\frac{d}{a}\\) (since \\(d = -3\\)).

---

### **Example 6**

**Problem:** Divide \\(2x^2+3x+1\\) by \\(x+2\\).

- **Solution:**
  - Using standard polynomial division:
    \\[\begin{array}{rll}
    2x - 1 && \text{(Quotient)} \\
    x + 2 \ \overline{\smash{)} \ 2x^2 + 3x + 1} \\
    \underline{-(2x^2 + 4x)} \\
    -x + 1 \\
    \underline{-(-x - 2)} \\
    3 && \text{(Remainder)}
    \end{array}\\]
  - **Verification:** \\((x+2)(2x-1) + 3 = 2x^2 + 3x + 1\\).

---

### **Example 7**

**Problem:** Divide \\(3x^3+x^2+2x+5\\) by \\(1+2x+x^2\\).

- **Solution:**
  - Arrange the divisor in standard form: \\(x^2 + 2x + 1\\).
  - Perform division:
    \\[\begin{array}{rll}
    3x - 5 && \text{(Quotient)} \\
    x^2 + 2x + 1 \ \overline{\smash{)} \ 3x^3 + x^2 + 2x + 5} \\
    \underline{-(3x^3 + 6x^2 + 3x)} \\
    -5x^2 - x + 5 \\
    \underline{-(-5x^2 - 10x - 5)} \\
    9x + 10 && \text{(Remainder)}
    \end{array}\\]
  - **Verification:** \\((x^2+2x+1)(3x-5) + (9x+10) = 3x^3 + x^2 + 2x + 5\\).

---

### **Example 8**

**Problem:** Divide \\(3x^2-x^3-3x+5\\) by \\(x-1-x^2\\), and verify the division algorithm.

- **Solution:**
  - Write dividend and divisor in standard form:
    - Dividend: \\(-x^3 + 3x^2 - 3x + 5\\)
    - Divisor: \\(-x^2 + x - 1\\)
  - Division gives:
    - **Quotient:** \\(x - 2\\)
    - **Remainder:** \\(3\\)
  - **Verification:** \\((-x^2+x-1)(x-2) + 3 = -x^3 + 3x^2 - 3x + 5\\).

---

### **Example 9**

**Problem:** Find all the zeroes of \\(2x^4-3x^3-3x^2+6x-2\\) if two of its zeroes are \\(\sqrt{2}\\) and \\(-\sqrt{2}\\).

- **Solution:**
  - The combined factor from the given zeroes is:
    \\[(x-\sqrt{2})(x+\sqrt{2}) = x^2 - 2 \quad \text{}\\]
  - Divide the polynomial by \\(x^2-2\\) to find the remaining quadratic factor:
    \\[(2x^4-3x^3-3x^2+6x-2) \div (x^2-2) = 2x^2 - 3x + 1 \quad \text{}\\]
  - Factorise \\(2x^2-3x+1\\) by splitting the middle term:
    \\[2x^2 - 3x + 1 = (2x-1)(x-1) \quad \text{}\\]
  - This yields the additional zeroes: \\(x = \frac{1}{2}\\) and \\(x = 1\\).
  - **Answer:** All zeroes of the polynomial are \\(\sqrt{2}, -\sqrt{2}, \frac{1}{2}, \text{ and } 1\\).

---

## **V. Textbook Exercises**

### **EXERCISE 9.1**

1.  **Find the number of zeroes** of \\(p(x)\\) from the graphs below:
    - (i) Line parallel to the x-axis \\(\rightarrow\\) **0 zeroes**.
    - (ii) Curve intersecting x-axis at 1 point \\(\rightarrow\\) **1 zero**.
    - (iii) Curve intersecting x-axis at 3 points \\(\rightarrow\\) **3 zeroes**.
    - (iv) Parabola intersecting x-axis at 2 points \\(\rightarrow\\) **2 zeroes**.
    - (v) Curve intersecting x-axis at 4 points \\(\rightarrow\\) **4 zeroes**.
    - (vi) Curve touching/intersecting x-axis at 3 points \\(\rightarrow\\) **3 zeroes**.

---

### **EXERCISE 9.2**

1.  **Find the zeroes** of the following quadratic polynomials and verify the relationship between zeroes and coefficients:
    - (i) \\(x^2-2x-8\\)
    - (ii) \\(4s^2-4s+1\\)
    - (iii) \\(6x^2-3-7x\\)
    - (iv) \\(4u^2+8u\\)
    - (v) \\(t^2-15\\)
    - (vi) \\(3x^2-x-4\\)
2.  **Find a quadratic polynomial** for each, given the sum and product of zeroes:
    - (i) \\(\frac{1}{4}, \ -1\\)
    - (ii) \\(\sqrt{2}, \ \frac{1}{3}\\)
    - (iii) \\(0, \ \sqrt{5}\\)
    - (iv) \\(1, \ 1\\)
    - (v) \\(-\frac{1}{4}, \ \frac{1}{4}\\)
    - (vi) \\(4, \ 1\\)

---

### **EXERCISE 9.3**

1.  **Divide** the polynomial \\(p(x)\\) by \\(g(x)\\) and find the quotient and remainder:
    - (i) \\(p(x) = x^3-3x^2+5x-3\\), \ \\(g(x) = x^2-2\\)
    - (ii) \\(p(x) = x^4-3x^2+4x+5\\), \ \\(g(x) = x^2+1-x\\)
    - (iii) \\(p(x) = x^4-5x+6\\), \ \\(g(x) = 2-x^2\\)
2.  **Verify factoring:** Check whether the first polynomial is a factor of the second polynomial by dividing:
    - (i) \\(t^2-3, \ 2t^4+3t^3-2t^2-9t-12\\)
    - (ii) \\(x^2+3x+1, \ 3x^4+5x^3-7x^2+2x+2\\)
    - (iii) \\(x^3-3x+1, \ x^5-4x^3+x^2+3x+1\\)
3.  Obtain all other zeroes of \\(3x^4+6x^3-2x^2-10x-5\\), if two of its zeroes are \\(\sqrt{\frac{5}{3}}\\) and \\(-\sqrt{\frac{5}{3}}\\).
4.  On dividing \\(x^3-3x^2+x+2\\) by a polynomial \\(g(x)\\), the quotient and remainder were \\(x-2\\) and \\(-2x+4\\), respectively. Find \\(g(x)\\).
5.  Give examples of polynomials \\(p(x)\\), \\(g(x)\\), \\(q(x)\\) and \\(r(x)\\) which satisfy the division algorithm and:
    - (i) \\(\text{deg } p(x) = \text{deg } q(x)\\)
    - (ii) \\(\text{deg } q(x) = \text{deg } r(x)\\)
    - (iii) \\(\text{deg } r(x) = 0\\)

---

### **EXERCISE 9.4 (Optional)\***

_\*These exercises are not from the examination point of view._

1.  Verify that the numbers given alongside the cubic polynomials are their zeroes, and verify the coefficient relationships:
    - (i) \\(2x^3+x^2-5x+2; \ \frac{1}{2}, \ 1, \ -2\\)
    - (ii) \\(x^3-4x^2+5x-2; \ 2, \ 1, \ 1\\)
2.  Find a cubic polynomial with the sum, sum of products of its zeroes taken two at a time, and the product of its zeroes as \\(2, -7, -14\\) respectively.
3.  If the zeroes of the polynomial \\(x^3-3x^2+x+1\\) are \\(a-b\\), \\(a\\), and \\(a+b\\), find \\(a\\) and \\(b\\).
4.  If two zeroes of the polynomial \\(x^4-6x^3-26x^2+138x-35\\) are \\(2\pm\sqrt{3}\\), find the other zeroes.
5.  If the polynomial \\(x^4-6x^3+16x^2-25x+10\\) is divided by another polynomial \\(x^2-2x+k\\), the remainder comes out to be \\(x+a\\), find \\(k\\) and \\(a\\).

---

📊 **I can update your master syllabus file with this comprehensive study guide for Chapter 9, or construct an interactive quiz on polynomial factorization and division. What would you like to explore next?**
