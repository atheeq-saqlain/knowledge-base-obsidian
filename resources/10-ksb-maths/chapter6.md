# **Chapter 6: Constructions — Study Guide**

---

## **I. Core Concepts & Geometrical Principles**

In previous chapters, geometric proofs were established through deductive reasoning. To construct geometric figures accurately, we use a straight edge (ruler) and a compass. Each construction step must be backed by a clear mathematical justification using established geometric theorems.

---

### **1. Division of a Line Segment (Construction 6.1)**

To divide a given line segment \\(AB\\) in a specified positive integer ratio \\(m : n\\) (for example, \\(3 : 2\\)), we can use one of two methods:

#### **Method 1: Single Acute Ray with Parallel Lines**

- **Step 1:** Draw any ray \\(AX\\) making an acute angle with the line segment \\(AB\\).
- **Step 2:** Locate \\(m + n\\) points (for \\(3:2\\), locate \\(5\\) points) \\(A_1, A_2, A_3, A_4, A_5\\) on the ray \\(AX\\) such that \\(AA_1 = A_1A_2 = A_2A_3 = A_3A_4 = A_4A_5\\).
- **Step 3:** Join the last point \\(A_5\\) to \\(B\\) (\\(BA_5\\)).
- **Step 4:** Through the point \\(A_3\\) (corresponding to \\(m = 3\\)), draw a line parallel to \\(A_5B\\) (by constructing an angle equal to \\(\angle AA_5B\\)) to intersect \\(AB\\) at point \\(C\\).
- **Result:** Point \\(C\\) divides \\(AB\\) in the ratio \\(3 : 2\\) (\\(AC : CB = 3 : 2\\)).

#### **Geometric Diagram of Line Segment Division:**

```xml
<svg width="400" height="250" viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .line-black { stroke: #0f172a; stroke-width: 2.5; fill: none; }
    .line-blue { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .line-gray { stroke: #64748b; stroke-width: 1.5; fill: none; }
    .point-dot { fill: #0f172a; }
    .point-accent { fill: #ef4444; }
    .label-text { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
  </style>

  <!-- Line Segment AB -->
  <line x1="50" y1="50" x2="320" y2="50" class="line-black"/>

  <!-- Ray AX -->
  <line x1="50" y1="50" x2="250" y2="220" class="line-gray"/>

  <!-- Ray Extension Mark -->
  <path d="M 245,215 L 250,220 L 243,222" stroke="#64748b" stroke-width="1.5" fill="none"/>

  <!-- Parallel lines: A5-B (Gray) and A3-C (Blue) -->
  <line x1="230" y1="200" x2="320" y2="50" class="line-gray" stroke-dasharray="3 3"/>
  <line x1="158" y1="140" x2="212" y2="50" class="line-blue"/>

  <!-- Points on Ray AX -->
  <circle cx="50" cy="50" r="4" class="point-dot"/>
  <circle cx="86" cy="80" r="3.5" class="point-dot"/>
  <circle cx="122" cy="110" r="3.5" class="point-dot"/>
  <circle cx="158" cy="140" r="4.5" class="point-accent"/>
  <circle cx="194" cy="170" r="3.5" class="point-dot"/>
  <circle cx="230" cy="200" r="4.5" class="point-dot"/>

  <!-- Point B and division point C -->
  <circle cx="320" cy="50" r="4" class="point-dot"/>
  <circle cx="212" cy="50" r="4.5" class="point-accent"/>

  <!-- Labels -->
  <text x="35" y="45" class="label-text">A</text>
  <text x="325" y="45" class="label-text">B</text>
  <text x="210" y="40" class="label-text" style="fill:#ef4444;">C</text>
  <text x="255" y="230" class="label-text" style="fill:#64748b;">X</text>

  <!-- Points Labels -->
  <text x="96" y="85" class="label-text" style="font-size: 11px; fill: #64748b;">A₁</text>
  <text x="132" y="115" class="label-text" style="font-size: 11px; fill: #64748b;">A₂</text>
  <text x="168" y="145" class="label-text" style="font-size: 11px; fill: #ef4444;">A₃ (m)</text>
  <text x="204" y="175" class="label-text" style="font-size: 11px; fill: #64748b;">A₄</text>
  <text x="240" y="205" class="label-text" style="font-size: 11px; fill: #64748b;">A₅ (m+n)</text>
</svg>
```

#### **Mathematical Justification:**

In triangle \\(AA_5B\\), the constructed line segment \\(A_3C\\) is parallel to \\(A_5B\\). By the **Basic Proportionality Theorem (Theorem 2.1)**:
\\[\frac{AA_3}{A_3A_5} = \frac{AC}{CB} \quad \text{--- (Eq. 1)} \quad \text{}\\]
By construction, the points on ray \\(AX\\) are equally spaced, so:
\\[\frac{AA_3}{A_3A_5} = \frac{3}{2} \quad \text{--- (Eq. 2)} \quad \text{}\\]
Equating (Eq. 1) and (Eq. 2) yields:
\\[\frac{AC}{CB} = \frac{3}{2} \quad \text{}\\]
Thus, \\(C\\) divides \\(AB\\) internally in the ratio \\(3 : 2\\).

---

#### **Method 2: Parallel Rays (Alternative Method)**

- **Step 1:** Draw any ray \\(AX\\) making an acute angle with \\(AB\\).
- **Step 2:** Draw a ray \\(BY\\) parallel to \\(AX\\) by making angle \\(\angle ABY\\) equal to \\(\angle BAX\\).
- **Step 3:** Locate \\(m\\) points (\\(A_1, A_2, A_3\\)) on \\(AX\\) and \\(n\\) points (\\(B_1, B_2\\)) on \\(BY\\) such that the spacing is equal (\\(AA_1 = A_1A_2 = A_2A_3 = BB_1 = B_1B_2\\)).
- **Step 4:** Join \\(A_3B_2\\) to intersect \\(AB\\) at point \\(C\\).
- **Justification:** In triangles \\(\Delta AA_3C\\) and \\(\Delta BB_2C\\), we have vertical opposite angles \\(\angle ACA_3 = \angle BCB_2\\) and alternate interior angles \\(\angle A_3AC = \angle B_2BC\\). Thus, by **AA Similarity**, \\(\Delta AA_3C \sim \Delta BB_2C\\). Their corresponding sides are proportional:
  \\[\frac{AC}{BC} = \frac{AA_3}{BB_2} = \frac{3}{2} \quad \text{}\\]

---

### **2. Construction of Similar Triangles (Construction 6.2)**

This construction produces a triangle similar to a given triangle such that its sides are in a ratio defined by a **scale factor** \\(\frac{m}{n}\\). Two cases exist depending on whether the scale factor is less than or greater than \\(1\\):

#### **Case A: Scale Factor \\(< 1\\) (e.g., \\(\frac{3}{4}\\))**

The constructed triangle is smaller than the original triangle.

- **Step 1:** Draw a ray \\(BX\\) making an acute angle with side \\(BC\\) on the side opposite to vertex \\(A\\).
- **Step 2:** Locate \\(4\\) points (since \\(4 > 3\\) in \\(\frac{3}{4}\\)) on \\(BX\\) such that \\(BB_1 = B_1B_2 = B_2B_3 = B_3B_4\\).
- **Step 3:** Join the denominator point \\(B_4\\) to \\(C\\) (\\(B_4C\\)).
- **Step 4:** Draw a line through the numerator point \\(B_3\\) parallel to \\(B_4C\\) to intersect \\(BC\\) at point \\(C'\\).
- **Step 5:** Draw a line through \\(C'\\) parallel to \\(CA\\) to intersect side \\(BA\\) at \\(A'\\).
- **Result:** \\(\Delta A'BC'\\) is the required similar triangle with sides equal to \\(\frac{3}{4}\\) of \\(\Delta ABC\\).

#### **Geometric Diagram of Similar Triangle Construction (Scale Factor < 1):**

```xml
<svg width="400" height="280" viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .tri-original { fill: none; stroke: #0f172a; stroke-width: 2.5; }
    .tri-similar { fill: #bae6fd; fill-opacity: 0.3; stroke: #0284c7; stroke-width: 2.5; }
    .line-construction { stroke: #64748b; stroke-width: 1.5; }
    .line-parallel { stroke: #0284c7; stroke-width: 2; fill: none; }
    .lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
    .pt-construction { fill: #64748b; }
    .pt-accent { fill: #ef4444; }
  </style>

  <!-- Ray BX -->
  <line x1="50" y1="180" x2="250" y2="260" class="line-construction"/>
  <path d="M 245,255 L 250,260 L 243,262" stroke="#64748b" stroke-width="1.5" fill="none"/>

  <!-- Construction lines -->
  <!-- B4-C -->
  <line x1="210" y1="260" x2="320" y2="180" class="line-construction" stroke-dasharray="3 3"/>
  <!-- B3-C' -->
  <line x1="170" y1="240" x2="252.5" y2="180" class="line-parallel"/>

  <!-- Triangles -->
  <!-- Original ABC -->
  <polygon points="150,50 50,180 320,180" class="tri-original"/>
  <!-- Similar A'BC' -->
  <polygon points="125,82.5 50,180 252.5,180" class="tri-similar"/>

  <!-- Points on Ray BX -->
  <circle cx="90" cy="200" r="3.5" class="pt-construction"/>
  <circle cx="130" cy="220" r="3.5" class="pt-construction"/>
  <circle cx="170" cy="240" r="4.5" class="pt-accent"/>
  <circle cx="210" cy="260" r="3.5" class="pt-construction"/>

  <!-- Special Vertex Dots -->
  <circle cx="125" cy="82.5" r="4.5" class="pt-accent"/>
  <circle cx="252.5" cy="180" r="4.5" class="pt-accent"/>

  <!-- Labels -->
  <text x="145" y="40" class="lbl">A</text>
  <text x="110" y="78" class="lbl" style="fill:#ef4444;">A'</text>
  <text x="35" y="195" class="lbl">B</text>
  <text x="325" y="195" class="lbl">C</text>
  <text x="245" y="172" class="lbl" style="fill:#ef4444;">C'</text>
  <text x="255" y="270" class="lbl" style="fill:#64748b;">X</text>

  <!-- Ray Point Labels -->
  <text x="100" y="205" class="lbl" style="font-size: 11px; fill: #64748b;">B₁</text>
  <text x="140" y="225" class="lbl" style="font-size: 11px; fill: #64748b;">B₂</text>
  <text x="180" y="245" class="lbl" style="font-size: 11px; fill: #ef4444;">B₃</text>
  <text x="220" y="265" class="lbl" style="font-size: 11px; fill: #64748b;">B₄</text>
</svg>
```

---

#### **Case B: Scale Factor \\(> 1\\) (e.g., \\(\frac{5}{3}\\))**

The constructed triangle is larger than the original triangle.

- **Step 1:** Draw a ray \\(BX\\) making an acute angle with side \\(BC\\) on the side opposite to vertex \\(A\\).
- **Step 2:** Locate \\(5\\) points (since \\(5 > 3\\) in \\(\frac{5}{3}\\)) such that \\(BB_1 = B_1B_2 = B_2B_3 = B_3B_4 = B_4B_5\\).
- **Step 3:** Join the denominator point \\(B_3\\) to \\(C\\) (\\(B_3C\\)).
- **Step 4:** Draw a line through the numerator point \\(B_5\\) parallel to \\(B_3C\\) to intersect the extended line segment \\(BC\\) at point \\(C'\\).
- **Step 5:** Draw a line through \\(C'\\) parallel to \\(CA\\) to intersect the extended line segment \\(BA\\) at \\(A'\\).
- **Result:** \\(\Delta A'BC'\\) is the required similar triangle with sides equal to \\(\frac{5}{3}\\) of \\(\Delta ABC\\).

---

### **3. Construction of Tangents to a Circle (Construction 6.3)**

Drawing a tangent to a circle at a point lying _on_ the circle is trivial (draw a radius and construct a line perpendicular to it through that point). However, if the point \\(P\\) lies _outside_ the circle, we can construct exactly two equal tangents:

- **Step 1:** Join the external point \\(P\\) to the centre of the circle \\(O\\), and bisect the segment \\(OP\\) to find its midpoint \\(M\\).
- **Step 2:** Taking \\(M\\) as the centre and \\(MO\\) (or \\(MP\\)) as the radius, draw a helper circle.
- **Step 3:** Let this helper circle intersect the original circle at two points, \\(Q\\) and \\(R\\).
- **Step 4:** Join \\(PQ\\) and \\(PR\\).
- **Result:** \\(PQ\\) and \\(PR\\) are the two required tangents.

#### **Geometric Diagram of Tangents Construction:**

```xml
<svg width="400" height="260" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .orig-circle { fill: none; stroke: #0f172a; stroke-width: 2.5; }
    .helper-circle { fill: none; stroke: #94a3b8; stroke-width: 1.5; stroke-dasharray: 4 4; }
    .tangent-line { stroke: #10b981; stroke-width: 2.5; fill: none; }
    .segment-line { stroke: #475569; stroke-width: 1.5; fill: none; }
    .pt-black { fill: #0f172a; }
    .pt-green { fill: #10b981; }
    .txt { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
  </style>

  <!-- Original Circle centered at O(130, 130) with r=60 -->
  <circle cx="130" cy="130" r="60" class="orig-circle"/>

  <!-- Helper Circle centered at M(220, 130) with r=90 -->
  <circle cx="220" cy="130" r="90" class="helper-circle"/>

  <!-- Segment OP and bisector line -->
  <line x1="130" y1="130" x2="310" y2="130" class="segment-line"/>
  <line x1="220" y1="30" x2="220" y2="230" class="segment-line" stroke-dasharray="3 3"/>

  <!-- Tangents PQ and PR -->
  <line x1="310" y1="130" x2="150" y2="73.4" class="tangent-line"/>
  <line x1="310" y1="130" x2="150" y2="186.6" class="tangent-line"/>

  <!-- Radii OQ and OR -->
  <line x1="130" y1="130" x2="150" y2="73.4" class="segment-line" stroke-dasharray="2 2"/>
  <line x1="130" y1="130" x2="150" y2="186.6" class="segment-line" stroke-dasharray="2 2"/>

  <!-- Dots -->
  <circle cx="130" cy="130" r="4.5" class="pt-black"/>
  <circle cx="310" cy="130" r="4.5" class="pt-black"/>
  <circle cx="220" cy="130" r="4" class="pt-black"/>
  <circle cx="150" cy="73.4" r="4.5" class="pt-green"/>
  <circle cx="150" cy="186.6" r="4.5" class="pt-green"/>

  <!-- Labels -->
  <text x="110" y="135" class="txt">O</text>
  <text x="320" y="135" class="txt">P</text>
  <text x="212" y="148" class="txt" style="fill:#64748b;">M</text>
  <text x="145" y="60" class="txt" style="fill:#10b981;">Q</text>
  <text x="145" y="205" class="txt" style="fill:#10b981;">R</text>
</svg>
```

#### **Mathematical Justification:**

If we join \\(OQ\\), the angle \\(\angle PQO\\) is inscribed within a semicircle of the helper circle.
\\[\angle PQO = 90^\circ \quad \text{(Angle in a semicircle is a right angle)} \quad \text{}\\]
Since \\(OQ\\) is the radius of the original circle, the line \\(PQ\\) must be perpendicular to the radius through its point of contact.
Thus, by **Theorem 4.1**, \\(PQ\\) is a tangent to the circle. Similarly, \\(PR\\) is also a tangent.

---

## **II. Example Problems (with Step-by-Step Solutions)**

### **Example 1**

**Problem:** Construct a triangle similar to a given triangle \\(ABC\\) with its sides equal to \\(\frac{3}{4}\\) of the corresponding sides of the triangle \\(ABC\\) (scale factor \\(\frac{3}{4}\\)).

- **Solution:**
  1.  Draw a triangle \\(ABC\\) of arbitrary dimensions.
  2.  Draw a ray \\(BX\\) making an acute angle with side \\(BC\\) opposite to vertex \\(A\\).
  3.  Mark \\(4\\) equidistant points \\(B_1, B_2, B_3, B_4\\) on \\(BX\\).
  4.  Join \\(B_4\\) (the denominator) to \\(C\\).
  5.  Through \\(B_3\\) (the numerator), construct a line parallel to \\(B_4C\\) to intersect \\(BC\\) at point \\(C'\\).
  6.  Through \\(C'\\), construct a line parallel to \\(CA\\) to intersect \\(BA\\) at \\(A'\\).
  7.  \\(\Delta A'BC'\\) is the required triangle.

---

### **Example 2**

**Problem:** Construct a triangle similar to a given triangle \\(ABC\\) with its sides equal to \\(\frac{5}{3}\\) of the corresponding sides of the triangle \\(ABC\\) (scale factor \\(\frac{5}{3}\\)).

- **Solution:**
  1.  Draw a triangle \\(ABC\\) of arbitrary dimensions.
  2.  Draw a ray \\(BX\\) making an acute angle with side \\(BC\\) opposite to vertex \\(A\\).
  3.  Mark \\(5\\) equidistant points \\(B_1, B_2, B_3, B_4, B_5\\) on \\(BX\\).
  4.  Join \\(B_3\\) (the denominator) to \\(C\\).
  5.  Through \\(B_5\\) (the numerator), construct a line parallel to \\(B_3C\\) to intersect the extended side \\(BC\\) at point \\(C'\\).
  6.  Through \\(C'\\), construct a line parallel to \\(CA\\) to intersect the extended side \\(BA\\) at \\(A'\\).
  7.  \\(\Delta A'BC'\\) is the required triangle.

---

## **III. Exercise Questions**

### **EXERCISE 6.1**

_Provide mathematical justifications for each construction._

1.  Draw a line segment of length \\(7.6\text{ cm}\\) and divide it in the ratio \\(5 : 8\\). Measure the two parts.
2.  Construct a triangle of sides \\(4\text{ cm}\\), \\(5\text{ cm}\\) and \\(6\text{ cm}\\) and then a triangle similar to it whose sides are \\(\frac{2}{3}\\) of the corresponding sides of the first triangle.
3.  Construct a triangle with sides \\(5\text{ cm}\\), \\(6\text{ cm}\\) and \\(7\text{ cm}\\) and then another triangle whose sides are \\(\frac{7}{5}\\) of the corresponding sides of the first triangle.
4.  Construct an isosceles triangle whose base is \\(8\text{ cm}\\) and altitude \\(4\text{ cm}\\) and then another triangle whose sides are \\(1\frac{1}{2}\\) times (i.e., \\(\frac{3}{2}\\) times) the corresponding sides of the isosceles triangle.
5.  Draw a triangle \\(ABC\\) with side \\(BC = 6\text{ cm}\\), \\(AB = 5\text{ cm}\\) and \\(\angle ABC = 60^\circ\\). Then construct a triangle whose sides are \\(\frac{3}{4}\\) of the corresponding sides of the triangle \\(ABC\\).
6.  Draw a triangle \\(ABC\\) with side \\(BC = 7\text{ cm}\\), \\(\angle B = 45^\circ\\), \\(\angle A = 105^\circ\\). Then, construct a triangle whose sides are \\(\frac{4}{3}\\) times the corresponding sides of \\(\Delta ABC\\).
7.  Draw a right triangle in which the sides (other than hypotenuse) are of lengths \\(4\text{ cm}\\) and \\(3\text{ cm}\\). Then construct another triangle whose sides are \\(\frac{5}{3}\\) times the corresponding sides of the given triangle.

---

### **EXERCISE 6.2**

_Provide mathematical justifications for each construction._

1.  Draw a circle of radius \\(6\text{ cm}\\). From a point \\(10\text{ cm}\\) away from its centre, construct the pair of tangents to the circle and measure their lengths.
2.  Construct a tangent to a circle of radius \\(4\text{ cm}\\) from a point on the concentric circle of radius \\(6\text{ cm}\\) and measure its length. Also verify the measurement by actual calculation.
3.  Draw a circle of radius \\(3\text{ cm}\\). Take two points \\(P\\) and \\(Q\\) on one of its extended diameters each at a distance of \\(7\text{ cm}\\) from its centre. Draw tangents to the circle from these two points \\(P\\) and \\(Q\\).
4.  Draw a pair of tangents to a circle of radius \\(5\text{ cm}\\) which are inclined to each other at an angle of \\(60^\circ\\).
5.  Draw a line segment \\(AB\\) of length \\(8\text{ cm}\\). Taking \\(A\\) as centre, draw a circle of radius \\(4\text{ cm}\\) and taking \\(B\\) as centre, draw another circle of radius \\(3\text{ cm}\\). Construct tangents to each circle from the centre of the other circle.
6.  Let \\(ABC\\) be a right triangle in which \\(AB = 6\text{ cm}\\), \\(BC = 8\text{ cm}\\) and \\(\angle B = 90^\circ\\). \\(BD\\) is the perpendicular from \\(B\\) on \\(AC\\). The circle through \\(B\\), \\(C\\), \\(D\\) is drawn. Construct the tangents from \\(A\\) to this circle.
7.  Draw a circle with the help of a bangle. Take a point outside the circle. Construct the pair of tangents from this point to the circle.

---

📊 **I can update your master syllabus file with these specific Construction summaries or formulate a custom geometry test sheet for you. What would you like to do next?**
