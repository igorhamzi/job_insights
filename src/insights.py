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
    list_of_dict = jobs

    filtered_jobs = []

    for job in list_of_dict:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)

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
    list_of_dict = jobs

    filtered_industry = []

    for job in list_of_dict:
        if job['industry'] == industry:
            filtered_industry.append(job)

    return filtered_industry


def get_max_salary(path):
    list_of_dict = read(path)

    value_max_salary = 0

    for job in list_of_dict:
        max_salary = job['max_salary']
        if max_salary != '' and max_salary.isnumeric():
            max_salary = int(max_salary)
            if max_salary > value_max_salary:
                value_max_salary = max_salary

    return value_max_salary


def get_min_salary(path):
    list_of_dict = read(path)

    value_min_salary = 1000000000000

    for job in list_of_dict:
        min_salary = job['min_salary']
        if min_salary != '' and min_salary.isnumeric():
            min_salary = int(min_salary)
            if min_salary < value_min_salary:
                value_min_salary = min_salary

    return value_min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []


if __name__ == '__main__':
    get_unique_industries('src/jobs.csv')
    get_unique_job_types('src/jobs.csv')
    get_max_salary('src/jobs.csv')
    get_min_salary('src/jobs.csv')
    filter_by_job_type('src/jobs.csv', 'PART_TIME')
    print(__name__)
