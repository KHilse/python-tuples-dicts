employees = [
    {
    "name": "Ron Swanson",
    "age": 55,
    "department": "Management",
    "phone": "555-1234",
    "salary": "$87,000"
    },
    {
    "name": "Andy Dwyer",
    "age": 55,
    "department": "Shoe Shining",
    "phone": "555-1122",
    "salary": "$87,000"
    },
    {
    "name": "Leslie Knope",
    "age": 55,
    "department": "Middle Management",
    "phone": "555-4321",
    "salary": "$87,000"
    },
    {
    "name": "April Ludgate",
    "age": 55,
    "department": "Administration",
    "phone": "555-3345",
    "salary": "$87,000"
    },

    ]

for employee in employees:
    print(f"{employee['name']} in {employee['department']} can be reached at {employee['phone']}")