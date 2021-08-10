import pandas as pd



class DegreeCompletionReport:
    columns = ['Student_ID', 'Major', 'GE_Status', 'Major_Status', 'Degree_Status', 'GE_Units', 'Total_Major_Units',
               'Degree_Major_Units', 'Elective_Units', 'Degree_Units', 'Total_Missing', 'GE_Missing', 'Major_Missing', 'Missing_GE',
               'Missing_Major', 'GE_Courses', 'Major_Courses', 'Elective_Courses']
    LS_AA_Degrees_df = pd.DataFrame(columns=columns)

    # degree_units_df.sort_values(by=['Total_Missing'], inplace=True, ascending=True)
    # columns2 = ['Student_ID', 'Major', 'Degree_Units', 'GE_Courses', 'Major_Courses', 'Elective_Courses']
    # degree_courses_df = pd.DataFrame(columns=columns2)

    def __init__(self, major_requirements_dict, completed_ge_courses, completed_ge_units, major_course_dict,
                 area_units_dict, elective_courses, elective_units, major_units_list, student_id, student_major,
                 missing_ge, missing_major_courses):
        self.missing_major_courses = missing_major_courses
        self.missing_ge = missing_ge
        self.major_units_list = major_units_list
        self.elective_units = elective_units
        self.elective_courses = elective_courses
        self.area_units_dict = area_units_dict
        self.major_course_dict = major_course_dict
        self.completed_ge_units = completed_ge_units
        self.completed_ge_courses = completed_ge_courses
        self.student_id = student_id
        self.student_major = student_major
        self.major_requirements_dict = major_requirements_dict
        print('MISSING maj course dic', self.missing_major_courses)

    def degree_completion(self):
        degree_status_ge = False
        degree_status_major = False
        # length1 = len(DegreeCompletion.degree_units_df)
        length = len(DegreeCompletionReport.LS_AA_Degrees_df)
        if len(self.completed_ge_courses) >= 10:
            if sum(self.completed_ge_units) >= 18:
                DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Status'] = 'Completed'
                degree_status_ge = True
            else:
                DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Status'] = 'Incomplete'
        else:
            DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Status'] = 'Incomplete'
            # print(('mcd',len(self.major_course_dict)), ('mrd', len(self.major_requirements_dict)))
            # print(('mcd', (self.major_course_dict)), ('mrd', (self.major_requirements_dict)))
        if len(self.major_course_dict) == len(self.major_requirements_dict):
            print(sum(self.area_units_dict.values()), sum(self.major_requirements_dict.values()))
            if sum(self.area_units_dict.values()) >= sum(self.major_requirements_dict.values()):
                DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Status'] = 'Completed'
                degree_status_major = True
            else:
                DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Status'] = 'Incomplete'
        else:
            DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Status'] = 'Incomplete'

        if sum(self.completed_ge_units) + sum(self.major_units_list) + sum(self.elective_units) >= 60:
            if degree_status_ge == True and degree_status_major == True:
                DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Status'] = 'Completed'
            else:
                DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Status'] = 'Incomplete'
        else:
            DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Status'] = 'Incomplete'

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Student_ID'] = self.student_id
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major'] = self.student_major
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Units'] = sum(self.completed_ge_units)
        major_units_total_value = sum(self.area_units_dict.values())
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Total_Major_Units'] = major_units_total_value
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Major_Units'] = sum(self.major_units_list)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Elective_Units'] = sum(self.elective_units)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Units'] = sum(self.completed_ge_units) + sum(
            self.elective_units) + sum(self.major_units_list)
        missing_major_list = sum(self.missing_major_courses.values())
        # print('missing ge', len(self.missing_ge), 'missing major', len(missing_major_list))
        total_missing = len(self.missing_ge) + missing_major_list
        major_courses_missing = self.missing_major_courses.items()
        # print(total_missing)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Total_Missing'] = total_missing
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Missing'] = len(self.missing_ge)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Missing'] = missing_major_list

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Missing_GE'] = self.missing_ge
        print('major missing', major_courses_missing)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Missing_Major'] = major_courses_missing

        ge_list = self.completed_ge_courses.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Courses'] = ge_list
        major_list = self.major_course_dict.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Courses'] = major_list
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Elective_Courses'] = self.elective_courses

