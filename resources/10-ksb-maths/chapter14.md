# **Chapter 14: Probability — Study Guide**

---

## **I. Core Concepts & Theoretical Principles**

### **1. Experimental vs. Theoretical Probability**

- **Experimental (Empirical) Probability:** Based on the actual results of performed experiments and the recording of the frequency of events `. The empirical probability \\(P(E)\\) of an event \\(E\\) is given by `:
  \\[P(E) = \frac{\text{Number of trials in which the event happened}}{\text{Total number of trials}}\\]
  Since experimental probabilities are only "estimates," repeating the same experiment under identical conditions can yield slightly different results `. However, as the number of trials increases, the experimental probability of an event converges to its theoretical value `.
- **Historical Coin Tossing Experiments:**
  - **Comte de Buffon (18th Century):** Tossed a coin \\(4,040\\) times and got \\(2,048\\) heads (empirical probability \\(\approx 0.507\\)) ``.
  - **J.E. Kerrich:** Tossed a coin \\(10,000\\) times and recorded \\(5,067\\) heads (empirical probability \\(= 0.5067\\)) ``.
  - **Karl Pearson:** Tossed a coin \\(24,000\\) times and obtained \\(12,012\\) heads (empirical probability \\(= 0.5005\\)) ``.
- **Theoretical (Classical) Probability:** Allows the direct calculation of the exact probability of an event under certain logical assumptions (specifically, equally likely outcomes) without performing the experiment `. The theoretical probability of an event \\(E\\) is defined as `:
  \\[P(E) = \frac{\text{Number of outcomes favourable to } E}{\text{Number of all possible outcomes of the experiment}}\\]

---

### **2. Important Probability Axioms & Definitions**

- **Equally Likely Outcomes:** Outcomes of an experiment are equally likely if none has a higher preference or chance of occurring over the others `. For example, rolling a fair, unbiased die has six equally likely outcomes: \\(1, 2, 3, 4, 5, \text{ and } 6\\) `.
- **Elementary Event:** An event that consists of exactly **one single outcome** of the experiment ``.
- **Sum of Elementary Events:** The sum of the probabilities of all the elementary events of a given random experiment is always **equal to 1** ``.
- **Range of Probability:** The probability of any event \\(E\\) is a real number strictly bounded between \\(0\\) and \\(1\\) (inclusive) ``:
  \\[0 \le P(E) \le 1\\]

#### **Pedagogical Probability Scale Visualisation:**

```xml
<svg width="500" height="120" viewBox="0 0 500 120" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .scale-bar { fill: url(#grad-scale); stroke: #cbd5e1; stroke-width: 1.5; }
    .mark-line { stroke: #0f172a; stroke-width: 2; }
    .lbl-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: bold; fill: #0f172a; }
    .lbl-sub { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #64748b; }
  </style>

  <defs>
    <linearGradient id="grad-scale" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#3b82f6" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#22c55e" stop-opacity="0.8"/>
    </linearGradient>
  </defs>

  <!-- Horizontal Axis Bar -->
  <rect x="50" y="45" width="400" height="16" rx="4" class="scale-bar"/>

  <!-- Ticks -->
  <line x1="50" y1="40" x2="50" y2="66" class="mark-line" />
  <line x1="250" y1="40" x2="250" y2="66" class="mark-line" />
  <line x1="450" y1="40" x2="450" y2="66" class="mark-line" />

  <!-- Labels -->
  <text x="50" y="30" class="lbl-title" text-anchor="middle">0 (Impossible)</text>
  <text x="50" y="85" class="lbl-sub" text-anchor="middle">P(E) = 0</text>
  <text x="50" y="100" class="lbl-sub" style="fill:#ef4444;" text-anchor="middle">[e.g., Rolling an 8 on a die]</text>

  <text x="250" y="30" class="lbl-title" text-anchor="middle">0.5 (Equally Likely)</text>
  <text x="250" y="85" class="lbl-sub" text-anchor="middle">P(E) = 0.5</text>
  <text x="250" y="100" class="lbl-sub" style="fill:#3b82f6;" text-anchor="middle">[e.g., Tossing a Head]</text>

  <text x="450" y="30" class="lbl-title" text-anchor="middle">1 (Sure/Certain)</text>
  <text x="450" y="85" class="lbl-sub" text-anchor="middle">P(E) = 1</text>
  <text x="450" y="100" class="lbl-sub" style="fill:#22c55e;" text-anchor="middle">[e.g., Getting number &lt; 7]</text>
</svg>
```

- **Impossible Event:** An event that cannot occur under any circumstance has a probability of **0** `. For example, the probability of rolling the number \\(8\\) on a single six-sided die is \\(0\\) `.
- **Sure (Certain) Event:** An event that is guaranteed to occur has a probability of **1** `. For example, the probability of rolling a number less than \\(7\\) on a standard die is \\(1\\) `.
- **Complementary Events:** For any event \\(E\\), the complementary event representing "not \\(E\\)" is denoted as \\(\overline{E}\\) `. The probabilities of an event and its complement are related by `:
  \\[P(E) + P(\overline{E}) = 1 \implies P(\overline{E}) = 1 - P(E)\\]

---

### **3. Historical and Academic Origins**

- **16th Century:** The Italian physician and mathematician **Gerolamo Cardan** wrote the first book on probability theory, **_"The Book on Games of Chance"_** (_Liber de Ludo Aleae_) ``.
- **Development:** Highly developed by scholars like **James Bernoulli** (1654–1705), **Abraham de Moivre** (1667–1754), and **Pierre Simon Laplace** (1749–1827) ``.
- **Laplace's Masterwork:** Laplace’s _“Théorie Analytique des Probabilités”_ (1812) is considered the single greatest classical contribution to probability theory ``.

---

## **II. Structured Experiments & Sample Spaces**

### **1. Coin Tossing Experiments**

- **Single Coin:** Sample space \\(S = \{H, T\}\\), total possible outcomes \\(= 2\\) ``.
- **Double Coin Tossing:** Tossing two different coins simultaneously yields \\(4\\) equally likely outcomes `:
\\[S = \{(H,H), \ (H,T), \ (T,H), \ (T,T)\\}\\]
where \\((H, T)\\) represents a Head on the first coin and a Tail on the second coin `.

---

### **2. Die Throwing Experiments**

- **Single Die:** Sample space \\(S = \{1, 2, 3, 4, 5, 6\}\\), total possible outcomes \\(= 6\\) ``.
- **Double Die Throwing:** Throwing two distinct dice (e.g., one blue and one grey) simultaneously yields \\(6 \times 6 = 36\\) equally likely outcomes ``:

#### **The 36-Outcome Grid for Rolling Two Dice:**

```xml
<svg width="400" height="280" viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .grid-bg { fill: #ffffff; stroke: #cbd5e1; stroke-width: 1; }
    .label-header { font-family: 'Consolas', monospace; font-size: 11px; font-weight: bold; fill: #0f172a; text-anchor: middle; }
    .outcome-cell { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #475569; text-anchor: middle; }
    .highlight-diagonal { fill: #fee2e2; stroke: #ef4444; stroke-width: 1.2; } /* Sum = 8 */
    .highlight-txt { fill: #b91c1c; font-weight: bold; }
  </style>

  <!-- Labels -->
  <text x="200" y="20" class="label-header" style="font-size:12px;">Grey Die Outcome (1 to 6) →</text>
  <text x="25" y="145" class="label-header" style="font-size:12px; transform: rotate(-90deg); transform-origin: 25px 145px;">← Blue Die Outcome</text>

  <!-- Table Grid Representation -->
  <g transform="translate(50, 30)">
    <!-- Draw Grid Cells -->
    <!-- Column/Row Header Backgrounds -->
    <rect x="0" y="0" width="320" height="230" fill="none" stroke="#e2e8f0" stroke-width="1.5"/>

    <!-- Cells with values -->
    <!-- Row 1 -->
    <text x="25" y="30" class="outcome-cell">(1,1)</text>
    <text x="75" y="30" class="outcome-cell">(1,2)</text>
    <text x="125" y="30" class="outcome-cell">(1,3)</text>
    <text x="175" y="30" class="outcome-cell">(1,4)</text>
    <text x="225" y="30" class="outcome-cell">(1,5)</text>
    <text x="275" y="30" class="outcome-cell">(1,6)</text>

    <!-- Row 2 -->
    <text x="25" y="65" class="outcome-cell">(2,1)</text>
    <text x="75" y="65" class="outcome-cell">(2,2)</text>
    <text x="125" y="65" class="outcome-cell">(2,3)</text>
    <text x="175" y="65" class="outcome-cell">(2,4)</text>
    <text x="225" y="65" class="outcome-cell">(2,5)</text>
    <!-- Highlight cell (2,6) as part of sum=8 diagonal -->
    <rect x="250" y="48" width="50" height="24" rx="4" class="highlight-diagonal"/>
    <text x="275" y="65" class="outcome-cell highlight-txt">(2,6)</text>

    <!-- Row 3 -->
    <text x="25" y="100" class="outcome-cell">(3,1)</text>
    <text x="75" y="100" class="outcome-cell">(3,2)</text>
    <text x="125" y="100" class="outcome-cell">(3,3)</text>
    <text x="175" y="100" class="outcome-cell">(3,4)</text>
    <rect x="200" y="83" width="50" height="24" rx="4" class="highlight-diagonal"/>
    <text x="225" y="100" class="outcome-cell highlight-txt">(3,5)</text>
    <text x="275" y="100" class="outcome-cell">(3,6)</text>

    <!-- Row 4 -->
    <text x="25" y="135" class="outcome-cell">(4,1)</text>
    <text x="75" y="135" class="outcome-cell">(4,2)</text>
    <text x="125" y="135" class="outcome-cell">(4,3)</text>
    <rect x="150" y="118" width="50" height="24" rx="4" class="highlight-diagonal"/>
    <text x="175" y="135" class="outcome-cell highlight-txt">(4,4)</text>
    <text x="225" y="135" class="outcome-cell">(4,5)</text>
    <text x="275" y="135" class="outcome-cell">(4,6)</text>

    <!-- Row 5 -->
    <text x="25" y="170" class="outcome-cell">(5,1)</text>
    <text x="75" y="170" class="outcome-cell">(5,2)</text>
    <rect x="100" y="153" width="50" height="24" rx="4" class="highlight-diagonal"/>
    <text x="125" y="170" class="outcome-cell highlight-txt">(5,3)</text>
    <text x="175" y="170" class="outcome-cell">(5,4)</text>
    <text x="225" y="170" class="outcome-cell">(5,5)</text>
    <text x="275" y="170" class="outcome-cell">(5,6)</text>

    <!-- Row 6 -->
    <rect x="0" y="188" width="50" height="24" rx="4" class="highlight-diagonal"/>
    <text x="25" y="205" class="outcome-cell highlight-txt">(6,2)</text>
    <text x="75" y="205" class="outcome-cell">(6,2)</text>
    <text x="125" y="205" class="outcome-cell">(6,3)</text>
    <text x="175" y="205" class="outcome-cell">(6,4)</text>
    <text x="225" y="205" class="outcome-cell">(6,5)</text>
    <text x="275" y="205" class="outcome-cell">(6,6)</text>
  </g>
</svg>
```

---

### **3. The Composition of a Standard 52-Card Deck**

A well-shuffled standard deck contains exactly **52 cards** split into **4 suits** of \\(13\\) cards each ``:

```
                    ┌─────────────────── 52 CARDS ───────────────────┐
                    │                                                │
         ┌────── 26 RED ──────┐                           ┌───── 26 BLACK ─────┐
         │                    │                           │                    │
  13 HEARTS (♥)       13 DIAMONDS (♦)              13 SPADES (♠)        13 CLUBS (♣)
```

- **Each suit** contains: Ace, King, Queen, Jack, 10, 9, 8, 7, 6, 5, 4, 3, 2 ``.
- **Face Cards:** Kings, Queens, and Jacks are referred to as **face cards** `. There are \\(3 \text{ face cards per suit} \times 4 \text{ suits} = 12\\) face cards in a full deck `.

---

## **III. Solved Example Problems**

### **Example 1 (Basic Coin Probability)**

**Problem:** Find the probability of getting a head when a fair coin is tossed once. Also find the probability of getting a tail ``.

- **Solution:**
  - The total number of possible outcomes is \\(2\\): Head (H) and Tail (T) ``.
  - Let \\(E\\) be the event "getting a head" `. Favourable outcomes \\(= 1\\) (only \\(H\\)) `.
    \\[P(E) = P(\text{Head}) = \frac{1}{2}\text{ ``}\\]
  - Let \\(F\\) be the event "getting a tail" `. Favourable outcomes \\(= 1\\) (only \\(T\\)) `.
    \\[P(F) = P(\text{Tail}) = \frac{1}{2}\text{ ``}\\]

---

### **Example 2 (Complementary Events & Card Probability)**

**Problem:** One card is drawn from a well-shuffled deck of 52 cards. Calculate the probability that the card will: (i) be an ace, (ii) not be an ace ``.

- **Solution:**
  - **Part (i):** Let \\(E\\) be the event "the drawn card is an ace" ``.
    - There are exactly \\(4\\) aces in a standard deck of \\(52\\) cards ``.
    - Total possible outcomes \\(= 52\\) `.
\\[P(E) = \frac{4}{52} = \frac{1}{13}\text{ `}\\]
  - **Part (ii):** Let \\(F\\) (or \\(\overline{E}\\)) be the event "the card is not an ace" ``.
    - Using the complementary event rule:
      \\[P(\overline{E}) = 1 - P(E) = 1 - \frac{1}{13} = \frac{12}{13}\text{ ``}\\]

---

### **Example 3 (Tossing Two Coins)**

**Problem:** Harpreet tosses two different coins simultaneously. What is the probability that she gets at least one head ``?

- **Solution:**
  - The possible outcomes are \\((H, H), (H, T), (T, H), \text{ and } (T, T)\\) `. Total outcomes \\(= 4\\) `.
  - Let \\(E\\) be the event "getting at least one head" ``.
  - Favourable outcomes are those containing one or two heads: \\((H, H), (H, T), \text{ and } (T, H)\\) ``.
  - Number of favourable outcomes \\(= 3\\) `.
\\[P(E) = \frac{3}{4}\text{ `}\\]

---

### **Example 4 (Geometric Probability - Helicopter Crash)**

**Problem:** A missing helicopter is reported to have crashed somewhere in a rectangular region of length \\(9\text{ km}\\) and width \\(4.5\text{ km}\\) `. Find the probability that it crashed inside a lake of length \\(3\text{ km}\\) and width \\(2.5\text{ km}\\) situated inside the region `.

```xml
<svg width="360" height="200" viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .rect-region { fill: #fef08a; stroke: #eab308; stroke-width: 2; }
    .lake-region { fill: #38bdf8; stroke: #0284c7; stroke-dasharray: 2 2; }
    .dim-lbl { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; fill: #0f172a; font-weight: bold; }
  </style>

  <!-- Outer Rect (9km x 4.5km scaled by 30) -> 270 x 135 -->
  <rect x="45" y="30" width="270" height="135" class="rect-region"/>
  <text x="180" y="24" class="dim-lbl" text-anchor="middle">9 km</text>
  <text x="25" y="100" class="dim-lbl" text-anchor="middle">4.5 km</text>

  <!-- Lake (3km x 2.5km scaled by 30) -> 90 x 75 -->
  <rect x="180" y="60" width="90" height="75" class="lake-region"/>
  <text x="225" y="105" class="dim-lbl" style="fill:#0284c7;" text-anchor="middle">Lake</text>
  <text x="225" y="152" class="dim-lbl" style="fill:#0f172a;" text-anchor="middle">3 km</text>
  <text x="285" y="100" class="dim-lbl" style="fill:#0f172a;">2.5 km</text>
</svg>
```

- **Solution:**
  - The helicopter is equally likely to crash anywhere inside the rectangular region ``.
  - \\[\text{Area of the entire region} = 9\text{ km} \times 4.5\text{ km} = 40.5\text{ km}^2\text{ ``}\\]
  - \\[\text{Area of the lake} = 3\text{ km} \times 2.5\text{ km} = 7.5\text{ km}^2\text{ ``}\\]
  - Apply area ratios to find the probability:
    \\[P(\text{helicopter crashed in lake}) = \frac{\text{Area of Lake}}{\text{Area of Entire Region}} = \frac{7.5}{40.5} = \frac{75}{405} = \frac{5}{27}\text{ ``}\\]

---

### **Example 5 (Double Dice Throw)**

**Problem:** Two dice are thrown simultaneously. Find the probability that the sum of the numbers appearing on top of the two dice is: (i) \\(8\\), (ii) \\(13\\), (iii) less than or equal to \\(12\\) ``.

- **Solution:**
  - Total possible outcomes when rolling two dice \\(= 6 \times 6 = 36\\) ``.
  - **Part (i) [Sum is 8]:** Let \\(E\\) be the event "the sum is 8" ``.
    - Favourable outcomes are \\((2,6), (3,5), (4,4), (5,3), \text{ and } (6,2)\\) ``.
    - Number of favourable outcomes \\(= 5\\) `.
\\[P(E) = \frac{5}{36}\text{ `}\\]
  - **Part (ii) [Sum is 13]:** Let \\(F\\) be the event "the sum is 13" ``.
    - The maximum possible sum is \\(6 + 6 = 12\\) `. No outcome has a sum of \\(13\\) `.
    - Number of favourable outcomes \\(= 0\\) `.
\\[P(F) = \frac{0}{36} = 0 \quad \text{(Impossible Event) `}\\]
  - **Part (iii) [Sum is \\(\le 12\\)]:** Let \\(G\\) be the event "the sum is less than or equal to 12" ``.
    - Since every possible outcome yields a sum less than or equal to \\(12\\), all \\(36\\) outcomes are favourable `.
\\[P(G) = \frac{36}{36} = 1 \quad \text{(Sure/Certain Event) `}\\]

---

## **IV. Textbook Exercises**

### **EXERCISE 14.1**

1.  **Complete the following statements:**
    - (i) Probability of an event \\(E\\) + Probability of the event "not \\(E\\)" = \_\_\_\_\_\_ ``.
    - (ii) The probability of an event that cannot happen is \_\_\_\_\_\_. Such an event is called \_\_\_\_\_\_ ``.
    - (iii) The probability of an event that is certain to happen is \_\_\_\_\_\_. Such an event is called \_\_\_\_\_\_ ``.
    - (iv) The sum of the probabilities of all the elementary events of an experiment is \_\_\_\_\_\_ ``.
    - (v) The probability of an event is greater than or equal to \_\_\_\_\_\_ and less than or equal to \_\_\_\_\_\_ ``.
2.  Which of the following experiments have equally likely outcomes? Explain ``:
    - (i) A driver attempts to start a car. The car starts or does not start ``.
    - (ii) A player attempts to shoot a basketball. She/he shoots or misses the shot ``.
    - (iii) A trial is made to answer a true-false question. The answer is right or wrong ``.
    - (iv) A baby is born. It is a boy or a girl ``.
3.  Why is tossing a coin considered to be a fair way of deciding which team should get the ball at the beginning of a football game ``?
4.  Which of the following cannot be the probability of an event ``?
    - (A) \\(\frac{2}{3}\\) \quad (B) \\(-1.5\\) \quad (C) \\(15\%\\) \quad (D) \\(0.7\\) ``
5.  If \\(P(E) = 0.05\\), what is the probability of "not \\(E\\)" ``?
6.  A bag contains lemon flavoured candies only. Malini takes out one candy without looking into the bag. What is the probability that she takes out ``:
    - (i) an orange flavoured candy? ``
    - (ii) a lemon flavoured candy? ``
7.  It is given that in a group of 3 students, the probability of 2 students not having the same birthday is \\(0.992\\). What is the probability that the 2 students have the same birthday ``?
8.  A bag contains 3 red balls and 5 black balls. A ball is drawn at random from the bag. What is the probability that the ball drawn is: (i) red? (ii) not red ``?
9.  A box contains 5 red marbles, 8 white marbles, and 4 green marbles. One marble is taken out of the box at random. What is the probability that the marble taken out will be: (i) red? (ii) white? (iii) not green ``?
10. A piggy bank contains hundred 50p coins, fifty ₹1 coins, twenty ₹2 coins, and ten ₹5 coins. If it is equally likely that one of the coins will fall out when the bank is turned upside down, what is the probability that the coin: (i) will be a 50p coin? (ii) will not be a ₹5 coin ``?
11. Gopi buys a fish from a shop for his aquarium. The shopkeeper takes out one fish at random from a tank containing 5 male fish and 8 female fish. What is the probability that the fish taken out is a male fish ``?
12. A game of chance consists of spinning an arrow which comes to rest pointing at one of the numbers \\(1, 2, 3, 4, 5, 6, 7, 8\\), and these are equally likely outcomes. What is the probability that it will point at ``:
    - (i) 8? ``
    - (ii) an odd number? ``
    - (iii) a number greater than 2? ``
    - (iv) a number less than 9? ``
13. A die is thrown once. Find the probability of getting ``:
    - (i) a prime number; ``
    - (ii) a number lying between 2 and 6; ``
    - (iii) an odd number ``.
14. One card is drawn from a well-shuffled deck of 52 cards. Find the probability of getting ``:
    - (i) a king of red colour ``
    - (ii) a face card ``
    - (iii) a red face card ``
    - (iv) the jack of hearts ``
    - (v) a spade ``
    - (vi) the queen of diamonds ``.
15. Five cards—the ten, jack, queen, king, and ace of diamonds, are well-shuffled with their face downwards. One card is then picked up at random ``.
    - (i) What is the probability that the card is the queen ``?
    - (ii) If the queen is drawn and put aside, what is the probability that the second card picked up is: (a) an ace? (b) a queen ``?
16. 12 defective pens are accidentally mixed with 132 good ones. It is not possible to just look at a pen and tell whether or not it is defective. One pen is taken out at random from this lot. Determine the probability that the pen taken out is a good one ``.
17. (i) A lot of 20 bulbs contains 4 defective ones. One bulb is drawn at random from the lot. What is the probability that this bulb is defective ``?
    - (ii) Suppose the bulb drawn in (i) is not defective and is not replaced. Now one bulb is drawn at random from the rest. What is the probability that this bulb is not defective ``?
18. A box contains 90 discs which are numbered from 1 to 90. If one disc is drawn at random from the box, find the probability that it bears: (i) a two-digit number, (ii) a perfect square number, (iii) a number divisible by 5 ``.
19. A child has a die whose six faces show the letters as given below:
    \\[[A] \quad [B] \quad [C] \quad [D] \quad [E] \quad [A]\\]
    The die is thrown once. What is the probability of getting: (i) A? (ii) D ``?
20. **\*** Suppose you drop a die at random on a rectangular region of \\(3\text{ m} \times 2\text{ m}\\). What is the probability that it will land inside a circle of diameter \\(1\text{ m}\\) situated inside the rectangle ``?
21. A lot consists of 144 ball pens of which 20 are defective and the others are good. Nuri will buy a pen if it is good, but will not buy if it is defective. The shopkeeper draws one pen at random and gives it to her. What is the probability that ``:
    - (i) She will buy it? ``
    - (ii) She will not buy it? ``
22. (i) Complete the cumulative probability table for rolling two dice shown in Example 5 ``.
    - (ii) A student argues that "there are 11 possible outcomes: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12. Therefore, each of them has a probability of \\(\frac{1}{11}\\)." Do you agree with this argument? Justify ``.
23. A game consists of tossing a one rupee coin 3 times and noting its outcome each time. Hanif wins if all the tosses give the same result (three heads or three tails), and loses otherwise. Calculate the probability that Hanif will lose the game ``.
24. A die is thrown twice. What is the probability that ``:
    - (i) 5 will not come up either time? ``
    - (ii) 5 will come up at least once? ``
25. Which of the following arguments are correct and which are not correct? Give reasons ``:
    - (i) If two coins are tossed simultaneously, there are three possible outcomes—two heads, two tails, or one of each. Therefore, for each of these outcomes, the probability is \\(\frac{1}{3}\\) ``.
    - (ii) If a die is thrown, there are two possible outcomes—an odd number or an even number. Therefore, the probability of getting an odd number is \\(\frac{1}{2}\\) ``.

---

### **EXERCISE 14.2 (Optional)\***

_\*These exercises are not from the examination point of view ``._

1.  Two customers Shyam and Ekta are visiting a particular shop in the same week (Tuesday to Saturday). Each is equally likely to visit the shop on any day as on another day. What is the probability that both will visit the shop on: (i) the same day? (ii) consecutive days? (iii) different days ``?
2.  A die is numbered in such a way that its faces show the numbers \\(1, 2, 2, 3, 3, 6\\). It is thrown two times and the total score in two throws is noted. Complete the score addition table, then find the probability that the total score is ``:
    - (i) even? ``
    - (ii) 6? ``
    - (iii) at least 6? ``
3.  A bag contains 5 red balls and some blue balls. If the probability of drawing a blue ball is double that of a red ball, determine the number of blue balls in the bag ``.
4.  A box contains 12 balls out of which \\(x\\) are black. If one ball is drawn at random from the box, what is the probability that it will be a black ball `? If 6 more black balls are put in the box, the probability of drawing a black ball is now double of what it was before. Find \\(x\\) `.
5.  A jar contains 24 marbles, some are green and others are blue. If a marble is drawn at random from the jar, the probability that it is green is \\(\frac{2}{3}\\). Find the number of blue marbles in the jar ``.

---

🎲 **I can generate an interactive Python simulator in your workspace to model thousands of coin flips or dice rolls to verify empirical vs theoretical probabilities. Would you like me to build it?**
