class StudentInfo:
    ineligible_courses = ['MATH 80A', 'MATH 60', 'ENGL 72', 'ENGL 52', 'ACLR 90', 'ACLR 91', 'ACLR 92', 'CHEM 95A',
                          'CHEM 95B', 'CHEM 95C', 'CHEM 95D', 'CHEM 95E', 'CHEM 95F', 'LIBR 50', 'LAW 98', 'LAW 99',
                          'BCOT 5A']
    ineligible_numbers = ['21A', '21B', '5A', '18.1', '3T', '1T', '6T', '42.07', '42.05']
    eligible_course_numbers1 = ['5L']
    eligible_course_numbers3 = ['5']
    eligible_course_numbers2 = ['50B', '50C', '51A', '51B', '51C', '52A', '52B', '52C', '62B', '71C', '60A', '62A',
                                '70A', '71A', '71B', '60L', '50A', '54A', '61A', '70C', '60B', '61B', '80B']
    eligible_grades = ['A', 'B', 'C', 'P']

    def __init__(self, student_id, courses):
        # self.major = major
        self.student_id = student_id
        self.courses = courses
        self.degree_applicable_dict = {}

    def eligible_course_list(self):
        for i in range(len(self.courses)):
            if self.student_id == self.courses.loc[i, "ID"]:
                if self.courses.loc[i, "Class Subject"] != "AED":
                    if self.courses.loc[i, "Course"] not in StudentInfo.ineligible_courses:
                        if self.courses.loc[i, "Class Catalog Number"] not in StudentInfo.ineligible_numbers:
                            course_number = self.courses.loc[i, "Class Catalog Number"]
                            if self.courses.loc[
                                i, 'Class Catalog Number'] in StudentInfo.eligible_course_numbers1:
                                course_number = course_number[0:1]
                                # print('eligible1', course_number)
                            if self.courses.loc[
                                i, 'Class Catalog Number'] in StudentInfo.eligible_course_numbers2:
                                course_number = course_number[0:2]
                                # print('eligible2', course_number)
                            else:
                                if len(str(course_number)) > 3:
                                    course_number = course_number[0:3]
                            if course_number == "5L" or course_number == '5':
                                self.degree_applicable_dict[self.courses.loc[i, "Course"]] = \
                                    self.courses.loc[i, "Units"]
                            else:
                                if int(course_number) >= 50:
                                    if self.courses.loc[i, 'Official Grade'] in StudentInfo.eligible_grades:
                                        self.degree_applicable_dict[
                                            self.courses.loc[i, "Course"]] = \
                                            self.courses.loc[i, "Units"]

        # print(self.student_id, self.degree_applicable_dict)
        return self.degree_applicable_dict

