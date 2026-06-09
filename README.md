# Student Course Registration System

A terminal-based Python application for managing students, courses, and registrations.

## Features
- Add students with validation
- Add courses with capacity limits
- Register students to courses
- Prevent duplicate IDs and duplicate registrations
- View all students and all courses
- Search students by ID, name, or email
- View students registered in a course
- View courses for a student
- Save and load data to/from JSON files

## Project Structure
- `main.py` — application entry point and CLI menu
- `models/person.py` — base class for `Student`
- `models/student.py` — student model using inheritance
- `models/course.py` — course model
- `services/school_system.py` — core registration system logic
- `data/` — data directory for saved JSON files

## How to Run
From the project folder:

```bash
python3 main.py
```

Use the menu options to add students, add courses, register students, and save/load data.

## Notes
- Default automatic load file is `data/data.json` if it exists.
- When exiting, you can choose to save the current data.
