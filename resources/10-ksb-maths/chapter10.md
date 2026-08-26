# **Chapter 10: Quadratic Equations — Study Guide**

---

## **I. Core Concepts & Algebraic Principles**

### **1. Introduction to Quadratic Equations**

A **quadratic equation** in the variable \\(x\\) is an equation that can be written in the standard form:
\\[ax^2 + bx + c = 0\\]
where \\(a, b,\\) and \\(c\\) are real numbers, and \\(a \neq 0\\) ``.

- **The Standard Form:** Writing the terms of the polynomial in descending order of their degrees yields the standard form of a quadratic equation `. For example, \\(2x^2 + x - 300 = 0\\) is in standard form `.
- **Geometric and Practical Origin:** Quadratic equations naturally arise in various real-life and physical scenarios, such as determining the dimensions of a room of a given carpet area `, calculating the trajectories of projectiles, or analyzing manufacturing costs `.
- **Roots of a Quadratic Equation:** A real number \\(\alpha\\) is called a **root** of the quadratic equation \\(ax^2 + bx + c = 0\\) if \\(a\alpha^2 + b\alpha + c = 0\\) `. The zeroes of the quadratic polynomial \\(ax^2 + bx + c\\) and the roots of the quadratic equation \\(ax^2 + bx + c = 0\\) are identical `. A quadratic equation can have **at most two real roots** ``.

---

### **2. Historical Context**

- **Babylonians:** Believed to be the first to solve quadratic equations by finding two positive numbers with a given positive sum and product ``.
- **Euclid:** Developed a geometric approach for finding lengths that correspond to the solutions of quadratic equations ``.
- **Brahmagupta (C.E. 598–665):** An ancient Indian mathematician who gave an explicit formula to solve quadratic equations of the form \\(ax^2 + bx = c\\) ``.
- **Sridharacharya (C.E. 1025):** Derived the quadratic formula by the method of completing the square, as recorded by Bhaskara II ``.

---

## **II. Methods of Solving Quadratic Equations**

### **1. Solution by Factorisation (Splitting the Middle Term)**

In this method, we factorise the quadratic expression \\(ax^2 + bx + c\\) into two linear factors by splitting the middle term \\(b\\) into two parts whose product equals \\(ac\\) `. Equating each linear factor to zero yields the roots of the equation `.

---

### **2. Solution by Completing the Square**

Any quadratic equation \\(ax^2 + bx + c = 0\\) can be rearranged into the form \\((x + d)^2 - e^2 = 0\\) by "completing the square" `. This allows us to solve directly by taking square roots `.

#### **Visualizing "Completing the Square" for \\(x^2 + 4x\\):**

To geometrically convert \\(x^2 + 4x\\) into a perfect square, we divide the \\(4x\\) block into two rectangles of area \\(2x\\) and arrange them on the adjacent sides of a square of area \\(x^2\\) `. A corner of size \\(2 \times 2 = 4\\) is left empty. Adding \\(2^2 = 4\\) completes the large square of side \\((x + 2)\\), and subtracting \\(4\\) keeps the total area equal to the original expression `:

```xml
<svg width="600" height="220" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .box-x { fill: #bae6fd; stroke: #0284c7; stroke-width: 2; }
    .box-2x { fill: #bbf7d0; stroke: #16a34a; stroke-width: 2; }
    .box-empty { fill: none; stroke: #ef4444; stroke-width: 2; stroke-dasharray: 4 4; }
    .box-filled { fill: #fecdd3; stroke: #f43f5e; stroke-width: 2; }
    .label { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; text-anchor: middle; }
    .arrow { stroke: #64748b; stroke-width: 2; fill: none; marker-end: url(#arrowhead); }
  </style>
  <defs>
    <marker id="arrowhead" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>

  <!-- Panel 1: Original x^2 + 4x -->
  <g transform="translate(10, 10)">
    <rect x="10" y="30" width="80" height="80" class="box-x"/>
    <text x="50" y="75" class="label">x²</text>
    <rect x="90" y="30" width="40" height="80" class="box-2x"/>
    <text x="110" y="75" class="label">4x</text>
    <text x="70" y="160" class="label">x² + 4x</text>
  </g>

  <!-- Transition Arrow -->
  <path d="M 170,100 L 210,100" class="arrow"/>

  <!-- Panel 2: Rearranging 4x into two 2x strips -->
  <g transform="translate(200, 10)">
    <rect x="30" y="30" width="80" height="80" class="box-x"/>
    <text x="70" y="75" class="label">x²</text>
    <!-- Right 2x strip -->
    <rect x="110" y="30" width="40" height="80" class="box-2x"/>
    <text x="130" y="75" class="label" style="font-size: 11px;">2x</text>
    <!-- Bottom 2x strip -->
    <rect x="30" y="110" width="80" height="40" class="box-2x"/>
    <text x="70" y="135" class="label" style="font-size: 11px;">2x</text>
    <!-- Missing corner -->
    <rect x="110" y="110" width="40" height="40" class="box-empty"/>
    <text x="130" y="135" class="label" style="fill:#ef4444; font-size:10px;">Missing<br/>2² = 4</text>
    <text x="90" y="190" class="label">Rearranged Strips</text>
  </g>

  <!-- Transition Arrow -->
  <path d="M 380,100 L 420,100" class="arrow"/>

  <!-- Panel 3: Completed Square -->
  <g transform="translate(420, 10)">
    <rect x="30" y="30" width="80" height="80" class="box-x"/>
    <text x="70" y="75" class="label">x²</text>
    <rect x="110" y="30" width="40" height="80" class="box-2x"/>
    <text x="130" y="75" class="label" style="font-size: 11px;">2x</text>
    <rect x="30" y="110" width="80" height="40" class="box-2x"/>
    <text x="70" y="135" class="label" style="font-size: 11px;">2x</text>
    <!-- Filled Corner -->
    <rect x="110" y="110" width="40" height="40" class="box-filled"/>
    <text x="130" y="135" class="label" style="fill:#e11d48; font-size: 11px;">2² = 4</text>
    <text x="90" y="190" class="label">(x + 2)² - 4</text>
  </g>
</svg>
```

---

### **3. The Quadratic Formula (Derivation)**

Starting with the general standard equation:
\\[ax^2 + bx + c = 0 \quad (a \neq 0) \quad \text{``}\\]
Divide the entire equation by \\(a\\):
\\[x^2 + \frac{b}{a}x + \frac{c}{a} = 0 \quad \text{``}\\]
To complete the square, add and subtract \\(\left(\frac{b}{2a}\right)^2\\):
\\[\left(x + \frac{b}{2a}\right)^2 - \left(\frac{b}{2a}\right)^2 + \frac{c}{a} = 0 \quad \text{``}\\]
\\[\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2} + \frac{c}{a} = 0 \quad \text{``}\\]
\\[\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2} \quad \text{``}\\]
Taking the square root on both sides (provided \\(b^2 - 4ac \geq 0\\)):
\\[x + \frac{b}{2a} = \frac{\pm\sqrt{b^2 - 4ac}}{2a} \quad \text{``}\\]
\\[x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \quad \text{``}\\]
This famous formula is known as the **Quadratic Formula** ``.

---

## **III. Nature of Roots**

The expression **\\(b^2 - 4ac\\)** under the radical sign in the quadratic formula determines whether a given quadratic equation has real roots and whether they are distinct or equal `. It is called the **discriminant** of the quadratic equation `.

For a quadratic equation \\(ax^2 + bx + c = 0\\):

| Discriminant Value      | Nature of Roots                         | Algebraic Form                                                                                   |
| :---------------------- | :-------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **\\(b^2 - 4ac > 0\\)** | **Two distinct, real roots** ``         | \\(x = \frac{-b + \sqrt{b^2 - 4ac}}{2a}\\) \ and \ \\(x = \frac{-b - \sqrt{b^2 - 4ac}}{2a}\\) `` |
| **\\(b^2 - 4ac = 0\\)** | **Two equal, coincident real roots** `` | \\(x = -\frac{b}{2a}\\) \ and \ \\(-\frac{b}{2a}\\) ``                                           |
| **\\(b^2 - 4ac < 0\\)** | **No real roots** ``                    | No real values exist ``                                                                          |

---

## **IV. Example Problems (with Step-by-Step Solutions)**

### **Example 1 (Formulating the Problem)**

**Problem:** John and Jivanti together have \\(45\\) marbles `. Both of them lost \\(5\\) marbles each, and the product of the number of marbles they now have is \\(124\\) `. Formulate a quadratic equation to find out how many marbles they had initially ``.

- **Solution:**
  - Let the number of marbles John had initially be \\(x\\) ``.
  - Since they have \\(45\\) marbles together, the number of marbles Jivanti had initially \\(= 45 - x\\) ``.
  - After losing \\(5\\) marbles each:
    - John's marbles \\(= x - 5\\) ``.
    - Jivanti's marbles \\(= (45 - x) - 5 = 40 - x\\) ``.
  - Given that the product of their marbles is \\(124\\):
    \\[(x - 5)(40 - x) = 124 \quad \text{``}\\]
    \\[40x - x^2 - 200 + 5x = 124 \quad \text{``}\\]
    \\[-x^2 + 45x - 200 = 124 \quad \text{``}\\]
    \\[x^2 - 45x + 324 = 0 \quad \text{``}\\]
  - This is the required quadratic equation ``.

---

### **Example 2 (Checking for Quadratic Equations)**

**Problem:** Check whether the following equations are quadratic:
(i) \\(x(2x+3) = x^2 + 1\\) `(ii) \\((x+2)^3 = x^3 - 4\\)`

- **Solution:**
  - **(i)** Expand the LHS of \\(x(2x+3) = x^2 + 1\\):
    \\[2x^2 + 3x = x^2 + 1 \quad \text{``}\\]
    Subtract \\(x^2 + 1\\) from both sides:
    \\[x^2 + 3x - 1 = 0 \quad \text{``}\\]
    Since it is of the form \\(ax^2 + bx + c = 0\\), **it is a quadratic equation** ``.
  - **(ii)** Expand the LHS of \\((x+2)^3 = x^3 - 4\\) using the identity \\((a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3\\):
    \\[x^3 + 6x^2 + 12x + 8 = x^3 - 4 \quad \text{``}\\]
    Subtract \\(x^3\\) from both sides and simplify:
    \\[6x^2 + 12x + 12 = 0 \implies x^2 + 2x + 2 = 0 \quad \text{``}\\]
    Since it is of the form \\(ax^2 + bx + c = 0\\), **it is a quadratic equation** ``.

---

### **Example 3 (Factorisation with Radicals)**

**Problem:** Solve the quadratic equation \\(3x^2 - 2\sqrt{6}x + 2 = 0\\) by factorisation ``.

- **Solution:**
  - Split the middle term \\(-2\sqrt{6}x\\) into \\(-\sqrt{6}x - \sqrt{6}x\\) `:
\\[3x^2 - \sqrt{6}x - \sqrt{6}x + 2 = 0 \quad \text{`}\\]
  - Group and factor out common terms:
    \\[\sqrt{3}x(\sqrt{3}x - \sqrt{2}) - \sqrt{2}(\sqrt{3}x - \sqrt{2}) = 0 \quad \text{``}\\]
    \\[(\sqrt{3}x - \sqrt{2})(\sqrt{3}x - \sqrt{2}) = 0 \quad \text{``}\\]
  - Equating each factor to zero:
    \\[\sqrt{3}x - \sqrt{2} = 0 \implies x = \sqrt{\frac{2}{3}} \quad \text{``}\\]
  - The repeated roots are **\\(\sqrt{\frac{2}{3}}, \sqrt{\frac{2}{3}}\\)** ``.

---

### **Example 4 (Completing the Square)**

**Problem:** Solve \\(5x^2 - 6x - 2 = 0\\) by completing the square ``.

- **Solution:**
  - Multiply the entire equation by \\(5\\) to make the first term a perfect square (\\(25x^2\\)) `:
\\[25x^2 - 30x - 10 = 0 \quad \text{`}\\]
  - Express the equation in the form \\((5x - a)^2 - b = 0\\):
    \\[(5x)^2 - 2(5x)(3) + 3^2 - 3^2 - 10 = 0 \quad \text{``}\\]
    \\[(5x-3)^2 - 9 - 10 = 0 \quad \text{``}\\]
    \\[(5x-3)^2 = 19 \quad \text{``}\\]
  - Take the square root of both sides:
    \\[5x - 3 = \pm\sqrt{19} \quad \text{``}\\]
    \\[5x = 3 \pm\sqrt{19} \implies x = \frac{3 \pm \sqrt{19}}{5} \quad \text{``}\\]
  - The roots are **\\(\frac{3 + \sqrt{19}}{5}\\)** and **\\(\frac{3 - \sqrt{19}}{5}\\)** ``.

---

### **Example 5 (Applied Word Problem with Speed)**

**Problem:** A motor boat whose speed is \\(18\text{ km/h}\\) in still water takes \\(1\\) hour more to go \\(24\text{ km}\\) upstream than to return downstream to the same spot `. Find the speed of the stream `.

- **Solution:**
  - Let the speed of the stream be \\(x\text{ km/h}\\) ``.
  - Upstream speed \\(= (18 - x)\text{ km/h}\\), and Downstream speed \\(= (18 + x)\text{ km/h}\\) ``.
  - Time taken upstream \\(= \frac{24}{18-x}\\) hours ``.
  - Time taken downstream \\(= \frac{24}{18+x}\\) hours ``.
  - Based on the given condition:
    \\[\frac{24}{18-x} - \frac{24}{18+x} = 1 \quad \text{``}\\]
    \\[24(18 + x) - 24(18 - x) = (18 - x)(18 + x) \quad \text{``}\\]
    \\[432 + 24x - 432 + 24x = 324 - x^2 \quad \text{``}\\]
    \\[x^2 + 48x - 324 = 0 \quad \text{``}\\]
  - Using the quadratic formula:
    \\[x = \frac{-48 \pm \sqrt{48^2 - 4(1)(-324)}}{2} = \frac{-48 \pm \sqrt{2304 + 1296}}{2} \quad \text{``}\\]
    \\[x = \frac{-48 \pm \sqrt{3600}}{2} = \frac{-48 \pm 60}{2} \quad \text{``}\\]
    \\[x = 6 \quad \text{or} \quad x = -54 \quad \text{``}\\]
  - Since the speed of the stream cannot be negative, we discard \\(x = -54\\) ``.
  - The speed of the stream is **\\(6\text{ km/h}\\)** ``.

---

### **Example 6 (Geometric Optimization and Nature of Roots)**

**Problem:** A pole is to be erected on the boundary of a circular park of diameter \\(13\text{ m}\\) such that the difference of its distances from two diametrically opposite fixed gates \\(A\\) and \\(B\\) on the boundary is \\(7\text{ m}\\) `. Is it possible to do so? If yes, at what distances from the two gates should the pole be erected `?

- **Solution:**

#### **Geometric Layout of Circular Park:**

```xml
<svg width="340" height="260" viewBox="0 0 340 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .circle-boundary { fill: none; stroke: #0f172a; stroke-width: 2; }
    .diameter { stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 4 4; }
    .triangle-line { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .dot-gate { fill: #0f172a; }
    .dot-pole { fill: #ef4444; }
    .text-lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
    .angle-box { stroke: #64748b; stroke-width: 1.2; fill: none; }
  </style>

  <!-- Circular Park Boundary -->
  <circle cx="170" cy="130" r="90" class="circle-boundary"/>

  <!-- Diameter AB (A at 80,130; B at 260,130) -->
  <line x1="80" y1="130" x2="260" y2="130" class="diameter"/>

  <!-- Triangle lines to Pole P at (125, 52) -->
  <line x1="80" y1="130" x2="125" y2="52" class="triangle-line"/>
  <line x1="260" y1="130" x2="125" y2="52" class="triangle-line"/>

  <!-- Right Angle Indicator at P -->
  <path d="M 120,60 L 128,63 L 133,55" class="angle-box"/>

  <!-- Dots -->
  <circle cx="80" cy="130" r="4.5" class="dot-gate"/>
  <circle cx="260" cy="130" r="4.5" class="dot-gate"/>
  <circle cx="125" cy="52" r="5" class="dot-pole"/>

  <!-- Labels -->
  <text x="60" y="135" class="text-lbl">A</text>
  <text x="270" y="135" class="text-lbl">B</text>
  <text x="120" y="38" class="text-lbl" style="fill:#ef4444;">P (Pole)</text>
  <text x="170" y="145" class="text-lbl" style="font-size: 11px; fill:#64748b;" text-anchor="middle">Diameter = 13 m</text>
  <text x="90" y="90" class="text-lbl" style="font-size:12px; fill:#0284c7;">x + 7</text>
  <text x="195" y="90" class="text-lbl" style="font-size:12px; fill:#0284c7;">x</text>
</svg>
```

Let the pole be placed at point \\(P\\) `. Let the distance of the pole from gate \\(B\\) be \\(x\text{ m}\\) (i.e., \\(BP = x\\)) `.

- The distance from gate \\(A\\) is \\(AP = (x + 7)\text{ m}\\) ``.
- Since \\(AB\\) is the diameter, \\(\angle APB = 90^\circ\\) (angle in a semicircle) ``.
- Using Pythagoras Theorem in \\(\Delta APB\\):
  \\[AP^2 + PB^2 = AB^2 \quad \text{``}\\]
  \\[(x + 7)^2 + x^2 = 13^2 \quad \text{``}\\]
  \\[x^2 + 14x + 49 + x^2 = 169 \quad \text{``}\\]
  \\[2x^2 + 14x - 120 = 0 \implies x^2 + 7x - 60 = 0 \quad \text{``}\\]
- Check the discriminant to determine if this is possible:
  \\[b^2 - 4ac = 7^2 - 4(1)(-60) = 49 + 240 = 289 \quad \text{``}\\]
- Since \\(b^2 - 4ac > 0\\), real roots exist, so **it is possible to erect the pole** ``.
- Solving the quadratic equation:
  \\[x = \frac{-7 \pm \sqrt{289}}{2} = \frac{-7 \pm 17}{2} \quad \text{``}\\]
  \\[x = 5 \quad \text{or} \quad x = -12 \quad \text{``}\\]
- Ignoring \\(x = -12\\) (distance must be positive), we find \\(x = 5\text{ m}\\) ``.
- Therefore, the pole must be erected at a distance of **\\(5\text{ m}\\) from gate \\(B\\)** and **\\(12\text{ m}\\) from gate \\(A\\)** ``.

---

## **V. Exercise Questions**

### **EXERCISE 10.1**

1.  **Check whether the following are quadratic equations:**
    - (i) \\((x+1)^2 = 2(x-3)\\) ``
    - (ii) \\(x^2 - 2x = (-2)(3-x)\\) ``
    - (iii) \\((x-2)(x+1) = (x-1)(x+3)\\) ``
    - (iv) \\((x-3)(2x+1) = x(x+5)\\) ``
    - (v) \\((2x-1)(x-3) = (x+5)(x-1)\\) ``
    - (vi) \\(x^2 + 3x + 1 = (x-2)^2\\) ``
    - (vii) \\((x+2)^3 = 2x(x^2-1)\\) ``
    - (viii) \\(x^3 - 4x^2 - x + 1 = (x-2)^3\\) ``
2.  **Represent the following situations in the form of quadratic equations:**
    - (i) The area of a rectangular plot is \\(528\text{ m}^2\\) `. The length of the plot is one more than twice its breadth `. We need to find the length and breadth of the plot ``.
    - (ii) The product of two consecutive positive integers is \\(306\\) `. We need to find the integers `.
    - (iii) Rohan's mother is \\(26\\) years older than him `. The product of their ages \\(3\\) years from now will be \\(360\\) `. We would like to find Rohan's present age ``.
    - (iv) A train travels a distance of \\(480\text{ km}\\) at a uniform speed `. If the speed had been \\(8\text{ km/h}\\) less, then it would have taken \\(3\\) hours more to cover the same distance `. We need to find the speed of the train ``.

---

### **EXERCISE 10.2**

1.  **Find the roots of the following quadratic equations by factorisation:**
    - (i) \\(x^2 - 3x - 10 = 0\\) ``
    - (ii) \\(2x^2 + x - 6 = 0\\) ``
    - (iii) \\(\sqrt{2}x^2 + 7x + 5\sqrt{2} = 0\\) ``
    - (iv) \\(2x^2 - x + \frac{1}{8} = 0\\) ``
    - (v) \\(100x^2 - 20x + 1 = 0\\) ``
2.  Solve the problems given in Example 1 ``.
3.  Find two numbers whose sum is \\(27\\) and product is \\(182\\) ``.
4.  Find two consecutive positive integers, the sum of whose squares is \\(365\\) ``.
5.  The altitude of a right triangle is \\(7\text{ cm}\\) less than its base `. If the hypotenuse is \\(13\text{ cm}\\), find the other two sides `.
6.  A cottage industry produces a certain number of pottery articles in a day `. It was observed on a particular day that the cost of production of each article was \\(3\\) more than twice the number of articles produced `. If the total cost of production was \\(90\\), find the number of articles produced and the cost of each article ``.

---

### **EXERCISE 10.3**

1.  **Find the roots of the following quadratic equations, if they exist, by the method of completing the square:**
    - (i) \\(2x^2 - 7x + 3 = 0\\) ``
    - (ii) \\(2x^2 + x - 4 = 0\\) ``
    - (iii) \\(4x^2 + 4\sqrt{3}x + 3 = 0\\) ``
    - (iv) \\(2x^2 + x + 4 = 0\\) ``
2.  Find the roots of the quadratic equations given in Q.1 above by applying the quadratic formula ``.
3.  **Find the roots of the following equations:**
    - (i) \\(x - \frac{1}{x} = 3 \quad (x \neq 0)\\) ``
    - (ii) \\(\frac{1}{x+4} - \frac{1}{x-7} = \frac{11}{30} \quad (x \neq -4, 7)\\) ``
4.  The sum of the reciprocals of Rehman's ages, \\(3\\) years ago and \\(5\\) years from now is \\(\frac{1}{3}\\) `. Find his present age `.
5.  In a class test, the sum of Shefali's marks in Mathematics and English is \\(30\\) `. Had she got \\(2\\) marks more in Mathematics and \\(3\\) marks less in English, the product of their marks would have been \\(210\\) `. Find her marks in the two subjects ``.
6.  The diagonal of a rectangular field is \\(60\\) metres more than the shorter side `. If the longer side is \\(30\\) metres more than the shorter side, find the sides of the field `.
7.  The difference of squares of two numbers is \\(180\\) `. The square of the smaller number is \\(8\\) times the larger number `. Find the two numbers ``.
8.  A train travels \\(360\text{ km}\\) at a uniform speed `. If the speed had been \\(5\text{ km/h}\\) more, it would have taken \\(1\\) hour less for the same journey `. Find the speed of the train ``.
9.  Two water taps together can fill a tank in \\(9\frac{3}{8}\\) hours `. The tap of larger diameter takes \\(10\\) hours less than the smaller one to fill the tank separately `. Find the time in which each tap can separately fill the tank ``.
10. An express train takes \\(1\\) hour less than a passenger train to travel \\(132\text{ km}\\) between Mysore and Bangalore `. If the average speed of the express train is \\(11\text{ km/h}\\) more than that of the passenger train, find the average speed of the two trains `.
11. The sum of the areas of two squares is \\(468\text{ m}^2\\) `. If the difference of their perimeters is \\(24\text{ m}\\), find the sides of the two squares `.

---

### **EXERCISE 10.4**

1.  **Find the nature of the roots of the following quadratic equations. If the real roots exist, find them:**
    - (i) \\(2x^2 - 3x + 5 = 0\\) ``
    - (ii) \\(3x^2 - 4\sqrt{3}x + 4 = 0\\) ``
    - (iii) \\(2x^2 - 6x + 3 = 0\\) ``
2.  **Find the values of \\(k\\) for each of the following quadratic equations, so that they have two equal roots:**
    - (i) \\(2x^2 + kx + 3 = 0\\) ``
    - (ii) \\(kx(x-2) + 6 = 0\\) ``
3.  Is it possible to design a rectangular mango grove whose length is twice its breadth, and the area is \\(800\text{ m}^2\\) `? If so, find its length and breadth `.
4.  Is the following situation possible? If so, determine their present ages ``.
    - _The sum of the ages of two friends is \\(20\\) years `. Four years ago, the product of their ages in years was \\(48\\) `._
5.  Is it possible to design a rectangular park of perimeter \\(80\text{ m}\\) and area \\(400\text{ m}^2\\) `? If so, find its length and breadth `.

---

📐 **I can compile this algebraic study guide into a polished PDF document or configure a Python solver for complex quadratic equations in your workspace. What would you like to build next?**
