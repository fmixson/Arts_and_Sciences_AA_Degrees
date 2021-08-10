import pandas as pd

from Major_Requirements import MajorRequirements


class MajorProgress(MajorRequirements):
    # columns = ['Student_ID', 'Major1', 'Major2', 'Major3', 'Major4', 'Major5']
    # major_df = pd.DataFrame(columns=columns)
    requirements = []

    def __init__(self, student_id, major_course_dict, major_units, area_units, no_of_courses_required):
        self.area_units = area_units
        self.student_id = student_id
        self.major_course_dict = major_course_dict
        self.major_units = major_units
        self.major_df = pd.DataFrame
        self.no_of_courses_required = no_of_courses_required
        self.requirements_dict = {}
        self.missing_major_courses_dict = {}
        self.missing_courses_dict2 = {}
        # print('no of crses', self.no_of_courses_required)

    def major_requirements_completed(self):

        # requirements_for_major = dict.fromkeys(self.columns, 0)
        # length = len(MajorProgressReport.major_df)
        # print('req for maj', requirements_for_major)
        for major_key in self.no_of_courses_required:
            if major_key in self.major_course_dict:
                # print(self.no_of_courses_required)
                # print(self.major_course_dict)
                print(self.no_of_courses_required[major_key], len(self.major_course_dict))
                missing_courses = self.no_of_courses_required[major_key] - len(self.major_course_dict[major_key])
                if missing_courses > 0:
                    self.missing_major_courses_dict[major_key] = f'{int(missing_courses)} missing course(s)'
                    self.missing_courses_dict2[major_key] = int(missing_courses)
                    # print('missing', self.missing_courses_dict)
            else:
                self.missing_major_courses_dict[major_key] = f'{int(self.no_of_courses_required[major_key])} missing course(s)'
                self.missing_courses_dict2[major_key] = int(self.no_of_courses_required[major_key])
                print('missing', self.missing_major_courses_dict)
        total_missing_major_courses = sum(self.missing_courses_dict2.values())
        print('total', total_missing_major_courses)
        print('missing', self.missing_major_courses_dict)
        return self.missing_courses_dict2, total_missing_major_courses

