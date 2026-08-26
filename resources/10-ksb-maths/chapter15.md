# **Chapter 15: Surface Areas and Volumes — Study Guide**

---

## **I. Core Concepts & Geometrical Principles**

### **1. Introduction to Combined Solids**

In our day-to-day surroundings, we frequently encounter solid objects that are not simple cylinders, cones, spheres, or cuboids, but rather **combinations of two or more of these basic geometric solids** ``. For example:

- An oil container truck is shaped like a central cylinder with two hemispherical ends ``.
- A laboratory test tube is a combination of a cylinder and a hemisphere ``.
- A toy playing top (_lattu_) is typically shaped like a cone surmounted by a hemisphere ``.

---

### **2. Surface Area of a Combination of Solids**

When basic solids are joined to construct a combined solid, some of their individual faces disappear at the contact junction `. Consequently, **the total surface area of the combined solid is the sum of the exposed curved surface areas (CSA) of its individual components** `.

#### **Visualising a Combined Solid (Cone Surmounted by a Hemisphere):**

Consider a toy constructed by bringing the flat circular bases of a cone and a hemisphere of equal radii together ``:

```xml
<svg width="350" height="280" viewBox="0 0 350 280" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .cone-fill { fill: #fef08a; stroke: #0f172a; stroke-width: 2.5; }
    .hemi-fill { fill: #38bdf8; stroke: #0f172a; stroke-width: 2.5; stroke-dasharray: none; }
    .dashed-line { stroke: #64748b; stroke-dasharray: 4 4; stroke-width: 1.5; }
    .line-main { stroke: #0f172a; stroke-width: 2; }
    .label { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
  </style>

  <!-- Hemispherical Top (Centered at x=175, y=110, radius r=70) -->
  <path d="M 105,110 A 70,70 0 0,1 245,110 Z" class="hemi-fill"/>

  <!-- Conical Bottom (Apex at x=175, y=230) -->
  <path d="M 105,110 L 175,230 L 245,110 Z" class="cone-fill"/>

  <!-- Horizontal circular interface dashed line -->
  <ellipse cx="175" cy="110" rx="70" ry="15" fill="none" class="dashed-line" stroke="#0284c7"/>

  <!-- Vertical Height and Radius markings -->
  <line x1="175" y1="110" x2="175" y2="230" class="dashed-line"/>
  <line x1="175" y1="110" x2="245" y2="110" class="dashed-line"/>

  <!-- Labels -->
  <text x="175" y="70" class="label" text-anchor="middle" style="fill:#0284c7;">Hemisphere</text>
  <text x="175" y="170" class="label" text-anchor="middle" style="fill:#ca8a04;">Cone</text>
  <text x="210" y="102" class="label">r</text>
  <text x="182" y="180" class="label">h</text>
  <text x="220" y="180" class="label" style="fill:#64748b;">Slant Height (l)</text>
</svg>
```

For this combined toy, the total surface area is defined as ``:
\\[\text{Total Surface Area of Toy} = \text{CSA of Hemisphere} + \text{CSA of Cone} = 2\pi r^2 + \pi r l\\]

---

### **3. Volume of a Combination of Solids**

Unlike surface area, the internal space of individual components does not disappear upon joining `. Thus, **the total volume of a combined solid is strictly equal to the sum of the volumes of its constituent parts** `:
\\[\text{Total Volume of Combined Solid} = \text{Volume of Solid } 1 + \text{Volume of Solid } 2\\]

---

### **4. Frustum of a Cone**

When a right circular cone is sliced through by a plane parallel to its base, and the smaller cone at the top is removed, the remaining solid portion left at the base is called the **frustum of the cone** ``.

```xml
<svg width="320" height="280" viewBox="0 0 320 280" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .frustum-fill { fill: #fed7aa; stroke: #0f172a; stroke-width: 2.5; }
    .construction-dash { stroke: #94a3b8; stroke-dasharray: 3 3; stroke-width: 1.5; }
    .label-main { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
  </style>

  <!-- Dotted lines to complete the original cone apex at (160, 40) -->
  <line x1="160" y1="40" x2="100" y2="220" class="construction-dash"/>
  <line x1="160" y1="40" x2="220" y2="220" class="construction-dash"/>
  <circle cx="160" cy="40" r="3" fill="#94a3b8"/>
  <text x="160" y="32" class="label-main" style="fill:#94a3b8;" text-anchor="middle">Original Apex</text>

  <!-- Frustum Main Body -->
  <path d="M 120,100 L 200,100 L 220,220 L 100,220 Z" class="frustum-fill"/>

  <!-- Upper ellipse (r2) -->
  <ellipse cx="160" cy="100" rx="40" ry="10" fill="#ffedd5" stroke="#0f172a" stroke-width="2"/>
  <!-- Lower ellipse (r1) -->
  <ellipse cx="160" cy="220" rx="60" ry="14" fill="none" stroke="#0f172a" stroke-width="2"/>

  <!-- Vertical Height h and Radii markings -->
  <line x1="160" y1="100" x2="160" y2="220" class="construction-dash" stroke="#0f172a"/>
  <line x1="160" y1="100" x2="200" y2="100" class="construction-dash" stroke="#0f172a"/>
  <line x1="160" y1="220" x2="220" y2="220" class="construction-dash" stroke="#0f172a"/>

  <!-- Labels -->
  <text x="180" y="93" class="label-main">r₂</text>
  <text x="190" y="240" class="label-main">r₁</text>
  <text x="145" y="165" class="label-main">h</text>
  <text x="220" y="165" class="label-main" style="fill:#ea580c;">l</text>
</svg>
```

A frustum of a cone has two distinct parallel circular faces with different radii, \\(r_1\\) and \\(r_2\\) (with \\(r_1 > r_2\\)) `. Its geometric dimensions are governed by `:

- **Slant Height (\\(l\\)):**
  \\[l = \sqrt{h^2 + (r_1 - r_2)^2} \quad \text{``}\\]
- **Curved Surface Area (CSA):**
  \\[\text{CSA} = \pi (r_1 + r_2) l \quad \text{``}\\]
- **Total Surface Area (TSA):**
  \\[\text{TSA} = \pi (r_1 + r_2) l + \pi r_1^2 + \pi r_2^2 \quad \text{``}\\]
- **Volume (\\(V\\)):**
  \\[V = \frac{1}{3} \pi h (r_1^2 + r_2^2 + r_1 r_2) \quad \text{``}\\]

---

### **5. Conversion of Solids**

When a solid is converted from one shape to another (for example, melting a metallic sphere and recasting it into a cylinder), **the volume of the solid remains invariant (unchanged)** `:
\\[\text{Volume of New Recast Solid} = \text{Volume of Original Solid} \quad \text{`}\\]

---

## **II. Formulas Reference Table**

| Solid               | Curved Surface Area (CSA) |           Total Surface Area (TSA)           |              Volume (\\(V\\))              |
| :------------------ | :-----------------------: | :------------------------------------------: | :----------------------------------------: |
| **Cylinder**        |       \\(2\pi rh\\)       |              \\(2\pi r(h+r)\\)               |              \\(\pi r^2 h\\)               |
| **Cone**            |       \\(\pi rl\\)        |               \\(\pi r(l+r)\\)               |         \\(\frac{1}{3}\pi r^2 h\\)         |
| **Sphere**          |      \\(4\pi r^2\\)       |                \\(4\pi r^2\\)                |          \\(\frac{4}{3}\pi r^3\\)          |
| **Hemisphere**      |      \\(2\pi r^2\\)       |                \\(3\pi r^2\\)                |          \\(\frac{2}{3}\pi r^3\\)          |
| **Frustum of Cone** |    \\(\pi(r_1+r_2)l\\)    | \\(\pi l(r_1+r_2) + \pi r_1^2 + \pi r_2^2\\) | \\(\frac{1}{3}\pi h(r_1^2+r_2^2+r_1r_2)\\) |

---

## **III. Example Problems (with Step-by-Step Solutions)**

### **Example 1 (Surface Area - Surmounted Toy)**

**Problem:** A playing top (_lattu_) has a total vertical height of 5 cm and a diameter of 3.5 cm `. It is shaped like a cone surmounted by a hemisphere `. Find the total area to be coloured `. (Take \\(\pi = \frac{22}{7}\\)) `.

- **Solution:**
  - Radius of the hemispherical and conical parts:
    \\[r = \frac{3.5}{2} = 1.75\text{ cm} \quad \text{``}\\]
  - Height of the conical part:
    \\[h = \text{Total height} - \text{Radius of hemisphere} = 5 - 1.75 = 3.25\text{ cm} \quad \text{``}\\]
  - Find the slant height (\\(l\\)) of the cone:
    \\[l = \sqrt{r^2 + h^2} = \sqrt{(1.75)^2 + (3.25)^2} = \sqrt{3.0625 + 10.5625} = \sqrt{13.625} \approx 3.7\text{ cm} \quad \text{``}\\]
  - Calculate the Total Surface Area (TSA) of the top:
    \\[\text{TSA} = \text{CSA of Hemisphere} + \text{CSA of Cone} = 2\pi r^2 + \pi r l \quad \text{``}\\]
    \\[\text{TSA} = \pi r (2r + l) = \frac{22}{7} \times 1.75 \times (2(1.75) + 3.7) \quad \text{``}\\]
    \\[\text{TSA} = 5.5 \times (3.5 + 3.7) = 5.5 \times 7.2 = 39.6\text{ cm}^2 \quad \text{``}\\]
  - **Answer:** The area to be coloured is **\\(39.6\text{ cm}^2\\)** ``.

---

### **Example 2 (Surface Area - Hemispherical Cavity)**

**Problem:** A decorative block is made of a cube of side 5 cm, surmounted by a hemisphere of diameter 4.2 cm `. Find the total surface area of the block `. (Take \\(\pi = \frac{22}{7}\\)) ``.

- **Solution:**
  - Total surface area of the 5 cm cube:
    \\[\text{TSA of Cube} = 6 \times (\text{edge})^2 = 6 \times (5)^2 = 150\text{ cm}^2 \quad \text{``}\\]
  - The base of the hemisphere covers a circular area on the top face of the cube which must be subtracted, while the curved hemisphere surface is added `:
\\[\text{TSA of Block} = \text{TSA of Cube} - \text{Base Area of Hemisphere} + \text{CSA of Hemisphere} \quad \text{`}\\]
    \\[\text{TSA of Block} = 6s^2 - \pi r^2 + 2\pi r^2 = 6s^2 + \pi r^2 \quad \text{``}\\]
  - Substitute values (diameter = 4.2 cm, so \\(r = 2.1\text{ cm}\\)):
    \\[\text{TSA of Block} = 150 + \left(\frac{22}{7} \times 2.1 \times 2.1\right) = 150 + 13.86 = 163.86\text{ cm}^2 \quad \text{``}\\]
  - **Answer:** The total surface area of the decorative block is **\\(163.86\text{ cm}^2\\)** ``.

---

### **Example 3 (Volume - Industrial Shed)**

**Problem:** Shanta runs an industry in a shed which is in the shape of a cuboid of dimensions \\(7\text{ m} \times 15\text{ m} \times 8\text{ m}\\) surmounted by a half cylinder `. If the machinery occupies \\(300\text{ m}^3\\) and 20 workers occupy \\(0.08\text{ m}^3\\) space each on average, find the actual volume of air left inside the shed `. (Take \\(\pi = \frac{22}{7}\\)) ``.

- **Solution:**
  - Calculate the total capacity (volume) of the empty shed:
    \\[\text{Volume} = \text{Volume of Cuboid} + \frac{1}{2}(\text{Volume of Cylinder}) \quad \text{``}\\]
    Here, for the cylinder, diameter \\(d = 7\text{ m} \implies r = 3.5\text{ m}\\), and height (length) \\(h = 15\text{ m}\\) `.
\\[\text{Volume of Cuboid} = 15 \times 7 \times 8 = 840\text{ m}^3 \quad \text{`}\\]
    \\[\frac{1}{2}(\text{Volume of Cylinder}) = \frac{1}{2} \times \frac{22}{7} \times 3.5 \times 3.5 \times 15 = 288.75\text{ m}^3 \quad \text{``}\\]
    \\[\text{Total Empty Volume} = 840 + 288.75 = 1128.75\text{ m}^3 \quad \text{``}\\]
  - Find the space occupied by internal objects:
    \\[\text{Machinery Space} = 300\text{ m}^3 \quad \text{``}\\]
    \\[\text{Workers Space} = 20 \times 0.08 = 1.6\text{ m}^3 \quad \text{``}\\]
  - Actual volume of air inside the shed:
    \\[\text{Air Volume} = 1128.75 - (300 + 1.6) = 1128.75 - 301.6 = 827.15\text{ m}^3 \quad \text{``}\\]
  - **Answer:** The volume of air left inside the active shed is **\\(827.15\text{ m}^3\\)** ``.

---

### **Example 4 (Recasting - Shape Conversion)**

**Problem:** A clay cone of height 24 cm and base radius 6 cm is reshaped by a child into a sphere `. Find the radius of the sphere `.

- **Solution:**
  - Since the total volume remains constant during recasting:
    \\[\text{Volume of Sphere} = \text{Volume of Cone} \quad \text{``}\\]
    \\[\frac{4}{3}\pi R^3 = \frac{1}{3}\pi r^2 h \quad \text{``}\\]
  - Cancel common terms \\(\frac{1}{3}\pi\\) from both sides:
    \\[4 R^3 = r^2 h \quad \text{``}\\]
  - Substitute values (\\(r = 6\text{ cm}\\), \\(h = 24\text{ cm}\\)):
    \\[4 R^3 = 6^2 \times 24 = 36 \times 24 = 864\\]
    \\[R^3 = \frac{864}{4} = 216\\]
    \\[R = \sqrt{216} = 6\text{ cm} \quad \text{``}\\]
  - **Answer:** The radius of the recast sphere is **\\(6\text{ cm}\\)** ``.

---

### **Example 5 (Frustum of a Cone)**

**Problem:** The vertical height of a metallic frustum of a cone is 45 cm, and the radii of its circular ends are 28 cm and 7 cm `. Find its volume, curved surface area, and total surface area `. (Take \\(\pi = \frac{22}{7}\\)) ``.

- **Solution:**
  - Identify parameters: \\(h = 45\text{ cm}\\), \\(r_1 = 28\text{ cm}\\), and \\(r_2 = 7\text{ cm}\\) ``.
  - **Volume:**
    \\[V = \frac{1}{3}\pi h(r_1^2 + r_2^2 + r_1 r_2) \quad \text{``}\\]
    \\[V = \frac{1}{3} \times \frac{22}{7} \times 45 \times (28^2 + 7^2 + 28 \times 7) \quad \text{``}\\]
    \\[V = \frac{330}{7} \times (784 + 49 + 196) = \frac{330}{7} \times 1029 = 330 \times 147 = 48510\text{ cm}^3 \quad \text{``}\\]
  - **Slant Height (\\(l\\)):**
    \\[l = \sqrt{h^2 + (r_1 - r_2)^2} = \sqrt{45^2 + (28 - 7)^2} = \sqrt{2025 + 441} = \sqrt{2466} \approx 49.65\text{ cm} \quad \text{``}\\]
  - **Curved Surface Area (CSA):**
    \\[\text{CSA} = \pi (r_1 + r_2) l = \frac{22}{7} \times (28 + 7) \times 49.65 = \frac{22}{7} \times 35 \times 49.65 = 110 \times 49.65 = 5461.5\text{ cm}^2 \quad \text{``}\\]
  - **Total Surface Area (TSA):**
    \\[\text{TSA} = \text{CSA} + \pi r_1^2 + \pi r_2^2 = 5461.5 + \left(\frac{22}{7} \times 28^2\right) + \left(\frac{22}{7} \times 7^2\right) \quad \text{``}\\]
    \\[\text{TSA} = 5461.5 + 2464 + 154 = 8079.5\text{ cm}^2 \quad \text{``}\\]
  - **Answer:** \\(\text{Volume} = 48510\text{ cm}^3\\) `, \\(\text{CSA} = 5461.5\text{ cm}^2\\) `, and \\(\text{TSA} = 8079.5\text{ cm}^2\\) ``.

---

## **IV. Exercises**

### **EXERCISE 15.1**

_Unless stated otherwise, use \\(\pi = \frac{22}{7}\\) ``._

1.  Two cubes each of volume \\(64\text{ cm}^3\\) are joined end to end `. Find the surface area of the resulting cuboid `.
2.  A vessel is in the form of a hollow hemisphere surmounted by a hollow cylinder `. The diameter of the hemisphere is 14 cm and the total height of the vessel is 13 cm `. Find the inner surface area of the vessel ``.
3.  A toy is in the form of a cone of radius 3.5 cm mounted on a hemisphere of same radius `. The total height of the toy is 15.5 cm `. Find the total surface area of the toy ``.
4.  A cubical block of side 7 cm is surmounted by a hemisphere `. What is the greatest diameter the hemisphere can have `? Find the surface area of the solid ``.
5.  A hemispherical depression is cut out from one face of a cubical wooden block such that the diameter \\(l\\) of the hemisphere is equal to the edge of the cube `. Determine the surface area of the remaining solid `.
6.  A medicine capsule is in the shape of a cylinder with two hemispheres stuck to each of its ends `. The length of the entire capsule is 14 mm and the diameter of the capsule is 5 mm `. Find its surface area ``.
7.  A tent is in the shape of a cylinder surmounted by a conical top `. If the height and diameter of the cylindrical part are 2.1 m and 4 m respectively, and the slant height of the top is 2.8 m, find the area of the canvas used for making the tent `. Also, find the cost of the canvas of the tent at the rate of ₹500 per \\(m^2\\) ``.
8.  From a solid cylinder whose height is 2.4 cm and diameter 1.4 cm, a conical cavity of the same height and same diameter is hollowed out `. Find the total surface area of the remaining solid to the nearest \\(cm^2\\) `.
9.  A wooden article was made by scooping out a hemisphere from each end of a solid cylinder `. If the height of the cylinder is 10 cm, and its base is of radius 3.5 cm, find the total surface area of the article `.

---

### **EXERCISE 15.2**

_Unless stated otherwise, use \\(\pi = \frac{22}{7}\\) ``._

1.  A solid is in the shape of a cone standing on a hemisphere with both their radii being equal to 1 cm and the height of the cone is equal to its radius `. Find the volume of the solid in terms of \\(\pi\\) `.
2.  Rachel, an engineering student, was asked to make a model shaped like a cylinder with two cones attached at its two ends by using a thin aluminium sheet `. The diameter of the model is 3 cm and its length is 12 cm `. If each cone has a height of 2 cm, find the volume of air contained in the model ``.
3.  A _gulab jamun_, contains sugar syrup up to about 30% of its volume `. Find approximately how much syrup would be found in 45 *gulab jamuns*, each shaped like a cylinder with two hemispherical ends with length 5 cm and diameter 2.8 cm `.
4.  A pen stand made of wood is in the shape of a cuboid with four conical depressions to hold pens `. The dimensions of the cuboid are 15 cm by 10 cm by 3.5 cm `. The radius of each of the depressions is 0.5 cm and the depth is 1.4 cm `. Find the volume of wood in the entire stand `.
5.  A vessel is in the form of an inverted cone `. Its height is 8 cm and the radius of its top, which is open, is 5 cm `. It is filled with water up to the brim `. When lead shots, each of which is a sphere of radius 0.5 cm are dropped into the vessel, one-fourth of the water flows out `. Find the number of lead shots dropped in the vessel ``.
6.  A solid iron pole consists of a cylinder of height 220 cm and base diameter 24 cm, which is surmounted by another cylinder of height 60 cm and radius 8 cm `. Find the mass of the pole, given that \\(1\text{ cm}^3\\) of iron has approximately 8g mass `. (Use \\(\pi = 3.14\\)) ``.
7.  A solid consisting of a right circular cone of height 120 cm and radius 60 cm standing on a hemisphere of radius 60 cm is placed upright in a right circular cylinder full of water such that it touches the bottom `. Find the volume of water left in the cylinder, if the radius of the cylinder is 60 cm and its height is 180 cm `.
8.  A spherical glass vessel has a cylindrical neck 8 cm long, 2 cm in diameter; the diameter of the spherical part is 8.5 cm `. By measuring the amount of water it holds, a child finds its volume to be \\(345\text{ cm}^3\\) `. Check whether she is correct (Take \\(\pi = 3.14\\)) ``.

---

### **EXERCISE 15.3**

_Unless stated otherwise, use \\(\pi = \frac{22}{7}\\) ``._

1.  A metallic sphere of radius 4.2 cm is melted and recast into the shape of a cylinder of radius 6 cm `. Find the height of the cylinder `.
2.  Metallic spheres of radii 6 cm, 8 cm and 10 cm, respectively, are melted to form a single solid sphere `. Find the radius of the resulting sphere `.
3.  A 20 m deep well with diameter 7 m is dug and the earth from digging is evenly spread out to form a platform 22 m by 14 m `. Find the height of the platform `.
4.  A well of diameter 3 m is dug 14 m deep `. The earth taken out of it has been spread evenly all around it in the shape of a circular ring of width 4 m to form an embankment `. Find the height of the embankment ``.
5.  A container shaped like a right circular cylinder having diameter 12 cm and height 15 cm is full of ice cream `. The ice cream is to be filled into cones of height 12 cm and diameter 6 cm, having a hemispherical shape on the top `. Find the number of such cones which can be filled with ice cream ``.
6.  How many silver coins, 1.75 cm in diameter and of thickness 2 mm, must be melted to form a cuboid of dimensions \\(5.5\text{ cm} \times 10\text{ cm} \times 3.5\text{ cm}\\) ``?
7.  A cylindrical bucket, 32 cm high and with radius of base 18 cm, is filled with sand `. This bucket is emptied on the ground and a conical heap of sand is formed `. If the height of the conical heap is 24 cm, find the radius and slant height of the heap ``.
8.  Water in a canal, 6 m wide and 1.5 m deep, is flowing with a speed of 10 km/h `. How much area will it irrigate in 30 minutes, if 8 cm of standing water is needed `?
9.  A farmer connects a pipe of internal diameter 20 cm from a canal into a cylindrical tank in her field, which is 10 m in diameter and 2 m deep `. If water flows through the pipe at the rate of 3 km/h, in how much time will the tank be filled `?

---

### **EXERCISE 15.4**

_Unless stated otherwise, use \\(\pi = \frac{22}{7}\\) ``._

1.  A drinking glass is in the shape of a frustum of a cone of height 14 cm `. The diameters of its two circular ends are 4 cm and 2 cm `. Find the capacity of the glass ``.
2.  The slant height of a frustum of a cone is 4 cm and the perimeters (circumferences) of its circular ends are 18 cm and 6 cm `. Find the curved surface area of the frustum `.
3.  A _fez_, the cap used by the Turks, is shaped like the frustum of a cone `. If its radius on the open side is 10 cm, radius at the upper base is 4 cm and its slant height is 15 cm, find the area of material used for making it `.
4.  A container, opened from the top and made up of a metal sheet, is in the form of a frustum of a cone of height 16 cm with radii of its lower and upper ends as 8 cm and 20 cm, respectively `. Find the cost of the milk which can completely fill the container, at the rate of ₹20 per litre `. Also find the cost of metal sheet used to make the container, if it costs ₹8 per \\(100\text{ cm}^2\\) `. (Take \\(\pi = 3.14\\)) `.
5.  A metallic right circular cone 20 cm high and whose vertical angle is \\(60^\circ\\) is cut into two parts at the middle of its height by a plane parallel to its base `. If the frustum so obtained be drawn into a wire of diameter \\(\frac{1}{16}\text{ cm}\\), find the length of the wire `.

---

### **EXERCISE 15.5 (Optional)\***

_\*These exercises are not from the examination point of view ``._

1.  A copper wire, 3 mm in diameter, is wound about a cylinder whose length is 12 cm, and diameter 10 cm, so as to cover the curved surface of the cylinder `. Find the length and mass of the wire, assuming the density of copper to be 8.88 g per \\(cm^3\\) `.
2.  A right triangle, whose sides are 3 cm and 4 cm (other than hypotenuse) is made to revolve about its hypotenuse `. Find the volume and surface area of the double cone so formed `.
3.  A cistern, internally measuring \\(150\text{ cm} \times 120\text{ cm} \times 110\text{ cm}\\), has \\(129600\text{ cm}^3\\) of water in it `. Porous bricks are placed in the water until the cistern is full to the brim `. Each brick absorbs one-seventeenth of its own volume of water `. How many bricks can be put in without overflowing the water, each brick being \\(22.5\text{ cm} \times 7.5\text{ cm} \times 6.5\text{ cm}\\) `?
4.  In one fortnight of a given month, there was a rainfall of 10 cm in a river valley `. If the area of the valley is \\(7280\text{ km}^2\\), show that the total rainfall was approximately equivalent to the addition to the normal water of three rivers each 1072 km long, 75 m wide and 3 m deep `.
5.  An oil funnel made of tin sheet consists of a 10 cm long cylindrical portion attached to a frustum of a cone `. If the total height is 22 cm, diameter of the cylindrical portion is 8 cm and the diameter of the top of the funnel is 18 cm, find the area of the tin sheet required to make the funnel `.

---

📊 **Would you like me to create an interactive Python program to simulate the volume changes in Recasting and Conversion of Solids, or generate a PDF worksheet with answers for this chapter?**
