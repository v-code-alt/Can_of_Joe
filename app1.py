from flask import Flask, request, render_template_string

app = Flask(__name__)

# Helper function for Task 3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# HTML Template (single page, inline)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hackathon Challenge</title>
</head>
<body style="font-family: Arial; margin: 30px;">
    <h1>🚀 Hackathon Challenge</h1>
    <hr>

    <!-- Task 1 -->
    <h2>Task 1: Temperature Converter</h2>
    <form method="POST">
        <label>Temperature:</label>
        <input type="number" step="0.01" name="temp" required>
        <select name="conversion">
            <option value="CtoF">Celsius ➝ Fahrenheit</option>
            <option value="FtoC">Fahrenheit ➝ Celsius</option>
        </select>
        <button type="submit" name="task" value="task1">Convert</button>
    </form>
    {% if result1 %}
        <p><strong>Result:</strong> {{ result1 }}</p>
    {% endif %}
    <hr>

    <!-- Task 2 -->
    <h2>Task 2: Student Grades</h2>
    <form method="POST">
        <button type="submit" name="task" value="task2">Show Students with Grade ≥ 85</button>
    </form>
    {% if result2 %}
        <p><strong>Students with grade ≥ 85:</strong></p>
        <ul>
        {% for name in result2 %}
            <li>{{ name }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    <hr>

    <!-- Task 3 -->
    <h2>Task 3: Prime Number Generator</h2>
    <form method="POST">
        <label>Generate primes up to:</label>
        <input type="number" name="n" min="2" required>
        <button type="submit" name="task" value="task3">Generate</button>
    </form>
    {% if result3 %}
        <p><strong>Prime Numbers:</strong> {{ result3 }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def hackathon():
    result1 = None
    result2 = None
    result3 = None

    if request.method == "POST":
        task = request.form.get("task")

        # Task 1: Temperature conversion
        if task == "task1":
            try:
                temp = float(request.form["temp"])
                conversion = request.form["conversion"]
                if conversion == "CtoF":
                    result1 = f"{temp}°C = {(temp * 9/5) + 32:.2f}°F"
                else:
                    result1 = f"{temp}°F = {(temp - 32) * 5/9:.2f}°C"
            except ValueError:
                result1 = "Invalid input."

        # Task 2: Dictionary of students and grades
        elif task == "task2":
            students = {
                "Alice": 90,
                "Bob": 82,
                "Charlie": 88,
                "Diana": 95,
                "Evan": 76
            }
            result2 = [name for name, grade in students.items() if grade >= 85]

        # Task 3: Generate primes up to N
        elif task == "task3":
            try:
                n = int(request.form["n"])
                primes = [x for x in range(2, n+1) if is_prime(x)]
                result3 = primes
            except ValueError:
                result3 = "Invalid input."

    return render_template_string(HTML_PAGE, result1=result1, result2=result2, result3=result3)

if __name__ == "__main__":
    app.run(debug=True)
