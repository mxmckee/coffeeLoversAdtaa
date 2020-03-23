import itertools
from .models import Course, ScheduledCourse, Instructor


def get_schedule_criteria():
    days = ['MW', 'TR']
    times = ['08:00 AM - 09:15 AM', '09:25 AM - 10:40 AM', '10:50 AM - 12:05 PM', '12:15 PM - 01:30 PM',
             '01:40 PM - 02:55 PM', '03:05 PM - 04:20 PM', '04:30 PM - 05:45 PM']
    disciplines = ['Programming - C++', 'Programming - Python', 'Game Development', 'Data Structures and Algorithms',
                   'Computer Organization', 'Operating Systems', 'Programming Languages', 'Cybersecurity',
                   'Mobile Applications', 'Artificial Intelligence', 'Networks', 'Theory of Computation',
                   'Parallel and Distributed Systems']

    coursesQuerySet = Course.objects.all()
    courses = coursesQuerySet[::1]
    instructorsQuerySet = Instructor.objects.all()
    instructors = instructorsQuerySet[::1]

    return days, times, courses, instructors


def get_course_schedule(days, times, courses):
    scheduled_courses = []
    for scheduled_day in days:
        for scheduled_time in times:
            for course in courses:
                if course.courseDays == scheduled_day and course.returnReadableTime() == scheduled_time:
                    scheduled_courses.append(course)

    return scheduled_courses


def get_valid_instructor_combinations(instructors, scheduled_courses):
    ordered_courses = scheduled_courses.copy()
    master_list = []
    for course in ordered_courses:
        sub_list = []
        for instructor in instructors:
            if compare_two_objects(course, instructor):
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
            if combination.count(instructor) > instructor.maxClassLoad:
                invalid_instructor_combinations.append(combination)
                break

    instructor_combinations = [x for x in master_list if x not in invalid_instructor_combinations]

    return instructor_combinations, ordered_courses


def compare_two_objects(course, instructor):
    course_disciplines = [course.discipline1, course.discipline2]
    instructor_disciplines = [instructor.discipline1, instructor.discipline2]
    for discipline in course_disciplines:
        if not discipline == '' and discipline in instructor_disciplines:
            return True

    return False


def sub_lists(list1):
    sublist = [[]]
    for i in range(len(list1) + 1):
        for j in range(i + 1, len(list1) + 1):
            sub = list1[i:j]
            sublist.append(sub)

    return sublist


def remove_duplicates(list1):
    seen_combinations = []
    duplicates_removed = []
    for combination in list1:
        if combination not in seen_combinations:
            duplicates_removed.append(combination)
            seen_combinations.append(combination)

    return duplicates_removed


def get_auto_solutions(instructor_combinations, courses, scheduled_courses, ordered_courses):
    instructor_combinations = remove_duplicates(instructor_combinations)

    list_of_nones = [None] * len(courses)

    combinations_of_correct_length = []
    for combination in instructor_combinations:
        new_combination = list_of_nones.copy()
        for i in range(len(combination)):
            new_combination[i] = combination[i]
        combinations_of_correct_length.append(new_combination)

    temp_list = []
    for combination in combinations_of_correct_length:
        temp_list.append([*itertools.permutations(combination, len(courses))])

    temp_list = list(itertools.chain.from_iterable(temp_list))

    instructor_combinations = remove_duplicates(temp_list)

    all_auto_solutions = []
    for combination in instructor_combinations:
        solution = [(i, j) for i, j in zip(scheduled_courses, combination) if j is not None and
                    compare_two_objects(i, j)]
        if len(solution) != 0:
            all_auto_solutions.append(solution)

    invalid_auto_solutions = []
    for solution in all_auto_solutions:
        for i in range(len(solution) - 1):
            for j in range(i + 1, len(solution)):
                if solution[i][0].courseDays == solution[j][0].courseDays and solution[i][0].courseTime == \
                        solution[j][0].courseTime and solution[i][1].lastName == solution[j][1].lastName:
                    invalid_auto_solutions.append(solution)
                    break

    valid_auto_solutions = [x for x in all_auto_solutions if x not in invalid_auto_solutions]

    valid_auto_solutions = remove_duplicates(valid_auto_solutions)

    max_schedule_length = 0
    for solution in valid_auto_solutions:
        curr_max_schedule_length = len(solution)
        if curr_max_schedule_length > max_schedule_length:
            max_schedule_length = curr_max_schedule_length

    auto_solutions_of_max_length = []
    for solution in valid_auto_solutions:
        if len(solution) == max_schedule_length:
            auto_solutions_of_max_length.append(solution)

    temp_auto_solutions = []
    for solution in auto_solutions_of_max_length:
        assigned_courses = []
        for assignment in solution:
            assigned_courses.append(assignment[0])
        unassigned_courses = [x for x in courses if x not in assigned_courses]
        for course in unassigned_courses:
            solution.append((course, None))
        temp_auto_solutions.append(solution)
        
    auto_solutions = []
    for assignment_list in temp_auto_solutions:
        correctly_ordered_assignments = []
        for course in ordered_courses:
            for assignment_tuple in assignment_list:
                if assignment_tuple[0] == course:
                    correctly_ordered_assignments.append(assignment_tuple)
                    break
        auto_solutions.append(correctly_ordered_assignments)

    return auto_solutions


def main():
    days, times, courses, instructors = get_schedule_criteria()
    scheduled_courses = get_course_schedule(days, times, courses)
    instructor_combinations, ordered_courses = get_valid_instructor_combinations(instructors, scheduled_courses)
    auto_solutions = get_auto_solutions(instructor_combinations, courses, scheduled_courses, ordered_courses)

    return auto_solutions
