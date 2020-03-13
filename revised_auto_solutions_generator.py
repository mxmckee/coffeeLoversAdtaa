import itertools


class Course:
    def __init__(self, course_number, course_title, course_days, course_time, course_discipline):
        self.courseNumber = course_number
        self.courseTitle = course_title
        self.courseDays = course_days
        self.courseTime = course_time
        self.courseDiscipline = course_discipline


class Instructor:
    def __init__(self, last_name, max_load, discipline_area):
        self.lastName = last_name
        self.maxLoad = max_load
        self.disciplineArea = discipline_area


def get_schedule_criteria():
    days = ['MW', 'TR']
    times = ['08:00 AM - 09:15 AM', '09:25 AM - 10:40 AM', '10:50 AM - 12:05 PM', '12:15 PM - 01:30 PM',
             '01:40 PM - 02:55 PM', '03:05 PM - 04:20 PM', '04:30 PM - 05:45 PM']
    disciplines = ['Programming - C++', 'Programming - Python', 'Game Development', 'Data Structures and Algorithms',
                   'Computer Organization', 'Operating Systems', 'Programming Languages', 'Cybersecurity',
                   'Mobile Applications', 'Artificial Intelligence', 'Networks', 'Theory of Computation',
                   'Parallel and Distributed Systems']

    # TODO: Modify course and instructor information to test different scenarios. The current scenario generates \
    #  65,536 possible schedules in ~16 seconds (I'm testing execution times...¯\_(ツ)_/¯)
    course1 = Course('CPSC 3300', 'Python Programming I', days[0], times[1], [disciplines[1]])
    course2 = Course('CPSC 3301', 'Game Design         ', days[0], times[2], [disciplines[1]])
    course3 = Course('CPSC 3302', 'AI                  ', days[0], times[3], [disciplines[1]])
    course4 = Course('CPSC 3303', 'Computer Security   ', days[0], times[4], [disciplines[1]])
    course5 = Course('CPSC 3304', 'Mobile Apps         ', days[0], times[5], [disciplines[1]])
    course6 = Course('CPSC 3305', 'Test1               ', days[0], times[6], [disciplines[1]])
    course7 = Course('CPSC 3306', 'Test2               ', days[1], times[0], [disciplines[1]])
    course8 = Course('CPSC 3307', 'Test3               ', days[1], times[1], [disciplines[1]])
    # course9 = Course('CPSC 3308', 'Test4               ', days[1], times[2], [disciplines[1]])
    # course10 = Course('CPSC 3309', 'Test5               ', days[1], times[3], [disciplines[1]])

    instructor1 = Instructor('Lovell', 8, [disciplines[1]])
    instructor2 = Instructor('Smith', 8, [disciplines[1]])
    instructor3 = Instructor('McKee', 8, [disciplines[1]])
    instructor4 = Instructor('T1', 8, [disciplines[1]])
    # instructor5 = Instructor('T2', 3, [disciplines[1]])
    # instructor6 = Instructor('T3', 2, [disciplines[1]])

    courses = [course1, course2, course3, course4, course5, course6, course7, course8]#, course9, course10]
    instructors = [instructor1, instructor2, instructor3, instructor4]#, instructor5, instructor6]

    return days, times, courses, instructors


def get_course_schedule(days, times, courses):
    scheduled_courses = []
    for day in days:
        for time in times:
            for course in courses:
                if course.courseDays == day and course.courseTime == time:
                    scheduled_courses.append(course)

    return scheduled_courses


def get_valid_instructor_combinations(instructors, scheduled_courses):
    temp_scheduled_courses = scheduled_courses.copy()
    master_list = []
    for course in temp_scheduled_courses:
        sub_list = []
        for instructor in instructors:
            if compare_two_lists(course.courseDiscipline, instructor.disciplineArea):
                sub_list.append(instructor)
        if len(sub_list) == 0:
            scheduled_courses.remove(course)
        else:
            master_list.append(sub_list)

    all_instructor_combinations = list(itertools.product(*master_list))

    combination_list = []
    for combination in all_instructor_combinations:
        sub_combination_list = []
        for instructor in combination:
            sub_combination_list.append(instructor)
        combination_list.append(sub_combination_list)

    master_list = []
    for combination in combination_list:
        list_of_sub_lists = sub_lists(combination)
        for sub_list in list_of_sub_lists:
            if len(sub_list) != 0:
                master_list.append(sub_list)

    invalid_instructor_combinations = []
    for combination in master_list:
        for instructor in instructors:
            if combination.count(instructor) > instructor.maxLoad:
                invalid_instructor_combinations.append(combination)
                break

    instructor_combinations = [x for x in master_list if x not in invalid_instructor_combinations]

    return instructor_combinations


def compare_two_lists(course_disciplines, instructor_disciplines):
    for discipline in course_disciplines:
        if discipline in instructor_disciplines:
            return True

    return False


def sub_lists(list1):
    sublist = [[]]
    for i in range(len(list1) + 1):
        for j in range(i + 1, len(list1) + 1):
            sub = list1[i:j]
            sublist.append(sub)

    return sublist


def get_auto_solutions(instructor_combinations, scheduled_courses):
    all_auto_solutions = []
    max_schedule_length = 0
    for combination in instructor_combinations:
        solution = [(i, j) for i, j in zip(scheduled_courses, combination) if
                    compare_two_lists(i.courseDiscipline, j.disciplineArea)]
        curr_max_schedule_length = len(solution)
        if curr_max_schedule_length > max_schedule_length:
            max_schedule_length = curr_max_schedule_length
        if len(solution) != 0:
            all_auto_solutions.append(solution)

    auto_solutions_of_max_length = []
    for solution in all_auto_solutions:
        if len(solution) == max_schedule_length:
            auto_solutions_of_max_length.append(solution)

    invalid_auto_solutions = []
    for solution in auto_solutions_of_max_length:
        for i in range(len(solution) - 1):
            for j in range(i + 1, len(solution)):
                if solution[i][0].courseDays == solution[j][0].courseDays and solution[i][0].courseTime == \
                        solution[j][0].courseTime and solution[i][1].lastName == solution[j][1].lastName:
                    invalid_auto_solutions.append(solution)
                    break
            break

    auto_solutions = [x for x in auto_solutions_of_max_length if x not in invalid_auto_solutions]

    return auto_solutions


def show_auto_solutions(auto_solutions):
    if len(auto_solutions) == 0:
        print('There are no valid schedules.')
    else:
        for i in range(len(auto_solutions)):
            print('Schedule #' + str(i + 1) + ':')
            for j in range(len(auto_solutions[i])):
                print(auto_solutions[i][j][0].courseNumber + '\t' + auto_solutions[i][j][0].courseTitle + '\t' +
                      auto_solutions[i][j][0].courseDays + '\t' + auto_solutions[i][j][0].courseTime + '\t' +
                      auto_solutions[i][j][1].lastName)
            print('')

    return


def main():
    days, times, courses, instructors = get_schedule_criteria()
    scheduled_courses = get_course_schedule(days, times, courses)
    instructor_combinations = get_valid_instructor_combinations(instructors, scheduled_courses)
    auto_solutions = get_auto_solutions(instructor_combinations, scheduled_courses)

    print(len(auto_solutions))

    show_auto_solutions(auto_solutions)

    return


import time
start_time = time.time()


if __name__ == '__main__':
    main()


print("--- %s seconds ---" % (time.time() - start_time))