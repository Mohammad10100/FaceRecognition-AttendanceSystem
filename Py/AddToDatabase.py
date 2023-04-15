import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-6d95f-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    # "321654":
    #     {
    #         "name": "Murtuza hassan",
    #         "role": "Student",
    #         "major": "Data Science",
    #         "starting_year": 2021,
    #         "total_attendance": 7,
    #         "standing": "G",
    #         "year": 4,
    #         "last_attendance_time": "2022-12-11 00:54:34"
    #     },
    "852741":
        {
            "name": "Emly Blunt",
            "role": "Student",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "role": "Student",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1391158261":
        {
            "name": "Prof. Ashfaque",
            "role": "Faculty",
            "major": "",
            "Subjects": "Java, Python",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1421218902132":
        {
            "name": "Prof. Anupam",
            "role": "Faculty",
            "major": "",
            "Subjects": "CG, OS",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1391163574":
        {
            "name": "Prof. Junaid",
            "role": "Faculty",
            "major": "",
            "Subjects": "Microprocessor",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1567049423546":
        {
            "name": "Prof. Reshma",
            "Subjects": "Data Structure",
            "major": "",
            "role": "Faculty",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "128736286":
        {
            "name": "Mohammad Abdul Lateef",
            "role": "Student",
            "major": "CyberSecurity",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)