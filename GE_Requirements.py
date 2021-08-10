import pandas as pd


class GeRequirements:
    ge_dataframe = pd.read_csv("PlanA_GE.csv")

    def __init__(self, degree_applicable_dict):
        self.degree_applicable_dict = degree_applicable_dict
        self.completed_ge_courses = {}
        self.completed_ge_units = []

    def ge_courses_completed(self, area_name):

        for i in range(len(GeRequirements.ge_dataframe[area_name])):
            for key in self.degree_applicable_dict:
                if key == GeRequirements.ge_dataframe.loc[i, area_name]:
                    if area_name not in self.completed_ge_courses:
                        self.completed_ge_courses[area_name] = key
                        if "Proficiency" not in area_name:
                            self.completed_ge_units.append(self.degree_applicable_dict[key])
                        # total = sum(self.completed_ge_units)
        return self.completed_ge_courses, self.completed_ge_units

    def area_e_ge_requirements(self):
        area_e_list = []
        total_ge_units = sum(self.completed_ge_units)
        print("total ge units", total_ge_units)
        for i in range(len(GeRequirements.ge_dataframe['Electives'])):
            for key in self.degree_applicable_dict:
                # print(key)
                if key == GeRequirements.ge_dataframe.loc[i, 'Electives']:
                    print('ge elective', GeRequirements.ge_dataframe.loc[i, 'Electives'])
                    print('key', key)
                    print(self.completed_ge_courses)
                    print('len of Ge dict', len(self.completed_ge_courses))
                    # print('ge len', len(self.completed_ge_courses))
                    # print('ge courses', self.completed_ge_courses)
                    # print('ge units', self.completed_ge_units)
                    if len(self.completed_ge_courses) == 8:
                        print('total units', total_ge_units)
                        if total_ge_units < 18:
                            print('past 18 units')
                            area_e_list.append(key)
                            self.completed_ge_courses['AreaE'] = area_e_list
                            self.completed_ge_units.append(self.degree_applicable_dict[key])
        return self.completed_ge_courses

    def reading_proficiency(self):
        if 'Reading Proficiency' not in self.completed_ge_courses:
            if sum(self.completed_ge_units) > 10:
                self.completed_ge_courses['Reading_Proficiency'] = 'Met(GE Units)'
        return self.completed_ge_courses

