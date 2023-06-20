import watch

def test_parse():
    assert watch.parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "http://www.youtube.com/embed/xvFZjo5PgG0"
    assert watch.parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://www.youtube.com/embed/xvFZjo5PgG0"
    assert watch.parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://www.youtube.com/embed/xvFZjo5PgG0"
    