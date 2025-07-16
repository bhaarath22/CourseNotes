# Infosys Python Web Developer - Complete Study Guide

## 1. Basic HTML and CSS for Web Development

### Key Notes:
• **HTML Structure**: DOCTYPE, html, head, body tags form the basic structure
• **Common HTML Tags**: h1-h6 (headings), p (paragraph), div (division), span (inline), a (anchor/links), img (images)
• **HTML Attributes**: id, class, src, href, alt, style are most commonly used
• **CSS Selectors**: Element (p), Class (.classname), ID (#idname), Universal (*), Descendant (div p)
• **CSS Properties**: color, background-color, font-size, margin, padding, border, width, height
• **CSS Box Model**: Content → Padding → Border → Margin (from inside out)
• **CSS Display**: block, inline, inline-block, none
• **CSS Positioning**: static, relative, absolute, fixed
• **Responsive Design**: Use media queries (@media) and flexible units (%, em, rem)

### Practice Questions:

**Multiple Choice:**
1. Which HTML tag is used to create a hyperlink?
   a) `<link>` b) `<a>` c) `<href>` d) `<url>`

2. What does CSS stand for?
   a) Computer Style Sheets b) Cascading Style Sheets c) Creative Style Sheets d) Colorful Style Sheets

3. Which CSS property is used to change text color?
   a) font-color b) text-color c) color d) foreground-color

**Short Answer:**
1. Explain the difference between margin and padding in CSS.
2. What is the purpose of the DOCTYPE declaration in HTML?
3. How do you make a CSS class selector?

**Coding Questions:**
1. Write HTML code to create a simple webpage with a heading, paragraph, and image.
2. Write CSS to style a button with blue background, white text, and rounded corners.

### How to Answer:

**Multiple Choice Answers:**
1. b) `<a>` - The anchor tag creates hyperlinks
2. b) Cascading Style Sheets - Standard definition
3. c) color - This is the correct CSS property

**Short Answer Solutions:**
1. **Margin vs Padding**: Margin is space outside the border, padding is space inside the border between border and content
2. **DOCTYPE**: Tells the browser which HTML version to use and ensures proper rendering
3. **CSS Class**: Use a dot followed by class name: `.classname { properties }`

**Coding Solutions:**
1. HTML Structure:
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <img src="image.jpg" alt="Description">
</body>
</html>
```

2. CSS Button:
```css
.button {
    background-color: blue;
    color: white;
    border-radius: 5px;
    padding: 10px 20px;
    border: none;
}
```

### Tips and Common Mistakes:
• **Always close HTML tags** - forgetting closing tags causes layout issues
• **Use semantic HTML** - h1 for main heading, p for paragraphs, not just divs
• **CSS specificity matters** - ID selectors override class selectors
• **Don't forget units** - specify px, em, % for CSS values
• **Test responsive design** - use browser developer tools
• **Validate your code** - use HTML/CSS validators

---

## 2. Basic Python Programming Concepts

### Key Notes:
• **Data Types**: int, float, str, bool, list, tuple, dict, set
• **Variables**: Use descriptive names, follow snake_case convention
• **Operators**: Arithmetic (+, -, *, /, //), Comparison (==, !=, <, >), Logical (and, or, not)
• **Control Structures**: if/elif/else, for loops, while loops
• **Functions**: def keyword, parameters, return statements, scope
• **Lists**: Ordered, mutable, allow duplicates - [1, 2, 3]
• **Dictionaries**: Key-value pairs, mutable - {"key": "value"}
• **Strings**: Immutable, indexable, many methods (.upper(), .lower(), .split())
• **Exception Handling**: try/except/finally blocks
• **File Operations**: open(), read(), write(), close()
• **Modules**: import statement, from module import function

### Practice Questions:

**Multiple Choice:**
1. Which of the following is a mutable data type in Python?
   a) tuple b) string c) list d) int

2. What is the output of: print(3 // 2)?
   a) 1.5 b) 1 c) 2 d) Error

3. Which keyword is used to define a function in Python?
   a) function b) def c) define d) func

**Short Answer:**
1. What is the difference between a list and a tuple?
2. Explain the purpose of the 'self' parameter in class methods.
3. How do you handle exceptions in Python?

**Coding Questions:**
1. Write a function that takes a list of numbers and returns the sum of even numbers.
2. Create a dictionary with 3 key-value pairs and print all keys.
3. Write a program that reads a file and counts the number of lines.

### How to Answer:

**Multiple Choice Answers:**
1. c) list - Lists are mutable (can be changed after creation)
2. b) 1 - Floor division returns integer result
3. b) def - Standard function definition keyword

**Short Answer Solutions:**
1. **List vs Tuple**: Lists are mutable (changeable) and use [], tuples are immutable and use ()
2. **Self parameter**: Refers to the instance of the class, allows access to instance variables and methods
3. **Exception handling**: Use try/except blocks to catch and handle errors gracefully

**Coding Solutions:**
1. Sum of even numbers:
```python
def sum_even(numbers):
    return sum(num for num in numbers if num % 2 == 0)
```

2. Dictionary operations:
```python
my_dict = {"name": "John", "age": 25, "city": "Delhi"}
for key in my_dict.keys():
    print(key)
```

3. File line counter:
```python
with open("file.txt", "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")
```

### Tips and Common Mistakes:
• **Indentation matters** - Python uses indentation for code blocks
• **Use meaningful variable names** - avoid single letters except for loops
• **Don't modify lists while iterating** - create a copy first
• **Remember Python is case-sensitive** - 'Name' and 'name' are different
• **Use 'is' for None comparisons** - if variable is None, not variable == None
• **Close files properly** - use 'with' statement for automatic closing

---

## 3. Introduction to Web Frameworks

### Key Notes:
• **Web Framework Definition**: Software framework designed to support web application development
• **Types**: Full-stack (Django), Micro (Flask), API-focused (FastAPI)
• **MVC Pattern**: Model (data), View (presentation), Controller (logic)
• **Django Features**: ORM, admin interface, URL routing, template engine, middleware
• **Flask Features**: Lightweight, flexible, minimal core with extensions
• **Key Concepts**: URL routing, templates, request/response cycle, middleware
• **Database Integration**: ORM (Object-Relational Mapping) for database operations
• **Template Engines**: Jinja2 (Flask), Django Template Language (Django)
• **Static Files**: CSS, JS, images served separately
• **Forms**: HTML forms, form validation, CSRF protection
• **Session Management**: User authentication, session storage
• **API Development**: RESTful APIs, JSON responses

### Practice Questions:

**Multiple Choice:**
1. Which Python web framework is known for being "batteries included"?
   a) Flask b) Django c) FastAPI d) Pyramid

2. What does MVC stand for in web development?
   a) Model-View-Controller b) Multiple-Virtual-Components c) Modern-Visual-Computing d) Main-View-Content

3. Which template engine is commonly used with Flask?
   a) Django Template Language b) Jinja2 c) Mustache d) Handlebars

**Short Answer:**
1. What is the difference between Django and Flask?
2. Explain the purpose of URL routing in web frameworks.
3. What is an ORM and why is it useful?

**Coding Questions:**
1. Write a basic Flask route that returns "Hello World".
2. Create a Django URL pattern that captures a user ID from the URL.
3. Write a simple template that displays a list of items.

### How to Answer:

**Multiple Choice Answers:**
1. b) Django - Known for including many built-in features
2. a) Model-View-Controller - Standard web architecture pattern
3. b) Jinja2 - Flask's default template engine

**Short Answer Solutions:**
1. **Django vs Flask**: Django is full-featured with built-in admin, ORM, authentication; Flask is minimal and flexible
2. **URL routing**: Maps URLs to specific functions/views, determines which code runs for each request
3. **ORM**: Object-Relational Mapping translates database tables to Python objects, simplifies database operations

**Coding Solutions:**
1. Flask route:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"
```

2. Django URL:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
]
```

3. Template example:
```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

### Tips and Common Mistakes:
• **Choose the right framework** - Django for full apps, Flask for simple/custom needs
• **Understand URL patterns** - practice regex and URL routing
• **Learn template syntax** - each framework has specific template language
• **Database migrations** - always migrate after model changes
• **Security considerations** - CSRF protection, input validation
• **Don't hardcode settings** - use environment variables

---

## 4. Quantitative Aptitude

### Key Notes:
• **Number Systems**: Natural, whole, integers, rational, irrational, real numbers
• **Arithmetic Operations**: BODMAS/PEMDAS rule for order of operations
• **Percentages**: Part/Whole × 100, percentage increase/decrease calculations
• **Ratios and Proportions**: a:b = c:d means a/b = c/d
• **Average**: Sum of values / Number of values
• **Time and Work**: Work rate = 1/time, combined work = sum of individual rates
• **Time, Speed, Distance**: Speed = Distance/Time, Distance = Speed × Time
• **Simple Interest**: SI = (P × R × T)/100
• **Compound Interest**: CI = P(1 + R/100)^T - P
• **Profit and Loss**: Profit% = (SP - CP)/CP × 100
• **Data Interpretation**: Tables, graphs, charts, pie charts
• **Sequences**: Arithmetic (common difference), Geometric (common ratio)
• **Permutations**: nPr = n!/(n-r)!, Combinations: nCr = n!/(r!(n-r)!)

### Practice Questions:

**Multiple Choice:**
1. If 25% of a number is 80, what is the number?
   a) 200 b) 240 c) 320 d) 400

2. A train travels 300 km in 4 hours. What is its speed?
   a) 75 km/h b) 80 km/h c) 70 km/h d) 85 km/h

3. What is 15% of 240?
   a) 36 b) 32 c) 40 d) 35

**Short Answer:**
1. Find the compound interest on ₹5000 at 10% per annum for 2 years.
2. If A can complete a work in 12 days and B in 15 days, in how many days can they complete it together?
3. The ratio of boys to girls in a class is 3:2. If there are 15 boys, how many girls are there?

**Problem Solving:**
1. A shopkeeper marks up his goods by 40% but gives a discount of 10%. What is his profit percentage?
2. In a data set: 12, 15, 18, 20, 25, find the median and mean.

### How to Answer:

**Multiple Choice Answers:**
1. c) 320 - If 25% = 80, then 100% = 80 × 4 = 320
2. a) 75 km/h - Speed = 300/4 = 75 km/h
3. a) 36 - 15% of 240 = 240 × 15/100 = 36

**Short Answer Solutions:**
1. **Compound Interest**: CI = 5000(1 + 10/100)² - 5000 = 5000(1.1)² - 5000 = 6050 - 5000 = ₹1050
2. **Combined Work**: A's rate = 1/12, B's rate = 1/15, Combined = 1/12 + 1/15 = 9/60 = 3/20, Time = 20/3 = 6.67 days
3. **Ratio**: If boys:girls = 3:2 and boys = 15, then girls = (15/3) × 2 = 10

**Problem Solutions:**
1. **Profit calculation**: Let CP = 100, SP = 140 × 0.9 = 126, Profit% = (126-100)/100 × 100 = 26%
2. **Statistics**: Median = 18 (middle value), Mean = (12+15+18+20+25)/5 = 18

### Tips and Common Mistakes:
• **Read questions carefully** - identify what's being asked
• **Use shortcuts** - learn percentage, ratio shortcuts
• **Check units** - ensure consistent units in calculations
• **Practice mental math** - improves speed significantly
• **Double-check answers** - verify calculations
• **Time management** - don't spend too long on one question

---

## 5. Logical Reasoning and Problem Solving

### Key Notes:
• **Pattern Recognition**: Number series, letter series, figure series
• **Logical Sequences**: Identify the rule and find next term
• **Analogies**: A:B :: C:? format, find relationships
• **Classification**: Odd one out, grouping similar items
• **Coding-Decoding**: Letter/number substitution patterns
• **Blood Relations**: Family tree relationships, generation analysis
• **Direction Sense**: North, South, East, West navigation
• **Ranking and Arrangement**: Linear, circular arrangements
• **Logical Deduction**: If-then statements, syllogisms
• **Puzzles**: Seating arrangements, scheduling problems
• **Venn Diagrams**: Set relationships, logical operations
• **Statement and Assumptions**: What assumptions are made
• **Data Sufficiency**: Is given information enough to solve

### Practice Questions:

**Multiple Choice:**
1. Find the next number in series: 2, 6, 12, 20, ?
   a) 28 b) 30 c) 32 d) 24

2. If CODING is written as DPEJOH, how is PYTHON written?
   a) QZUIPO b) QZUIPM c) QZUIPO d) QZUIOP

3. A is B's father. B is C's mother. What is A to C?
   a) Father b) Grandfather c) Uncle d) Brother

**Short Answer:**
1. Complete the analogy: Book : Library :: Car : ?
2. If you face North and turn 90° clockwise, then 180° anticlockwise, which direction are you facing?
3. Find the odd one out: Apple, Banana, Carrot, Orange

**Problem Solving:**
1. Five friends sit in a row. A is not at either end. B is to the immediate left of C. D is at one end. Where is E?
2. All roses are flowers. Some flowers are red. What can you conclude?

### How to Answer:

**Multiple Choice Answers:**
1. b) 30 - Pattern: +4, +6, +8, +10 (differences increase by 2)
2. a) QZUIPO - Each letter is shifted by +1 position
3. b) Grandfather - A is B's father, B is C's mother, so A is C's grandfather

**Short Answer Solutions:**
1. **Analogy**: Garage/Parking (place where cars are kept/stored)
2. **Direction**: North → East (90° clockwise) → West (180° anticlockwise)
3. **Odd one**: Carrot (vegetable, others are fruits)

**Problem Solutions:**
1. **Seating**: If D is at one end, B is left of C, A is not at ends, possible arrangement: D-E-A-B-C or D-B-C-A-E
2. **Logical deduction**: Some roses might be red (since roses are flowers and some flowers are red)

### Tips and Common Mistakes:
• **Look for patterns** - numbers, letters, positions
• **Draw diagrams** - helps visualize relationships
• **Read carefully** - don't make assumptions
• **Eliminate options** - use process of elimination
• **Practice regularly** - improves pattern recognition
• **Time management** - move on if stuck

---

## 6. English Comprehension

### Key Notes:
• **Reading Comprehension**: Main idea, supporting details, author's tone
• **Vocabulary**: Synonyms, antonyms, word meanings in context
• **Grammar**: Tenses, subject-verb agreement, prepositions, articles
• **Sentence Structure**: Simple, compound, complex sentences
• **Parts of Speech**: Noun, verb, adjective, adverb, pronoun
• **Active/Passive Voice**: Subject performs action vs. subject receives action
• **Direct/Indirect Speech**: Quoted speech vs. reported speech
• **Comprehension Skills**: Inference, conclusion, assumption identification
• **Error Spotting**: Grammar, spelling, punctuation errors
• **Paragraph Formation**: Logical sequence, coherence
• **Cloze Test**: Fill in blanks with appropriate words
• **Idioms and Phrases**: Common expressions and their meanings

### Practice Questions:

**Multiple Choice:**
1. Choose the correct synonym for "abundant":
   a) scarce b) plentiful c) limited d) rare

2. Identify the error: "Each of the students have completed their assignment."
   a) Each of b) students have c) completed their d) No error

3. Change to passive voice: "The teacher explains the lesson."
   a) The lesson is explained by the teacher b) The lesson was explained by the teacher c) The lesson will be explained by the teacher d) The lesson has been explained by the teacher

**Short Answer:**
1. What is the difference between "affect" and "effect"?
2. Explain the difference between simple past and present perfect tense.
3. What is a dangling modifier?

**Comprehension:**
Read the passage and answer: "Technology has revolutionized education. Online learning platforms provide access to quality education globally. However, digital divide remains a challenge."

1. What is the main idea of the passage?
2. What challenge is mentioned regarding technology in education?

### How to Answer:

**Multiple Choice Answers:**
1. b) plentiful - Abundant means existing in large quantities
2. b) students have - Should be "has" (Each takes singular verb)
3. a) The lesson is explained by the teacher - Present tense passive

**Short Answer Solutions:**
1. **Affect vs Effect**: Affect is a verb (influence), Effect is a noun (result)
2. **Tenses**: Simple past (completed action), Present perfect (past action with present relevance)
3. **Dangling modifier**: Modifier that doesn't clearly relate to the word it's supposed to modify

**Comprehension Solutions:**
1. **Main idea**: Technology has transformed education through online platforms
2. **Challenge**: Digital divide (unequal access to technology)

### Tips and Common Mistakes:
• **Read questions first** - helps focus while reading
• **Look for keywords** - main idea, author's opinion, specific details
• **Context clues** - use surrounding words to understand meanings
• **Grammar rules** - review basic grammar concepts
• **Practice reading** - improves speed and comprehension
• **Time allocation** - don't spend too much time on one passage

---

## General Test-Taking Strategies:

### Time Management:
• **Allocate time per section** - don't spend too long on difficult questions
• **Quick review** - save 5-10 minutes for final review
• **Mark and return** - flag difficult questions, return if time permits

### Preparation Tips:
• **Practice mock tests** - familiarize with exam format
• **Review basics** - ensure strong foundation in fundamentals
• **Stay calm** - manage test anxiety through preparation
• **Read instructions carefully** - understand marking scheme

### Common Mistakes to Avoid:
• **Rushing through questions** - accuracy over speed
• **Not reading full question** - missing key information
• **Overthinking** - trust first instinct for simple questions
• **Leaving blanks** - attempt all questions if no negative marking
• **Poor time distribution** - balance time across all sections

Good luck with your pretest! Focus on understanding concepts rather than memorizing, and practice regularly to build confidence.
