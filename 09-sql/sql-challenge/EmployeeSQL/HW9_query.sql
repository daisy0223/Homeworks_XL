--1--List the following details of each employee: employee number, last name, first name, sex, and salary.
SELECT COUNT(*) FROM employees
SELECT COUNT(*) FROM salaries
SELECT e.emp_no,
  e.last_name,
  e.first_name,
  e.sex,
  s.salary
FROM employees as e
INNER JOIN salaries as s ON
e.emp_no= s.emp_no;

--2-List first name, last name, and hire date for employees who were hired in 1986
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

--3-List the manager of each department with the following information: department number, department name, 
--the manager's employee number,last name, first name.
SELECT dept_manager.dept_no, dept_manager.emp_no, departments.dept_name, employees.first_name, employees.last_name
FROM ((dept_manager
INNER JOIN departments ON dept_manager.dept_no = departments.dept_no)
INNER JOIN employees ON dept_manager.emp_no = employees.emp_no);

--4-List the department of each employee with the following information: employee number, last name, first name, 
--and department name. 
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM ((employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no)
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no);

--5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B." "B%"
SELECT employees.first_name, employees.last_name, employees.sex
FROM employees
WHERE first_name='Hercules' AND last_name LIKE 'B%'

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM ((employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no)
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no)
WHERE departments.dept_name='Sales'

--7--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM ((employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no)
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no)
WHERE departments.dept_name='Sales' OR departments.dept_name='Development'

--8--In descending order list the frequency count of employee last names, i.e., how many employees share each last name.
 Select last_name, count(*)
 From employees
 Group By last_name
 ORDER BY count(*) DESC