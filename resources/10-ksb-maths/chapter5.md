# **Chapter 5: Areas Related to Circles — Study Guide**

---

## **I. Core Concepts & Geometrical Principles**

### **1. Perimeter (Circumference) of a Circle**

The distance covered by travelling once around a circle is called its **perimeter** or **circumference**.

- **The Constant Ratio (\\(\pi\\)):** The circumference of any circle bears a constant ratio with its diameter. This constant ratio is represented by the Greek letter **\\(\pi\\)** (pi):
  \\[\frac{\text{Circumference}}{\text{Diameter}} = \pi \implies \text{Circumference} = \pi \times d = 2\pi r\\]
  where \\(r\\) is the radius of the circle.
- **Historical Context of \\(\pi\\):**
  - The ancient Indian mathematician **Aryabhata** (476–550 C.E.) calculated an approximate value of \\(\pi \approx \frac{62832}{20000} \approx 3.1416\\).
  - The Indian mathematical genius **Srinivasa Ramanujan** (1887–1920) formulated mathematical identities that allowed modern calculators to compute \\(\pi\\) correct to millions of decimal places.
  - Because \\(\pi\\) is an **irrational number**, its decimal expansion is non-terminating and non-recurring. For practical purposes, we take:
    \\[\pi \approx \frac{22}{7} \quad \text{or} \quad \pi \approx 3.14\\]

---

### **2. Area of a Circle**

The area of a circular region of radius \\(r\\) is **\\(\pi r^2\\)**.

- **Visual Derivation:** By cutting a circle into \\(n\\) numerous small sectors and rearranging them, the shape resembles a rectangle of length \\(\frac{1}{2} \times 2\pi r = \pi r\\) and breadth \\(r\\). Thus, the area is:
  \\[\text{Area} = \text{length} \times \text{breadth} = (\pi r) \times r = \pi r^2\\]

---

### **3. Sector of a Circle**

A **sector** is the portion (or part) of a circular region enclosed by two radii and the corresponding arc connecting their endpoints.

- **Minor Sector:** The sector corresponding to the smaller arc (central angle \\(\theta < 180^\circ\\)).
- **Major Sector:** The sector corresponding to the larger arc (central angle \\(360^\circ - \theta\\)).
- **Area of a Sector:**
  \\[\text{Area of Minor Sector} = \frac{\theta}{360^\circ} \times \pi r^2\\]
- **Length of an Arc of a Sector:**
  \\[\text{Length of Arc } (l) = \frac{\theta}{360^\circ} \times 2\pi r\\]

#### **Geometric Setup of Sectors and Segments:**

```xml
<svg width="550" height="240" viewBox="0 0 550 240" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .c-edge { fill: #ffffff; stroke: #0f172a; stroke-width: 2; }
    .sec-shade { fill: #bae6fd; stroke: #0284c7; stroke-width: 2.5; }
    .seg-shade { fill: #bbf7d0; stroke: #16a34a; stroke-width: 2.5; }
    .line-c { stroke: #64748b; stroke-width: 1.5; }
    .dot { fill: #0f172a; }
    .lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #1e293b; }
    .lbl-b { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; text-anchor: middle; }
  </style>

  <!-- Panel 1: Sector -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="240" height="200" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <!-- Unshaded Circle -->
    <circle cx="120" cy="100" r="70" class="c-edge"/>
    <!-- Shaded Sector -->
    <path d="M 120,100 L 66,145 A 70,70 0 0,0 174,145 Z" class="sec-shade"/>
    <!-- Labels -->
    <circle cx="120" cy="100" r="4.5" class="dot"/>
    <text x="120" y="90" class="lbl-b">O</text>
    <text x="50" y="152" class="lbl-b">A</text>
    <text x="190" y="152" class="lbl-b">B</text>
    <text x="120" y="165" class="lbl-b" style="fill:#0284c7;">P</text>
    <text x="120" y="45" class="lbl-b" style="fill:#64748b;">Q</text>
    <text x="120" y="125" class="lbl" style="font-size:11px; fill:#0369a1; text-anchor:middle;">Minor Sector</text>
    <text x="120" y="218" class="lbl-b">1. Sector of a Circle</text>
  </g>

  <!-- Panel 2: Segment -->
  <g transform="translate(290, 10)">
    <rect x="0" y="0" width="240" height="200" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <!-- Unshaded Circle -->
    <circle cx="120" cy="100" r="70" class="c-edge"/>
    <!-- Shaded Segment -->
    <path d="M 66,145 A 70,70 0 0,0 174,145 Z" class="seg-shade"/>
    <!-- Chord Line -->
    <line x1="66" y1="145" x2="174" y2="145" class="line-c" stroke-width="2.5" stroke="#16a34a"/>
    <!-- Radii lines -->
    <line x1="120" y1="100" x2="66" y2="145" class="line-c" stroke-dasharray="3 3"/>
    <line x1="120" y1="100" x2="174" y2="145" class="line-c" stroke-dasharray="3 3"/>
    <!-- Labels -->
    <circle cx="120" cy="100" r="4.5" class="dot"/>
    <text x="120" y="90" class="lbl-b">O</text>
    <text x="50" y="152" class="lbl-b">A</text>
    <text x="190" y="152" class="lbl-b">B</text>
    <text x="120" y="165" class="lbl-b" style="fill:#16a34a;">P</text>
    <text x="120" y="45" class="lbl-b" style="fill:#64748b;">Q</text>
    <text x="120" y="155" class="lbl" style="font-size:11px; fill:#15803d; text-anchor:middle;">Minor Segment</text>
    <text x="120" y="218" class="lbl-b">2. Segment of a Circle</text>
  </g>
</svg>
```

---

### **4. Segment of a Circle**

A **segment** is the portion of a circular region enclosed between a chord and its corresponding arc.

- **Minor Segment:** The region bounded by the chord and the minor arc.
- **Major Segment:** The region bounded by the chord and the major arc.
- **Area of a Segment:**
  The area of the minor segment \\(APB\\) is calculated by subtracting the area of the central triangle \\(\Delta OAB\\) from the area of the corresponding sector \\(OAPB\\):
  \\[\text{Area of Segment } APB = \text{Area of Sector } OAPB - \text{Area of } \Delta OAB\\]
  \\[\text{Area of Segment } APB = \frac{\theta}{360^\circ} \times \pi r^2 - \text{Area of } \Delta OAB\\]
- **Calculating the Area of the Central Triangle (\\(\Delta OAB\\)):**
  If the central angle is \\(\theta\\) and the radius is \\(r\\):
  - For \\(\theta = 60^\circ\\), \\(\Delta OAB\\) is equilateral: \\(\text{Area} = \frac{\sqrt{3}}{4}r^2\\).
  - For \\(\theta = 90^\circ\\), \\(\Delta OAB\\) is a right-angled isosceles triangle: \\(\text{Area} = \frac{1}{2}r^2\\).
  - For any general angle \\(\theta\\) (using trigonometry): \\(\text{Area} = \frac{1}{2}r^2 \sin\theta\\).

---

## **II. Example Problems (with Step-by-Step Solutions)**

### **Example 1**

**Problem:** The cost of fencing a circular field at the rate of ₹24 per metre is ₹5280. The field is to be ploughed at the rate of ₹0.50 per \\(m^2\\). Find the cost of ploughing the field (Take \\(\pi = \frac{22}{7}\\)).

- **Solution:**
  - First, determine the perimeter (circumference) of the circular field:
    \\[\text{Circumference} = \frac{\text{Total Cost of Fencing}}{\text{Rate of Fencing}} = \frac{5280}{24} = 220\text{ metres}\\]
  - Find the radius (\\(r\\)) of the field using \\(2\pi r = 220\\):
    \\[2 \times \frac{22}{7} \times r = 220 \implies r = \frac{220 \times 7}{44} = 35\text{ m}\\]
  - Now, calculate the area of the circular field:
    \\[\text{Area} = \pi r^2 = \frac{22}{7} \times 35 \times 35 = 22 \times 5 \times 35 = 3850\text{ } m^2\\]
  - Calculate the total cost of ploughing the field:
    \\[\text{Cost} = \text{Area} \times \text{Rate of Ploughing} = 3850 \times 0.50 = \text{₹}1925\\]

---

### **Example 2**

**Problem:** Find the area of the sector of a circle with radius 4 cm and of angle \\(30^\circ\\). Also, find the area of the corresponding major sector (Use \\(\pi = 3.14\\)).

- **Solution:**
  - **Area of Minor Sector (\\(OAPB\\)):**
    \\[\text{Area} = \frac{\theta}{360^\circ} \times \pi r^2 = \frac{30}{360} \times 3.14 \times 4^2 = \frac{1}{12} \times 3.14 \times 16 \approx 4.19\text{ } cm^2\\]
  - **Area of Major Sector (\\(OAQB\\)):**
    \\[\text{Area of Major Sector} = \pi r^2 - \text{Area of Minor Sector} = (3.14 \times 16) - 4.19 = 50.24 - 4.19 = 46.05\text{ } cm^2\\]
    _Alternative Method:_
    \\[\text{Area} = \frac{360^\circ - \theta}{360^\circ} \times \pi r^2 = \frac{330}{360} \times 3.14 \times 16 \approx 46.1\text{ } cm^2\text{ (approx.)}\\]

---

### **Example 3**

**Problem:** Find the area of the segment \\(AYB\\) shown below, if the radius of the circle is 21 cm and \\(\angle AOB = 120^\circ\\) (Use \\(\pi = \frac{22}{7}\\)).

- **Solution:**
  - Calculate the **Area of Sector (\\(OAYB\\))**:
    \\[\text{Area of Sector} = \frac{120}{360} \times \frac{22}{7} \times 21 \times 21 = 462\text{ } cm^2\\]
  - To find the **Area of \\(\Delta OAB\\)**, draw perpendicular \\(OM \perp AB\\). Since \\(OA=OB=21\text{ cm}\\), \\(\Delta AMO \cong \Delta BMO\\).
    - Hence, \\(M\\) is the midpoint of \\(AB\\) and \\(\angle AOM = \angle BOM = 60^\circ\\).
    - In right \\(\Delta OMA\\):
      \\[OM = OA \cos 60^\circ = 21 \times \frac{1}{2} = 10.5\text{ cm}\\]
      \\[AM = OA \sin 60^\circ = 21 \times \frac{\sqrt{3}}{2}\text{ cm}\\]
      \\[AB = 2 \times AM = 21\sqrt{3}\text{ cm}\\]
    - Calculate the area of \\(\Delta OAB\\):
      \\[\text{Area} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 21\sqrt{3} \times \frac{21}{2} = \frac{441}{4}\sqrt{3}\text{ } cm^2\\]
  - Subtract to find the **Area of Segment \\(AYB\\)**:
    \\[\text{Area of Segment} = \text{Area of Sector} - \text{Area of Triangle} = \left(462 - \frac{441}{4}\sqrt{3}\right) = \frac{21}{4}(88 - 21\sqrt{3})\text{ } cm^2\\]

---

### **Example 4**

**Problem:** Two circular flower beds are placed on opposite sides of a square lawn \\(ABCD\\) of side 56 m. If the centre of each circular flower bed is the point of intersection \\(O\\) of the diagonals of the square lawn, find the sum of the areas of the lawn and the flower beds.

- **Solution:**
  - Let the side of the square lawn be \\(s = 56\text{ m}\\) and the intersection of the diagonals be \\(O\\).
  - Let \\(OA = OB = r\\) (radius of the circular sector).
  - Using Pythagoras theorem in right-angled \\(\Delta AOB\\) (since diagonals of a square bisect each other at \\(90^\circ\\)):
    \\[r^2 + r^2 = 56^2 \implies 2r^2 = 3136 \implies r^2 = 1568\\]
  - The total area of the entire design is the sum of the areas of sectors \\(OAB\\) and \\(ODC\\) and triangles \\(\Delta OAD\\) and \\(\Delta OBC\\):
    \\[\text{Area of Sector } OAB = \frac{90}{360} \times \pi r^2 = \frac{1}{4} \times \frac{22}{7} \times 1568 = 1232\text{ } m^2\\]
    \\[\text{Area of Sector } ODC = 1232\text{ } m^2\\]
    \\[\text{Area of } \Delta OAD = \frac{1}{2} \times r^2 = \frac{1568}{2} = 784\text{ } m^2\\]
    \\[\text{Area of } \Delta OBC = 784\text{ } m^2\\]
  - Total Area of Lawn & Beds:
    \\[\text{Total Area} = 1232 + 1232 + 784 + 784 = 4032\text{ } m^2\\]

---

### **Example 5**

**Problem:** Find the area of the shaded region where \\(ABCD\\) is a square of side 14 cm enclosing four identical inscribed circles.

```xml
<svg width="280" height="240" viewBox="0 0 280 240" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <!-- Inscribed circles in a square -->
  <rect x="50" y="30" width="160" height="160" fill="#bae6fd" stroke="#0f172a" stroke-width="2.5"/>
  <!-- 4 Congruent Circles -->
  <circle cx="90" cy="70" r="40" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
  <circle cx="170" cy="70" r="40" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
  <circle cx="90" cy="150" r="40" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
  <circle cx="170" cy="150" r="40" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
  <!-- Labels -->
  <text x="40" y="25" font-family="Segoe UI, Arial" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="215" y="25" font-family="Segoe UI, Arial" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="215" y="205" font-family="Segoe UI, Arial" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="40" y="205" font-family="Segoe UI, Arial" font-size="14" font-weight="bold" fill="#0f172a">D</text>
  <text x="130" y="222" font-family="Segoe UI, Arial" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Side = 14 cm</text>
</svg>
```

- **Solution:**
  - Calculate the **Area of the Square (\\(ABCD\\))**:
    \\[\text{Area of Square} = 14 \times 14 = 196\text{ } cm^2\\]
  - Since the four circles are congruent and touch each other, the diameter of each circle is half the side of the square:
    \\[\text{Diameter} = \frac{14}{2} = 7\text{ cm} \implies \text{Radius } (r) = 3.5\text{ cm}\\]
  - Calculate the **Area of the Four Circles**:
    \\[\text{Area of One Circle} = \pi r^2 = \frac{22}{7} \times 3.5 \times 3.5 = 38.5\text{ } cm^2\\]
    \\[\text{Area of Four Circles} = 4 \times 38.5 = 154\text{ } cm^2\\]
  - Subtract the areas:
    \\[\text{Area of Shaded Region} = \text{Area of Square} - \text{Area of 4 Circles} = 196 - 154 = 42\text{ } cm^2\\]

---

### **Example 6**

**Problem:** Find the area of the shaded design shown below, where \\(ABCD\\) is a square of side 10 cm and four identical semicircles are drawn with each side of the square acting as a diameter (Use \\(\pi = 3.14\\)).

```xml
<svg width="280" height="240" viewBox="0 0 280 240" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <!-- Semicircles in a square forming a flower design -->
  <rect x="50" y="30" width="160" height="160" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
  <!-- Overlapping Semicircles using path (Fill opacity overlaps to shade petals) -->
  <path d="M 50,30 A 80,80 0 0,0 210,30 Z" fill="#8b5cf6" fill-opacity="0.25" stroke="#8b5cf6" stroke-width="2"/>
  <path d="M 210,190 A 80,80 0 0,0 50,190 Z" fill="#8b5cf6" fill-opacity="0.25" stroke="#8b5cf6" stroke-width="2"/>
  <path d="M 50,190 A 80,80 0 0,0 50,30 Z" fill="#8b5cf6" fill-opacity="0.25" stroke="#8b5cf6" stroke-width="2"/>
  <path d="M 210,30 A 80,80 0 0,0 210,190 Z" fill="#8b5cf6" fill-opacity="0.25" stroke="#8b5cf6" stroke-width="2"/>
  <!-- Labels -->
  <text x="40" y="25" font-family="Segoe UI, Arial" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="215" y="25" font-family="Segoe UI, Arial" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="215" y="205" font-family="Segoe UI, Arial" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="40" y="205" font-family="Segoe UI, Arial" font-size="14" font-weight="bold" fill="#0f172a">D</text>
  <text x="130" y="115" font-family="Segoe UI, Arial" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Petal Design</text>
</svg>
```

- **Solution:**
  - Let the four unshaded regions at the corners of the square be labeled as **I, II, III, and IV**.
  - The combined area of region **I and III** is the area of the square minus the area of two semicircles (of radius \\(5\text{ cm}\\)):
    \\[\text{Area of I} + \text{Area of III} = \text{Area of Square} - \text{Area of 1 Full Circle}\\]
    \\[\text{Area of I} + \text{Area of III} = (10 \times 10) - (3.14 \times 5^2) = 100 - 78.5 = 21.5\text{ } cm^2\\]
  - Similarly, the combined area of region **II and IV** is:
    \\[\text{Area of II} + \text{Area of IV} = 21.5\text{ } cm^2\\]
  - Subtract the unshaded regions from the square to find the **Area of the Shaded Design**:
    \\[\text{Area of Shaded Design} = \text{Area of Square} - (\text{Area of I + II + III + IV})\\]
    \\[\text{Area of Shaded Design} = 100 - (21.5 + 21.5) = 100 - 43 = 57\text{ } cm^2\\]

---

## **III. Exercises**

### **EXERCISE 5.1**

1.  The radii of two circles are 19 cm and 9 cm respectively. Find the radius of the circle which has a circumference equal to the sum of the circumferences of these two circles.
2.  The radii of two circles are 8 cm and 6 cm respectively. Find the radius of the circle having an area equal to the sum of the areas of these two circles.
3.  **Archery Target:** An archery target is marked with five concentric scoring regions from the centre outwards as **Gold, Red, Blue, Black, and White**. The diameter of the Gold region is 21 cm and each of the other outer bands is 10.5 cm wide. Find the area of each of the five scoring regions.

```xml
<svg width="340" height="260" viewBox="0 0 340 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <!-- Archery Target -->
  <g transform="translate(170, 130)">
    <!-- White Ring -->
    <circle cx="0" cy="0" r="110" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
    <text x="0" y="-95" font-family="Segoe UI, Arial" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">WHITE</text>
    <!-- Black Ring -->
    <circle cx="0" cy="0" r="88" fill="#1e293b" stroke="#ffffff" stroke-width="1"/>
    <text x="0" y="-73" font-family="Segoe UI, Arial" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">BLACK</text>
    <!-- Blue Ring -->
    <circle cx="0" cy="0" r="66" fill="#0284c7" stroke="#ffffff" stroke-width="1"/>
    <text x="0" y="-51" font-family="Segoe UI, Arial" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">BLUE</text>
    <!-- Red Ring -->
    <circle cx="0" cy="0" r="44" fill="#ef4444" stroke="#ffffff" stroke-width="1"/>
    <text x="0" y="-29" font-family="Segoe UI, Arial" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">RED</text>
    <!-- Gold Circle -->
    <circle cx="0" cy="0" r="22" fill="#f59e0b" stroke="#ffffff" stroke-width="1"/>
    <text x="0" y="4" font-family="Segoe UI, Arial" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">GOLD</text>
  </g>
</svg>
```

4.  The wheels of a car have a diameter of 80 cm each. How many complete revolutions does each wheel make in 10 minutes when the car is travelling at a speed of 66 km per hour?
5.  If the perimeter and the area of a circle are numerically equal, then the radius of the circle is:
    - (A) 2 units \quad (B) \\(\pi\\) units \quad (C) 4 units \quad (D) 7 units

---

### **EXERCISE 5.2**

1.  Find the area of a sector of a circle with a radius of 6 cm if the angle of the sector is \\(60^\circ\\).
2.  Find the area of a quadrant of a circle whose circumference is 22 cm.
3.  The length of the minute hand of a clock is 14 cm. Find the area swept by the minute hand in 5 minutes.
4.  A chord of a circle of radius 10 cm subtends a right angle at the centre. Find the area of the corresponding:
    - (i) minor segment
    - (ii) major sector (Use \\(\pi = 3.14\\))
5.  In a circle of radius 21 cm, an arc subtends an angle of \\(60^\circ\\) at the centre. Find:
    - (i) the length of the arc
    - (ii) the area of the sector formed by the arc
    - (iii) the area of the segment formed by the corresponding chord
6.  A chord of a circle of radius 15 cm subtends an angle of \\(60^\circ\\) at the centre. Find the areas of the corresponding minor and major segments of the circle (Use \\(\pi = 3.14\\) and \\(\sqrt{3} = 1.73\\)).
7.  A chord of a circle of radius 12 cm subtends an angle of \\(120^\circ\\) at the centre. Find the area of the corresponding segment of the circle (Use \\(\pi = 3.14\\) and \\(\sqrt{3} = 1.73\\)).
8.  **Grazing Horse:** A horse is tied to a peg at one corner of a square-shaped grass field of side 15 m by means of a 5 m long rope. Find:
    - (i) the area of that part of the field in which the horse can graze
    - (ii) the increase in the grazing area if the rope were 10 m long instead of 5 m (Use \\(\pi = 3.14\\))
9.  **Silver Brooch:** A brooch is made with silver wire in the form of a circle with a diameter of 35 mm. The wire is also used to make 5 diameters which divide the circle into 10 equal sectors. Find:
    - (i) the total length of the silver wire required
    - (ii) the area of each sector of the brooch
10. An umbrella has 8 ribs which are equally spaced. Assuming the umbrella to be a flat circle of radius 45 cm, find the area between two consecutive ribs of the umbrella.
11. A car has two wipers which do not overlap. Each wiper has a blade of length 25 cm sweeping through an angle of \\(115^\circ\\). Find the total area cleaned at each sweep of the blades.
12. To warn ships of underwater rocks, a lighthouse spreads a red-coloured light over a sector of angle \\(80^\circ\\) to a distance of 16.5 km. Find the area of the sea over which the ships are warned (Use \\(\pi = 3.14\\)).
13. A round table cover has six equal designs. If the radius of the cover is 28 cm, find the cost of making the designs at the rate of ₹0.35 per \\(cm^2\\) (Use \\(\sqrt{3} = 1.7\\)).
14. Area of a sector of angle \\(p\\) (in degrees) of a circle with radius \\(R\\) is:
    - (A) \\(\frac{p}{180} \times 2\pi R\\) \quad (B) \\(\frac{p}{180} \times \pi R^2\\) \quad (C) \\(\frac{p}{360} \times 2\pi R\\) \quad (D) \\(\frac{p}{720} \times 2\pi R^2\\)

---

### **EXERCISE 5.3**

1.  Find the area of the shaded region in the circle below, if \\(PQ = 24\text{ cm}\\), \\(PR = 7\text{ cm}\\) and \\(O\\) is the centre of the circle. _(Note: QR is the diameter of the circle, so \\(\angle QPR = 90^\circ\\))_.
2.  Find the area of the shaded region, if the radii of the two concentric circles with centre \\(O\\) are 7 cm and 14 cm respectively, and \\(\angle AOC = 40^\circ\\).
3.  Find the area of the shaded region, if \\(ABCD\\) is a square of side 14 cm, and \\(APD\\) and \\(BPC\\) are semicircles.
4.  Find the area of the shaded region, where a circular arc of radius 6 cm has been drawn with vertex \\(O\\) of an equilateral triangle \\(OAB\\) of side 12 cm as its centre.
5.  From each corner of a square of side 4 cm, a quadrant of a circle of radius 1 cm is cut, and a central circle of diameter 2 cm is also cut. Find the area of the remaining portion of the square.
6.  In a circular table cover of radius 32 cm, a design is formed leaving an equilateral triangle \\(ABC\\) in the middle. Find the area of the design.
7.  In a square \\(ABCD\\) of side 14 cm, four circles are drawn with centres \\(A, B, C, \text{ and } D\\) such that each circle touches externally two of the remaining three circles. Find the area of the shaded region.
8.  **Racing Track:** A racing track has parallel straight segments connected by semicircular ends. The distance between the two inner parallel line segments is 60 m and they are each 106 m long. If the track is 10 m wide, find:
    - (i) the distance around the track along its inner edge
    - (ii) the total area of the track
9.  \\(AB\\) and \\(CD\\) are two diameters of a circle (with centre \\(O\\)) perpendicular to each other, and \\(OD\\) is the diameter of the smaller circle. If \\(OA = 7\text{ cm}\\), find the area of the shaded region.
10. The area of an equilateral triangle \\(ABC\\) is \\(17320.5\text{ } cm^2\\). With each vertex of the triangle as centre, a circle is drawn with its radius equal to half the length of the side of the triangle. Find the area of the shaded region (Use \\(\pi = 3.14\\) and \\(\sqrt{3} = 1.73205\\)).
11. On a square handkerchief, nine circular designs each of radius 7 cm are made. Find the area of the remaining portion of the handkerchief.
12. \\(OACB\\) is a quadrant of a circle with centre \\(O\\) and radius 3.5 cm. If \\(OD = 2\text{ cm}\\), find the area of the:
    - (i) quadrant \\(OACB\\)
    - (ii) shaded region
13. A square \\(OABC\\) is inscribed in a quadrant \\(OPBQ\\). If \\(OA = 20\text{ cm}\\), find the area of the shaded region (Use \\(\pi = 3.14\\)).
14. \\(AB\\) and \\(CD\\) are respectively arcs of two concentric circles of radii 21 cm and 7 cm with centre \\(O\\). If \\(\angle AOB = 30^\circ\\), find the area of the shaded region.
15. \\(ABC\\) is a quadrant of a circle of radius 14 cm and a semicircle is drawn with \\(BC\\) as its diameter. Find the area of the shaded region.
16. Calculate the area of the designed region common between two quadrants of circles of radius 8 cm each.

```xml
<svg width="280" height="240" viewBox="0 0 280 240" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <!-- Overlapping quadrants leaf design -->
  <rect x="50" y="30" width="160" height="160" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
  <!-- Leaf intersection (Quadrant from bottom-left & top-right) -->
  <path d="M 210,30 A 160,160 0 0,1 50,190 A 160,160 0 0,1 210,30 Z" fill="#bbf7d0" stroke="#16a34a" stroke-width="2.5"/>
  <!-- Labels -->
  <text x="130" y="115" font-family="Segoe UI, Arial" font-size="13" font-weight="bold" fill="#16a34a" text-anchor="middle">Common Leaf</text>
  <text x="40" y="25" font-family="Segoe UI, Arial" font-size="11" font-weight="bold" fill="#64748b">8 cm</text>
  <text x="215" y="115" font-family="Segoe UI, Arial" font-size="11" font-weight="bold" fill="#64748b">8 cm</text>
</svg>
```

---

📊 **I can help you build an Excel sheet tool with custom solvers for all sector, segment, and compound geometry calculations. Would you like me to construct this spreadsheet tool?**
