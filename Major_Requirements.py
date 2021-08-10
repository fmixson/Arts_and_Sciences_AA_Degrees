import pandas as pd


class MajorRequirements:
    # major_requirements_dataframe = pd.read_csv("C:/Users/family/Desktop/Programming/English_PlanA_GE.csv")
    # major_requirements_dataframe = pd.read_csv("C:/Users/family/Desktop/Programming/Copy of COMM_AA.csv")
    # major_requirements_dict = {}

    def __init__(self, revised_course_list, completed_ge_courses, major_requirements):
        self.major_requirements = major_requirements
        self.revised_course_list = revised_course_list
        self.completed_ge_courses = completed_ge_courses
        self.major_course_dict = {}
        self.major_courses_list = []
        self.major_courses_list2 = []
        self.major_units_list = []
        self.major_units_dict = {}
        self.area_units_dict = {}
        self.major_requirements_dict = {}
        self.major_no_courses_requirement_dict = {}
        # self.discipline_list = []
        # self.discipline_set = set()

    def _two_disciplines(self, course_key, total_area_units, total_units):
        discipline = course_key.split()
        discipline = discipline[0]
        disc = False
        # print('area units', total_area_units, 'total units', total_units - 3)
        if total_area_units == (total_units - 3):
            unique_disciplines = set(self.discipline_list)
            # print(len(unique_disciplines))
            # print('unique', unique_disciplines)
            if len(unique_disciplines) < 2:
                if discipline in unique_disciplines:
                    disc = True
                else:
                    self.discipline_list.append(discipline)
        else:
            self.discipline_list.append(discipline)
        # print('discipline list', self.discipline_list)
        return disc

    def _three_disciplines(self, course_key, total_area_units, total_units):
        discipline = course_key.split()
        discipline = discipline[0]
        disc = False
        # print('area units', total_area_units, 'total units', total_units - 6)
        if total_area_units >= (total_units - 6):
            unique_disciplines = set(self.discipline_list)
            # print(len(unique_disciplines))
            # print('unique', unique_disciplines)
            if len(unique_disciplines) < 3:
                if len(unique_disciplines) == 2:
                    self.discipline_list.append(discipline)
                elif unique_disciplines == 1:
                    if discipline in unique_disciplines:
                        disc = True
            else:
                self.discipline_list.append(discipline)
        else:
            self.discipline_list.append(discipline)
        return disc

    def major_courses_completed(self, area_name, total_units, number_of_disciplines=1):
        proficiency_list = ['Writing_Proficiency', 'Math_Proficiency', 'Health_Proficiency', 'Reading_Proficiency']
        major_requirements_dataframe = pd.read_csv(self.major_requirements)
        self.major_courses_list2 = []
        total_area_units = 0
        area_units_list = []
        ge_course_list = []

        self.major_requirements_dict[area_name] = total_units
        print('total units', total_units)
        if total_units == '':
            pass
        else:
            if total_units < 3:
                self.major_no_courses_requirement_dict[area_name] = 1
            else:
                self.major_no_courses_requirement_dict[area_name] = total_units / 3

        disc = False
        self.discipline_list = []
        self.discipline_set = set()

        # print('maj course no', self.major_no_courses_requirement_dict)
        # print('maj req dict', self.major_requirements_dict)
        for key in self.completed_ge_courses:
            if key not in proficiency_list:
                ge_course_list.append(self.completed_ge_courses[key])

        for i in range(len(major_requirements_dataframe[area_name])):
            ge_course = False
            major_course = False

            if total_area_units < total_units:
                for course_key in self.revised_course_list:

                    if course_key == major_requirements_dataframe.loc[i, area_name]:
                        if course_key in ge_course_list:
                            ge_course = True

                        if course_key in self.major_courses_list:
                            major_course = True
                        if not major_course:
                            if number_of_disciplines > 1:
                                if number_of_disciplines == 2:
                                    disc = MajorRequirements._two_disciplines(self, course_key=course_key,
                                                                              total_area_units=total_area_units,
                                                                              total_units=total_units)
                                    # print(disc)
                                elif number_of_disciplines == 3:
                                    disc = MajorRequirements._three_disciplines(self, course_key=course_key,
                                                                                total_area_units=total_area_units,
                                                                                total_units=total_units)
                            if not disc:
                                self.area_units_dict[area_name] = self.revised_course_list[course_key]
                                self.major_courses_list.append(course_key)
                                self.major_courses_list2.append(course_key)
                                self.major_course_dict[area_name] = self.major_courses_list2
                                # print('dict under',self.major_course_dict)
                                area_units_list.append(self.revised_course_list[course_key])
                                if not ge_course:
                                    self.major_units_list.append(self.revised_course_list[course_key])

                    total_area_units = sum(area_units_list)
                    self.area_units_dict[area_name] = total_area_units
                    # print('maj course dict', self.major_course_dict)
        return self.major_requirements_dict, self.major_course_dict, self.major_no_courses_requirement_dict

