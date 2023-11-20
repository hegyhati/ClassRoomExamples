import json


with open("gain_2022.json") as f:
    data = json.load(f)

def get_schedule(already_done = {}, observe_semesters = False):
    schedule = { subject["name"] : None if subject["name"] not in already_done else -1 for subject in data }
    semester = 1
    while None in schedule.values():
        for subject in data:
            if schedule[subject["name"]] == None:
                for prerequisite in subject["prerequisites"]:
                    if not schedule[prerequisite] or schedule[prerequisite] == semester:
                        break
                else:
                    if not observe_semesters or (semester % 2 == 1) == subject["autumn"]:
                        schedule[subject["name"]] = semester
        semester += 1
    return schedule

def print_schedule(schedule):
    for semester in range(1, max(schedule.values()) + 1):
        print(f"{semester}. félév:")
        for subject in data:
            if schedule[subject["name"]] == semester:
                print(f"\t{subject['name']}")

# print_schedule(get_schedule())
# print_schedule(get_schedule(already_done={"BevMat"}))
# print_schedule(get_schedule(already_done={"ProgAlap", "BevMat"}))

def dependent_subjects(subject_name:str):
    return [ subject["name"] for subject in data if subject_name in subject["prerequisites"] ]

def get_subject(subject_name:str):
    return next(subject for subject in data if subject["name"] == subject_name)

def delayed_schedule(original_schedule:dict, failed_subject:str, observe_semesters = False):
    def check_subject(subject_name:str):
        for prerequisites in get_subject(subject_name)["prerequisites"]:
            if schedule[prerequisites] >= schedule[subject_name]:
                schedule[subject_name] += 2 if observe_semesters else 1
                for dependent_subject in dependent_subjects(subject_name):
                    check_subject(dependent_subject)
                return

    schedule = original_schedule.copy()
    schedule[failed_subject] += 2 if observe_semesters else 1
    for subject in dependent_subjects(failed_subject):
        check_subject(subject)
    return schedule


gergo_schedule = get_schedule(observe_semesters=True)
gergo_schedule = delayed_schedule(gergo_schedule, "Prog1", observe_semesters=True)
gergo_schedule = delayed_schedule(gergo_schedule, "Prog2", observe_semesters=True)
print_schedule(gergo_schedule)

