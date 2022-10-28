from src.jobs import read


def get_unique_job_types(path):
    list_of_dict = read(path)

    all_jobs_type = set()

    for job in list_of_dict:
        job_type = job['job_type']
        all_jobs_type.add(job_type)

    list_of_jobs_type = list(all_jobs_type)

    return list_of_jobs_type


def filter_by_job_type(jobs, job_type):

    filtered_jobs = [job
                     for job in jobs
                     if job['job_type'] == job_type
                     ]

    # for job in list_of_dict:
    #    if job['job_type'] == job_type:
    #        filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    list_of_dict = read(path)

    all_industries = set()

    for job in list_of_dict:
        industry = job['industry']
        if industry != '':
            all_industries.add(industry)

    list_of_industries = list(all_industries)

    return list_of_industries


def filter_by_industry(jobs, industry):

    # filtered_industry = []

    filtered_industry = [job
                         for job in jobs
                         if job['industry'] == industry
                         ]

    # for job in list_of_dict:
    #    if job['industry'] == industry:
    #        filtered_industry.append(job)

    return filtered_industry


def get_max_salary(path):
    list_of_dict = read(path)

    # value_max_salary = 0

    list_of_salaries = [int(job['max_salary'])
                        for job in list_of_dict
                        if job['max_salary'].isnumeric()
                        ]

    # for job in list_of_dict:
    #    max_salary = job['max_salary']
    #    if max_salary != '' and max_salary.isnumeric():
    #        max_salary = int(max_salary)
    #       if max_salary > value_max_salary:
    #            value_max_salary = max_salary

    return max(list_of_salaries)


def get_min_salary(path):
    list_of_dict = read(path)

    # value_min_salary = 1000000000000

    list_of_salaries = [int(job['min_salary'])
                        for job in list_of_dict
                        if job['min_salary'].isnumeric()
                        ]

    # for job in list_of_dict:
    #    min_salary = job['min_salary']
    #    if min_salary != '' and min_salary.isnumeric():
    #        min_salary = int(min_salary)
    #        if min_salary < value_min_salary:
    #            value_min_salary = min_salary

    return min(list_of_salaries)


def matches_salary_range(job, salary):

    if (('min_salary' or 'max_salary') not in job
            or (type(job['min_salary']) or type(job['max_salary'])) != int
            or job['min_salary'] > job['max_salary']
            or type(salary) != int):
        raise ValueError

    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):

    list_of_jobs = [job
                    for job in jobs
                    if matches_salary_range((jobs, salary))
                    ]

    return list_of_jobs


if __name__ == '__main__':
    get_unique_industries('src/jobs.csv')
    get_unique_job_types('src/jobs.csv')
    get_max_salary('src/jobs.csv')
    get_min_salary('src/jobs.csv')
    filter_by_job_type('src/jobs.csv', 'PART_TIME')
    print(__name__)
