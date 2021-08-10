from GE_Requirements import GeRequirements


class DegreeApplicableUnits(GeRequirements):

    def __init__(self, degree_applicable_dict, major_courses_list, completed_ge_courses, completed_ge_units,
                 major_units_list):
        self.degree_applicable_dict = degree_applicable_dict
        self.major_courses_list = major_courses_list
        self.major_units_list = major_units_list
        self.completed_ge_courses = completed_ge_courses
        self.completed_ge_units = completed_ge_units
        self.elective_course_list = []
        self.elective_units_list = []
        self.elective_dict = {}

    def elective_courses(self):
        proficiency_list = ['Writing_Proficiency', 'Math_Proficiency', 'Health_Proficiency', 'Reading_Proficiency']
        ge_course_list = []
        ge_course = False
        major_course = False
        elective_course = False
        degree_units = sum(self.completed_ge_units) + sum(self.major_units_list) + sum(
            self.elective_units_list)
        for key in self.completed_ge_courses:
            if key not in proficiency_list:
                ge_course_list.append(self.completed_ge_courses[key])
                # print('elective ge courses', ge_course_list)
        for course_key in self.degree_applicable_dict:
            # print('degree units', degree_units)
            if degree_units < 60:
                ge_course = False
                major_course = False
                # print('course key', course_key)
                # print('GE list', self.completed_ge_courses)

                if course_key in ge_course_list:
                    ge_course = True

                if course_key in self.major_courses_list:
                    major_course = True

                if course_key in self.elective_course_list:
                    elective_course = True

                if not ge_course:
                    if not major_course:
                        if not elective_course:
                            self.elective_course_list.append(course_key)
                            # print('elective list', self.elective_course_list)
                            self.elective_units_list.append(self.degree_applicable_dict[course_key])
                            degree_units = sum(self.completed_ge_units) + sum(self.major_units_list) + sum(
                                self.elective_units_list)
