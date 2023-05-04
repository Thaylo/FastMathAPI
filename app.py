from flask import Flask, request, jsonify
import sympy
import cachetools

app = Flask(__name__)

# Calculate the max number of items for the LRU cache based on an approximate size per item
bytes_per_item = 1000  # Adjust this value based on the expected average size of cache items
max_items = 4 * (10**9) // bytes_per_item
cache = cachetools.LRUCache(max_items)

def solve_equation(equation, variable):
    expression = sympy.sympify(equation)
    variable = sympy.Symbol(variable)
    solution = sympy.solve(expression, variable)
    return solution

def get_solution_from_cache_or_solve(equation, variable):
    cache_key = f"{equation}-{variable}"
    if cache_key in cache:
        return cache[cache_key]
    else:
        solution = solve_equation(equation, variable)
        cache[cache_key] = solution
        return solution

@app.route('/solve', methods=['POST'])
def solve_api():
    data = request.get_json()
    equation = data.get('equation')
    variable = data.get('variable')

    if not equation or not variable:
        return jsonify({"error": "Missing equation or variable"}), 400

    try:
        solution = get_solution_from_cache_or_solve(equation, variable)
        return jsonify({"solution": str(solution)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
