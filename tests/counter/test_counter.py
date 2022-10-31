from src.counter import count_ocurrences


def test_counter():
    result_python = count_ocurrences("src/jobs.csv", "python") == 1639
    result_javascript = count_ocurrences("src/jobs.csv", "javascript") == 122
    assert result_python
    assert result_javascript
