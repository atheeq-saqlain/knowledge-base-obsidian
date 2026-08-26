# **Chapter 12: Some Applications of Trigonometry — Study Guide**

---

## **I. Core Concepts & Geometrical Principles**

### **1. Historical & Practical Significance**

- **Origin:** Trigonometry was originally invented because its need arose in the field of astronomy `. Ancient astronomers used it to calculate the distances from the Earth to the planets and stars `.
- **Modern Applications:** Today, the study of trigonometry is widely used in geography, navigation, map-making, and determining the positions of islands using longitudes and latitudes ``.
- **Theodolites & Great Trigonometric Survey:** In the nineteenth century, the "Great Trigonometric Survey" of British India was conducted using the largest-ever built **theodolites**—surveying instruments based on trigonometric principles used for measuring horizontal and vertical angles with a rotating telescope `. In 1852, this survey led to the discovery of the highest mountain peak in the world, which was later named after Sir George Everest `.

---

### **2. Important Terms in Heights and Distances**

To find heights of objects and distances between different points without actual measurement, we define three fundamental concepts ``:

1.  **Line of Sight:** The line of sight is the straight line drawn from the eye of an observer to the point on the object being viewed by the observer ``.
2.  **Angle of Elevation:** The angle of elevation of an object viewed is the angle formed by the line of sight with the horizontal level when the object is **above** the horizontal level `. This is the case when we raise our head to look up at the object `.
3.  **Angle of Depression:** The angle of depression of an object viewed is the angle formed by the line of sight with the horizontal level when the object is **below** the horizontal level `. This is the case when we lower our head to look down at the object `.

```xml
<svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .horizontal { stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 4 4; fill: none; }
    .sight-line { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .ground-line { stroke: #475569; stroke-width: 3; }
    .arc-elev { stroke: #ef4444; stroke-width: 2; fill: none; }
    .arc-dep { stroke: #f59e0b; stroke-width: 2; fill: none; }
    .label-bold { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
    .label-sub { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #64748b; }
    .dot-node { fill: #0f172a; }
  </style>

  <!-- Ground Level -->
  <line x1="30" y1="210" x2="570" y2="210" class="ground-line" />

  <!-- Observer Eye Point at (100, 110) -->
  <circle cx="100" cy="110" r="5" class="dot-node" />
  <text x="80" y="100" class="label-bold">Observer (Eye)</text>

  <!-- Horizontal Level from Eye -->
  <line x1="100" y1="110" x2="500" y2="110" class="horizontal" />
  <text x="510" y="114" class="label-bold" style="fill:#64748b;">Horizontal Level</text>

  <!-- Object Above (Angle of Elevation) -->
  <line x1="100" y1="110" x2="450" y2="40" class="sight-line" />
  <circle cx="450" cy="40" r="5" class="dot-node" style="fill:#ef4444;" />
  <text x="460" y="45" class="label-bold" style="fill:#ef4444;">Object (Up)</text>
  <path d="M 160,110 A 60,60 0 0,0 151,99" class="arc-elev" />
  <text x="170" y="102" class="label-bold" style="fill:#ef4444;">Angle of Elevation</text>
  <text x="250" y="70" class="label-sub" style="fill:#0284c7; transform: rotate(-11deg); transform-origin: 250px 70px;">Line of Sight</text>

  <!-- Object Below (Angle of Depression) -->
  <line x1="100" y1="110" x2="450" y2="180" class="sight-line" style="stroke:#0284c7;" />
  <circle cx="450" cy="180" r="5" class="dot-node" style="fill:#f59e0b;" />
  <text x="460" y="185" class="label-bold" style="fill:#f59e0b;">Object (Down)</text>
  <path d="M 160,110 A 60,60 0 0,1 151,121" class="arc-dep" />
  <text x="170" y="125" class="label-bold" style="fill:#f59e0b;">Angle of Depression</text>
  <text x="250" y="150" class="label-sub" style="fill:#0284c7; transform: rotate(11deg); transform-origin: 250px 150px;">Line of Sight</text>
</svg>
```

---

## **II. Example Problems (with Step-by-Step Solutions)**

### **Example 1 (Direct Angle of Elevation)**

**Problem:** A tower stands vertically on the ground `. From a point on the ground, which is \\(15\text{ m}\\) away from the foot of the tower, the angle of elevation of the top of the tower is found to be \\(60^\circ\\) `. Find the height of the tower ``.

- **Solution:**
  - Let \\(AB\\) represent the vertical tower of height \\(h\text{ m}\\), and \\(BC\\) represent the distance from the observer to the foot of the tower (\\(BC = 15\text{ m}\\)) `. The angle of elevation is \\(\angle ACB = 60^\circ\\) `.
  - In the right-angled triangle \\(\Delta ABC\\) `:
\tan 60^\circ = \frac{\text{Opposite Side}}{\text{Adjacent Side}} = \frac{AB}{BC} \quad \text{`}\\[
    \\]\sqrt{3} = \frac{AB}{15} \implies AB = 15\sqrt{3}\text{ m} \quad \text{``}\$\$
  - **Answer:** The height of the tower is **\\(15\sqrt{3}\text{ m}\\)** ``.

---

### **Example 2 (Electrician and Pole Problem)**

**Problem:** An electrician has to repair an electric fault on a pole of height \\(5\text{ m}\\) `. She needs to reach a point \\(1.3\text{ m}\\) below the top of the pole to undertake the repair work `. What should be the length of the ladder that she should use which, when inclined at an angle of \\(60^\circ\\) to the horizontal, would enable her to reach the required position? Also, how far from the foot of the pole should she place the foot of the ladder? (Take \\(\sqrt{3} = 1.73\\)) ``.

- **Solution:**

```xml
<svg width="400" height="280" viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .ground { stroke: #475569; stroke-width: 3; }
    .pole { stroke: #0f172a; stroke-width: 4; fill: none; }
    .fault-pole { stroke: #ef4444; stroke-width: 4; fill: none; }
    .ladder { stroke: #0284c7; stroke-width: 3; fill: none; }
    .dim-line { stroke: #94a3b8; stroke-width: 1; fill: none; }
    .txt-lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
    .angle-arc { stroke: #ef4444; stroke-width: 1.5; fill: none; }
  </style>

  <!-- Ground -->
  <line x1="40" y1="230" x2="360" y2="230" class="ground" />

  <!-- Pole AD (D at bottom 80, 230; A at top 80, 40) -->
  <line x1="80" y1="230" x2="80" y2="40" class="pole" />
  <!-- Upper 1.3m (AB) highlighted in Red -->
  <line x1="80" y1="40" x2="80" y2="89" class="fault-pole" />

  <!-- Ladder BC (C on ground at 240, 230; B at 80, 89) -->
  <line x1="80" y1="89" x2="240" y2="230" class="ladder" />

  <!-- Angle arc at C -->
  <path d="M 215,230 A 25,25 0 0,0 223,215" class="angle-arc" />
  <text x="200" y="210" class="txt-lbl" style="fill:#ef4444;">60°</text>

  <!-- Vertex Dots -->
  <circle cx="80" cy="40" r="4" class="dot-node" />
  <circle cx="80" cy="89" r="4.5" class="dot-node" style="fill:#ef4444;" />
  <circle cx="80" cy="230" r="4" class="dot-node" />
  <circle cx="240" cy="230" r="4.5" class="dot-node" style="fill:#0284c7;" />

  <!-- Labels -->
  <text x="95" y="45" class="txt-lbl">A (Top)</text>
  <text x="95" y="94" class="txt-lbl" style="fill:#ef4444;">B (Reach Point)</text>
  <text x="60" y="245" class="txt-lbl">D (Foot)</text>
  <text x="245" y="245" class="txt-lbl" style="fill:#0284c7;">C (Ladder Foot)</text>

  <!-- Dimension notations -->
  <text x="30" y="70" class="txt-lbl" style="fill:#ef4444;">1.3 m</text>
  <text x="30" y="160" class="txt-lbl">3.7 m</text>
  <text x="175" y="145" class="txt-lbl" style="fill:#0284c7;">Ladder (BC)</text>
</svg>
```

    *   Let \\(AD\\) be the vertical pole of height \\(5\text{ m}\\) ``. The electrician must reach point \\(B\\), which is \\(1.3\text{ m}\\) below the top \\(A\\) ``.
    *   Thus, the vertical height to be climbed is:
        \$\$BD = AD - AB = 5 - 1.3 = 3.7\text{ m} \quad \text{``}\$\$
    *   Let \\(BC\\) represent the length of the ladder inclined at \\(60^\circ\\) to the ground ``.
    *   In the right triangle \\(\Delta BDC\\) ``:
        \frac{BD}{BC} = \sin 60^\circ \implies \frac{3.7}{BC} = \frac{\sqrt{3}}{2} \quad \text{``}\\[
        \\]BC = \frac{3.7 \times 2}{\sqrt{3}} = \frac{7.4}{1.73} \approx 4.28\text{ m} \quad \text{``}\$\$
    *   To find the distance of the foot of the ladder from the pole (\\(DC\\)) ``:
        \frac{DC}{BD} = \cot 60^\circ \implies \frac{DC}{3.7} = \frac{1}{\sqrt{3}} \quad \text{``}\\[
        \\]DC = \frac{3.7}{\sqrt{3}} = \frac{3.7}{1.73} \approx 2.14\text{ m} \quad \text{``}\$\$
    *   **Answer:** The required length of the ladder is **\\(4.28\text{ m}\\)** `` and its foot should be placed **\\(2.14\text{ m}\\)** away from the base of the pole ``.

---

### **Example 3 (Observer and Chimney)**

**Problem:** An observer \\(1.5\text{ m}\\) tall is \\(28.5\text{ m}\\) away from a chimney `. The angle of elevation of the top of the chimney from her eyes is \\(45^\circ\\) `. What is the height of the chimney? ``.

- **Solution:**
  - Let \\(AB\\) represent the chimney of height \\(H\\) and \\(CD\\) represent the observer of height \\(1.5\text{ m}\\) ``.
  - The horizontal distance from the observer to the chimney is \\(DE = CB = 28.5\text{ m}\\) ``.
  - The height of the chimney above the observer's eye level is \\(AE\\) `. Thus, the total height of the chimney is:
\$\$AB = AE + BE = AE + 1.5\text{ m} \quad \text{`}\$\$
  - In the right-angled triangle \\(\Delta ADE\\), with \\(\angle ADE = 45^\circ\\) `:
\tan 45^\circ = \frac{AE}{DE} \implies 1 = \frac{AE}{28.5} \implies AE = 28.5\text{ m} \quad \text{`}\$\$
  - Calculate the total height \\(AB\\):
    \$\$AB = 28.5 + 1.5 = 30\text{ m} \quad \text{``}\$\$
  - **Answer:** The height of the chimney is **\\(30\text{ m}\\)** ``.

---

### **Example 4 (Building with Flagstaff)**

**Problem:** From a point \\(P\\) on the ground the angle of elevation of the top of a \\(10\text{ m}\\) tall building is \\(30^\circ\\) `. A flag is hoisted at the top of the building and the angle of elevation of the top of the flagstaff from \\(P\\) is \\(45^\circ\\) `. Find the length of the flagstaff and the distance of the building from the point \\(P\\). (Take \\(\sqrt{3} = 1.732\\)) ``.

- **Solution:**
  - Let \\(AB\\) represent the building of height \\(10\text{ m}\\) `, \\(BD\\) represent the flagstaff of height \\(x\text{ m}\\) `, and \\(AP\\) represent the distance of point \\(P\\) from the building ``.
  - In the right triangle \\(\Delta PAB\\), with \\(\angle APB = 30^\circ\\) `:
\tan 30^\circ = \frac{AB}{AP} \implies \frac{1}{\sqrt{3}} = \frac{10}{AP} \implies AP = 10\sqrt{3}\text{ m} \quad \text{`}\\[
    \\]AP = 10 \times 1.732 = 17.32\text{ m} \quad \text{``}\$\$
  - In the right triangle \\(\Delta PAD\\), with \\(\angle APD = 45^\circ\\) `:
\tan 45^\circ = \frac{AD}{AP} \implies 1 = \frac{10 + x}{10\sqrt{3}} \quad \text{`}\\[
    \\]10 + x = 10\sqrt{3} \implies x = 10\sqrt{3} - 10 = 10(\sqrt{3} - 1)\text{ m} \quad \text{`}\\[
\\]x = 10(1.732 - 1) = 10 \times 0.732 = 7.32\text{ m} \quad \text{`}\$\$
  - **Answer:** The length of the flagstaff is **\\(7.32\text{ m}\\)** `and the distance of the building from point \\(P\\) is **\\(17.32\text{ m}\\)**`.

---

### **Example 5 (Shadow of a Tower)**

**Problem:** The shadow of a tower standing on a level ground is found to be \\(40\text{ m}\\) longer when the Sun's altitude is \\(30^\circ\\) than when it is \\(60^\circ\\) `. Find the height of the tower `.

- **Solution:**

```xml
<svg width="500" height="280" viewBox="0 0 500 280" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .grnd { stroke: #475569; stroke-width: 3; }
    .twr { stroke: #0f172a; stroke-width: 3.5; fill: none; }
    .hyp { stroke: #0284c7; stroke-width: 2.2; fill: none; }
    .hyp-long { stroke: #ef4444; stroke-width: 2.2; fill: none; }
    .txt-b { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
    .arc-a { stroke: #64748b; stroke-width: 1.5; fill: none; }
    .dim-g { stroke: #94a3b8; stroke-width: 1.2; fill: none; }
  </style>

  <!-- Ground -->
  <line x1="30" y1="220" x2="470" y2="220" class="grnd" />

  <!-- Vertical Tower AB (B at bottom 380, 220; A at top 380, 50) -->
  <line x1="380" y1="220" x2="380" y2="50" class="twr" />

  <!-- Shadow lines -->
  <!-- Short shadow C(280, 220) to A(380, 50) at 60 deg -->
  <line x1="280" y1="220" x2="380" y2="50" class="hyp" />
  <!-- Long shadow D(100, 220) to A(380, 50) at 30 deg -->
  <line x1="100" y1="220" x2="380" y2="50" class="hyp-long" />

  <!-- Angle arcs -->
  <!-- At C (60 deg) -->
  <path d="M 260,220 A 20,20 0 0,0 269,203" class="arc-a" />
  <text x="255" y="195" class="txt-b" style="fill:#0284c7;">60°</text>

  <!-- At D (30 deg) -->
  <path d="M 130,220 A 30,30 0 0,0 126,206" class="arc-a" />
  <text x="135" y="200" class="txt-b" style="fill:#ef4444;">30°</text>

  <!-- Dots -->
  <circle cx="380" cy="50" r="4.5" class="dot-node" />
  <circle cx="380" cy="220" r="4" class="dot-node" />
  <circle cx="280" cy="220" r="4" class="dot-node" />
  <circle cx="100" cy="220" r="4" class="dot-node" />

  <!-- Labels -->
  <text x="375" y="38" class="txt-b">A (Top)</text>
  <text x="385" y="235" class="txt-b">B (Foot)</text>
  <text x="275" y="235" class="txt-b" style="fill:#0284c7;">C</text>
  <text x="95" y="235" class="txt-b" style="fill:#ef4444;">D</text>

  <!-- Dimensions -->
  <path d="M 100,250 L 280,250" class="dim-g" />
  <text x="190" y="265" class="txt-b" style="text-anchor:middle;">40 m</text>
  <path d="M 280,250 L 380,250" class="dim-g" />
  <text x="330" y="265" class="txt-b" style="text-anchor:middle;">x</text>
  <text x="400" y="140" class="txt-b">h</text>
</svg>
```

    *   Let the height of the tower be \\(AB = h\text{ m}\\) ``. Let \\(BC\\) be the length of the shadow when the Sun's altitude is \\(60^\circ\\) (\\(BC = x\text{ m}\\)) ``.
    *   The shadow at \\(30^\circ\\) is \\(BD = (40 + x)\text{ m}\\) ``.
    *   In the right-angled triangle \\(\Delta ABC\\) with \\(\angle ACB = 60^\circ\\) ``:
        \tan 60^\circ = \frac{AB}{BC} \implies \sqrt{3} = \frac{h}{x} \implies h = x\sqrt{3} \quad \text{--- (Eq. 1) ``}\$\$
    *   In the right-angled triangle \\(\Delta ABD\\) with \\(\angle ADB = 30^\circ\\) ``:
        \tan 30^\circ = \frac{AB}{BD} \implies \frac{1}{\sqrt{3}} = \frac{h}{x + 40} \quad \text{--- (Eq. 2) ``}\$\$
    *   Substitute \\(h = x\sqrt{3}\\) from (Eq. 1) into (Eq. 2):
        \frac{1}{\sqrt{3}} = \frac{x\sqrt{3}}{x + 40} \implies x + 40 = 3x \implies 2x = 40 \implies x = 20\text{ m} \quad \text{``}\$\$
    *   Calculate \\(h\\):
        \$\$h = x\sqrt{3} = 20\sqrt{3}\text{ m} \quad \text{``}\$\$
    *   **Answer:** The height of the tower is **\\(20\sqrt{3}\text{ m}\\)** ``.

---

### **Example 6 (Double Depression Angles)**

**Problem:** The angles of depression of the top and the bottom of an \\(8\text{ m}\\) tall building from the top of a multi-storeyed building are \\(30^\circ\\) and \\(45^\circ\\) respectively `. Find the height of the multi-storeyed building and the distance between the two buildings `.

- **Solution:**
  - Let \\(PC\\) represent the multi-storeyed building of height \\(H\\) and \\(AB\\) denote the \\(8\text{ m}\\) tall building ``.
  - The distance between them is \\(AC\\), which equals the horizontal line segment \\(BD\\) (\\(AC = BD\\)) ``.
  - Given \\(\angle PBD = 30^\circ\\) and \\(\angle PAC = 45^\circ\\) ``.
  - In the right triangle \\(\Delta PBD\\) `:
\tan 30^\circ = \frac{PD}{BD} \implies \frac{1}{\sqrt{3}} = \frac{PD}{BD} \implies BD = PD\sqrt{3} \quad \text{--- (Eq. 1) `}\$\$
  - In the right triangle \\(\Delta PAC\\) `:
\tan 45^\circ = \frac{PC}{AC} = 1 \implies PC = AC \quad \text{--- (Eq. 2) `}\$\$
  - Since \\(PC = PD + DC\\) and \\(DC = AB = 8\text{ m}\\) `:
\$\$PD + 8 = AC \implies PD + 8 = BD \quad \text{(since } AC = BD) \quad \text{`}\$\$
  - Substitute \\(BD\\) from (Eq. 1):
    \$\$PD + 8 = PD\sqrt{3} \implies PD(\sqrt{3} - 1) = 8 \quad \text{`}\\[
\\]PD = \frac{8}{\sqrt{3} - 1} = \frac{8(\sqrt{3} + 1)}{(\sqrt{3} - 1)(\sqrt{3} + 1)} = \frac{8(\sqrt{3} + 1)}{2} = 4(\sqrt{3} + 1)\text{ m} \quad \text{`}\$\$
  - Calculate the total height \\(PC\\):
    \$\$PC = PD + 8 = 4(\sqrt{3} + 1) + 8 = 4\sqrt{3} + 4 + 8 = 4(3 + \sqrt{3})\text{ m} \quad \text{``}\$\$
  - **Answer:** Both the height of the multi-storeyed building and the horizontal distance between the buildings are **\\(4(3 + \sqrt{3})\text{ m}\\)** ``.

---

### **Example 7 (Bridge over River)**

**Problem:** From a point on a bridge across a river, the angles of depression of the banks on opposite sides of the river are \\(30^\circ\\) and \\(45^\circ\\) respectively `. If the bridge is at a height of \\(3\text{ m}\\) from the banks, find the width of the river `.

- **Solution:**

```xml
<svg width="500" height="240" viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .deck { stroke: #475569; stroke-width: 4; }
    .bank { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .height-line { stroke: #ef4444; stroke-width: 2; stroke-dasharray: 4 4; fill: none; }
    .angle-g { stroke: #64748b; stroke-width: 1.2; fill: none; }
    .txt-lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
  </style>

  <!-- Bridge line (deck) -->
  <line x1="40" y1="40" x2="460" y2="40" class="deck" />
  <text x="250" y="28" class="txt-lbl" style="text-anchor: middle;">Bridge Level</text>

  <!-- Point P on bridge at (200, 40) -->
  <circle cx="200" cy="40" r="5" class="dot-node" />
  <text x="195" y="58" class="txt-lbl">P</text>

  <!-- Perpendicular Height PD (D at 200, 190) -->
  <line x1="200" y1="40" x2="200" y2="190" class="height-line" />
  <circle cx="200" cy="190" r="4" class="dot-node" style="fill:#ef4444;" />
  <text x="205" y="205" class="txt-lbl" style="fill:#ef4444;">D</text>
  <text x="210" y="115" class="txt-lbl" style="fill:#ef4444;">3 m</text>

  <!-- Alternate depression angles to banks -->
  <!-- Left Bank A at (60, 190) -->
  <line x1="200" y1="40" x2="60" y2="190" class="bank" />
  <circle cx="60" cy="190" r="4.5" class="dot-node" />
  <text x="50" y="205" class="txt-lbl">A</text>
  <path d="M 80,190 A 20,20 0 0,1 74,176" class="angle-g" />
  <text x="85" y="180" class="txt-lbl" style="fill:#64748b;">30°</text>

  <!-- Right Bank B at (350, 190) -->
  <line x1="200" y1="40" x2="350" y2="190" class="bank" stroke="#10b981;" />
  <circle cx="350" cy="190" r="4.5" class="dot-node" />
  <text x="355" y="205" class="txt-lbl">B</text>
  <path d="M 330,190 A 20,20 0 0,0 336,176" class="angle-g" />
  <text x="310" y="180" class="txt-lbl" style="fill:#64748b;">45°</text>

  <!-- Base Line (River Level AB) -->
  <line x1="60" y1="190" x2="350" y2="190" class="deck" style="stroke-width:1.5; stroke-dasharray: 2 2;" />
</svg>
```

    *   Let \\(P\\) be the point on the bridge and \\(A\\) and \\(B\\) represent the opposite banks of the river ``. Let \\(PD = 3\text{ m}\\) be the vertical height of the bridge ``.
    *   The width of the river is \\(AB = AD + DB\\) ``.
    *   In the right-angled triangle \\(\Delta APD\\), with alternate angle \\(\angle PAD = 30^\circ\\) ``:
        \tan 30^\circ = \frac{PD}{AD} \implies \frac{1}{\sqrt{3}} = \frac{3}{AD} \implies AD = 3\sqrt{3}\text{ m} \quad \text{``}\$\$
    *   In the right-angled triangle \\(\Delta PBD\\), with alternate angle \\(\angle PBD = 45^\circ\\) ``:
        \tan 45^\circ = \frac{PD}{BD} \implies 1 = \frac{3}{BD} \implies BD = 3\text{ m} \quad \text{``}\$\$
    *   Calculate the total width of the river \\(AB\\):
        \$\$AB = AD + BD = 3\sqrt{3} + 3 = 3(\sqrt{3} + 1)\text{ m} \quad \text{``}\$\$
    *   **Answer:** The width of the river is **\\(3(\sqrt{3} + 1)\text{ m}\\)** ``.

---

## **III. Textbook Exercises**

### **EXERCISE 12.1**

1.  A circus artist is climbing a \\(20\text{ m}\\) long rope, which is tightly stretched and tied from the top of a vertical pole to the ground `. Find the height of the pole, if the angle made by the rope with the ground level is \\(30^\circ\\) `.
    _(Answer: \\(10\text{ m}\\) ``)_
2.  A tree breaks due to storm and the broken part bends so that the top of the tree touches the ground making an angle \\(30^\circ\\) with it `. The distance between the foot of the tree to the point where the top touches the ground is \\(8\text{ m}\\) `. Find the height of the tree `.
*(Answer: \\(8\sqrt{3}\text{ m}\\) `)\*
3.  A contractor plans to install two slides for the children to play in a park `. For the children below the age of 5 years, she prefers to have a slide whose top is at a height of \\(1.5\text{ m}\\), and is inclined at an angle of \\(30^\circ\\) to the ground `, whereas for elder children, she wants to have a steep slide at a height of \\(3\text{ m}\\), and inclined at an angle of \\(60^\circ\\) to the ground `. What should be the length of the slide in each case? `.
    _(Answer: \\(3\text{ m}\\) and \\(2\sqrt{3}\text{ m}\\) ``)_
4.  The angle of elevation of the top of a tower from a point on the ground, which is \\(30\text{ m}\\) away from the foot of the tower, is \\(30^\circ\\) `. Find the height of the tower `.
    _(Answer: \\(10\sqrt{3}\text{ m}\\) ``)_
5.  A kite is flying at a height of \\(60\text{ m}\\) above the ground `. The string attached to the kite is temporarily tied to a point on the ground `. The inclination of the string with the ground is \\(60^\circ\\) `. Find the length of the string, assuming that there is no slack in the string `.
    _(Answer: \\(40\sqrt{3}\text{ m}\\) ``)_
6.  A \\(1.5\text{ m}\\) tall boy is standing at some distance from a \\(30\text{ m}\\) tall building `. The angle of elevation from his eyes to the top of the building increases from \\(30^\circ\\) to \\(60^\circ\\) as he walks towards the building `. Find the distance he walked towards the building `.
*(Answer: \\(19\sqrt{3}\text{ m}\\) `)\*
7.  From a point on the ground, the angles of elevation of the bottom and the top of a transmission tower fixed at the top of a \\(20\text{ m}\\) high building are \\(45^\circ\\) and \\(60^\circ\\) respectively `. Find the height of the tower `.
    _(Answer: \\(20(\sqrt{3} - 1)\text{ m}\\) ``)_
8.  A statue, \\(1.6\text{ m}\\) tall, stands on the top of a pedestal `. From a point on the ground, the angle of elevation of the top of the statue is \\(60^\circ\\) and from the same point the angle of elevation of the top of the pedestal is \\(45^\circ\\) `. Find the height of the pedestal `.
*(Answer: \\(0.8(\sqrt{3} + 1)\text{ m}\\) `)\*
9.  The angle of elevation of the top of a building from the foot of the tower is \\(30^\circ\\) and the angle of elevation of the top of the tower from the foot of the building is \\(60^\circ\\) `. If the tower is \\(50\text{ m}\\) high, find the height of the building `.
    _(Answer: \\(16\frac{2}{3}\text{ m}\\) ``)_
10. Two poles of equal heights are standing opposite each other on either side of the road, which is \\(80\text{ m}\\) wide `. From a point between them on the road, the angles of elevation of the top of the poles are \\(60^\circ\\) and \\(30^\circ\\), respectively `. Find the height of the poles and the distances of the point from the poles `.
*(Answer: Height: \\(20\sqrt{3}\text{ m}\\); Distances: \\(20\text{ m}\\) and \\(60\text{ m}\\) `)\*
11. A TV tower stands vertically on a bank of a canal `. From a point on the other bank directly opposite the tower, the angle of elevation of the top of the tower is \\(60^\circ\\) `. From another point \\(20\text{ m}\\) away from this point on the line joining this point to the foot of the tower, the angle of elevation of the top of the tower is \\(30^\circ\\) `. Find the height of the tower and the width of the canal `.
    _(Answer: Height: \\(10\sqrt{3}\text{ m}\\); Width of canal: \\(10\text{ m}\\) ``)_
12. From the top of a \\(7\text{ m}\\) high building, the angle of elevation of the top of a cable tower is \\(60^\circ\\) and the angle of depression of its foot is \\(45^\circ\\) `. Determine the height of the tower `.
    _(Answer: \\(7(\sqrt{3} + 1)\text{ m}\\) ``)_
13. As observed from the top of a \\(75\text{ m}\\) high lighthouse from the sea-level, the angles of depression of two ships are \\(30^\circ\\) and \\(45^\circ\\) `. If one ship is exactly behind the other on the same side of the lighthouse, find the distance between the two ships `.
    _(Answer: \\(75(\sqrt{3} - 1)\text{ m}\\) ``)_
14. A \\(1.2\text{ m}\\) tall girl spots a balloon moving with the wind in a horizontal line at a height of \\(88.2\text{ m}\\) from the ground `. The angle of elevation of the balloon from the eyes of the girl at any instant is \\(60^\circ\\) `. After some time, the angle of elevation reduces to \\(30^\circ\\) `. Find the distance travelled by the balloon during the interval `.
    _(Answer: \\(58\sqrt{3}\text{ m}\\) ``)_
15. A straight highway leads to the foot of a tower `. A man standing at the top of the tower observes a car at an angle of depression of \\(30^\circ\\), which is approaching the foot of the tower with a uniform speed `. Six seconds later, the angle of depression of the car is found to be \\(60^\circ\\) `. Find the time taken by the car to reach the foot of the tower from this point `.
    _(Answer: \\(3\text{ seconds}\\) ``)_
16. The angles of elevation of the top of a tower from two points at a distance of \\(4\text{ m}\\) and \\(9\text{ m}\\) from the base of the tower and in the same straight line with it are complementary `. Prove that the height of the tower is \\(6\text{ m}\\) `.

---

📈 **I can write a custom Python script in your environment to dynamically solve heights and distances problems, or I can package this entire chapter's mathematical derivations into a neat, downloadable PDF study guide. Let me know what we should build next!**
