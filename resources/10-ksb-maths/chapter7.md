# **Chapter 7: Coordinate Geometry — Study Guide**

---

## **I. Core Concepts & Geometrical Principles**

Coordinate geometry is an algebraic tool for studying the geometry of figures. It allows us to study geometry using algebra and understand algebra with the help of geometry.

### **1. The Cartesian Coordinate System**

- **Abscissa (x-coordinate):** The distance of a point from the y-axis.
- **Ordinate (y-coordinate):** The distance of a point from the x-axis.
- **x-axis Point Format:** Any point on the x-axis is of the form **\\((x, 0)\\)**.
- **y-axis Point Format:** Any point on the y-axis is of the form **\\((0, y)\\)**.

---

### **2. The Distance Formula**

To find the distance between any two points \\(P(x_1, y_1)\\) and \\(Q(x_2, y_2)\\), we use the **Pythagoras Theorem**.

#### **Derivation of Distance Formula:**

Let \\(P(x_1, y_1)\\) and \\(Q(x_2, y_2)\\) be two points in the first quadrant. Draw perpendiculars \\(PR\\) and \\(QS\\) on the x-axis, and draw a perpendicular \\(PT\\) from \\(P\\) on \\(QS\\).

#### **Geometric Setup of Distance Formula:**

```xml
<svg width="400" height="300" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .grid { stroke: #cbd5e1; stroke-width: 0.5; }
    .axis { stroke: #0f172a; stroke-width: 2; }
    .line-main { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .dash-line { stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 4 4; fill: none; }
    .lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #1e293b; }
    .lbl-bold { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
    .dot { fill: #0f172a; }
  </style>
  <!-- Cartesian Axes -->
  <line x1="50" y1="20" x2="50" y2="260" class="axis"/> <!-- y-axis -->
  <line x1="40" y1="240" x2="360" y2="240" class="axis"/> <!-- x-axis -->

  <line x1="150" y1="160" x2="300" y2="80" class="line-main"/>

  <!-- Dashed perpendiculars -->
  <line x1="150" y1="160" x2="150" y2="240" class="dash-line"/> <!-- PR -->
  <line x1="300" y1="80" x2="300" y2="240" class="dash-line"/> <!-- QS -->
  <line x1="150" y1="160" x2="300" y2="160" class="dash-line"/> <!-- PT -->

  <!-- Dots -->
  <circle cx="150" cy="160" r="4.5" class="dot"/>
  <circle cx="300" cy="80" r="4.5" class="dot"/>
  <circle cx="300" cy="160" r="4" class="dot" style="fill:#ef4444;"/>

  <!-- Labels -->
  <text x="365" y="245" class="lbl-bold">X</text>
  <text x="45" y="15" class="lbl-bold">Y</text>
  <text x="40" y="255" class="lbl">O</text>

  <text x="95" y="155" class="lbl-bold">P(x₁, y₁)</text>
  <text x="310" y="75" class="lbl-bold">Q(x₂, y₂)</text>
  <text x="310" y="165" class="lbl-bold" style="fill:#ef4444;">T(x₂, y₁)</text>

  <text x="145" y="255" class="lbl">R</text>
  <text x="295" y="255" class="lbl">S</text>

  <!-- Dimension Labels -->
  <text x="210" y="150" class="lbl" style="fill:#0284c7;">x₂ - x₁</text>
  <text x="310" y="125" class="lbl" style="fill:#0284c7;">y₂ - y₁</text>
</svg>
```

We see that:
\\[OR = x_1, \quad OS = x_2 \implies RS = x_2 - x_1 = PT\\\\]
\\[SQ = y_2, \quad ST = PR = y_1 \implies QT = y_2 - y_1\\\\]
Applying the Pythagoras Theorem in right-angled triangle \\(\Delta PTQ\\):
\\[PQ^2 = PT^2 + QT^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2\\\\]
\\[PQ = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\\\\]

- **Distance from the Origin:** The distance of a point \\(P(x, y)\\) from the origin \\(O(0,0)\\) is given by:
  \\[OP = \sqrt{x^2 + y^2}\\\\]

---

### **3. The Section Formula**

If a point \\(P(x, y)\\) divides the line segment joining the points \\(A(x_1, y_1)\\) and \\(B(x_2, y_2)\\) internally in a positive ratio **\\(m_1 : m_2\\)**:

#### **Geometric Setup of Section Formula:**

```xml
<svg width="400" height="260" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .axis { stroke: #64748b; stroke-width: 1.5; }
    .line-seg { stroke: #8b5cf6; stroke-width: 3; fill: none; }
    .proj { stroke: #94a3b8; stroke-width: 1; stroke-dasharray: 3 3; }
    .lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; fill: #0f172a; }
    .lbl-b { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
    .dot { fill: #0f172a; }
  </style>
  <line x1="40" y1="20" x2="40" y2="220" class="axis"/>
  <line x1="30" y1="200" x2="370" y2="200" class="axis"/>

  <line x1="80" y1="160" x2="300" y2="50" class="line-seg"/>

  <!-- Perpendiculars to X-axis -->
  <line x1="80" y1="160" x2="80" y2="200" class="proj"/> <!-- AR -->
  <line x1="180" y1="110" x2="180" y2="200" class="proj"/> <!-- PS -->
  <line x1="300" y1="50" x2="300" y2="200" class="proj"/> <!-- BT -->

  <!-- Horizontals AQ and PC -->
  <line x1="80" y1="160" x2="180" y2="160" class="proj"/> <!-- AQ -->
  <line x1="180" y1="110" x2="300" y2="110" class="proj"/> <!-- PC -->

  <!-- Dots -->
  <circle cx="80" cy="160" r="4.5" class="dot"/>
  <circle cx="180" cy="110" r="4.5" class="dot" style="fill:#ef4444;"/>
  <circle cx="300" cy="50" r="4.5" class="dot"/>
  <circle cx="180" cy="160" r="3.5" class="dot"/>
  <circle cx="300" cy="110" r="3.5" class="dot"/>

  <!-- Labels -->
  <text x="45" y="150" class="lbl-b">A(x₁, y₁)</text>
  <text x="160" y="95" class="lbl-b" style="fill:#ef4444;">P(x, y)</text>
  <text x="310" y="45" class="lbl-b">B(x₂, y₂)</text>

  <text x="185" y="155" class="lbl">Q</text>
  <text x="305" y="105" class="lbl">C</text>

  <text x="75" y="215" class="lbl">R</text>
  <text x="175" y="215" class="lbl">S</text>
  <text x="295" y="215" class="lbl">T</text>

  <!-- Ratio Labels -->
  <text x="120" y="125" class="lbl-b" style="fill:#8b5cf6;">m₁</text>
  <text x="235" y="70" class="lbl-b" style="fill:#8b5cf6;">m₂</text>
</svg>
```

By AA similarity, \\(\Delta PAQ \sim \Delta BPC\\). Thus:
\\[\frac{PA}{BP} = \frac{AQ}{PC} = \frac{PQ}{BC} = \frac{m_1}{m_2} \quad \text{--- (Eq. 1)}\\\\]
From coordinates:
\\[AQ = x - x_1, \quad PC = x_2 - x\\\\]
\\[PQ = y - y_1, \quad BC = y_2 - y\\\\]
Substituting these into Eq. 1:
\\[\frac{m_1}{m_2} = \frac{x - x_1}{x_2 - x} \implies x = \frac{m_1x_2 + m_2x_1}{m_1 + m_2}\\\\]
\\[\frac{m_1}{m_2} = \frac{y - y_1}{y_2 - y} \implies y = \frac{m_1y_2 + m_2y_1}{m_1 + m_2}\\\\]
Therefore, the **Section Formula** is:
\\[P(x, y) = \left( \frac{m_1x_2 + m_2x_1}{m_1 + m_2}, \ \frac{m_1y_2 + m_2y_1}{m_1 + m_2} \right)\\\\]

- **Mid-point Case:** The mid-point of a line segment divides it in the ratio \\(1:1\\). Its coordinates are:
  \\[P(x, y) = \left( \frac{x_1 + x_2}{2}, \ \frac{y_1 + y_2}{2} \right)\\\\]

---

### **4. Area of a Triangle**

Given three non-collinear points \\(A(x_1, y_1)\\), \\(B(x_2, y_2)\\), and \\(C(x_3, y_3)\\) forming a triangle:

#### **Geometric Setup of Area of a Triangle:**

```xml
<svg width="400" height="260" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .axis { stroke: #64748b; stroke-width: 1.5; }
    .poly-tri { fill: #fbcfe8; fill-opacity: 0.3; stroke: #db2777; stroke-width: 2.5; }
    .proj { stroke: #94a3b8; stroke-width: 1; stroke-dasharray: 3 3; }
    .lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; fill: #0f172a; }
    .lbl-b { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
    .dot { fill: #0f172a; }
  </style>
  <line x1="40" y1="20" x2="40" y2="220" class="axis"/>
  <line x1="30" y1="200" x2="370" y2="200" class="axis"/>

  <polygon points="180,70 90,140 280,110" class="poly-tri"/>

  <!-- Perpendicular projections BQ, AP, CR to X-axis -->
  <line x1="90" y1="140" x2="90" y2="200" class="proj"/> <!-- BQ -->
  <line x1="180" y1="70" x2="180" y2="200" class="proj"/> <!-- AP -->
  <line x1="280" y1="110" x2="280" y2="200" class="proj"/> <!-- CR -->

  <!-- Dots -->
  <circle cx="180" cy="70" r="4.5" class="dot"/>
  <circle cx="90" cy="140" r="4.5" class="dot"/>
  <circle cx="280" cy="110" r="4.5" class="dot"/>

  <!-- Labels -->
  <text x="165" y="60" class="lbl-b">A(x₁, y₁)</text>
  <text x="45" y="135" class="lbl-b">B(x₂, y₂)</text>
  <text x="290" y="105" class="lbl-b">C(x₃, y₃)</text>

  <text x="85" y="215" class="lbl">Q</text>
  <text x="175" y="215" class="lbl">P</text>
  <text x="275" y="215" class="lbl">R</text>
</svg>
```

By projecting vertices perpendicular to the x-axis, we obtain three trapezia: \\(ABQP\\), \\(APRC\\), and \\(BQRC\\).
\\[\text{Area of } \Delta ABC = \text{Area}(ABQP) + \text{Area}(APRC) - \text{Area}(BQRC)\\\\]
Using the formula for the area of a trapezium \\(\left(\text{Area} = \frac{1}{2} \times \text{sum of parallel sides} \times \text{distance between them}\right)\\):
\\[\text{Area} = \frac{1}{2}(BQ + AP)QP + \frac{1}{2}(AP + CR)PR - \frac{1}{2}(BQ + CR)QR\\\\]
\\[\text{Area} = \frac{1}{2}(y_2 + y_1)(x_1 - x_2) + \frac{1}{2}(y_1 + y_3)(x_3 - x_1) - \frac{1}{2}(y_2 + y_3)(x_3 - x_2)\\\\]
\\[\text{Area} = \frac{1}{2} [x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)]\\\\]

- **Collinear Points:** If three points are collinear, they cannot form a triangle, and the **area of the triangle is 0**.

---

## **II. Example Problems (with Step-by-Step Solutions)**

### **Example 1**

**Problem:** Do the points \\((3, 2)\\), \\((-2, -3)\\), and \\((2, 3)\\) form a triangle? If so, name the type of triangle formed.

- **Solution:**
  Let the points be \\(P(3, 2)\\), \\(Q(-2, -3)\\), and \\(R(2, 3)\\). Applying the distance formula:
  \\[PQ = \sqrt{(3 - (-2))^2 + (2 - (-3))^2} = \sqrt{5^2 + 5^2} = \sqrt{50} \approx 7.07\\\\]
  \\[QR = \sqrt{(-2 - 2)^2 + (-3 - 3)^2} = \sqrt{(-4)^2 + (-6)^2} = \sqrt{16 + 36} = \sqrt{52} \approx 7.21\\\\]
  \\[PR = \sqrt{(3 - 2)^2 + (2 - 3)^2} = \sqrt{1^2 + (-1)^2} = \sqrt{2} \approx 1.41\\\\]
  Since the sum of any two of these distances is greater than the third, the points **form a triangle**.
  Furthermore, we observe:
  \\[PQ^2 + PR^2 = 50 + 2 = 52 = QR^2\\\\]
  By the converse of the Pythagoras Theorem, the triangle is a **right-angled triangle**.

---

### **Example 2**

**Problem:** Show that the points \\((1, 7)\\), \\((4, 2)\\), \\((-1, -1)\\), and \\((-4, 4)\\) are the vertices of a square.

- **Solution:**
  Let the vertices be \\(A(1, 7)\\), \\(B(4, 2)\\), \\(C(-1, -1)\\), and \\(D(-4, 4)\\).
  Calculate the length of all four sides:
  \\[AB = \sqrt{(1 - 4)^2 + (7 - 2)^2} = \sqrt{(-3)^2 + 5^2} = \sqrt{34}\\\\]
  \\[BC = \sqrt{(4 - (-1))^2 + (2 - (-1))^2} = \sqrt{5^2 + 3^2} = \sqrt{34}\\\\]
  \\[CD = \sqrt{(-1 - (-4))^2 + (-1 - 4)^2} = \sqrt{3^2 + (-5)^2} = \sqrt{34}\\\\]
  \\[DA = \sqrt{(1 - (-4))^2 + (7 - 4)^2} = \sqrt{5^2 + 3^2} = \sqrt{34}\\\\]
  Calculate the lengths of both diagonals:
  \\[AC = \sqrt{(1 - (-1))^2 + (7 - (-1))^2} = \sqrt{2^2 + 8^2} = \sqrt{68}\\\\]
  \\[BD = \sqrt{(4 - (-4))^2 + (2 - 4)^2} = \sqrt{8^2 + (-2)^2} = \sqrt{68}\\\\]
  Since \\(AB = BC = CD = DA\\) and \\(AC = BD\\), all four sides are equal and the diagonals are equal. Therefore, \\(ABCD\\) is a **square**.

---

### **Example 3**

**Problem:** Find a point on the y-axis which is equidistant from the points \\(A(6, 5)\\) and \\(B(-4, 3)\\).

- **Solution:**
  Any point on the y-axis has coordinates of the form \\(P(0, y)\\).
  Since \\(P\\) is equidistant from \\(A\\) and \\(B\\), we have \\(AP^2 = BP^2\\):
  \\[(6 - 0)^2 + (5 - y)^2 = (-4 - 0)^2 + (3 - y)^2\\\\]
  \\[36 + 25 - 10y + y^2 = 16 + 9 - 6y + y^2\\\\]
  \\[61 - 10y = 25 - 6y\\\\]
  \\[4y = 36 \implies y = 9\\\\]
  The required point on the y-axis is **\\((0, 9)\\)**.

---

### **Example 4**

**Problem:** Find the coordinates of the point which divides the line segment joining the points \\((4, -3)\\) and \\((8, 5)\\) in the ratio \\(3 : 1\\) internally.

- **Solution:**
  Here, \\(x_1 = 4, y_1 = -3, x_2 = 8, y_2 = 5, m_1 = 3, m_2 = 1\\).
  Applying the Section Formula:
  \\[x = \frac{m_1x_2 + m_2x_1}{m_1 + m_2} = \frac{3(8) + 1(4)}{3 + 1} = \frac{24 + 4}{4} = 7\\\\]
  \\[y = \frac{m_1y_2 + m_2y_1}{m_1 + m_2} = \frac{3(5) + 1(-3)}{3 + 1} = \frac{15 - 3}{4} = 3\\\\]
  The coordinates of the point are **\\((7, 3)\\)**.

---

### **Example 5**

**Problem:** In what ratio does the point \\((-4, 6)\\) divide the line segment joining the points \\(A(-6, 10)\\) and \\(B(3, -8)\\)?

- **Solution:**
  Let the point \\(P(-4, 6)\\) divide the segment \\(AB\\) in the ratio \\(k : 1\\). Using the Section Formula:
  \\[-4 = \frac{k(3) + 1(-6)}{k + 1} \implies -4(k + 1) = 3k - 6\\\\]
  \\[-4k - 4 = 3k - 6 \implies 7k = 2 \implies k = \frac{2}{7}\\\\]
  The ratio \\(k : 1\\) is **\\(2 : 7\\)**.

---

### **Example 6**

**Problem:** Find the area of a triangle whose vertices are \\((1, -1)\\), \\((-4, 6)\\), and \\((-3, -5)\\).

- **Solution:**
  Let \\(x_1 = 1, y_1 = -1, x_2 = -4, y_2 = 6, x_3 = -3, y_3 = -5\\).
  Using the Triangle Area formula:
  \\[\text{Area} = \frac{1}{2} |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|\\\\]
  \\[\text{Area} = \frac{1}{2} |1(6 - (-5)) + (-4)(-5 - (-1)) + (-3)(-1 - 6)|\\\\]
  \\[\text{Area} = \frac{1}{2} |1(11) + (-4)(-4) + (-3)(-7)|\\\\]
  \\[\text{Area} = \frac{1}{2} |11 + 16 + 21| = \frac{1}{2} |48| = 24\\\\]
  The area is **\\(24\\) square units**.

---

## **III. Exercises**

### **EXERCISE 7.1**

1.  Find the distance between the following pairs of points:
    (i) \\((2, 3), (4, 1)\\)
    (ii) \\((-5, 7), (-1, 3)\\)
    (iii) \\((a, b), (-a, -b)\\).
2.  Find the distance between the points \\((0, 0)\\) and \\((36, 15)\\).
3.  Determine if the points \\((1, 5)\\), \\((2, 3)\\), and \\((-2, -11)\\) are collinear.
4.  Check whether \\((5, -2)\\), \\((6, 4)\\), and \\((7, -2)\\) are the vertices of an isosceles triangle.
5.  In Fig 7.8, four friends are seated at the points \\(A\\), \\(B\\), \\(C\\), and \\(D\\). Champa asks Chameli, "Don't you think ABCD is a square?" Chameli disagrees. Using the distance formula, find who is correct.
6.  Name the type of quadrilateral formed, if any, by the following points:
    (i) \\((-1, -2), (1, 0), (-1, 2), (-3, 0)\\)
    (ii) \\((-3, 5), (3, 1), (0, 3), (-1, -4)\\)
    (iii) \\((4, 5), (7, 6), (4, 3), (1, 2)\\).
7.  Find the point on the x-axis which is equidistant from \\((2, -5)\\) and \\((-2, 9)\\).
8.  Find the values of \\(y\\) for which the distance between the points \\(P(2, -3)\\) and \\(Q(10, y)\\) is \\(10\\) units.
9.  If \\(Q(0, 1)\\) is equidistant from \\(P(5, -3)\\) and \\(R(x, 6)\\), find the values of \\(x\\). Also find the distances \\(QR\\) and \\(PR\\).
10. Find a relation between \\(x\\) and \\(y\\) such that the point \\((x, y)\\) is equidistant from the points \\((3, 6)\\) and \\((-3, 4)\\).

---

### **EXERCISE 7.2**

1.  Find the coordinates of the point which divides the join of \\((-1, 7)\\) and \\((4, -3)\\) in the ratio \\(2 : 3\\).
2.  Find the coordinates of the points of trisection of the line segment joining \\((4, -1)\\) and \\((-2, -3)\\).
3.  In your rectangular school ground, lines are drawn with chalk at a distance of 1m. Niharika runs \\(\frac{1}{4}\\)th the distance AD along the 2nd line and posts a green flag. Preet runs \\(\frac{1}{5}\\)th the distance AD along the 8th line and posts a red flag. Find the distance between the flags. If Rashmi has to post a blue flag exactly halfway between the line segment joining the two flags, where should she post it?
4.  Find the ratio in which the line segment joining the points \\((-3, 10)\\) and \\((6, -8)\\) is divided by \\((-1, 6)\\).
5.  Find the ratio in which the line segment joining \\(A(1, -5)\\) and \\(B(-4, 5)\\) is divided by the x-axis. Also find the coordinates of the point of division.
6.  If \\((1, 2)\\), \\((4, y)\\), \\((x, 6)\\), and \\((3, 5)\\) are the vertices of a parallelogram taken in order, find \\(x\\) and \\(y\\).
7.  Find the coordinates of a point \\(A\\) where \\(AB\\) is the diameter of a circle whose centre is \\((2, -3)\\) and \\(B\\) is \\((1, 4)\\).
8.  If \\(A\\) and \\(B\\) are \\((-2, -2)\\) and \\((2, -4)\\) respectively, find the coordinates of \\(P\\) such that \\(AP = \frac{3}{7}AB\\) and \\(P\\) lies on the line segment \\(AB\\).
9.  Find the coordinates of the points which divide the line segment joining \\(A(-2, 2)\\) and \\(B(2, 8)\\) into four equal parts.
10. Find the area of a rhombus if its vertices are \\((3, 0)\\), \\((4, 5)\\), \\((-1, 4)\\), and \\((-2, -1)\\) taken in order.

---

### **EXERCISE 7.3**

1.  Find the area of the triangle whose vertices are:
    (i) \\((2, 3), (-1, 0), (2, -4)\\)
    (ii) \\((-5, -1), (3, -5), (5, 2)\\).
2.  In each of the following find the value of \\(k\\) for which the points are collinear:
    (i) \\((7, -2), (5, 1), (3, k)\\)
    (ii) \\((8, 1), (k, -4), (2, -5)\\).
3.  Find the area of the triangle formed by joining the mid-points of the sides of the triangle whose vertices are \\((0, -1)\\), \\((2, 1)\\), and \\((0, 3)\\). Find the ratio of this area to the area of the given triangle.
4.  Find the area of the quadrilateral whose vertices, taken in order, are \\((-4, -2)\\), \\((-3, -5)\\), \\((3, -2)\\), and \\((2, 3)\\).
5.  Verify that a median of a triangle divides it into two triangles of equal areas for \\(\Delta ABC\\) whose vertices are \\(A(4, -6)\\), \\(B(3, -2)\\), and \\(C(5, 2)\\).

---

### **EXERCISE 7.4 (Optional)\***

_\*These exercises are not from the examination point of view._

1.  Determine the ratio in which the line \\(2x + y - 4 = 0\\) divides the line segment joining the points \\(A(2, -2)\\) and \\(B(3, 7)\\).
2.  Find a relation between \\(x\\) and \\(y\\) if the points \\((x, y)\\), \\((1, 2)\\), and \\((7, 0)\\) are collinear.
3.  Find the centre of a circle passing through the points \\((6, -6)\\), \\((3, -7)\\), and \\((3, 3)\\).
4.  The two opposite vertices of a square are \\((-1, 2)\\) and \\((3, 2)\\). Find the coordinates of the other two vertices.
5.  In a rectangular plot of land, Gulmohar saplings are planted on the boundary at a distance of 1m from each other. There is a triangular grassy lawn \\(PQR\\).
    (i) Taking \\(A\\) as the origin, find the coordinates of the vertices of the triangle.
    (ii) What will the coordinates be if \\(C\\) is the origin?
    Calculate the areas of the triangles in both cases and make your observation.
6.  The vertices of a \\(\Delta ABC\\) are \\(A(4, 6)\\), \\(B(1, 5)\\), and \\(C(7, 2)\\). A line is drawn to intersect sides \\(AB\\) and \\(AC\\) at \\(D\\) and \\(E\\) respectively, such that \\(\frac{AD}{AB} = \frac{AE}{AC} = \frac{1}{4}\\). Calculate the area of the \\(\Delta ADE\\) and compare it with the area of \\(\Delta ABC\\).
7.  Let \\(A(4, 2)\\), \\(B(6, 5)\\), and \\(C(1, 4)\\) be the vertices of \\(\Delta ABC\\).
    (i) The median from \\(A\\) meets \\(BC\\) at \\(D\\). Find the coordinates of the point \\(D\\).
    (ii) Find the coordinates of the point \\(P\\) on \\(AD\\) such that \\(AP : PD = 2 : 1\\).
    (iii) Find the coordinates of points \\(Q\\) and \\(R\\) on medians \\(BE\\) and \\(CF\\) respectively such that \\(BQ : QE = 2 : 1\\) and \\(CR : RF = 2 : 1\\).
    (iv) What do you observe?
8.  \\(ABCD\\) is a rectangle formed by the points \\(A(-1, -1)\\), \\(B(-1, 4)\\), \\(C(5, 4)\\), and \\(D(5, -1)\\). \\(P, Q, R, S\\) are the mid-points of \\(AB, BC, CD, DA\\) respectively. Is the quadrilateral \\(PQRS\\) a square, a rectangle, or a rhombus? Justify your answer.

---

📈 **I can help you write a Python script in our environment to solve coordinate equations, find midpoint coordinates, or calculate triangle areas dynamically. Let me know if you would like me to set up a programmatic coordinate tool!**
