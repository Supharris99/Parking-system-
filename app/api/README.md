# API Documentation

## Student Endpoints

### GET /api/mahasiswa/list
Get all registered students.

### GET /api/mahasiswa/{nim}
Get student details by NIM.

### GET /api/mahasiswa/plate/{license_plate}
Get student details by license plate.

### POST /api/mahasiswa/register
Register a new student.
```json
{
    "nim": "string",
    "name": "string",
    "major": "string",
    "phone": "string",
    "license_plate": "string"
}
```

### PUT /api/mahasiswa/{nim}
Update student information.
```json
{
    "name": "string",
    "major": "string",
    "phone": "string",
    "license_plate": "string"
}
```

### DELETE /api/mahasiswa/{nim}
Delete a student record.

## Parking Endpoints

### GET /api/parking/active
Get all active parking records.
Query params:
- plate (optional): Filter by license plate

### GET /api/parking/history
Get parking history.
Query params:
- limit (optional): Limit number of records (default: 100)

### GET /api/parking/student/{nim}/history
Get parking history for specific student.
Query params:
- limit (optional): Limit number of records (default: 10)

### POST /api/parking/entry
Record parking entry.
```json
{
    "license_plate": "string"
}
```

### POST /api/parking/exit
Record parking exit.
```json
{
    "license_plate": "string"
}
``` 