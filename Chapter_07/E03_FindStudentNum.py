def find_student_number(stu_no, stu_name, num):

    for i in range(0, len(stu_no)):

        if num == stu_no[i]:

            return stu_name[i]

    return "?"


if __name__ == '__main__':

    stu_no = [39, 14, 67, 105]

    stu_name = ['Justin', 'John', 'Mike', 'Summer']

    print (find_student_number(stu_no, stu_name, 105))
    print (find_student_number(stu_no, stu_name, 50))
