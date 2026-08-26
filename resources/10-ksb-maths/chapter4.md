# **Chapter 4: Circles — Study Guide**

---

## **I. Core Concepts & Geometrical Principles**

### **1. Introduction to the Geometry of Circles**

A circle is defined as the collection of all points in a plane that are at a constant distance (the radius) from a fixed point (the centre). Based on the relative positions of a straight line and a circle in a plane, three distinct geometric scenarios can occur:

1.  **Non-intersecting Line:** The line and the circle share no common points.
2.  **Secant:** The line cuts through the circle, sharing exactly two distinct common points (\\(A\\) and \\(B\\)) with it.
3.  **Tangent:** The line touches the circle at exactly one single point.

#### **Geometric Comparison of Line-Circle Relationships:**

```xml
<svg width="600" height="220" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .circle { fill: #ffffff; stroke: #0f172a; stroke-width: 2.5; }
    .line { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .secant-line { stroke: #ef4444; stroke-width: 2.5; fill: none; }
    .tangent-line { stroke: #10b981; stroke-width: 2.5; fill: none; }
    .pt { fill: #0f172a; }
    .lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #1e293b; }
    .lbl-bold { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; text-anchor: middle; }
    .lbl-sec { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #64748b; text-anchor: middle; }
  </style>

  <!-- Panel 1: Non-intersecting Line -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="180" height="180" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <circle cx="80" cy="90" r="45" class="circle"/>
    <line x1="145" y1="20" x2="145" y2="160" class="line"/>
    <text x="153" y="25" class="lbl">P</text>
    <text x="153" y="155" class="lbl">Q</text>
    <text x="90" y="195" class="lbl-bold">1. Non-intersecting Line</text>
    <text x="90" y="210" class="lbl-sec">No common points</text>
  </g>

  <!-- Panel 2: Secant -->
  <g transform="translate(210, 10)">
    <rect x="0" y="0" width="180" height="180" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <circle cx="90" cy="90" r="45" class="circle"/>
    <line x1="40" y1="35" x2="140" y2="145" class="secant-line"/>
    <circle cx="58" cy="55" r="4" class="pt"/>
    <circle cx="122" cy="125" r="4" class="pt"/>
    <text x="50" y="50" class="lbl">A</text>
    <text x="130" y="135" class="lbl">B</text>
    <text x="32" y="35" class="lbl">P</text>
    <text x="145" y="150" class="lbl">Q</text>
    <text x="90" y="195" class="lbl-bold">2. Secant</text>
    <text x="90" y="210" class="lbl-sec">Two intersection points (A, B)</text>
  </g>

  <!-- Panel 3: Tangent -->
  <g transform="translate(410, 10)">
    <rect x="0" y="0" width="180" height="180" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <circle cx="90" cy="90" r="45" class="circle"/>
    <line x1="30" y1="135" x2="150" y2="135" class="tangent-line"/>
    <circle cx="90" cy="135" r="4" class="pt"/>
    <text x="90" y="150" class="lbl-bold" style="font-size:12px;">A (Point of Contact)</text>
    <text x="22" y="139" class="lbl">P</text>
    <text x="155" y="139" class="lbl">Q</text>
    <text x="90" y="195" class="lbl-bold">3. Tangent</text>
    <text x="90" y="210" class="lbl-sec">Exactly one common point (A)</text>
  </g>
</svg>
```

### **2. Characteristics & Etymology of a Tangent**

- **Etymology:** The word 'tangent' originates from the Latin word **_'tangere'_**, which means **'to touch'**. It was introduced to modern mathematics by the Danish mathematician **Thomas Fineke** in **1583**.
- **Definition:** A tangent is a straight line that intersects the circle at only one single point.
- **The Point of Contact:** The unique common point where the tangent touches the circle is called the **point of contact**.
- **The Limiting Case:** A tangent can be mathematically conceptualized as a special limiting case of a secant, occurring when the two endpoints of the secant's corresponding chord coincide into a single point.
- **Parallel Tangents Constraint:** There can be at most **two** tangents drawn parallel to any given secant of a circle.

---

## **II. Theorems and Formal Proofs**

### **Theorem 4.1 (Tangent-Radius Perpendicularity)**

> **Statement:** The tangent at any point of a circle is perpendicular to the radius through the point of contact.

#### **Formal Proof:**

Let there be a circle with centre \\(O\\) and a tangent line \\(XY\\) touching the circle at the point of contact \\(P\\). We must prove that the radius \\(OP\\) is perpendicular to \\(XY\\) (i.e., \\(OP \perp XY\\)).

#### **Geometric Setup of Theorem 4.1:**

```xml
<svg width="400" height="260" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .circ { fill: #ffffff; stroke: #0f172a; stroke-width: 2.5; }
    .tangent { stroke: #10b981; stroke-width: 2.5; fill: none; }
    .radius { stroke: #0f172a; stroke-width: 2; fill: none; }
    .hypot { stroke: #0284c7; stroke-width: 1.8; stroke-dasharray: 4 4; fill: none; }
    .lbl-text { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
    .indicator { stroke: #64748b; stroke-width: 1.2; fill: none; }
    .pt-dot { fill: #0f172a; }
  </style>

  <!-- Circle -->
  <circle cx="200" cy="100" r="75" class="circ"/>

  <!-- Tangent XY at P(200, 175) -->
  <line x1="60" y1="175" x2="340" y2="175" class="tangent"/>

  <!-- Perpendicular radius OP -->
  <line x1="200" y1="100" x2="200" y2="175" class="radius"/>

  <!-- Line OQ where Q is at (280, 175) -->
  <line x1="200" y1="100" x2="280" y2="175" class="hypot"/>

  <!-- Intersection of OQ with circle at (248, 145) -->
  <circle cx="248" cy="145" r="4" class="pt-dot"/>

  <!-- Dots for O, P, Q -->
  <circle cx="200" cy="100" r="4.5" class="pt-dot"/>
  <circle cx="200" cy="175" r="4.5" class="pt-dot"/>
  <circle cx="280" cy="175" r="4.5" class="pt-dot"/>

  <!-- Right Angle Indicator -->
  <rect x="185" y="160" width="15" height="15" class="indicator"/>

  <!-- Labels -->
  <text x="195" y="90" class="lbl-text">O (Centre)</text>
  <text x="192" y="195" class="lbl-text">P</text>
  <text x="282" y="195" class="lbl-text" style="fill:#0284c7;">Q</text>
  <text x="254" y="140" class="lbl-text" style="font-size:12px;">R</text>
  <text x="45" y="180" class="lbl-text" style="fill:#10b981;">X</text>
  <text x="345" y="180" class="lbl-text" style="fill:#10b981;">Y</text>
</svg>
```

1.  Take any point \\(Q\\) on the tangent line \\(XY\\) other than the point of contact \\(P\\). Join the line segment \\(OQ\\).
2.  The point \\(Q\\) must lie completely outside the circle. If \\(Q\\) lay inside the circle, the line \\(XY\\) would cut the circle at two points, making it a secant rather than a tangent.
3.  Because \\(Q\\) lies outside the circle, the distance \\(OQ\\) from the centre must be greater than the radius of the circle (\\(OP\\)). Thus:
    \\[OQ > OP\\]
4.  This inequality holds true for **every** point on the line \\(XY\\) except the point of contact \\(P\\).
5.  Consequently, the segment \\(OP\\) is the **shortest distance** from the centre \\(O\\) to any point on the line \\(XY\\).
6.  By geometric principle, the shortest line segment from a point to a line is the perpendicular to that line. Therefore:
    \\[OP \perp XY\\]

- **Deduction 1:** There can be one and only one tangent drawn at any given point on a circle.
- **Definition:** The line containing the radius through the point of contact is also referred to as the **'normal'** to the circle at that point.

---

### **Theorem 4.2 (Tangents from an External Point)**

> **Statement:** The lengths of tangents drawn from an external point to a circle are equal.

#### **Formal Proof:**

Let there be a circle with centre \\(O\\), an external point \\(P\\), and two tangents \\(PQ\\) and \\(PR\\) touching the circle at points of contact \\(Q\\) and \\(R\\) respectively. We must prove that \\(PQ = PR\\).

#### **Geometric Setup of Theorem 4.2:**

```xml
<svg width="400" height="260" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .c-outline { fill: #ffffff; stroke: #0f172a; stroke-width: 2.5; }
    .t-line { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .c-line { stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 4 4; fill: none; }
    .r-line { stroke: #ef4444; stroke-width: 2; fill: none; }
    .d-pt { fill: #0f172a; }
    .txt-lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
    .rt-ang { stroke: #64748b; stroke-width: 1.2; fill: none; }
  </style>

  <!-- Circle centered at (150, 130) with r=70 -->
  <circle cx="150" cy="130" r="70" class="c-outline"/>

  <!-- External point P at (340, 130) -->
  <circle cx="340" cy="130" r="4.5" class="d-pt"/>

  <!-- Points of contact Q and R -->
  <circle cx="176" cy="65" r="4.5" class="d-pt"/>
  <circle cx="176" cy="195" r="4.5" class="d-pt"/>
  <circle cx="150" cy="130" r="4.5" class="d-pt"/>

  <!-- Tangents PQ and PR -->
  <line x1="340" y1="130" x2="176" y2="65" class="t-line"/>
  <line x1="340" y1="130" x2="176" y2="195" class="t-line"/>

  <!-- Radii OQ and OR -->
  <line x1="150" y1="130" x2="176" y2="65" class="r-line"/>
  <line x1="150" y1="130" x2="176" y2="195" class="r-line"/>

  <!-- Line OP -->
  <line x1="150" y1="130" x2="340" y2="130" class="c-line"/>

  <!-- Right Angle Markers -->
  <!-- At Q -->
  <path d="M 170,78 L 163,75 L 169,62" class="rt-ang"/>
  <!-- At R -->
  <path d="M 170,182 L 163,185 L 169,198" class="rt-ang"/>

  <!-- Labels -->
  <text x="130" y="135" class="txt-lbl">O</text>
  <text x="175" y="52" class="txt-lbl">Q</text>
  <text x="175" y="215" class="txt-lbl">R</text>
  <text x="350" y="135" class="txt-lbl">P</text>
</svg>
```

Join the segments \\(OP\\), \\(OQ\\), and \\(OR\\).

1.  According to **Theorem 4.1**, the angles between the radii and the tangent lines at the points of contact are right angles:
    \\[\angle OQP = \angle ORP = 90^\circ\\]
2.  In the right-angled triangles \\(\Delta OQP\\) and \\(\Delta ORP\\):
    - \\(OQ = OR\\) (Radii of the same circle)
    - \\(OP = OP\\) (Common hypotenuse)
3.  By the **RHS (Right-Angle Hypotenuse Side) Congruence Criterion**:
    \\[\Delta OQP \cong \Delta ORP \quad \text{}\\]
4.  By the property of **CPCT** (Corresponding Parts of Congruent Triangles):
    \\[PQ = PR\\]

#### **Alternative Proof (Using Pythagoras Theorem):**

In the right-angled triangles \\(\Delta OQP\\) and \\(\Delta ORP\\):
\\[PQ^2 = OP^2 - OQ^2 \quad \text{--- (Using Pythagoras Theorem in } \Delta OQP\text{)} \quad \text{}\\]
\\[PR^2 = OP^2 - OR^2 \quad \text{--- (Using Pythagoras Theorem in } \Delta ORP\text{)} \quad \text{}\\]
Since the radii are equal (\\(OQ = OR\\)), we substitute \\(OR\\) with \\(OQ\\) in the second equation:
\\[PR^2 = OP^2 - OQ^2 = PQ^2 \implies PQ = PR \quad \text{}\\]

- **Deduction:** Since \\(\Delta OQP \cong \Delta ORP\\), the corresponding angles \\(\angle OPQ\\) and \\(\angle OPR\\) are equal (CPCT). Thus, the line segment \\(OP\\) bisects the angle \\(\angle QPR\\) between the two tangents, meaning **the centre of the circle lies on the angle bisector of the tangents**.

---

## **III. Solved Example Problems**

### **Example 1**

**Problem:** Prove that in two concentric circles, the chord of the larger circle, which touches the smaller circle, is bisected at the point of contact.

```xml
<svg width="300" height="260" viewBox="0 0 300 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .outer-c { fill: none; stroke: #0f172a; stroke-width: 2.5; }
    .inner-c { fill: none; stroke: #64748b; stroke-width: 1.8; }
    .chord { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .rad-line { stroke: #ef4444; stroke-width: 2; fill: none; }
    .c-pt { fill: #0f172a; }
    .t-lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
  </style>

  <!-- Concentric Circles -->
  <circle cx="150" cy="130" r="100" class="outer-c"/>
  <circle cx="150" cy="130" r="50" class="inner-c"/>

  <!-- Chord AB touching smaller circle at P(150, 180) -->
  <line x1="63" y1="180" x2="237" y2="180" class="chord"/>
  <line x1="150" y1="130" x2="150" y2="180" class="rad-line"/>

  <!-- Dots -->
  <circle cx="150" cy="130" r="4.5" class="c-pt"/>
  <circle cx="150" cy="180" r="4.5" class="c-pt"/>

  <!-- Labels -->
  <text x="145" y="120" class="t-lbl">O</text>
  <text x="145" y="198" class="t-lbl">P</text>
  <text x="45" y="185" class="t-lbl">A</text>
  <text x="245" y="185" class="t-lbl">B</text>
  <text x="200" y="240" class="t-lbl" style="font-size:12px; fill:#64748b;">C₁ (Outer)</text>
  <text x="200" y="100" class="t-lbl" style="font-size:12px; fill:#64748b;">C₂ (Inner)</text>
</svg>
```

- **Solution:**
  - Let \\(C_1\\) and \\(C_2\\) be two concentric circles with a common centre \\(O\\).
  - Let \\(AB\\) be a chord of the larger circle \\(C_1\\) that touches the smaller circle \\(C_2\\) at the point \\(P\\).
  - Since \\(AB\\) touches \\(C_2\\) at \\(P\\), \\(AB\\) acts as a tangent to the smaller circle \\(C_2\\) with \\(OP\\) as the radius through the point of contact.
  - By **Theorem 4.1**, the radius is perpendicular to the tangent at the point of contact:
    \\[OP \perp AB\\]
  - Now, \\(AB\\) is a chord of the larger circle \\(C_1\\), and \\(OP\\) is a perpendicular segment drawn from the centre \\(O\\) to the chord \\(AB\\).
  - By the standard geometric theorem (the perpendicular drawn from the centre of a circle to a chord bisects the chord), we have:
    \\[AP = BP\\]
  - Hence, the chord is bisected at the point of contact.

---

### **Example 2**

**Problem:** Two tangents \\(TP\\) and \\(TQ\\) are drawn to a circle with centre \\(O\\) from an external point \\(T\\). Prove that:
\\[\angle PTQ = 2\angle OPQ \quad \text{}\\]

```xml
<svg width="400" height="260" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .c-out { fill: #ffffff; stroke: #0f172a; stroke-width: 2.5; }
    .tg-line { stroke: #0284c7; stroke-width: 2.2; fill: none; }
    .ch-line { stroke: #ef4444; stroke-width: 2; fill: none; }
    .rad-line { stroke: #475569; stroke-width: 1.5; fill: none; }
    .co-line { stroke: #8b5cf6; stroke-width: 1.5; stroke-dasharray: 4 4; fill: none; }
    .d-dot { fill: #0f172a; }
    .tx-lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
  </style>

  <!-- Circle centered at (150, 130) with r=70 -->
  <circle cx="150" cy="130" r="70" class="c-out"/>

  <!-- External point T at (340, 130) -->
  <circle cx="340" cy="130" r="4.5" class="d-dot"/>
  <circle cx="176" cy="65" r="4.5" class="d-dot"/>
  <circle cx="176" cy="195" r="4.5" class="d-dot"/>
  <circle cx="150" cy="130" r="4.5" class="d-dot"/>

  <!-- Tangents TP and TQ -->
  <line x1="340" y1="130" x2="176" y2="65" class="tg-line"/>
  <line x1="340" y1="130" x2="176" y2="195" class="tg-line"/>

  <!-- Chord PQ -->
  <line x1="176" y1="65" x2="176" y2="195" class="ch-line"/>

  <!-- Radii OP and OQ -->
  <line x1="150" y1="130" x2="176" y2="65" class="rad-line"/>
  <line x1="150" y1="130" x2="176" y2="195" class="rad-line"/>

  <!-- Line OT -->
  <line x1="150" y1="130" x2="340" y2="130" class="co-line"/>

  <!-- Labels -->
  <text x="130" y="135" class="tx-lbl">O</text>
  <text x="175" y="52" class="tx-lbl">P</text>
  <text x="175" y="215" class="tx-lbl">Q</text>
  <text x="350" y="135" class="tx-lbl">T</text>
</svg>
```

- **Solution:**
  - Let the angle \\(\angle PTQ\\) be denoted as \\(\theta\\).
  - By **Theorem 4.2**, we know that the lengths of tangents from an external point are equal (\\(TP = TQ\\)). Thus, \\(\Delta TPQ\\) forms an **isosceles triangle**.
  - Since the angles opposite to equal sides are equal:
    \\[\angle TPQ = \angle TQP = \frac{1}{2}(180^\circ - \theta) = 90^\circ - \frac{1}{2}\theta \quad \text{--- (Eq. 1)} \quad \text{}\\]
  - By **Theorem 4.1**, the radius \\(OP\\) is perpendicular to the tangent \\(TP\\), giving:
    \\[\angle OPT = 90^\circ \quad \text{--- (Eq. 2)}\\]
  - Now, we calculate the angle \\(\angle OPQ\\) by subtraction:
    \\[\angle OPQ = \angle OPT - \angle TPQ = 90^\circ - \left(90^\circ - \frac{1}{2}\theta\right) = \frac{1}{2}\theta \quad \text{}\\]
  - Substituting \\(\theta = \angle PTQ\\) back into the equation:
    \\[\angle OPQ = \frac{1}{2}\angle PTQ \implies \angle PTQ = 2\angle OPQ \quad \text{}\\]

---

### **Example 3**

**Problem:** \\(PQ\\) is a chord of length \\(8\text{ cm}\\) of a circle of radius \\(5\text{ cm}\\). The tangents at \\(P\\) and \\(Q\\) intersect at an external point \\(T\\). Find the length of the tangent \\(TP\\).

- **Solution:**

#### **Method 1: Using Similar Triangles**

1.  Join the segment \\(OT\\) and let it intersect the chord \\(PQ\\) at point \\(R\\).
2.  \\(\Delta TPQ\\) is an isosceles triangle (\\(TP = TQ\\)), and \\(TO\\) is the angle bisector of \\(\angle PTQ\\).
3.  Therefore, \\(OT \perp PQ\\) and \\(OT\\) bisects the chord \\(PQ\\).
    \\[PR = RQ = \frac{8}{2} = 4\text{ cm} \quad \text{}\\]
4.  In the right-angled triangle \\(\Delta PRO\\), using Pythagoras Theorem:
    \\[OR = \sqrt{OP^2 - PR^2} = \sqrt{5^2 - 4^2} = \sqrt{9} = 3\text{ cm} \quad \text{}\\]
5.  Now, let us examine the angles:
    \\[\angle TPR + \angle RPO = 90^\circ \quad \text{(since } OP \perp TP\text{)} \quad \text{}\\]
    \\[\angle TPR + \angle PTR = 90^\circ \quad \text{(from right-angled } \Delta TRP\text{)} \quad \text{}\\]
    Equating these yields:
    \\[\angle RPO = \angle PTR \quad \text{}\\]
6.  By **AA Similarity**, the right-angled triangle \\(\Delta TRP\\) is similar to the right-angled triangle \\(\Delta PRO\\).
7.  Since similar triangles have proportional corresponding sides:
    \\[\frac{TP}{PO} = \frac{RP}{RO} \implies \frac{TP}{5} = \frac{4}{3} \implies TP = \frac{20}{3}\text{ cm} \approx 6.67\text{ cm} \quad \text{}\\]

#### **Method 2: Using the Pythagoras Theorem**

1.  Let \\(TP = x\text{ cm}\\) and \\(TR = y\text{ cm}\\).
2.  In the right-angled triangle \\(\Delta PRT\\):
    \\[x^2 = y^2 + 16 \quad \text{--- (Eq. 1)}\\]
3.  In the right-angled triangle \\(\Delta OPT\\):
    \\[x^2 + 5^2 = (y + 3)^2 \implies x^2 + 25 = y^2 + 6y + 9 \quad \text{--- (Eq. 2)}\\]
4.  Subtracting Eq. 1 from Eq. 2:
    \\[(x^2 + 25) - x^2 = (y^2 + 6y + 9) - (y^2 + 16) \implies 25 = 6y - 7 \implies 6y = 32 \implies y = \frac{16}{3}\text{ cm} \quad \text{}\\]
5.  Substitute \\(y = \frac{16}{3}\\) back into Eq. 1 to find \\(x\\):
    \\[x^2 = \left(\frac{16}{3}\right)^2 + 16 = \frac{256}{9} + 16 = \frac{256 + 144}{9} = \frac{400}{9} \implies x = \sqrt{\frac{400}{9}} = \frac{20}{3}\text{ cm} \quad \text{}\\]

---

## **IV. Textbook Exercises**

### **EXERCISE 4.1**

1.  How many tangents can a circle have?
2.  **Fill in the blanks:**
    - (i) A tangent to a circle intersects it in \_\_\_\_\_\_ point(s).
    - (ii) A line intersecting a circle in two points is called a \_\_\_\_\_\_.
    - (iii) A circle can have \_\_\_\_\_\_ parallel tangents at the most.
    - (iv) The common point of a tangent to a circle and the circle is called \_\_\_\_\_\_.
3.  A tangent \\(PQ\\) at a point \\(P\\) of a circle of radius \\(5\text{ cm}\\) meets a line through the centre \\(O\\) at a point \\(Q\\) so that \\(OQ = 12\text{ cm}\\). The length of \\(PQ\\) is:
    - (A) \\(12\text{ cm}\\)
    - (B) \\(13\text{ cm}\\)
    - (C) \\(8.5\text{ cm}\\)
    - (D) \\(\sqrt{119}\text{ cm}\\).
4.  Draw a circle and two lines parallel to a given line such that one is a tangent and the other, a secant to the circle.

---

### **EXERCISE 4.2**

- **In Q.1 to 3, choose the correct option and provide full mathematical justification:**

1.  From a point \\(Q\\), the length of the tangent to a circle is \\(24\text{ cm}\\) and the distance of \\(Q\\) from the centre is \\(25\text{ cm}\\). The radius of the circle is:
    - (A) \\(7\text{ cm}\\)
    - (B) \\(12\text{ cm}\\)
    - (C) \\(15\text{ cm}\\)
    - (D) \\(24.5\text{ cm}\\).
2.  In the figure below, if \\(TP\\) and \\(TQ\\) are the two tangents to a circle with centre \\(O\\) so that \\(\angle POQ = 110^\circ\\), then \\(\angle PTQ\\) is equal to:
    - (A) \\(60^\circ\\)
    - (B) \\(70^\circ\\)
    - (C) \\(80^\circ\\)
    - (D) \\(90^\circ\\).
3.  If tangents \\(PA\\) and \\(PB\\) from a point \\(P\\) to a circle with centre \\(O\\) are inclined to each other at an angle of \\(80^\circ\\), then \\(\angle POA\\) is equal to:
    - (A) \\(50^\circ\\)
    - (B) \\(60^\circ\\)
    - (C) \\(70^\circ\\)
    - (D) \\(80^\circ\\).
4.  Prove that the tangents drawn at the ends of a diameter of a circle are parallel.
5.  Prove that the perpendicular at the point of contact to the tangent to a circle passes through the centre.
6.  The length of a tangent from a point \\(A\\) at a distance of \\(5\text{ cm}\\) from the centre of the circle is \\(4\text{ cm}\\). Find the radius of the circle.
7.  Two concentric circles are of radii \\(5\text{ cm}\\) and \\(3\text{ cm}\\). Find the length of the chord of the larger circle which touches the smaller circle.
8.  A quadrilateral \\(ABCD\\) is drawn to circumscribe a circle. Prove that:
    \\[AB + CD = AD + BC \quad \text{}\\]
9.  In the figure below, \\(XY\\) and \\(X'Y'\\) are two parallel tangents to a circle with centre \\(O\\), and another tangent \\(AB\\) with point of contact \\(C\\) intersects \\(XY\\) at \\(A\\) and \\(X'Y'\\) at \\(B\\). Prove that:
    \\[\angle AOB = 90^\circ \quad \text{}\\]
10. Prove that the angle between the two tangents drawn from an external point to a circle is supplementary to the angle subtended by the line-segment joining the points of contact at the centre.
11. Prove that the parallelogram circumscribing a circle is a rhombus.
12. A triangle \\(ABC\\) is drawn to circumscribe a circle of radius \\(4\text{ cm}\\) such that the segments \\(BD\\) and \\(DC\\) into which \\(BC\\) is divided by the point of contact \\(D\\) are of lengths \\(8\text{ cm}\\) and \\(6\text{ cm}\\) respectively. Find the lengths of the sides \\(AB\\) and \\(AC\\).
13. Prove that opposite sides of a quadrilateral circumscribing a circle subtend supplementary angles at the centre of the circle.

---

📐 I can compile these geometric steps, proofs, and vector illustrations into a polished, downloadable PDF formula guide. Would you like me to build it for you?
