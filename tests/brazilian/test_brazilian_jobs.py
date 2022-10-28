from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    route = 'tests/mocks/brazilians_jobs.csv'
    titles = read_brazilian_file(route)

    for job in titles:
        assert list(job.keys()) == ['title', 'salary', 'type']
