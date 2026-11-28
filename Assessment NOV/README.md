# Employee Payroll Management System

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run `database/schema.sql` in MySQL.
3. Set `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, and optionally `DB_NAME`.
4. From the `EmployeePayrollSystem` folder, run `python main.py`.

The application follows the required database, DAO, service, and main layers. All SQL is contained in `dao/employee_dao.py` and uses parameterized queries.
