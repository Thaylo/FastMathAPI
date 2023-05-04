import requests

def solve_equation(equation, variable):
    url = 'http://localhost:8000/solve'
    payload = {'equation': equation, 'variable': variable}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        solution = response.json()['solution']
        print(f"The solution for the equation '{equation}' is: {solution}")
    else:
        error = response.json()['error']
        print(f"Error: {error}")

if __name__ == "__main__":
    equation = input("Enter the equation to be solved: ")
    variable = input("Enter the variable to be solved for: ")

    solve_equation(equation, variable)
