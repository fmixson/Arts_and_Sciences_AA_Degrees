import pandas as pd


class GEProgress:
    # columns = ['Student_ID', 'Major', 'GE_Status', 'Major_Status', 'Degree_Status', 'GE_Units', 'Total_Major_Units',
    #            'Degree_Major_Units', 'Elective_Units', 'Degree_Units','GE_Courses', 'Major_Courses', 'Elective_Courses']
    # degree_units_df = pd.DataFrame(columns=columns)
    # degree_units_df = pd.DataFrame(columns=columns)
    # degree_units_df.sort_values(by=['Degree_Units'], inplace=True, ascending=False)

    AA_ge_requirements = {'Math_Proficiency': 0, 'Writing_Proficiency': 0, 'Reading_Proficiency': 0,
                          'Health_Proficiency': 0, 'Nat_Sci': 0,
                          'Soc_Sci': 0, 'FA_Hum': 0, 'Comp': 0, 'Analytic': 0}

    def __init__(self, completed_ge_courses, completed_ge_units, student_id):
        self.student_id = student_id
        self.completed_ge_units = completed_ge_units
        self.completed_ge_courses = completed_ge_courses
        self.missing_ge_courses = []

    def ge_requirements_completed(self):
        # length = len(DegreeProgressReports.degree_units_df)
        for ge_key in GEProgress.AA_ge_requirements:
            # print('ge key', ge_key)
            # print('aa require', DegreeProgressReports.AA_ge_requirements)
            if ge_key not in self.completed_ge_courses:
                self.missing_ge_courses.append(ge_key)
        # print('missing ge', self.missing_ge_courses)
        # print('no of missing ge', len(self.missing_ge_courses))
        # DegreeProgressReports.degree_courses_df.loc[length, 'GE_Courses'] = ge_list
        # major_list = self.major_course_dict.items()

    def area_e_requirements_completed(self):
        # print('len of ge courses',len(self.completed_ge_courses))
        if len(self.completed_ge_courses) == 10:
            if sum(self.completed_ge_units) < 18:
                self.missing_ge_courses.append('AreaE')
        # print(len(self.completed_ge_units))
        # print(sum(self.completed_ge_units))
        # print('no of missing ge2', len(self.missing_ge_courses))
        return self.missing_ge_courses

