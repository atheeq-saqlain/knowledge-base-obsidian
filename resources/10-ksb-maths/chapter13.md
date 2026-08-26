# **Chapter 13: Statistics — Study Guide**

---

## **I. Core Concepts & Algebraic Principles**

### **1. Introduction to Measures of Central Tendency**

In real-world scenarios, raw data is often too large to interpret directly. To make meaningful observations, ungrouped data is condensed into a structured **grouped frequency distribution**. To analyze the middle-most characteristics of this data, three primary numerical representatives—known as **measures of central tendency**—are calculated: **Mean**, **Median**, and **Mode**.

---

### **2. Mean of Grouped Data (Average)**

The **mean** (\\(\overline{x}\\)) is the sum of the values of all observations divided by the total number of observations. For grouped data, we assume the frequency of each class interval is centered around its **class mark** (mid-point).

\\[\text{Class Mark } (x_i) = \frac{\text{Upper Class Limit} + \text{Lower Class Limit}}{2} \quad \text{}\\]

There are three algebraic methods to calculate the mean of grouped data, depending on the scale of the numerical values:

```xml
<svg width="620" height="200" viewBox="0 0 620 200" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .card { fill: #ffffff; stroke: #cbd5e1; stroke-width: 1; }
    .title-direct { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0284c7; font-weight: bold; text-anchor: middle; }
    .title-assumed { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #16a34a; font-weight: bold; text-anchor: middle; }
    .title-step { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #db2777; font-weight: bold; text-anchor: middle; }
    .math-text { font-family: 'Consolas', 'Courier New', monospace; font-size: 12px; fill: #0f172a; text-anchor: middle; }
    .desc-text { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #64748b; text-anchor: middle; }
  </style>

  <!-- Card 1: Direct Method -->
  <g transform="translate(15, 15)">
    <rect x="0" y="0" width="180" height="170" rx="6" class="card" />
    <text x="90" y="30" class="title-direct">1. Direct Method</text>
    <text x="90" y="60" class="desc-text">Used for small</text>
    <text x="90" y="75" class="desc-text">numerical values.</text>
    <text x="90" y="115" class="math-text" font-weight="bold" style="font-size:14px;">x̄ = Σ(f_i x_i) / Σf_i</text>
    <text x="90" y="145" class="desc-text" style="font-style: italic;">[Passage 648]</text>
  </g>

  <!-- Card 2: Assumed Mean Method -->
  <g transform="translate(220, 15)">
    <rect x="0" y="0" width="180" height="170" rx="6" class="card" />
    <text x="90" y="30" class="title-assumed">2. Assumed Mean Method</text>
    <text x="90" y="60" class="desc-text">Reduces calculations by</text>
    <text x="90" y="75" class="desc-text">using deviation (d_i = x_i - a).</text>
    <text x="90" y="115" class="math-text" font-weight="bold" style="font-size:14px;">x̄ = a + Σ(f_i d_i) / Σf_i</text>
    <text x="90" y="145" class="desc-text" style="font-style: italic;">[Passage 658]</text>
  </g>

  <!-- Card 3: Step-Deviation Method -->
  <g transform="translate(425, 15)">
    <rect x="0" y="0" width="180" height="170" rx="6" class="card" />
    <text x="90" y="30" class="title-step">3. Step-Deviation</text>
    <text x="90" y="55" class="desc-text">Best for large values</text>
    <text x="90" y="70" class="desc-text">with common class width (h).</text>
    <text x="90" y="105" class="math-text" font-weight="bold" style="font-size:13px;">u_i = (x_i - a) / h</text>
    <text x="90" y="125" class="math-text" font-weight="bold" style="font-size:13px;">x̄ = a + h * [Σ(f_i u_i) / Σf_i]</text>
    <text x="90" y="150" class="desc-text" style="font-style: italic;">[Passage 661]</text>
  </g>
</svg>
```

---

### **3. Mode of Grouped Data**

The **mode** is the value of the observation that occurs most frequently. In a grouped distribution, we cannot determine the mode simply by looking at the frequencies. We must first locate the **modal class** (the class interval with the maximum frequency) and then apply the following formula:

\\[\text{Mode} = l + \left( \frac{f_1 - f_0}{2f_1 - f_0 - f_2} \right) \times h \quad \text{}\\]

Where:

- **\\(l\\)** = lower limit of the modal class.
- **\\(h\\)** = size of the class interval (assuming equal class sizes).
- **\\(f_1\\)** = frequency of the modal class.
- **\\(f_0\\)** = frequency of the class preceding the modal class.
- **\\(f_2\\)** = frequency of the class succeeding the modal class.

---

### **4. Median of Grouped Data**

The **median** is the measure of central tendency representing the value of the middle-most observation. To calculate the median for grouped data:

1.  Construct a **cumulative frequency (\\(cf\\)) table** (typically of the "less than" type).
2.  Find \\(\frac{n}{2}\\), where \\(n\\) is the total number of observations (total frequency).
3.  Locate the **median class**, which is the class whose cumulative frequency is greater than and closest to \\(\frac{n}{2}\\).
4.  Apply the interpolation formula:

\\[\text{Median} = l + \left( \frac{\frac{n}{2} - cf}{f} \right) \times h \quad \text{}\\]

Where:

- **\\(l\\)** = lower limit of the median class.
- **\\(n\\)** = total number of observations.
- **\\(cf\\)** = cumulative frequency of the class preceding the median class.
- **\\(f\\)** = frequency of the median class.
- **\\(h\\)** = class size.

---

### **5. Empirical Relationship Between the Three Measures**

There is a fundamental empirical relationship that connects all three measures of central tendency for a given distribution:

\\[3 \text{ Median} = \text{Mode} + 2 \text{ Mean} \quad \text{}\\]

---

### **6. Graphical Representation of Cumulative Frequency Distributions (Ogives)**

A cumulative frequency distribution can be plotted as a curve called an **Ogive** (pronounced _'ojeev'_):

1.  **"Less Than" Ogive:** Plot points with the **upper limits** of the class intervals as x-coordinates and their corresponding **cumulative frequencies** as y-coordinates.
2.  **"More Than" Ogive:** Plot points with the **lower limits** of the class intervals as x-coordinates and their corresponding **cumulative frequencies** as y-coordinates.

```xml
<svg width="400" height="260" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .axis { stroke: #475569; stroke-width: 1.5; fill: none; }
    .grid { stroke: #cbd5e1; stroke-width: 0.5; stroke-dasharray: 2 2; }
    .less-than-curve { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .more-than-curve { stroke: #16a34a; stroke-width: 2.5; fill: none; }
    .indicator-line { stroke: #ef4444; stroke-width: 1.5; stroke-dasharray: 4 4; fill: none; }
    .point-dot { fill: #0f172a; }
    .intersection-dot { fill: #ef4444; }
    .label { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #334155; }
    .label-bold { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #0f172a; font-weight: bold; }
  </style>

  <!-- Background Grid lines -->
  <line x1="60" y1="50" x2="350" y2="50" class="grid"/>
  <line x1="60" y1="120" x2="350" y2="120" class="grid"/>
  <line x1="60" y1="190" x2="350" y2="190" class="grid"/>
  <line x1="205" y1="40" x2="205" y2="210" class="grid"/>

  <!-- Axis Lines (Origin at 60, 210) -->
  <line x1="60" y1="30" x2="60" y2="210" class="axis"/>
  <line x1="60" y1="210" x2="360" y2="210" class="axis"/>

  <!-- Axis Labels -->
  <text x="365" y="215" class="label-bold">Class Limits</text>
  <text x="50" y="20" class="label-bold" text-anchor="middle">cf</text>
  <text x="45" y="214" class="label">0</text>
  <text x="45" y="124" class="label">n/2</text>

  <!-- Less than Ogive Curve -->
  <path d="M 60,200 C 110,180 160,150 205,120 C 250,90 300,60 340,45" class="less-than-curve"/>
  <text x="300" y="35" class="label" style="fill:#0284c7; font-weight:bold;">'Less than' Ogive</text>

  <!-- More than Ogive Curve -->
  <path d="M 60,40 C 110,55 160,90 205,120 C 250,150 300,180 340,195" class="more-than-curve"/>
  <text x="300" y="185" class="label" style="fill:#16a34a; font-weight:bold;">'More than' Ogive</text>

  <!-- Intersection Indicator (Red dashed line) -->
  <line x1="205" y1="120" x2="205" y2="210" class="indicator-line"/>
  <line x1="60" y1="120" x2="205" y2="120" class="indicator-line"/>

  <!-- Dots -->
  <circle cx="205" cy="120" r="5" class="intersection-dot"/>

  <!-- Intersection Labels -->
  <text x="212" y="115" class="label-bold" style="fill:#ef4444;">P (Intersection)</text>
  <text x="205" y="225" class="label-bold" style="fill:#ef4444;" text-anchor="middle">Median</text>
</svg>
```

- **Finding the Median Graphically:** The x-coordinate of the point of intersection of the "less than" and "more than" ogives represents the exact **median** of the distribution. Alternatively, you can locate \\(\frac{n}{2}\\) on the y-axis, draw a horizontal line to meet the "less than" ogive, and project a perpendicular down to the x-axis.

---

## **II. Step-by-Step Solved Examples**

### **Example 1 (Calculating the Mean via Direct vs. Assumed Mean Methods)**

**Problem:** The table below presents the marks obtained by \\(30\\) students of Class X in a Mathematics test. Convert this into a grouped distribution of class size \\(15\\) and calculate the mean using the Direct and Assumed Mean methods.

\\[\text{Raw Marks Data: } 10, 20, 36 (3 \text{ times}), 40 (4), 50 (3), 56 (2), 60 (4), 70 (4), 72 (1), 80 (1), 88 (2), 92 (3), 95 (1) \quad \text{}\\]

- **Step 1: Form Grouped Frequency Table**:
  - \\(10-25\\): \\(10, 20 \implies f_1 = 2\\)
  - \\(25-40\\): \\(36 (3 \text{ times}) \implies f_2 = 3\\)
  - \\(40-55\\): \\(40 (4 \text{ times}), 50 (3 \text{ times}) \implies f_3 = 7\\)
  - \\(55-70\\): \\(56 (2), 60 (4) \implies f_4 = 6\\)
  - \\(70-85\\): \\(70 (4), 72 (1), 80 (1) \implies f_5 = 6\\)
  - \\(85-100\\): \\(88 (2), 92 (3), 95 (1) \implies f_6 = 6\\)

- **Step 2: Tabulate Calculations with Class Marks (\\(x_i\\)) and Deviations (\\(d_i\\))**:
  Let the Assumed Mean \\(a = 47.5\\). Hence, \\(d_i = x_i - 47.5\\).

| Class Interval |   Frequency (\\(f_i\\))   | Class Mark (\\(x_i\\)) |           \\(f_i x_i\\)           | Deviation (\\(d_i\\)) |         \\(f_i d_i\\)          |
| :------------- | :-----------------------: | :--------------------: | :-------------------------------: | :-------------------: | :----------------------------: |
| \\(10-25\\)    |          \\(2\\)          |       \\(17.5\\)       |            \\(35.0\\)             |      \\(-30.0\\)      |           \\(-60\\)            |
| \\(25-40\\)    |          \\(3\\)          |       \\(32.5\\)       |            \\(97.5\\)             |      \\(-15.0\\)      |           \\(-45\\)            |
| \\(40-55\\)    |          \\(7\\)          |       \\(47.5\\)       |            \\(332.5\\)            |       \\(0.0\\)       |            \\(0\\)             |
| \\(55-70\\)    |          \\(6\\)          |       \\(62.5\\)       |            \\(375.0\\)            |      \\(15.0\\)       |            \\(90\\)            |
| \\(70-85\\)    |          \\(6\\)          |       \\(77.5\\)       |            \\(465.0\\)            |      \\(30.0\\)       |           \\(180\\)            |
| \\(85-100\\)   |          \\(6\\)          |       \\(92.5\\)       |            \\(555.0\\)            |      \\(45.0\\)       |           \\(270\\)            |
| **Total**      | **\\(\Sigma f_i = 30\\)** |                        | **\\(\Sigma f_i x_i = 1860.0\\)** |                       | **\\(\Sigma f_i d_i = 435\\)** |

- **Step 3: Apply the Direct Method**:
  \\[\overline{x} = \frac{\Sigma f_i x_i}{\Sigma f_i} = \frac{1860}{30} = 62 \quad \text{}\\]

- **Step 4: Apply the Assumed Mean Method**:
  \\[\overline{x} = a + \frac{\Sigma f_i d_i}{\Sigma f_i} = 47.5 + \frac{435}{30} = 47.5 + 14.5 = 62 \quad \text{}\\]
  _Note: Both grouped calculation techniques yield \\(\overline{x} = 62\\)._

---

### **Example 2 (Calculating Mode)**

**Problem:** In a survey conducted on the size of \\(20\\) households in a locality, the following frequency distribution was recorded:

| Family Size         | \\(1-3\\) | \\(3-5\\) | \\(5-7\\) | \\(7-9\\) | \\(9-11\\) |
| :------------------ | :-------: | :-------: | :-------: | :-------: | :--------: |
| **No. of Families** |  \\(7\\)  |  \\(8\\)  |  \\(2\\)  |  \\(2\\)  |  \\(1\\)   |

Find the modal family size.

- **Solution:**
  - **Identify parameters:** The maximum class frequency is \\(8\\), corresponding to the modal class **\\(3-5\\)**.
  - Lower limit of modal class (\\(l\\)) = \\(3\\)
  - Class size (\\(h\\)) = \\(2\\)
  - Frequency of modal class (\\(f_1\\)) = \\(8\\)
  - Preceding frequency (\\(f_0\\)) = \\(7\\)
  - Succeeding frequency (\\(f_2\\)) = \\(2\\)
  - **Calculate Mode**:
    \\[\text{Mode} = l + \left( \frac{f_1 - f_0}{2f_1 - f_0 - f_2} \right) \times h \quad \text{}\\]
    \\[\text{Mode} = 3 + \left( \frac{8 - 7}{2(8) - 7 - 2} \right) \times 2 = 3 + \frac{1}{7} \times 2 = 3 + 0.286 = 3.286 \quad \text{}\\]
  - **Answer:** The modal family size is **\\(3.286\\)**.

---

### **Example 3 (Calculating Median and Missing Frequencies)**

**Problem:** The median of a grouped frequency distribution with \\(100\\) total observations is \\(525\\). Find the missing frequencies \\(x\\) and \\(y\\) from the following table:

| Class Interval | Frequency (\\(f_i\\)) | Cumulative Frequency (\\(cf\\)) |
| :------------- | :-------------------: | :-----------------------------: |
| \\(0-100\\)    |        \\(2\\)        |             \\(2\\)             |
| \\(100-200\\)  |        \\(5\\)        |             \\(7\\)             |
| \\(200-300\\)  |        \\(x\\)        |           \\(7 + x\\)           |
| \\(300-400\\)  |       \\(12\\)        |          \\(19 + x\\)           |
| \\(400-500\\)  |       \\(17\\)        |          \\(36 + x\\)           |
| \\(500-600\\)  |       \\(20\\)        |          \\(56 + x\\)           |
| \\(600-700\\)  |        \\(y\\)        |        \\(56 + x + y\\)         |
| \\(700-800\\)  |        \\(9\\)        |        \\(65 + x + y\\)         |
| \\(800-900\\)  |        \\(7\\)        |        \\(72 + x + y\\)         |
| \\(900-1000\\) |        \\(4\\)        |        \\(76 + x + y\\)         |

- **Step 1: Set up the total frequency equation**:
  \\[76 + x + y = 100 \implies x + y = 24 \quad \text{--- (Eq. 1)}\\]

- **Step 2: Identify the Median Class**:
  Since the given median is \\(525\\), the median class must be **\\(500-600\\)**.
  - Lower limit (\\(l\\)) = \\(500\\)
  - Median class frequency (\\(f\\)) = \\(20\\)
  - Preceding cumulative frequency (\\(cf\\)) = \\(36 + x\\)
  - Class size (\\(h\\)) = \\(100\\)
  - Total frequency (\\(n\\)) = \\(100 \implies \frac{n}{2} = 50\\)

- **Step 3: Solve for \\(x\\) using the Median formula**:
  \\[\text{Median} = l + \left( \frac{\frac{n}{2} - cf}{f} \right) \times h \quad \text{}\\]
  \\[525 = 500 + \left( \frac{50 - (36 + x)}{20} \right) \times 100 \quad \text{}\\]
  \\[25 = (14 - x) \times 5 \quad \text{}\\]
  \\[5 = 14 - x \implies x = 9 \quad \text{}\\]

- **Step 4: Solve for \\(y\\) using (Eq. 1)**:
  \\[9 + y = 24 \implies y = 15 \quad \text{}\\]
  - **Answer:** The missing frequencies are **\\(x = 9\\)** and **\\(y = 15\\)**.

---

## **III. Practice Exercises**

### **EXERCISE 13.1 (Mean Calculation)**

1.  **Survey plants:** The table below shows the number of plants in \\(20\\) houses in a locality:
    - \\(\text{Number of plants: } 0-2, \ 2-4, \ 4-6, \ 6-8, \ 8-10, \ 10-12, \ 12-14\\)
    - \\(\text{Number of houses: } 1, \ 2, \ 1, \ 5, \ 6, \ 2, \ 3\\)
      Find the mean number of plants per house using an appropriate method.
2.  **Factory Wages:** Find the mean daily wage of \\(50\\) factory workers:
    - \\(\text{Daily wages (in ₹): } 500-520, \ 520-540, \ 540-560, \ 560-580, \ 580-600\\)
    - \\(\text{No. of workers: } 12, \ 14, \ 8, \ 6, \ 10\\)
3.  **Missing Frequency Pocket Money:** The mean pocket allowance of children in a locality is ₹18. Find the missing frequency \\(f\\):
    - \\(\text{Daily pocket allowance (in ₹): } 11-13, \ 13-15, \ 15-17, \ 17-19, \ 19-21, \ 21-23, \ 23-25\\)
    - \\(\text{No. of children: } 7, \ 6, \ 9, \ 13, \ f, \ 5, \ 4\\)
4.  **Heartbeats Study:** Thirty women were examined in a hospital. Find the mean heartbeats per minute:
    - \\(\text{Heartbeats per minute: } 65-68, \ 68-71, \ 71-74, \ 74-77, \ 77-80, \ 80-83, \ 83-86\\)
    - \\(\text{No. of women: } 2, \ 4, \ 3, \ 8, \ 7, \ 4, \ 2\\)
5.  **Mango Packing Boxes:** Fruit vendors sell mangoes stored in packing boxes containing varying quantities. Calculate the mean number of mangoes per box:
    - \\(\text{No. of mangoes: } 50-52, \ 53-55, \ 56-58, \ 59-61, \ 62-64\\)
    - \\(\text{No. of boxes: } 15, \ 110, \ 135, \ 115, \ 25\\)
6.  **Daily Food Expenditure:** The daily food expenditures of \\(25\\) households in a locality are shown below. Calculate the mean daily food expenditure:
    - \\(\text{Daily expenditure (in ₹): } 100-150, \ 150-200, \ 200-250, \ 250-300, \ 300-350\\)
    - \\(\text{No. of households: } 4, \ 12, \ 5, \ 2, \ 2\\)
7.  **Air Quality (\\(SO_2\\) concentration):** Calculate the mean concentration of \\(SO_2\\) (in ppm) across \\(30\\) different localities in a city:
    - \\(\text{Concentration (in ppm): } 0.00-0.04, \ 0.04-0.08, \ 0.08-0.12, \ 0.12-0.16, \ 0.16-0.20, \ 0.20-0.24\\)
    - \\(\text{Frequency: } 4, \ 9, \ 9, \ 2, \ 4, \ 2\\)
8.  **Student Absentees:** A class teacher has an absentee record of \\(40\\) students for a full term. Find the mean number of days a student was absent:
    - \\(\text{No. of days: } 0-6, \ 6-10, \ 10-14, \ 14-20, \ 20-28, \ 28-38, \ 38-40\\)
    - \\(\text{No. of students: } 11, \ 10, \ 7, \ 4, \ 4, \ 3, \ 1\\)
9.  **Literacy Rate:** Find the mean literacy rate across \\(35\\) cities:
    - \\(\text{Literacy rate (in %): } 45-55, \ 55-65, \ 65-75, \ 75-85, \ 85-95\\)
    - \\(\text{No. of cities: } 3, \ 10, \ 11, \ 8, \ 3\\)

---

### **EXERCISE 13.2 (Mode Calculation)**

1.  **Hospital Patients:** Find the mode and mean age of patients admitted during a year:
    - \\(\text{Age (in years): } 5-15, \ 15-25, \ 25-35, \ 35-45, \ 45-55, \ 55-65\\)
    - \\(\text{No. of patients: } 6, \ 11, \ 21, \ 23, \ 14, \ 5\\)
2.  **Electrical Components:** Find the modal lifetime of \\(225\\) electrical components:
    - \\(\text{Lifetime (in hours): } 0-20, \ 20-40, \ 40-60, \ 60-80, \ 80-100, \ 100-120\\)
    - \\(\text{Frequency: } 10, \ 35, \ 52, \ 61, \ 38, \ 29\\)
3.  **Household Expenditures:** Find the modal monthly expenditure of \\(200\\) families in a village:
    - \\(\text{Expenditure (in ₹): } 1000-1500, \ 1500-2000, \ 2000-2500, \ 2500-3000, \ 3000-3500, \ 3500-4000, \ 4000-4500, \ 4500-5000\\)
    - \\(\text{No. of families: } 24, \ 40, \ 33, \ 28, \ 30, \ 22, \ 16, \ 7\\)
4.  **Teacher-Student Ratio:** Find the mode and mean of student-teacher ratios across states:
    - \\(\text{Students per teacher: } 15-20, \ 20-25, \ 25-30, \ 30-35, \ 35-40, \ 40-45, \ 45-50, \ 50-55\\)
    - \\(\text{No. of states: } 3, \ 8, \ 9, \ 10, \ 3, \ 0, \ 0, \ 2\\)
5.  **ODI Batsmen Runs:** Find the modal runs scored by world-class batsmen:
    - \\(\text{Runs scored: } 3000-4000, \ 4000-5000, \ 5000-6000, \ 6000-7000, \ 7000-8000, \ 8000-9000, \ 9000-10000, \ 10000-11000\\)
    - \\(\text{No. of batsmen: } 4, \ 18, \ 9, \ 7, \ 6, \ 3, \ 1, \ 1\\)
6.  **Highway Cars:** Find the mode of the number of cars passing a spot on a road:
    - \\(\text{No. of cars: } 0-10, \ 10-20, \ 20-30, \ 30-40, \ 40-50, \ 50-60, \ 60-70, \ 70-80\\)
    - \\(\text{Frequency: } 7, \ 14, \ 13, \ 12, \ 20, \ 11, \ 15, \ 8\\)

---

### **EXERCISE 13.3 (Median Calculation)**

1.  **Electricity Consumption:** Find the median, mean, and mode for the monthly power consumption of \\(68\\) consumers:
    - \\(\text{Consumption (in units): } 65-85, \ 85-105, \ 105-125, \ 125-145, \ 145-165, \ 165-185, \ 185-205\\)
    - \\(\text{No. of consumers: } 4, \ 5, \ 13, \ 20, \ 14, \ 8, \ 4\\)
2.  **Missing Frequencies \\(x\\) and \\(y\\):** If the median of the distribution below is \\(28.5\\) and the total frequency is \\(60\\), find \\(x\\) and \\(y\\):
    - \\(\text{Class Interval: } 0-10, \ 10-20, \ 20-30, \ 30-40, \ 40-50, \ 50-60\\)
    - \\(\text{Frequency (\\(f_i\\)): } 5, \ x, \ 20, \ 15, \ y, \ 5\\)
3.  **Policy Holder Ages:** Calculate the median age of \\(100\\) policyholders:
    - \\(\text{Age (in years): Below } 20, \ 25, \ 30, \ 35, \ 40, \ 45, \ 50, \ 55, \ 60\\)
    - \\(\text{No. of policyholders: } 2, \ 6, \ 24, \ 45, \ 78, \ 89, \ 92, \ 98, \ 100\\)
4.  **Leaf Lengths:** Find the median length of \\(40\\) leaves measured to the nearest millimeter:
    - \\(\text{Length (in mm): } 118-126, \ 127-135, \ 136-144, \ 145-153, \ 154-162, \ 163-171, \ 172-180\\)
    - \\(\text{No. of leaves: } 3, \ 5, \ 9, \ 12, \ 5, \ 4, \ 2\\)
      _(Hint: Convert classes into continuous boundaries before starting: \\(117.5-126.5\\) etc.)_
5.  **Neon Lamps Lifetime:** Find the median lifetime of \\(400\\) neon lamps:
    - \\(\text{Lifetime (in hours): } 1500-2000, \ 2000-2500, \ 2500-3000, \ 3000-3500, \ 3500-4000, \ 4000-4500, \ 4500-5000\\)
    - \\(\text{No. of lamps: } 14, \ 56, \ 60, \ 86, \ 74, \ 62, \ 48\\)
6.  **Telephone Directory Surnames:** In a survey, \\(100\\) surnames were picked. Find the median, mean, and modal size of surnames:
    - \\(\text{No. of letters: } 1-4, \ 4-7, \ 7-10, \ 10-13, \ 13-16, \ 16-19\\)
    - \\(\text{No. of surnames: } 6, \ 30, \ 40, \ 16, \ 4, \ 4\\)
7.  **Student Weights:** Find the median weight of \\(30\\) students:
    - \\(\text{Weight (in kg): } 40-45, \ 45-50, \ 50-55, \ 55-60, \ 60-65, \ 65-70, \ 70-75\\)
    - \\(\text{No. of students: } 2, \ 3, \ 8, \ 6, \ 6, \ 3, \ 2\\)

---

### **EXERCISE 13.4 (Ogives / Cumulative Frequency Graphs)**

1.  **Less Than Ogive:** Convert the daily income of \\(50\\) factory workers into a "less than" cumulative frequency distribution and draw its ogive:
    - \\(\text{Daily income (in ₹): } 100-120, \ 120-140, \ 140-160, \ 160-180, \ 180-200\\)
    - \\(\text{No. of workers: } 12, \ 14, \ 8, \ 6, \ 10\\)
2.  **Medical Checkup Weights:** Plot a "less than" ogive for the weights of \\(35\\) students. Locate the median from your graph and verify it mathematically:
    - \\(\text{Weight (in kg): Less than } 38, \ 40, \ 42, \ 44, \ 46, \ 48, \ 50, \ 52\\)
    - \\(\text{No. of students: } 0, \ 3, \ 5, \ 9, \ 14, \ 28, \ 32, \ 35\\)
3.  **Wheat Production Yield:** Change the distribution below to a "more than" type cumulative frequency distribution and plot its ogive:
    - \\(\text{Production yield (in kg/ha): } 50-55, \ 55-60, \ 60-65, \ 65-70, \ 70-75, \ 75-80\\)
    - \\(\text{No. of farms: } 2, \ 8, \ 12, \ 24, \ 38, \ 16\\)

---

📊 **I can help you build an interactive spreadsheet in your workspace containing automated solvers for Grouped Mean, Mode, and Median calculations, as well as a script to draw custom Ogives. Would you like me to construct this?**
