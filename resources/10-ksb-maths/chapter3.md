# **Chapter 3: Pair of Linear Equations in Two Variables — Study Guide**

---

## **I. Core Concepts & Algebraic Principles**

### **1. Introduction to Linear Equations in Two Variables**

An equation which can be put in the form **(ax + by + c = 0)**, where (a, b,) and (c) are real numbers, and (a) and (b) are not both zero ((a^2 + b^2 \neq 0)), is called a **linear equation in two variables** (x) and (y).

- **The Geometric Meaning:** Geometrically, any solution ((x, y)) of a linear equation corresponds to a point lying on the straight line representing that equation.

---

### **2. Pair of Linear Equations in Two Variables**

Two linear equations in the same two variables (x) and (y) are called a **pair of linear equations in two variables**. Their general algebraic form is:
[a_1x + b_1y + c_1 = 0]
[a_2x + b_2y + c_2 = 0]
Where (a_1, b_1, c_1, a_2, b_2, c_2) are real numbers such that (a_1^2 + b_1^2 \neq 0) and (a_2^2 + b_2^2 \neq 0).

---

### **3. Graphical Representation & Nature of Solutions**

Given a pair of linear equations representing two lines in a plane, only one of three geometric possibilities can occur:

```xml
<svg width="600" height="200" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .grid-line { stroke: #e2e8f0; stroke-width: 1; }
    .axis { stroke: #64748b; stroke-width: 1.5; }
    .line1 { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .line2 { stroke: #ef4444; stroke-width: 2.5; fill: none; }
    .coincident { stroke: #8b5cf6; stroke-width: 3; stroke-dasharray: 5 3; fill: none; }
    .title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; text-anchor: middle; }
    .subtitle { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #64748b; text-anchor: middle; }
    .pt { fill: #0f172a; }
  </style>

  <!-- Panel 1: Intersecting -->
  <g transform="translate(10, 0)">
    <rect x="0" y="10" width="180" height="180" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <line x1="90" y1="20" x2="90" y2="160" class="axis"/>
    <line x1="20" y1="90" x2="160" y2="90" class="axis"/>
    <line x1="30" y1="140" x2="150" y2="40" class="line1"/>
    <line x1="30" y1="40" x2="150" y2="140" class="line2"/>
    <circle cx="90" cy="90" r="5" class="pt"/>
    <text x="90" y="168" class="title">1. Intersecting Lines</text>
    <text x="90" y="182" class="subtitle">Exactly One Unique Solution</text>
  </g>

  <!-- Panel 2: Parallel -->
  <g transform="translate(210, 0)">
    <rect x="0" y="10" width="180" height="180" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <line x1="90" y1="20" x2="90" y2="160" class="axis"/>
    <line x1="20" y1="90" x2="160" y2="90" class="axis"/>
    <line x1="30" y1="120" x2="150" y2="40" class="line1"/>
    <line x1="30" y1="145" x2="150" y2="65" class="line2"/>
    <text x="90" y="168" class="title">2. Parallel Lines</text>
    <text x="90" y="182" class="subtitle">No Solution (Inconsistent)</text>
  </g>

  <!-- Panel 3: Coincident -->
  <g transform="translate(410, 0)">
    <rect x="0" y="10" width="180" height="180" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <line x1="90" y1="20" x2="90" y2="160" class="axis"/>
    <line x1="20" y1="90" x2="160" y2="90" class="axis"/>
    <line x1="30" y1="130" x2="150" y2="50" class="line1" stroke-width="4"/>
    <line x1="30" y1="130" x2="150" y2="50" class="coincident"/>
    <text x="90" y="168" class="title">3. Coincident Lines</text>
    <text x="90" y="182" class="subtitle">Infinitely Many Solutions</text>
  </g>
</svg>
```

These three states translate to the following algebraic characteristics:

1. **Consistent Pair:** A pair of linear equations that possesses **at least one solution** (this includes intersecting and coincident lines).
2. **Inconsistent Pair:** A pair of linear equations that has **no solution** (parallel lines).
3. **Dependent Pair:** Equivalent linear equations that have **infinitely many distinct common solutions** (coincident lines). A dependent pair is always consistent.

---

### **4. Algebraic Relationship between Coefficients**

We can check the consistency and graphical behaviour of a pair of linear equations simply by comparing their ratios of coefficients:

| Ratio Comparison                                             | Graphical Representation | Algebraic Interpretation        | Consistency                |
| ------------------------------------------------------------ | ------------------------ | ------------------------------- | -------------------------- |
| **(\frac{a_1}{a_2} \neq \frac{b_1}{b_2})**                   | Intersecting lines       | Exactly **one unique** solution | **Consistent**             |
| **(\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2})**    | Coincident lines         | **Infinitely many** solutions   | **Dependent (Consistent)** |
| **(\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2})** | Parallel lines           | **No** solution                 | **Inconsistent**           |

---

## **II. Algebraic Methods of Solving Pairs of Equations**

When graphical coordinates yield non-integral values (such as fractional or irrational points), algebraic methods are preferred.

### **1. Substitution Method**

- **Step 1:** Express one variable (say (y)) in terms of the other variable ((x)) from one of the equations.
- **Step 2:** Substitute this value of (y) into the second equation to reduce it to a single-variable linear equation in (x), and solve.
- **Step 3:** Substitute this value of (x) back into the first equation to solve for (y).

---

### **2. Elimination Method**

- **Step 1:** Multiply one or both equations by suitable non-zero constants to make the coefficients of one variable numerically equal.
- **Step 2:** Add or subtract the equations to eliminate that variable.
- **Step 3:** Solve the resulting single-variable equation, and substitute the value back into either original equation to find the other variable.

---

### **3. Cross-Multiplication Method**

For the general equations $a_1x + b_1y + c_1 = 0$ and $a_2x + b_2y + c_2 = 0$, we arrange the coefficients according to the cross-multiplication layout:

```xml
<svg width="450" height="150" viewBox="0 0 450 150" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .header-text { font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; fill: #0f172a; font-weight: bold; text-anchor: middle; }
    .coef-text { font-family: 'Consolas', 'Courier New', monospace; font-size: 15px; fill: #334155; text-anchor: middle; }
    .pos-arrow { stroke: #0284c7; stroke-width: 1.8; fill: none; marker-end: url(#arrow-blue); }
    .neg-arrow { stroke: #ef4444; stroke-width: 1.8; fill: none; marker-end: url(#arrow-red); }
  </style>
  <defs>
    <!-- Markers for arrows -->
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#0284c7"/>
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#ef4444"/>
    </marker>
  </defs>

  <!-- Variables Header -->
  <text x="110" y="30" class="header-text">x</text>
  <text x="225" y="30" class="header-text">y</text>
  <text x="340" y="30" class="header-text">1</text>

  <!-- Coefficients Row 1 -->
  <text x="50" y="60" class="coef-text">b₁</text>
  <text x="165" y="60" class="coef-text">c₁</text>
  <text x="280" y="60" class="coef-text">a₁</text>
  <text x="395" y="60" class="coef-text">b₁</text>

  <!-- Coefficients Row 2 -->
  <text x="50" y="120" class="coef-text">b₂</text>
  <text x="165" y="120" class="coef-text">c₂</text>
  <text x="280" y="120" class="coef-text">a₂</text>
  <text x="395" y="120" class="coef-text">b₂</text>

  <!-- Positive diagonal arrows (downward blue) -->
  <path d="M 65,70 L 145,110" class="pos-arrow"/>
  <path d="M 180,70 L 260,110" class="pos-arrow"/>
  <path d="M 295,70 L 375,110" class="pos-arrow"/>

  <!-- Negative diagonal arrows (upward red) -->
  <path d="M 65,110 L 145,70" class="neg-arrow"/>
  <path d="M 180,110 L 260,70" class="neg-arrow"/>
  <path d="M 295,110 L 375,70" class="neg-arrow"/>
</svg>
```

This structural layout gives us the following equations:
$$\frac{x}{b_1c_2 - b_2c_1} = \frac{y}{c_1a_2 - c_2a_1} = \frac{1}{a_1b_2 - a_2b_1}$$
Hence:
$$x = \frac{b_1c_2 - b_2c_1}{a_1b_2 - a_2b_1} \quad \text{and} \quad y = \frac{c_1a_2 - c_2a_1}{a_1b_2 - a_2b_1} \quad \left(\text{provided } a_1b_2 - a_2b_1 \neq 0\right) \text{}$$

---

## **III. Example Problems & Step-by-Step Solutions**

### **Example 1**

**Problem:** represent the situation of Akhila at the fair mathematically (algebraically and graphically). Akhila spent ₹20 to have rides on the Giant Wheel (costing ₹3 per ride) and play Hoopla (costing ₹4 per game), where the number of Hoopla games played is half the number of rides on the Giant Wheel.

- **Solution:**
  - Let (x) represent the number of rides on the Giant Wheel, and (y) represent the number of games of Hoopla.
  - **Equation 1:** (y = \frac{1}{2}x \implies x - 2y = 0)
  - **Equation 2:** (3x + 4y = 20)

#### **Geometric Plot (Intersection at $(4, 2)$):**

```xml
<svg width="400" height="300" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .grid { stroke: #cbd5e1; stroke-width: 0.5; }
    .axis { stroke: #0f172a; stroke-width: 2; }
    .line-eq1 { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .line-eq2 { stroke: #ef4444; stroke-width: 2.5; fill: none; }
    .label { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; fill: #334155; }
    .pt-highlight { fill: #1e293b; stroke: #ffffff; stroke-width: 1.5; }
  </style>

  <!-- Background Grid (30px spacing = 1 unit) -->
  <path d="M 60,30 L 60,270 M 90,30 L 90,270 M 120,30 L 120,270 M 150,30 L 150,270 M 180,30 L 180,270 M 210,30 L 210,270 M 240,30 L 240,270 M 270,30 L 270,270 M 300,30 L 300,270 M 330,30 L 330,270 M 360,30 L 360,270" class="grid"/>
  <path d="M 30,240 L 370,240 M 30,210 L 370,210 M 30,180 L 370,180 M 30,150 L 370,150 M 30,120 L 370,120 M 30,90 L 370,90 M 30,60 L 370,60 M 30,30 L 370,30" class="grid"/>

  <!-- Axis Lines -->
  <line x1="60" y1="20" x2="60" y2="260" class="axis"/> <!-- y-axis -->
  <line x1="40" y1="240" x2="380" y2="240" class="axis"/> <!-- x-axis -->

  <!-- Axis numbers -->
  <text x="50" y="245" class="label">0</text>
  <text x="120" y="255" class="label">2</text>
  <text x="180" y="255" class="label">4</text>
  <text x="240" y="255" class="label">6</text>
  <text x="300" y="255" class="label">8</text>
  <text x="45" y="215" class="label">1</text>
  <text x="45" y="185" class="label">2</text>
  <text x="45" y="155" class="label">3</text>
  <text x="45" y="125" class="label">4</text>
  <text x="45" y="95" class="label">5</text>

  <!-- Equation 1: x - 2y = 0  (points: (0,0), (4,2)) -->
  <line x1="60" y1="240" x2="240" y2="150" class="line-eq1"/>
  <text x="245" y="145" class="label" style="fill:#0284c7;">x - 2y = 0</text>

  <!-- Equation 2: 3x + 4y = 20 (points: (0,5), (4,2), (6.67,0)) -->
  <line x1="60" y1="90" x2="260" y2="240" class="line-eq2"/>
  <text x="265" y="235" class="label" style="fill:#ef4444;">3x + 4y = 20</text>

  <!-- Intersection point at (4,2) which is SVG (180, 180) -->
  <circle cx="180" cy="180" r="5" class="pt-highlight"/>
  <text x="190" y="175" class="label" style="font-weight:bold;">Intersection Q(4,2)</text>
</svg>
```

---

### **Example 2**

**Problem:** Romila purchased 2 pencils and 3 erasers for ₹9. Her friend Sonali bought 4 pencils and 6 erasers of the same kind for ₹18. Represent this situation algebraically and graphically.

- **Solution:**
  - Let (x) be the cost of one pencil, and (y) be the cost of one eraser.
  - **Equation 1:** (2x + 3y = 9)
  - **Equation 2:** (4x + 6y = 18)
  - Comparing coefficients: (\frac{a_1}{a_2} = \frac{2}{4} = \frac{1}{2}); (\frac{b_1}{b_2} = \frac{3}{6} = \frac{1}{2}); (\frac{c_1}{c_2} = \frac{-9}{-18} = \frac{1}{2}).
  - Since (\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}), the lines are **coincident** and have **infinitely many solutions**.

---

### **Example 3**

**Problem:** Two rails are represented by the equations $x + 2y - 4 = 0$ and $2x + 4y - 12 = 0$. Represent this geometrically.

- **Solution:**
  - Comparing ratios: (\frac{a_1}{a_2} = \frac{1}{2}); (\frac{b_1}{b_2} = \frac{2}{4} = \frac{1}{2}); (\frac{c_1}{c_2} = \frac{-4}{-12} = \frac{1}{3}).
  - Since (\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}), the lines are **parallel**. They do not intersect anywhere, meaning there is no common solution.

---

### **Example 4**

**Problem:** Check graphically whether the pair of equations $x + 3y = 6$ and $2x - 3y = 12$ is consistent. If so, solve them graphically.

- **Solution:**
  - Points for (x + 3y = 6): ((0, 2)) and ((6, 0)).
  - Points for (2x - 3y = 12): ((0, -4)) and ((6, 0)).
  - Graphing both lines shows they intersect at the common point (B(6, 0)). Since they intersect, the pair is **consistent**, and the unique solution is **(x = 6, y = 0)**.

---

### **Example 5**

**Problem:** Graphically find whether the pair of equations $5x - 8y + 1 = 0$ and $3x - \frac{24}{5}y + \frac{3}{5} = 0$ has no solution, a unique solution, or infinitely many solutions.

- **Solution:**
  - Write Equation 2: (3x - \frac{24}{5}y + \frac{3}{5} = 0).
  - Multiply this equation by (\frac{5}{3}) to clear fractions:
    $$\frac{5}{3}\left(3x - \frac{24}{5}y + \frac{3}{5}\right) = 0 \implies 5x - 8y + 1 = 0 \text{}$$
  - This is identical to Equation 1. Since both equations are equivalent, they form coincident lines and have **infinitely many solutions**.

---

### **Example 6**

**Problem:** Champa went to a sale to buy pants ((x)) and skirts ((y)). She told her friends, "The number of skirts is two less than twice the number of pants purchased. Also, the number of skirts is four less than four times the number of pants purchased". Find the number of pants and skirts bought.

- **Solution:**
  - **Equation 1:** (y = 2x - 2)
  - **Equation 2:** (y = 4x - 4)
  - Plotting both lines reveals that they intersect at ((1, 0)).
  - **Answer:** (x = 1, y = 0) (Champa bought **1 pair of pants** and **no skirts**).

---

### **Example 7**

**Problem:** Solve the pair of equations $7x - 15y = 2$ and $x + 2y = 3$ by the substitution method.

- **Solution:**
  - From Equation 2, express (x) in terms of (y):
    $$x = 3 - 2y \quad \text{--- (Eq. 3)}$$
  - Substitute this into Equation 1:
    $$7(3 - 2y) - 15y = 2 \implies 21 - 14y - 15y = 2 \text{}$$
    $$-29y = -19 \implies y = \frac{19}{29} \text{}$$
  - Substitute (y = \frac{19}{29}) back into Equation 3:
    $$x = 3 - 2\left(\frac{19}{29}\right) = \frac{87 - 38}{29} = \frac{49}{29} \text{}$$
  - **Answer:** (x = \frac{49}{29}, y = \frac{19}{29}).

---

### **Example 8**

**Problem:** Solve the age problem (Aftab and his daughter) using the substitution method: "Seven years ago, I was seven times as old as you were then. Also, three years from now, I shall be three times as old as you will be".

- **Solution:**
  - Let Aftab's present age be (s), and his daughter's present age be (t).
  - Seven years ago: (s - 7 = 7(t - 7) \implies s - 7t + 42 = 0)
  - Three years from now: (s + 3 = 3(t + 3) \implies s - 3t - 6 = 0 \implies s = 3t + 6)
  - Substitute (s = 3t + 6) into the first equation:
    $$(3t + 6) - 7t + 42 = 0 \implies -4t + 48 = 0 \implies t = 12 \text{}$$
  - Find (s): (s = 3(12) + 6 = 42).
  - **Answer:** Aftab is **42 years old** and his daughter is **12 years old**.

---

### **Example 9**

**Problem:** Analyze the cost of 2 pencils and 3 erasers for ₹9, and 4 pencils and 6 erasers for ₹18 using substitution.

- **Solution:**
  - (2x + 3y = 9 \implies x = \frac{9 - 3y}{2})
  - Substitute (x) into (4x + 6y = 18):
    $$4\left(\frac{9 - 3y}{2}\right) + 6y = 18 \implies 2(9 - 3y) + 6y = 18 \implies 18 = 18 \text{}$$
  - This is a constant identity statement true for all values of (y). Since no single specific value of (y) can be obtained, the system has **infinitely many solutions**.

---

### **Example 10**

**Problem:** Solve the parallel rail equations $x + 2y - 4 = 0$ and $2x + 4y - 12 = 0$ using substitution.

- **Solution:**
  - From Equation 1: (x = 4 - 2y)
  - Substitute (x) into (2x + 4y - 12 = 0):
    $$2(4 - 2y) + 4y - 12 = 0 \implies 8 - 4y + 4y - 12 = 0 \implies -4 = 0 \text{}$$
  - This is a false mathematical statement, indicating that the equations have **no common solution**. The rails will never cross.

---

### **Example 11**

**Problem:** The ratio of incomes of two persons is $9:7$ and the ratio of their expenditures is $4:3$. If each of them manages to save ₹2000 per month, find their monthly incomes.

- **Solution:**
  - Let the monthly incomes be (9x) and (7x), and monthly expenditures be (4y) and (3y).
  - **Equation 1 (Person 1 savings):** (9x - 4y = 2000)
  - **Equation 2 (Person 2 savings):** (7x - 3y = 2000)
  - Using the **elimination method**, multiply Eq. 1 by 3 and Eq. 2 by 4:
    $$27x - 12y = 6000 \quad \text{--- (Eq. 3)}$$
    $$28x - 12y = 8000 \quad \text{--- (Eq. 4)}$$
  - Subtract Eq. 3 from Eq. 4:
    $$(28x - 27x) - (12y - 12y) = 8000 - 6000 \implies x = 2000 \text{}$$
  - Calculate incomes:
    - Person 1 income: (9(2000) = \text{₹}18,000)
    - Person 2 income: (7(2000) = \text{₹}14,000)
  - **Answer:** The monthly incomes are **₹18,000** and **₹14,000**.

---

### **Example 12**

**Problem:** Solve $2x + 3y = 8$ and $4x + 6y = 7$ using elimination.

- **Solution:**
  - Multiply Equation 1 by 2:
    $$4x + 6y = 16 \quad \text{--- (Eq. 3)}$$
  - Subtract Equation 2 ((4x + 6y = 7)) from Equation 3:
    $$(4x - 4x) + (6y - 6y) = 16 - 7 \implies 0 = 9 \text{}$$
  - This is a false statement, so the system has **no solution**.

---

### **Example 13**

**Problem:** The sum of a two-digit number and the number obtained by reversing its digits is 66. If the digits of the number differ by 2, find the number.

- **Solution:**
  - Let the ten's and unit's digits be (x) and (y) respectively.
  - Original number = (10x + y); Reversed number = (10y + x).
  - **Condition 1:** ((10x + y) + (10y + x) = 66 \implies 11(x + y) = 66 \implies x + y = 6).
  - **Condition 2:** The digits differ by 2:
    - _Case A:_ (x - y = 2)
    - _Case B:_ (y - x = 2)
  - **Solving Case A:** (x + y = 6) and (x - y = 2 \implies x = 4, y = 2). The number is **42**.
  - **Solving Case B:** (x + y = 6) and (y - x = 2 \implies x = 2, y = 4). The number is **24**.
  - **Answer:** There are two such numbers: **42** and **24**.

---

### **Example 14**

**Problem:** If 2 bus tickets to Malleswaram and 3 tickets to Yeshwanthpur cost ₹46, while 3 tickets to Malleswaram and 5 tickets to Yeshwanthpur cost ₹74, find the individual ticket fares from Bangalore bus stand.

- **Solution:**
  - Let (x) be the fare to Malleswaram and (y) be the fare to Yeshwanthpur.
  - **Equation 1:** (2x + 3y - 46 = 0)
  - **Equation 2:** (3x + 5y - 74 = 0)
  - Apply the **cross-multiplication method**:
    $$\frac{x}{(3)(-74) - (5)(-46)} = \frac{y}{(-46)(3) - (-74)(2)} = \frac{1}{(2)(5) - (3)(3)} \text{}$$
    $$\frac{x}{-222 + 230} = \frac{y}{-138 + 148} = \frac{1}{10 - 9} \text{}$$
    $$\frac{x}{8} = \frac{y}{10} = \frac{1}{1} \implies x = 8, y = 10 \text{}$$
  - **Answer:** Malleswaram fare is **₹8** and Yeshwanthpur fare is **₹10**.

---

### **Example 15**

**Problem:** Find the values of $p$ for which the pair of equations $4x + py + 8 = 0$ and $2x + 2y + 2 = 0$ has a unique solution.

- **Solution:**
  - Here (a_1 = 4, a_2 = 2, b_1 = p, b_2 = 2).
  - For a unique solution, (\frac{a_1}{a_2} \neq \frac{b_1}{b_2}):
    $$\frac{4}{2} \neq \frac{p}{2} \implies 2 \neq \frac{p}{2} \implies p \neq 4 \text{}$$
  - **Answer:** The system has a unique solution for **all real values of (p) except 4**.

---

### **Example 16**

**Problem:** For what values of $k$ will the pair of linear equations $kx + 3y - (k-3) = 0$ and $12x + ky - k = 0$ have infinitely many solutions?

- **Solution:**
  - For infinite solutions: (\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}).
  - Ratio setup: (\frac{k}{12} = \frac{3}{k} = \frac{-(k-3)}{-k} = \frac{k-3}{k}).
  - From the first part: (\frac{k}{12} = \frac{3}{k} \implies k^2 = 36 \implies k = \pm 6).
  - From the second part: (\frac{3}{k} = \frac{k-3}{k} \implies 3k = k^2 - 3k \implies k^2 - 6k = 0 \implies k = 0 \text{ or } k = 6).
  - **Answer:** The value of (k) satisfying both conditions is **(k = 6)**.

---

### **Example 17**

**Problem:** Solve the non-linear pair of equations:
$$\frac{2}{x} + \frac{3}{y} = 13 \quad \text{and} \quad \frac{5}{x} - \frac{4}{y} = -2 \text{}$$

- **Solution:**
  - Substitute (p = \frac{1}{x}) and (q = \frac{1}{y}):
    $$2p + 3q = 13 \quad \text{--- (Eq. 3)}$$
    $$5p - 4q = -2 \quad \text{--- (Eq. 4)}$$
  - Solving this linear system gives (p = 2, q = 3).
  - Now convert back to (x) and (y):
    $$x = \frac{1}{p} = \frac{1}{2} \quad \text{and} \quad y = \frac{1}{q} = \frac{1}{3} \text{}$$
  - **Answer:** (x = \frac{1}{2}, y = \frac{1}{3}).

---

### **Example 18**

**Problem:** Solve the following reducible system:
$$\frac{5}{x-1} + \frac{1}{y-2} = 2 \quad \text{and} \quad \frac{6}{x-1} - \frac{3}{y-2} = 1 \text{}$$

- **Solution:**
  - Let (p = \frac{1}{x-1}) and (q = \frac{1}{y-2}).
  - The system becomes:
    $$5p + q = 2 \quad \text{--- (Eq. 3)}$$
    $$6p - 3q = 1 \quad \text{--- (Eq. 4)}$$
  - Multiply Eq. 3 by 3: (15p + 3q = 6). Add this to Eq. 4:
    $$21p = 7 \implies p = \frac{1}{3} \text{}$$
  - Substitute (p = \frac{1}{3}) into Eq. 3: (5\left(\frac{1}{3}\right) + q = 2 \implies q = 2 - \frac{5}{3} = \frac{1}{3}).
  - Solve for (x) and (y):
    $$\frac{1}{x-1} = \frac{1}{3} \implies x - 1 = 3 \implies x = 4 \text{}$$
    $$\frac{1}{y-2} = \frac{1}{3} \implies y - 2 = 3 \implies y = 5 \text{}$$
  - **Answer:** (x = 4, y = 5).

---

### **Example 19**

**Problem:** A boat travels 30 km upstream and 44 km downstream in 10 hours. In 13 hours, it can travel 40 km upstream and 55 km downstream. Determine the speed of the stream and that of the boat in still water.

- **Solution:**
  - Let speed of boat in still water be (x\text{ km/h}), and speed of the stream be (y\text{ km/h}).
  - Upstream speed = ((x - y)\text{ km/h}); Downstream speed = ((x + y)\text{ km/h}).
  - **Equation 1:** (\frac{30}{x-y} + \frac{44}{x+y} = 10)
  - **Equation 2:** (\frac{40}{x-y} + \frac{55}{x+y} = 13)
  - Let (u = \frac{1}{x-y}) and (v = \frac{1}{x+y}).
  - The linear equations are:
    $$30u + 44v = 10 \quad \text{--- (Eq. 3)}$$
    $$40u + 55v = 13 \quad \text{--- (Eq. 4)}$$
  - Solving using cross-multiplication gives (u = \frac{1}{5}) and (v = \frac{1}{11}).
  - Thus:
    $$x - y = 5 \quad \text{and} \quad x + y = 11 \text{}$$
  - Adding these equations gives (2x = 16 \implies x = 8).
  - Subtracting them gives (2y = 6 \implies y = 3).
  - **Answer:** Speed of boat in still water is **(8\text{ km/h})**; Speed of stream is **(3\text{ km/h})**.

---

## **IV. Exercises**

### **EXERCISE 3.1**

1. **Aftab & Daughter:** Represent algebraically and graphically: Seven years ago, Aftab was seven times as old as his daughter. Three years from now, he will be three times as old as she will be.
2. **Cricket Equipment:** A coach buys 3 bats and 6 balls for ₹3900. Later, she buys another bat and 3 more balls of the same kind for ₹1300. Represent this algebraically and geometrically.
3. **Apples & Grapes:** The cost of 2 kg of apples and 1 kg of grapes was ₹160. After a month, the cost of 4 kg of apples and 2 kg of grapes is ₹300. Represent the situation algebraically and geometrically.

---

### **EXERCISE 3.2**

1. **Formulate and Solve Graphically:**

- (i) 10 students of Class X took part in a Mathematics quiz. If the number of girls is 4 more than the number of boys, find the number of boys and girls who took part in the quiz.
- (ii) 5 pencils and 7 pens together cost ₹50, whereas 7 pencils and 5 pens together cost ₹46. Find the cost of one pencil and that of one pen.

2. **Ratio Comparison:** On comparing the ratios $\frac{a_1}{a_2}, \frac{b_1}{b_2},$ and $\frac{c_1}{c_2}$, find out whether the lines representing the following pairs of linear equations intersect at a point, are parallel, or coincide:

- (i) (5x - 4y + 8 = 0) and (7x + 6y - 9 = 0)
- (ii) (9x + 3y + 12 = 0) and (18x + 6y + 24 = 0)
- (iii) (6x - 3y + 10 = 0) and (2x - y + 9 = 0)

3. **Consistency Check:** On comparing coefficient ratios, find out whether the following pairs of linear equations are consistent or inconsistent:

- (i) (3x + 2y = 5); (2x - 3y = 7)
- (ii) (2x - 3y = 8); (4x - 6y = 9)
- (iii) (\frac{3}{2}x + \frac{5}{3}y = 7); (9x - 10y = 14)
- (iv) (5x - 3y = 11); (-10x + 6y = -22)
- (v) (\frac{4}{3}x + 2y = 8); (2x + 3y = 12)

4. **Solve Graphically if Consistent:**

- (i) (x + y = 5); (2x + 2y = 10)
- (ii) (x - y = 8); (3x - 3y = 16)
- (iii) (2x + y - 6 = 0); (4x - 2y - 4 = 0)
- (iv) (2x - 2y - 2 = 0); (4x - 4y - 5 = 0)

5. **Garden Dimensions:** Half the perimeter of a rectangular garden, whose length is $4\text{ m}$ more than its width, is $36\text{ m}$. Find the dimensions of the garden.
6. **Create Linear Equations:** Given the linear equation $2x + 3y - 8 = 0$, write another linear equation in two variables such that the geometrical representation of the pair so formed is:

- (i) intersecting lines
- (ii) parallel lines
- (iii) coincident lines

7. **Triangle Vertices:** Draw the graphs of the equations $x - y + 1 = 0$ and $3x + 2y - 12 = 0$. Determine the coordinates of the vertices of the triangle formed by these lines and the x-axis, and shade the triangular region.

---

### **EXERCISE 3.3**

1. **Solve by Substitution:**

- (i) (x + y = 14); (x - y = 4)
- (ii) (s - t = 3); (\frac{s}{3} + \frac{t}{2} = 6)
- (iii) (3x - y = 3); (9x - 3y = 9)
- (iv) (0.2x + 0.3y = 1.3); (0.4x + 0.5y = 2.3)
- (v) (\sqrt{2}x + \sqrt{3}y = 0); (\sqrt{3}x - \sqrt{8}y = 0)
- (vi) (\frac{3x}{2} - \frac{5y}{3} = -2); (\frac{x}{3} + \frac{y}{2} = \frac{13}{6})

2. **Find parameter $m$:** Solve $2x + 3y = 11$ and $2x - 4y = -24$, and hence find the value of '$m$' for which $y = mx + 3$.
3. **Formulate and Solve by Substitution:**

- (i) The difference between two numbers is 26 and one number is three times the other. Find them.
- (ii) The larger of two supplementary angles exceeds the smaller by 18 degrees. Find them.
- (iii) The coach of a cricket team buys 7 bats and 6 balls for ₹3800. Later, she buys 3 bats and 5 balls for ₹1750. Find the cost of each bat and each ball.
- (iv) The taxi charges in a city consist of a fixed charge together with the charge for the distance covered. For a distance of (10\text{ km}), the charge paid is ₹105 and for a journey of (15\text{ km}), the charge paid is ₹155. What are the fixed charges and the charge per km? How much does a person have to pay for travelling a distance of (25\text{ km})?
- (v) A fraction becomes (\frac{9}{11}), if 2 is added to both the numerator and the denominator. If 3 is added to both the numerator and the denominator, it becomes (\frac{5}{6}). Find the fraction.
- (vi) Five years hence, the age of Jacob will be three times that of his son. Five years ago, Jacob's age was seven times that of his son. What are their present ages?

---

### **EXERCISE 3.4**

1. **Solve by Elimination & Substitution:**

- (i) (x + y = 5) and (2x - 3y = 4)
- (ii) (3x + 4y = 10) and (2x - 2y = 2)
- (iii) (3x - 5y - 4 = 0) and (9x = 2y + 7)
- (iv) (\frac{x}{2} + \frac{2y}{3} = -1) and (x - \frac{y}{3} = 3)

2. **Formulate and Solve by Elimination:**

- (i) If we add 1 to the numerator and subtract 1 from the denominator, a fraction reduces to 1. It becomes (\frac{1}{2}) if we only add 1 to the denominator. What is the fraction?
- (ii) Five years ago, Nuri was thrice as old as Sonu. Ten years later, Nuri will be twice as old as Sonu. How old are Nuri and Sonu?
- (iii) The sum of the digits of a two-digit number is 9. Also, nine times this number is twice the number obtained by reversing the order of the digits. Find the number.
- (iv) Meena went to a bank to withdraw ₹2000. She asked the cashier to give her ₹50 and ₹100 notes only. Meena got 25 notes in all. Find how many notes of ₹50 and ₹100 she received.
- (v) A lending library has a fixed charge for the first three days and an additional charge for each day thereafter. Saritha paid ₹27 for a book kept for seven days, while Susy paid ₹21 for the book she kept for five days. Find the fixed charge and the charge for each extra day.

---

### **EXERCISE 3.5**

1. **Classify and Solve Unique Cases via Cross-Multiplication:**

- (i) (x - 3y - 3 = 0); (3x - 9y - 2 = 0)
- (ii) (2x + y = 5); (3x + 2y = 8)
- (iii) (3x - 5y = 20); (6x - 10y = 40)
- (iv) (x - 3y - 7 = 0); (3x - 3y - 15 = 0)

2. **Find Variables for Special Solutions:**

- (i) For which values of (a) and (b) does the following pair of linear equations have an infinite number of solutions?
  $$2x + 3y = 7$$
  $$(a-b)x + (a+b)y = 3a+b-2 \text{}$$
- (ii) For which value of (k) will the following pair of linear equations have no solution?
  $$3x + y = 1$$
  $$(2k-1)x + (k-1)y = 2k+1 \text{}$$

3. **Solve by Substitution & Cross-Multiplication:**
   $$8x + 5y = 9 \quad \text{and} \quad 3x + 2y = 4 \text{}$$
4. **Formulate and Solve via Any Method:**

- (i) A part of monthly hostel charges is fixed and the remaining depends on the number of days one has taken food in the mess. When a student A takes food for 20 days she has to pay ₹1000 as hostel charges whereas a student B, who takes food for 26 days, pays ₹1180 as hostel charges. Find the fixed charges and the cost of food per day.
- (ii) A fraction becomes (\frac{1}{3}) when 1 is subtracted from the numerator and it becomes (\frac{1}{4}) when 8 is added to its denominator. Find the fraction.
- (iii) Yash scored 40 marks in a test, getting 3 marks for each right answer and losing 1 mark for each wrong answer. Had 4 marks been awarded for each correct answer and 2 marks been deducted for each incorrect answer, then Yash would have scored 50 marks. How many questions were there in the test?
- (iv) Places A and B are (100\text{ km}) apart on a highway. One car starts from A and another from B at the same time. If the cars travel in the same direction at different speeds, they meet in 5 hours. If they travel towards each other, they meet in 1 hour. What are the speeds of the two cars?
- (v) The area of a rectangle gets reduced by 9 square units, if its length is reduced by 5 units and breadth is increased by 3 units. If we increase the length by 3 units and the breadth by 2 units, the area increases by 67 square units. Find the dimensions of the rectangle.

---

### **EXERCISE 3.6**

1. **Solve by Reducing to Linear Form:**

- (i) (\frac{1}{2x} + \frac{1}{3y} = 2); (\frac{1}{3x} + \frac{1}{2y} = \frac{13}{6})
- (ii) (\frac{2}{\sqrt{x}} + \frac{3}{\sqrt{y}} = 2); (\frac{4}{\sqrt{x}} - \frac{9}{\sqrt{y}} = -1)
- (iii) (\frac{4}{x} + 3y = 14); (\frac{3}{x} - 4y = 23)
- (iv) (\frac{5}{x-1} + \frac{1}{y-2} = 2); (\frac{6}{x-1} - \frac{3}{y-2} = 1)
- (v) (\frac{7x-2y}{xy} = 5); (\frac{8x+7y}{xy} = 15)
- (vi) (6x + 3y = 6xy); (2x + 4y = 5xy)
- (vii) (\frac{10}{x+y} + \frac{2}{x-y} = 4); (\frac{15}{x+y} - \frac{5}{x-y} = -2)
- (viii) (\frac{1}{3x+y} + \frac{1}{3x-y} = \frac{3}{4}); (\frac{1}{2(3x+y)} - \frac{1}{2(3x-y)} = -\frac{1}{8})

2. **Formulate and Solve:**

- (i) Ritu can row downstream (20\text{ km}) in 2 hours, and upstream (4\text{ km}) in 2 hours. Find her speed of rowing in still water and the speed of the current.
- (ii) 2 women and 5 men can together finish an embroidery work in 4 days, while 3 women and 6 men can finish it in 3 days. Find the time taken by 1 woman alone to finish the work, and also that taken by 1 man alone.
- (iii) Roohi travels (300\text{ km}) to her home partly by train and partly by bus. She takes 4 hours if she travels (60\text{ km}) by train and the remaining by bus. If she travels (100\text{ km}) by train and the remaining by bus, she takes 10 minutes longer. Find the speed of the train and the bus separately.

---

### **EXERCISE 3.7 (Optional)**

_These exercises are not from the examination point of view._

1. **Friends' Ages:** The ages of two friends Ani and Biju differ by 3 years. Ani's father Dharam is twice as old as Ani and Biju is twice as old as his sister Cathy. The ages of Cathy and Dharam differ by 30 years. Find the ages of Ani and Biju.
2. **Ancient Riddles:** One says, "Give me a hundred, friend! I shall then become twice as rich as you". The other replies, "If you give me ten, I shall be six times as rich as you". Tell me what is the amount of their (respective) capital? [From the *Bijaganita* of Bhaskara II]
3. **Train Journey:** A train covered a certain distance at a uniform speed. If the train would have been $10\text{ km/h}$ faster, it would have taken 2 hours less than the scheduled time. And, if the train were slower by $10\text{ km/h}$, it would have taken 3 hours more than the scheduled time. Find the distance covered by the train.
4. **Classroom Rows:** The students of a class are made to stand in rows. If 3 students are extra in a row, there would be 1 row less. If 3 students are less in a row, there would be 2 rows more. Find the number of students in the class.
5. **Triangle Geometry:** In a $\Delta ABC$, $\angle C = 3\angle B = 2(\angle A + \angle B)$. Find the three angles.
6. **Triangular Coordinates:** Draw the graphs of the equations $5x - y = 5$ and $3x - y = 3$. Determine the coordinates of the vertices of the triangle formed by these lines and the y-axis.
7. **Solve:**

- (i) (px + qy = p-q) and (qx - py = p+q)
- (ii) (ax + by = c) and (bx + ay = 1+c)
- (iii) (\frac{x}{a} - \frac{y}{b} = 0) and (ax + by = a^2 + b^2)
- (iv) ((a-b)x + (a+b)y = a^2 - 2ab - b^2) and ((a+b)(x+y) = a^2 + b^2)
- (v) (152x - 378y = -74) and (-378x + 152y = -604)

8. **Cyclic Quadrilateral:** ABCD is a cyclic quadrilateral. Find the angles of the cyclic quadrilateral (with angles given as $3y-5, 4y+20, -4x,$ and $-7x+5$).

---

🎨 I can create a dynamic, downloadable spreadsheet tool containing these Chapter 3 mathematical linear solvers or package this guide into a beautifully polished PDF. Let me know what you would like to tackle next!
