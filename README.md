## models/student.py

- `class Student:`
  - Đại diện cho một sinh viên, gồm các thuộc tính như mã số, tên, tuổi, điểm số...

## utils/io.py

- `def read_students_from_file(path):`
  - Đọc danh sách sinh viên từ file JSON.
- `def write_students_to_file(path, students):`
  - Ghi danh sách sinh viên ra file JSON.

## controllers/student_controllers.py

- `def add_student(student_list, student):`
  - Thêm một sinh viên vào danh sách.
- `def remove_student(student_list, student_id):`
  - Xóa sinh viên theo mã số.
- `def update_student(student_list, student_id, new_info):`
  - Cập nhật thông tin sinh viên.
- `def find_student(student_list, student_id):`
  - Tìm kiếm sinh viên theo mã số.
