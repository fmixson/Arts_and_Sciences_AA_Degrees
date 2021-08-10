import pandas as pd

from Degree_Applicable_Electives import DegreeApplicableUnits
from Degree_Completion_Report import DegreeCompletionReport
from GE_Progress_Report import GEProgress
from GE_Requirements import GeRequirements
from Major_Progress import MajorProgress
from Major_Requirements import MajorRequirements
from Student_Info import StudentInfo


# def degree_processing(student_id, courses, major, major1, major1_units, major1_disciplines, major2,
#                       major2_units, major3, major3_units, major4, major4_units, major4_disciplines, major5, major5_units,
#                       major_course_requirements, major_name):
def degree_processing(student_id, courses, major, major_name, major_course_requirements, **kwargs):
    print('kwargs',kwargs)
    print('kwargs len', len(kwargs))
    student = StudentInfo(student_id, courses)
    student.eligible_course_list()
    ge_requirements = GeRequirements(student.degree_applicable_dict)
    ge_requirements.ge_courses_completed('Math_Proficiency')
    ge_requirements.ge_courses_completed('Writing_Proficiency')
    ge_requirements.ge_courses_completed('Health_Proficiency')
    ge_requirements.ge_courses_completed('Reading_Proficiency')
    ge_requirements.ge_courses_completed('Nat_Sci')
    ge_requirements.ge_courses_completed('Soc_Sci')
    # ge_requirements.ge_courses_completed('Beh_Sci')
    ge_requirements.ge_courses_completed('FA_Hum')
    ge_requirements.ge_courses_completed('Comp')
    ge_requirements.ge_courses_completed('Analytic')
    ge_requirements.area_e_ge_requirements()
    major = MajorRequirements(revised_course_list=student.degree_applicable_dict,
                              completed_ge_courses=ge_requirements.completed_ge_courses,
                              major_requirements=major_course_requirements)
    if len(kwargs) == 15:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])
        major.major_courses_completed(area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                      number_of_disciplines=kwargs['major4_disciplines'])
        major.major_courses_completed(area_name=kwargs['major5'], total_units=kwargs['major5_units'],
                                      number_of_disciplines=kwargs['major5_disciplines'])
    elif len(kwargs) == 12:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])
        major.major_courses_completed(area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                      number_of_disciplines=kwargs['major4_disciplines'])

    elif len(kwargs) == 9:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])

    elif len(kwargs) == 6:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])

    elif len(kwargs) == 3:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])

    degree_applicable_units = DegreeApplicableUnits(student.eligible_course_list(),
                                                    major.major_courses_list,
                                                    ge_requirements.area_e_ge_requirements(),
                                                    ge_requirements.completed_ge_units,
                                                    major.major_units_list)
    degree_applicable_units.elective_courses()
    ge_requirements.reading_proficiency()

    degree_reports = GEProgress(ge_requirements.completed_ge_courses, ge_requirements.completed_ge_units,
                                student.student_id)
    degree_reports.ge_requirements_completed()
    degree_reports.area_e_requirements_completed()
    degree_reports.area_e_requirements_completed()
    major_report = MajorProgress(student_id=student.student_id,
                                 major_course_dict=major.major_course_dict,
                                 major_units=major.major_units_list,
                                 area_units=major.area_units_dict,
                                 no_of_courses_required=major.major_no_courses_requirement_dict)

    major_report.major_requirements_completed()

    degree_completion = DegreeCompletionReport(
        major_requirements_dict=major.major_requirements_dict,
        completed_ge_courses=ge_requirements.completed_ge_courses,
        completed_ge_units=ge_requirements.completed_ge_units,
        major_course_dict=major.major_course_dict,
        area_units_dict=major.area_units_dict,
        elective_courses=degree_applicable_units.elective_course_list,
        elective_units=degree_applicable_units.elective_units_list,
        major_units_list=major.major_units_list,
        student_id=student_id,
        student_major=major_name,
        missing_ge=degree_reports.missing_ge_courses,
        missing_major_courses=major_report.missing_courses_dict2)
    degree_completion.degree_completion()
#End of function

pd.set_option('display.max_columns', None)

student_course_list = pd.read_csv(
    "C:/Users/fmixson/Desktop/Programming/Enrollment_Histories/A bit longer Enrollment history.csv")
student_id_list = []

for i in range(len(student_course_list)):
    if student_course_list.loc[i, "ID"] not in student_id_list:
        student_id_list.append(student_course_list.loc[i, "ID"])

for student_id in student_id_list:
        degree_processing(student_id=student_id, courses=student_course_list, major='art_major_requirements',
                          major_name="Art_and_Culture", major_course_requirements="Arts_and_Culture_AA.csv",
                          major1='Required', major1_units=9, major1_disciplines=1,
                          major2='West_Art', major2_units=3, major2_disciplines=1,
                          major3='Non_West_Art', major3_units=3, major3_disciplines=1,
                          major4='Lit_and_Perf_Art', major4_units=3, major4_disciplines=1,
                          major5='Art_and_Culture', major5_units=3, major5_disciplines=1)

        degree_processing(student_id=student_id, courses=student_course_list, major='as_comm_major_requirements',
                          major_name="AS_Comm", major_course_requirements="AS_Comm_AA.csv",
                          major1='Comm1', major1_units=3, major1_disciplines=1,
                          major2='Comm2', major2_units=3, major2_disciplines=1,
                          major3='Crit_Think', major3_units=3, major3_disciplines=1,
                          major4='Electives', major4_units=9, major4_disciplines=2)

        degree_processing(student_id=student_id, courses=student_course_list, major='cul_and_soc_major_requirements',
                          major_name="Culture/Society", major_course_requirements="Culture_and_Society_AA.csv",
                          major1="World_Soc", major1_units=6, major1_disciplines=2,
                          major2="Arts", major2_units=6, major2_disciplines=2,
                          major3="World_Hist_Pol_Inst", major3_units=6, major3_disciplines=2,
                          major4="World_Lit", major4_units=3, major4_disciplines=1)

        degree_processing(student_id=student_id, courses=student_course_list, major='earth_and_space_major_requirements',
                          major_name="Earth/Space", major_course_requirements="Earth_and_Space_AA.csv",
                          major1="Astr", major1_units=6, major1_disciplines=1,
                          major2="Astr_Lab", major2_units=1, major2_disciplines=1,
                          major3="Earth_Sci", major3_units=6, major3_disciplines=1,
                          major4='Earth_Sci_Lab', major4_units=1, major4_disciplines=1,
                          major5='Astr_Esci', major5_units=3, major5_disciplines=1)

        degree_processing(student_id=student_id, courses=student_course_list, major='hist_persp_major_requirements',
                          major_name="History_Persp_AA", major_course_requirements="Hist_Persp_AA.csv",
                          major1="Amer_Hist", major1_units=6, major1_disciplines=1,
                          major2="World_Hist", major2_units=6, major2_disciplines=1,
                          major3="Arts_Sci_Hist", major3_units=6, major3_disciplines=1)

        degree_processing(student_id=student_id, courses=student_course_list, major='lit_and_lang_major_requirements',
                          major_name="Lit_and_Lang_AA", major_course_requirements="Lit_and_Lang_AA.csv",
                          major1="Core", major1_units=3, major1_disciplines=1,
                          major2="Lit_Lang", major2_units=15, major2_disciplines=1)

        degree_processing(student_id=student_id, courses=student_course_list, major='media_major_requirements',
                          major_name="Media_Studies", major_course_requirements="Media_Studies_AA.csv",
                          major1="Media", major1_units=18, major1_disciplines=2)

        degree_processing(student_id=student_id, courses=student_course_list, major='english_major_requirements',
                          major_name="English_AA", major_course_requirements="English_AA.csv",
                          major1="Core1", major1_units=4, major1_disciplines=1,
                          major2="Core2", major2_units=3, major2_disciplines=1,
                          major3="Lit", major3_units=12, major3_disciplines=1)

        degree_processing(student_id=student_id, courses=student_course_list,
                          major='self_def_soc_behav_major_requirements',
                          major_name="Self_Dev_Soc_Behav", major_course_requirements="Self_Dev_Soc_Behav_AA.csv",
                          major1="Theory_Background", major1_units=6, major1_disciplines=1,
                          major2="Stud_Dev_App", major2_units=3, major2_disciplines=1,
                          major3="Stud_Vit", major3_units=3, major3_disciplines=1)

        degree_processing(student_id=student_id, courses=student_course_list, major='soc_behav_sci_requirements',
                          major_name="Soc_Behav_Sci_AA", major_course_requirements="Soc_Behav_Sci_AA.csv",
                          major1="Soc_Behav", major1_units=18, major1_disciplines=3)

        degree_processing(student_id=student_id, courses=student_course_list, major='visual_comm_major_requirements',
                          major_name="Visual_Comm_AA", major_course_requirements="Visual_Comm_AA.csv",
                          major1="Crit_Analysis_Img", major1_units=3, major1_disciplines=1,
                          major2="Theories_Vis_Comm", major2_units=6, major2_disciplines=1,
                          major3="App_Tech_Comm", major3_units=9, major3_disciplines=1)


DegreeCompletionReport.LS_AA_Degrees_df.sort_values(by=['Total_Missing'], inplace=True, ascending=True)
DegreeCompletionReport.LS_AA_Degrees_df.to_csv(
    'C:/Users/fmixson/Desktop/Programming/Units_Sort_Arts_and_Sciences_AA_Degrees.csv')
DegreeCompletionReport.LS_AA_Degrees_df.sort_values(by=['Student_ID', 'Total_Missing'], inplace=True, ascending=True)
DegreeCompletionReport.LS_AA_Degrees_df.to_csv(
    'C:/Users/fmixson/Desktop/Programming/Student_Sort_Arts_and_Sciences_AA_Degrees.csv')



