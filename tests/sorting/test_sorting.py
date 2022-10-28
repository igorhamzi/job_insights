from src.sorting import sort_by


def test_sort_by_criteria():

    sorted_keys = [
        {
            "min_salary": 3,
            "max_salary": 1,
            "date_posted": 1
        },
        {
            "min_salary": 2,
            "max_salary": 2,
            "date_posted": 2
        },
        {
            "min_salary": 1,
            "max_salary": 3,
            "date_posted": 3
        },
    ]

    ranked_criteria = sorted_keys == [sorted_keys[2],
                                      sorted_keys[1],
                                      sorted_keys[0]]

    try:
        sort_by(sorted_keys, 'min_salary')
        assert ranked_criteria

        sort_by(sorted_keys, 'max_salary')
        assert ranked_criteria

        sort_by(sorted_keys, 'date_posted')
        assert ranked_criteria

    except ValueError:
        raise ValueError
