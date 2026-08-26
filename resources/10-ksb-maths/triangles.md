# **Chapter 2: Triangles

---

## **I. Core Concepts & Geometrical Principles**

### **1. Congruence vs. Similarity of Figures**

- **Congruent Figures:** Two geometric figures are congruent if they have the **same shape** and the **same size**.
- **Similar Figures:** Two geometric figures are similar if they have the **same shape** but not necessarily the same size.
  - _Fundamental Rule:_ All congruent figures are similar, but similar figures are not necessarily congruent.
- **Similarity of Polygons:** Two polygons with the same number of sides are similar if:
  1. Their corresponding angles are equal.
  2. Their corresponding sides are in the same ratio (or proportion).
- **Scale Factor:** The constant ratio of the corresponding sides is called the **scale factor** or Representative Fraction.

---

### **2. Similarity of Triangles**

Since a triangle is also a polygon, the same conditions apply for similarity. Two triangles are similar if:

1. Their corresponding angles are equal.
2. Their corresponding sides are in the same ratio (proportional).

---

### **3. The Basic Proportionality Theorem (BPT / Thales Theorem)**

- **Theorem 2.1:** If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.

#### **Proof of BPT (Thales Theorem):**

Let there be a triangle (ABC) where a line (DE) is drawn parallel to (BC) intersecting (AB) at (D) and (AC) at (E). We need to prove that:
[\frac{AD}{DB} = \frac{AE}{EC}]

#### **Geometric Diagram of BPT:**

```xml
<svg width="400" height="300" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .line { stroke: #0f172a; stroke-width: 2.5; fill: none; }
    .parallel { stroke: #0284c7; stroke-width: 3; fill: none; }
    .dash { stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 4 4; fill: none; }
    .altitude { stroke: #ef4444; stroke-width: 1.5; stroke-dasharray: 3 3; fill: none; }
    .label { font-family: 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 15px; fill: #0f172a; font-weight: bold; }
    .right-angle { stroke: #64748b; stroke-width: 1.2; fill: none; }
  </style>

  <!-- Triangle ABC Body -->
  <polygon points="200,40 60,240 340,240" stroke="#0f172a" stroke-width="2.5" fill="#ffffff"/>

  <!-- Parallel Line DE (Blue) -->
  <line x1="130" y1="140" x2="270" y2="140" class="parallel"/>

  <!-- Construction Lines BE and CD (Dashed Grey) -->
  <line x1="60" y1="240" x2="270" y2="140" class="dash"/>
  <line x1="340" y1="240" x2="130" y2="140" class="dash"/>

  <!-- Altitudes EN and DM (Dashed Red) -->
  <line x1="270" y1="140" x2="95" y2="190" class="altitude"/> <!-- EN perpendicular to AB -->
  <line x1="130" y1="140" x2="305" y2="190" class="altitude"/> <!-- DM perpendicular to AC -->

  <!-- Right Angle Markers -->
  <path d="M 98,185 L 103,192 L 100,197" class="right-angle"/>
  <path d="M 302,185 L 297,192 L 300,197" class="right-angle"/>

  <!-- Alphabetical Vertex Labels -->
  <text x="193" y="30" class="label">A</text>
  <text x="45" y="255" class="label">B</text>
  <text x="345" y="255" class="label">C</text>
  <text x="110" y="145" class="label">D</text>
  <text x="280" y="145" class="label">E</text>
  <text x="80" y="200" class="label" style="fill:#ef4444;">N</text>
  <text x="312" y="200" class="label" style="fill:#ef4444;">M</text>
</svg>
```

Join (BE) and (CD). Draw perpendiculars (DM \perp AC) and (EN \perp AB).
[\text{Area of } \Delta ADE = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times AD \times EN \quad \text{--- (Eq. 1)}]
[\text{Area of } \Delta BDE = \frac{1}{2} \times DB \times EN \quad \text{--- (Eq. 2)}]
Dividing Eq. 1 by Eq. 2:
[\frac{\text{ar}(ADE)}{\text{ar}(BDE)} = \frac{\frac{1}{2} \times AD \times EN}{\frac{1}{2} \times DB \times EN} = \frac{AD}{DB} \quad \text{--- (Eq. 3)}]

Similarly, finding the areas with base (AE) and (EC) and altitude (DM):
[\frac{\text{ar}(ADE)}{\text{ar}(DEC)} = \frac{\frac{1}{2} \times AE \times DM}{\frac{1}{2} \times EC \times DM} = \frac{AE}{EC} \quad \text{--- (Eq. 4)}]

Since triangles (BDE) and (DEC) stand on the same base (DE) and between the same parallel lines (BC) and (DE), their areas are equal:
[\text{ar}(BDE) = \text{ar}(DEC) \quad \text{--- (Eq. 5)}]

Therefore, from Equations 3, 4, and 5, we conclude:
[\frac{AD}{DB} = \frac{AE}{EC}]

---

### **4. Converse of the Basic Proportionality Theorem**

- **Theorem 2.2:** If a line divides any two sides of a triangle in the same ratio, then the line is parallel to the third side.

---

### **5. Criteria for Similarity of Triangles**

- **AAA Similarity (Theorem 2.3):** If in two triangles, corresponding angles are equal, then their corresponding sides are in the same ratio, making the triangles similar.
- **AA Similarity:** If two angles of one triangle are respectively equal to two angles of another triangle, then the two triangles are similar.
- **SSS Similarity (Theorem 2.4):** If the corresponding sides of two triangles are proportional, their corresponding angles are equal, making the triangles similar.
- **SAS Similarity (Theorem 2.5):** If one angle of a triangle is equal to one angle of another triangle and the sides including these angles are proportional, then the two triangles are similar.

---

### **6. Areas of Similar Triangles**

- **Theorem 2.6:** The ratio of the areas of two similar triangles is equal to the square of the ratio of their corresponding sides.
  [\frac{\text{ar}(ABC)}{\text{ar}(PQR)} = \left(\frac{AB}{PQ}\right)^2 = \left(\frac{BC}{QR}\right)^2 = \left(\frac{CA}{RP}\right)^2]

---

### **7. Pythagoras Theorem & Right Triangles**

- **Theorem 2.7:** If a perpendicular is drawn from the vertex of the right angle of a right triangle to the hypotenuse, then triangles on both sides of the perpendicular are similar to the whole triangle and to each other.
- **Pythagoras Theorem (Theorem 2.8):** In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides ((AC^2 = AB^2 + BC^2)).

#### **Geometric Diagram of Pythagoras Theorem Altitude (Fig. 2.45):**

```xml
<svg width="400" height="240" viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .tri { fill: #ffffff; stroke: #0f172a; stroke-width: 2.5; }
    .perp { stroke: #ef4444; stroke-width: 2.5; stroke-dasharray: 4 4; fill: none; }
    .lbl-bold { font-family: 'Segoe UI', Arial, sans-serif; font-size: 15px; fill: #0f172a; font-weight: bold; }
    .ra-indicator { stroke: #64748b; stroke-width: 1.5; fill: none; }
  </style>
  <!-- Right triangle ABC angled at B -->
  <polygon points="80,40 80,190 320,190" class="tri"/>
  <!-- Perpendicular BD from B(80,190) to AC -->
  <line x1="80" y1="190" x2="147" y2="82" class="perp"/>
  <!-- Right angle at B -->
  <rect x="80" y="175" width="15" height="15" class="ra-indicator"/>
  <!-- Right angle at D -->
  <path d="M 139,87 L 144,95 L 152,90" class="ra-indicator" style="stroke:#ef4444;"/>
  <!-- Labels -->
  <text x="75" y="32" class="lbl-bold">A</text>
  <text x="60" y="205" class="lbl-bold">B</text>
  <text x="325" y="195" class="lbl-bold">C</text>
  <text x="155" y="78" class="lbl-bold" style="fill:#ef4444;">D</text>
</svg>
```

- **Converse of Pythagoras Theorem (Theorem 2.9):** In a triangle, if the square of one side is equal to the sum of the squares of the other two sides, then the angle opposite the first side is a right angle ((90^\circ)).

---

## **II. Example Problems (with Step-by-Step Solutions)**

### **Example 1**

**Problem:** If a line intersects sides (AB) and (AC) of a (\Delta ABC) at (D) and (E) respectively and is parallel to (BC), prove that (\frac{AD}{AB} = \frac{AE}{AC}).

- **Solution:**
  - Since (DE \parallel BC), by Theorem 2.1 (BPT):
    [\frac{AD}{DB} = \frac{AE}{EC}]
  - Taking the reciprocal:
    [\frac{DB}{AD} = \frac{EC}{AE}]
  - Adding (1) to both sides:
    [\frac{DB}{AD} + 1 = \frac{EC}{AE} + 1]
    [\frac{DB + AD}{AD} = \frac{EC + AE}{AE}]
    [\frac{AB}{AD} = \frac{AC}{AE}]
  - Inverting again:
    [\frac{AD}{AB} = \frac{AE}{AC}]

---

### **Example 2**

**Problem:** (ABCD) is a trapezium with (AB \parallel DC). (E) and (F) are points on non-parallel sides (AD) and (BC) respectively such that (EF \parallel AB). Show that (\frac{AE}{ED} = \frac{BF}{FC}).

- **Solution:**

#### **Geometric Diagram of Trapezium Construction:**

```xml
<svg width="400" height="240" viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .poly { fill: #ffffff; stroke: #0f172a; stroke-width: 2.5; }
    .line-main { stroke: #0284c7; stroke-width: 2.5; }
    .dash-const { stroke: #ef4444; stroke-width: 1.5; stroke-dasharray: 4 4; fill: none; }
    .lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 15px; fill: #0f172a; font-weight: bold; }
  </style>
  <!-- Trapezium ABCD -->
  <polygon points="100,50 300,50 350,190 50,190" class="poly"/>
  <!-- Parallel line EF at y=120 -->
  <line x1="75" y1="120" x2="325" y2="120" class="line-main"/>
  <!-- Diagonal AC -->
  <line x1="100" y1="50" x2="350" y2="190" class="dash-const"/>
  <!-- Labels -->
  <text x="90" y="42" class="lbl">A</text>
  <text x="300" y="42" class="lbl">B</text>
  <text x="355" y="205" class="lbl">C</text>
  <text x="35" y="205" class="lbl">D</text>
  <text x="50" y="125" class="lbl">E</text>
  <text x="330" y="125" class="lbl">F</text>
  <!-- Intersection G -->
  <circle cx="225" cy="120" r="4.5" fill="#ef4444"/>
  <text x="215" y="112" class="lbl" style="fill:#ef4444;">G</text>
</svg>
```

```
*   Let us join \\(AC\\) to intersect \\(EF\\) at \\(G\\).
*   Since \\(AB \parallel DC\\) and \\(EF \parallel AB\\), then \\(EF \parallel DC\\) (lines parallel to the same line are parallel to each other).
*   In \\(\Delta ADC\\), since \\(EG \parallel DC\\), by the Basic Proportionality Theorem (BPT):
    \\[\frac{AE}{ED} = \frac{AG}{GC} \quad \text{--- (Eq. 1)}\\]
*   In \\(\Delta CAB\\), since \\(GF \parallel AB\\), by BPT:
    \\[\frac{CG}{AG} = \frac{CF}{BF} \Rightarrow \frac{AG}{GC} = \frac{BF}{FC} \quad \text{--- (Eq. 2)}\\]
*   Equating (Eq. 1) and (Eq. 2):
    \\[\frac{AE}{ED} = \frac{BF}{FC}\\]
```

---

### **Example 3 (Shadow & Similar Triangle Application)**

**Problem:** A girl of height (90\text{ cm}) is walking away from the base of a lamp-post at a speed of (1.2\text{ m/s}). If the lamp is (3.6\text{ m}) above the ground, find the length of her shadow after 4 seconds.

- **Solution:**

#### **Shadow Vector Diagram:**

```xml
<svg width="500" height="240" viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .ground { stroke: #475569; stroke-width: 3; }
    .pole { stroke: #0f172a; stroke-width: 4.5; fill: none; }
    .girl { stroke: #0284c7; stroke-width: 3; fill: none; }
    .ray { stroke: #f59e0b; stroke-dasharray: 5 5; stroke-width: 2; fill: none; }
    .dim-line { stroke: #94a3b8; stroke-width: 1.2; fill: none; }
    .txt { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #1e293b; }
    .txt-bold { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
  </style>
  <!-- Ground line -->
  <line x1="40" y1="200" x2="460" y2="200" class="ground"/>
  <!-- Lamp-post AB -->
  <line x1="80" y1="200" x2="80" y2="40" class="pole"/>
  <!-- Light ray -->
  <line x1="80" y1="40" x2="400" y2="200" class="ray"/>
  <!-- Girl CD -->
  <line x1="240" y1="200" x2="240" y2="120" class="girl"/>
  <!-- Labels -->
  <text x="75" y="32" class="txt-bold">A (Lamp)</text>
  <text x="70" y="218" class="txt-bold">B</text>
  <text x="230" y="112" class="txt-bold" style="fill:#0284c7;">C (Girl)</text>
  <text x="235" y="218" class="txt-bold">D</text>
  <text x="405" y="215" class="txt-bold">E</text>
  <!-- Heights -->
  <text x="25" y="125" class="txt">3.6 m</text>
  <text x="250" y="160" class="txt" style="fill:#0284c7;">0.9 m</text>
  <!-- Dimension markers -->
  <path d="M 80,225 L 240,225" class="dim-line"/>
  <text x="130" y="238" class="txt">BD = 4.8 m</text>
  <path d="M 240,225 L 400,225" class="dim-line"/>
  <text x="300" y="238" class="txt">DE = x = 1.6 m</text>
</svg>
```

```
*   Let \\(AB\\) represent the lamp-post (\\(3.6\text{ m}\\)) and \\(CD\\) denote the girl (\\(90\text{ cm} = 0.9\text{ m}\\)). Her shadow is \\(DE = x\text{ m}\\).
*   Distance walked in 4 seconds:
    \\[BD = 1.2\text{ m/s} \times 4 = 4.8\text{ m}\\]
*   In \\(\Delta ABE\\) and \\(\Delta CDE\\):
    *   \\(\angle B = \angle D = 90^\circ\\) (both vertical structures)
    *   \\(\angle E = \angle E\\) (common angle)
*   By AA similarity, \\(\Delta ABE \sim \Delta CDE\\).
*   Therefore:
    \\[\frac{BE}{DE} = \frac{AB}{CD} \Rightarrow \frac{4.8 + x}{x} = \frac{3.6}{0.9}\\]
    \\[\frac{4.8 + x}{x} = 4 \Rightarrow 4.8 + x = 4x \Rightarrow 3x = 4.8 \Rightarrow x = 1.6\text{ m}\\]
*   The length of her shadow is **\\(1.6\text{ m}\\)**.
```

---

## **III. Exercise Questions**

### **EXERCISE 2.1**

1. **Fill in the blanks:**

- (i) All circles are (similar)
- (ii) All squares are (similar)
- (iii) All triangles are similar (equilateral)
- (iv) Two polygons of the same number of sides are similar, if (a) their corresponding angles are and (b) their corresponding sides are (equal, proportional)

2. Give two different examples of a pair of:

- (i) similar figures
- (ii) non-similar figures

3. State whether the following quadrilaterals are similar or not:
   _(A rhombus of side (1.5\text{ cm}) and a square of side (3\text{ cm}))_.

---

### **EXERCISE 2.2**

1. In Fig. 2.17, (i) and (ii), (DE \parallel BC). Find (EC) in (i) and (AD) in (ii).
   _(Measurements: (i) (AD = 1.5\text{ cm}, DB = 3\text{ cm}, AE = 1\text{ cm}); (ii) (DB = 7.2\text{ cm}, AE = 1.8\text{ cm}, EC = 5.4\text{ cm}))_.
2. (E) and (F) are points on the sides (PQ) and (PR) respectively of a (\Delta PQR). State whether (EF \parallel QR) for each of the following cases:

- (i) (PE = 3.9\text{ cm}, EQ = 3\text{ cm}, PF = 3.6\text{ cm}) and (FR = 2.4\text{ cm})
- (ii) (PE = 4\text{ cm}, QE = 4.5\text{ cm}, PF = 8\text{ cm}) and (RF = 9\text{ cm})
- (iii) (PQ = 1.28\text{ cm}, PR = 2.56\text{ cm}, PE = 0.18\text{ cm}) and (PF = 0.36\text{ cm})

3. In Fig. 2.18, if (LM \parallel CB) and (LN \parallel CD), prove that (\frac{AM}{AB} = \frac{AN}{AD}).
4. In Fig. 2.19, (DE \parallel AC) and (DF \parallel AE). Prove that (\frac{BF}{FE} = \frac{BE}{EC}).
5. In Fig. 2.20, (DE \parallel OQ) and (DF \parallel OR). Show that (EF \parallel QR).
6. In Fig. 2.21, A, B and (C) are points on (OP, OQ) and (OR) respectively such that (AB \parallel PQ) and (AC \parallel PR). Show that (BC \parallel QR).
7. Using Theorem 2.1, prove that a line drawn through the mid-point of one side of a triangle parallel to another side bisects the third side.
8. Using Theorem 2.2, prove that the line joining the mid-points of any two sides of a triangle is parallel to the third side.
9. (ABCD) is a trapezium in which (AB \parallel DC) and its diagonals intersect each other at the point (O). Show that (\frac{AO}{BO} = \frac{CO}{DO}).
10. The diagonals of a quadrilateral (ABCD) intersect each other at the point (O) such that (\frac{AO}{BO} = \frac{CO}{DO}). Show that (ABCD) is a trapezium.

---

### **EXERCISE 2.3**

1. State which pairs of triangles in Fig. 2.34 are similar. Write the similarity criterion used and write the pairs of similar triangles in symbolic form.
2. In Fig. 2.35, (\Delta ODC \sim \Delta OBA), (\angle BOC = 125^\circ) and (\angle CDO = 70^\circ). Find (\angle DOC), (\angle DCO) and (\angle OAB).
3. Diagonals (AC) and (BD) of a trapezium (ABCD) with (AB \parallel DC) intersect each other at the point (O). Using a similarity criterion for two triangles, show that (\frac{AO}{OC} = \frac{OB}{OD}).
4. In Fig. 2.36, (\frac{QR}{QS} = \frac{QT}{PR}) and (\angle 1 = \angle 2). Show that (\Delta PQS \sim \Delta TQR).
5. (S) and (T) are points on sides (PR) and (QR) of (\Delta PQR) such that (\angle P = \angle RTS). Show that (\Delta RPQ \sim \Delta RTS).
6. In Fig. 2.37, if (\Delta ABE \cong \Delta ACD), show that (\Delta ADE \sim \Delta ABC).
7. In Fig. 2.38, altitudes (AD) and (CE) of (\Delta ABC) intersect each other at the point (P). Show that:

- (i) (\Delta AEP \sim \Delta CDP)
- (ii) (\Delta ABD \sim \Delta CBE)
- (iii) (\Delta AEP \sim \Delta ABD)
- (iv) (\Delta PDC \sim \Delta BEC)

8. (E) is a point on the side (AD) produced of a parallelogram (ABCD) and (BE) intersects (CD) at (F). Show that (\Delta ABE \sim \Delta CFB).
9. In Fig. 2.39, (ABC) and (AMP) are two right triangles, right-angled at (B) and (M) respectively. Prove that:

- (i) (\Delta ABC \sim \Delta AMP)
- (ii) (\frac{CA}{PA} = \frac{BC}{MP})

10. (CD) and (GH) are respectively the bisectors of (\angle ACB) and (\angle EGF) such that (D) and (H) lie on sides (AB) and (FE) of (\Delta ABC) and (\Delta EFG) respectively. If (\Delta ABC \sim \Delta FEG), show that:

- (i) (\frac{CD}{GH} = \frac{AC}{FG})
- (ii) (\Delta DCB \sim \Delta HGE)
- (iii) (\Delta DCA \sim \Delta HGF)

11. In Fig. 2.40, (E) is a point on side (CB) produced of an isosceles triangle (ABC) with (AB = AC). If (AD \perp BC) and (EF \perp AC), prove that (\Delta ABD \sim \Delta ECF).
12. Sides (AB) and (BC) and median (AD) of a triangle (ABC) are respectively proportional to sides (PQ) and (QR) and median (PM) of (\Delta PQR). Show that (\Delta ABC \sim \Delta PQR).
13. (D) is a point on the side (BC) of a triangle (ABC) such that (\angle ADC = \angle BAC). Show that (CA^2 = CB \cdot CD).
14. Sides (AB) and (AC) and median (AD) of a triangle (ABC) are respectively proportional to sides (PQ) and (PR) and median (PM) of another triangle (PQR). Show that (\Delta ABC \sim \Delta PQR).
15. A vertical pole of length (6\text{ m}) casts a shadow (4\text{ m}) long on the ground and at the same time a tower casts a shadow (28\text{ m}) long. Find the height of the tower.
16. If (AD) and (PM) are medians of triangles (ABC) and (PQR), respectively, where (\Delta ABC \sim \Delta PQR), prove that (\frac{AB}{PQ} = \frac{AD}{PM}).

---

### **EXERCISE 2.4**

1. Let (\Delta ABC \sim \Delta DEF) and their areas be, respectively, (64\text{ cm}^2) and (121\text{ cm}^2). If (EF = 15.4\text{ cm}), find (BC).
2. Diagonals of a trapezium (ABCD) with (AB \parallel DC) intersect each other at the point (O). If (AB = 2CD), find the ratio of the areas of triangles (AOB) and (COD).
3. In Fig. 2.44, (ABC) and (DBC) are two triangles on the same base (BC). If (AD) intersects (BC) at (O), show that (\frac{\text{ar}(ABC)}{\text{ar}(DBC)} = \frac{AO}{DO}).
4. If the areas of two similar triangles are equal, prove that they are congruent.
5. (D, E) and (F) are respectively the mid-points of sides (AB, BC) and (CA) of (\Delta ABC). Find the ratio of the areas of (\Delta DEF) and (\Delta ABC).
6. Prove that the ratio of the areas of two similar triangles is equal to the square of the ratio of their corresponding medians.
7. Prove that the area of an equilateral triangle described on one side of a square is equal to half the area of the equilateral triangle described on one of its diagonals.
8. (ABC) and (BDE) are two equilateral triangles such that (D) is the mid-point of (BC). The ratio of the areas of triangles (ABC) and (BDE) is:

- (A) 2:1 \quad (B) 1:2 \quad (C) 4:1 \quad (D) 1:4

9. Sides of two similar triangles are in the ratio 4:9. Areas of these triangles are in the ratio:

- (A) 2:3 \quad (B) 4:9 \quad (C) 81:16 \quad (D) 16:81

---

### **EXERCISE 2.5**

1. Sides of triangles are given below. Determine which of them are right triangles. In case of a right triangle, write the length of its hypotenuse:

- (i) (7\text{ cm}, 24\text{ cm}, 25\text{ cm})
- (ii) (3\text{ cm}, 8\text{ cm}, 6\text{ cm})
- (iii) (50\text{ cm}, 80\text{ cm}, 100\text{ cm})
- (iv) (13\text{ cm}, 12\text{ cm}, 5\text{ cm})

2. (PQR) is a triangle right-angled at (P) and (M) is a point on (QR) such that (PM \perp QR). Show that (PM^2 = QM \cdot MR).
3. In Fig. 2.53, (ABD) is a triangle right-angled at (A) and (AC \perp BD). Show that:

- (i) (AB^2 = BC \cdot BD)
- (ii) (AC^2 = BC \cdot DC)
- (iii) (AD^2 = BD \cdot CD)

4. (ABC) is an isosceles triangle right-angled at (C). Prove that (AB^2 = 2AC^2).
5. (ABC) is an isosceles triangle with (AC = BC). If (AB^2 = 2AC^2), prove that (ABC) is a right triangle.
6. (ABC) is an equilateral triangle of side (2a). Find each of its altitudes.
7. Prove that the sum of the squares of the sides of a rhombus is equal to the sum of the squares of its diagonals.
8. In Fig. 2.54, (O) is a point in the interior of a triangle (ABC), (OD \perp BC), (OE \perp AC) and (OF \perp AB). Show that:

- (i) (OA^2 + OB^2 + OC^2 - OD^2 - OE^2 - OF^2 = AF^2 + BD^2 + CE^2)
- (ii) (AF^2 + BD^2 + CE^2 = AE^2 + CD^2 + BF^2)

9. A ladder (10\text{ m}) long reaches a window (8\text{ m}) above the ground. Find the distance of the foot of the ladder from the base of the wall.
10. A guy wire attached to a vertical pole of height (18\text{ m}) is (24\text{ m}) long and has a stake attached to the other end. How far from the base of the pole should the stake be driven so that the wire will be taut?
11. An aeroplane leaves an airport and flies due north at a speed of (1000\text{ km/h}). At the same time, another aeroplane leaves the same airport and flies due west at a speed of (1200\text{ km/h}). How far apart will the two planes be after (1\frac{1}{2}) hours?
12. Two poles of heights (6\text{ m}) and (11\text{ m}) stand on plane ground. If the distance between the feet of the poles is (12\text{ m}), find the distance between their tops.
13. (D) and (E) are points on the sides (CA) and (CB) respectively of a triangle (ABC) right-angled at (C). Prove that (AE^2 + BD^2 = AB^2 + DE^2).
14. The perpendicular from (A) on side (BC) of a (\Delta ABC) intersects (BC) at (D) such that (DB = 3CD). Prove that (2AB^2 = 2AC^2 + BC^2).
15. In an equilateral triangle (ABC), (D) is a point on side (BC) such that (BD = \frac{1}{3}BC). Prove that (9AD^2 = 7AB^2).
16. In an equilateral triangle, prove that three times the square of one side is equal to four times the square of one of its altitudes.
17. In (\Delta ABC), (AB = 6\sqrt{3}\text{ cm}), (AC = 12\text{ cm}) and (BC = 6\text{ cm}). The angle (B) is:

- (A) (120^\circ) \quad (B) (60^\circ) \quad (C) (90^\circ) \quad (D) (45^\circ).

---

### **EXERCISE 2.6 (Optional)**

_These exercises are not from the examination point of view._

1. In Fig. 2.56, (PS) is the bisector of (\angle QPR) of (\Delta PQR). Prove that (\frac{QS}{SR} = \frac{PQ}{PR}).
2. In Fig. 2.57, (D) is a point on hypotenuse (AC) of (\Delta ABC), such that (BD \perp AC), (DM \perp BC) and (DN \perp AB). Prove that:

- (i) (DM^2 = DN \cdot MC)
- (ii) (DN^2 = DM \cdot AN)

3. In Fig. 2.58, (ABC) is a triangle in which (\angle ABC > 90^\circ) and (AD \perp CB) produced. Prove that (AC^2 = AB^2 + BC^2 + 2BC \cdot BD).
4. In Fig. 2.59, (ABC) is a triangle in which (\angle ABC < 90^\circ) and (AD \perp BC). Prove that (AC^2 = AB^2 + BC^2 - 2BC \cdot BD).
5. In Fig. 2.60, (AD) is a median of a triangle (ABC) and (AM \perp BC). Prove that:

- (i) (AC^2 = AD^2 + BC \cdot DM + \left(\frac{BC}{2}\right)^2)
- (ii) (AB^2 = AD^2 - BC \cdot DM + \left(\frac{BC}{2}\right)^2)
- (iii) (AC^2 + AB^2 = 2AD^2 + \frac{1}{2}BC^2)

6. Prove that the sum of the squares of the diagonals of a parallelogram is equal to the sum of the squares of its sides.
7. In Fig. 2.61, two chords (AB) and (CD) intersect each other at the point (P). Prove that:

- (i) (\Delta APC \sim \Delta DPB)
- (ii) (AP \cdot PB = CP \cdot DP)

8. In Fig. 2.62, two chords (AB) and (CD) of a circle intersect each other at the point (P) (when produced) outside the circle. Prove that:

- (i) (\Delta PAC \sim \Delta PDB)
- (ii) (PA \cdot PB = PC \cdot PD)

9. In Fig. 2.63, (D) is a point on side (BC) of (\Delta ABC) such that (\frac{BD}{CD} = \frac{AB}{AC}). Prove that (AD) is the bisector of (\angle BAC).
10. Nazima is fly fishing in a stream. The tip of her fishing rod is (1.8\text{ m}) above the surface of the water and the fly at the end of the string rests on the water (3.6\text{ m}) away and (2.4\text{ m}) from a point directly under the tip of the rod. Assuming that her string is taut, how much string does she have out? If she pulls in the string at the rate of (5\text{ cm}) per second, what will be the horizontal distance of the fly from her after 12 seconds?

---

📐 I can compile this geometric study guide into a downloadable PDF document or create a interactive solver app for right-angled triangles in your notebook. Let me know what you'd like to do next!
