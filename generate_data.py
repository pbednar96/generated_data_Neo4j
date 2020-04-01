import names
import random
import csv
import faker

import data_list

NUMBER_ROW_PERSON = 1000
NUMBER_ROW_COMPANY = 87

GEN_PERSON = False
GEN_SKILL = False
GEN_FRIEND = False
GEN_COMPANY = False

def generate_person(filename):
    # generate person (node)
    persons_array = [["personID", "personName", "gender"]]
    for index in range(NUMBER_ROW_PERSON):
        gender = random.choices(["male", "female"], [5, 3])
        persons_array.append([index, names.get_full_name(gender[0]), gender[0]])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(persons_array)

    return len(persons_array) - 1


def generate_skill(filename):
    # generate skill for list skills (node)
    skill_array = [["skillID", "skillName"]]
    for index, item in enumerate(data_list.programming_skills):
        skill_array.append([index, item])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(skill_array)

    return len(skill_array) - 1


def generate_skill_person(filename):
    # generate skill - person (relationship)
    skill_array = [["personID", "skillID", "skillLevel"]]
    count_skills = len(data_list.programming_skills)
    for index in range(NUMBER_ROW_PERSON):
        num_skills = random.randint(3, 7)
        tmp = []
        for i in range(num_skills):
            x = random.randint(0, count_skills)
            if x not in tmp:
                tmp.append(x)
                skill_level = random.randint(1, 5)
                skill_array.append([index, x, skill_level])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(skill_array)

    return len(skill_array) - 1


def generate_friendship(filename):
    # generate relationship between persons (relationship)
    friend_array = [["personID", "know_personID"]]
    for index in range(NUMBER_ROW_PERSON):
        tmp = []
        num_friends = random.randint(4, 8)
        for friend in range(num_friends):
            id_friends = random.randint(0, NUMBER_ROW_PERSON)
            if id not in tmp:
                tmp.append(id_friends)
                friend_array.append([index, id_friends])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(friend_array)


def generate_company(filename):
    # generate companies (node)
    x = faker.Faker()
    company_array = [["companyID", "companyName"]]
    for index in range(NUMBER_ROW_COMPANY):
        company_array.append([index, x.company()])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(company_array)



def generate_person_company(filename):
    experience_array = [["personID", "companyID", "job", "current_job"]]
    for person in range(NUMBER_ROW_PERSON):
        count_jobs = random.randint(0, 2)
        job = random.randint(0, len(data_list.job)-1)
        x = random.random()
        tmp_current_job = False
        if x < .8:
            tmp_current_job = True
        for i in range(count_jobs):
            companyID = random.randint(0, NUMBER_ROW_COMPANY)
            if x < .2:
                job = random.randint(0, len(data_list.job)-1)
            if tmp_current_job:
                experience_array.append([person, companyID, job, tmp_current_job])
                tmp_current_job = False
            else:
                experience_array.append([person, companyID, job, tmp_current_job])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(experience_array)


def generate_workship(filename):
    # generate workship between persons (relationship)

    workship_array = [["personID", "know_personID"]]
    with open('generated_data/company_person.csv', newline='') as f:
        reader = csv.reader(f)
        person_company_data = list(reader)
    for item in person_company_data:
        for nested_item in person_company_data:
            x = random.random()
            if item[1] == nested_item[1] and x < .3 and item[0] != nested_item[0]:
                workship_array.append([item[0], nested_item[0]])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(workship_array)

if __name__ == "__main__":
    if GEN_PERSON:
        generate_person('generated_data/person.csv')
    if GEN_SKILL:
        generate_skill("generated_data/skill.csv")
    if GEN_SKILL or GEN_PERSON:
        generate_skill_person("generated_data/person_skill.csv")
    if GEN_FRIEND:
        generate_friendship("generated_data/friendship.csv")
    if GEN_COMPANY:
        generate_company("generated_data/company.csv")
        generate_person_company("generated_data/company_person.csv")
        generate_workship("generated_data/workship.csv")