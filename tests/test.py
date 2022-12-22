import nw.align as align


def test_score_nomatrix_1():
    score = align.score_nomatrix("ACGT", "ACGT")
    assert score == 20


def test_score_nomatrix_2():
    score = align.score_nomatrix("ACG", "ACGT")
    assert score == 10


def test_score_nomatrix_3():
    score = align.score_nomatrix("ACGT", "ACG")
    assert score == 10


def test_score_nomatrix_4():
    score = align.score_nomatrix("ACAGT", "ACGT")
    assert score == 15


def test_score_nomatrix_5():
    score = align.score_nomatrix("ACGT", "ACAGT")
    assert score == 15


def test_score_nomatrix_6():
    score = align.score_nomatrix("CAGT", "ACAGT")
    assert score == 15


def test_score_nomatrix_7():
    score = align.score_nomatrix("ACAGT", "CAGT")
    assert score == 15


def test_score_nomatrix_8():
    score = align.score_nomatrix("ACGT", "A")
    assert score == -10


def test_score_nomatrix_9():
    score = align.score_nomatrix("ACGT", "")
    assert score == -20


def test_score_nomatrix_10():
    score = align.score_nomatrix("A", "ACGT")
    assert score == -10


def test_score_nomatrix_11():
    score = align.score_nomatrix("", "ACGT")
    assert score == -20


def test_score_nomatrix_12():
    score = align.score_nomatrix("", "")
    assert score == 0


def test_score_nomatrix_13():
    score = align.score_nomatrix("TACGT", "ATGT")
    assert score == 6


def test_score_nomatrix_14():
    score = align.score_nomatrix("TACGT", "ACTGT")
    assert score == 10


def test_score_nomatrix_15():
    score = align.score_nomatrix("ACGT", "TAGTA")
    assert score == 0


def test_score_nomatrix_16():
    score = align.score_nomatrix("TAGTA", "ACGT")
    assert score == 0


def test_score_nomatrix_17():
    score = align.score_nomatrix("ACGT", "TAGT", gap=0)
    assert score == 15


def test_score_nomatrix_18():
    score = align.score_nomatrix("TAGT", "ACGT", gap=10)
    assert score == 80


def test_score_nomatrix_19():
    score = align.score_nomatrix("GGAGCCAAGGTGAAGTTGTAGCAGTGTGTCC", "GACTTGTGGAACCTCTGTCCTCCGAGCTCTC", gap=-5)
    assert score == 8


def test_score_nomatrix_20():
    score = align.score_nomatrix("AAAAAAATTTTTTT", "TTTTTTTAAAAAAA", gap=-5)
    assert score == -35


def test_score_k_1():
    score = align.score_k("ACGT", "ACGT")
    assert score == 20


def test_score_k_2():
    score = align.score_k("ACG", "ACGT")
    assert score == 10


def test_score_k_3():
    score = align.score_k("ACGT", "ACG")
    assert score == 10


def test_score_k_4():
    score = align.score_k("ACAGT", "ACGT")
    assert score == 15


def test_score_k_5():
    score = align.score_k("ACGT", "ACAGT")
    assert score == 15


def test_score_k_6():
    score = align.score_k("CAGT", "ACAGT")
    assert score == 15


def test_score_k_7():
    score = align.score_k("ACAGT", "CAGT")
    assert score == 15


def test_score_k_8():
    score = align.score_k("", "")
    assert score == 0


def test_score_k_9():
    score = align.score_k("TACGT", "ATGT")
    assert score == 6


def test_score_k_10():
    score = align.score_k("TACGT", "ACTGT")
    assert score == 10


def test_score_k_11():
    score = align.score_k("ACGT", "TAGTA")
    assert score == 0


def test_score_k_12():
    score = align.score_k("TAGTA", "ACGT")
    assert score == 0


def test_score_k_13():
    score = align.score_k("ACGT", "TAGT", gap=0)
    assert score == 15


def test_score_k_14():
    score = align.score_k("TAGT", "ACGT", gap=10)
    assert score == 80


def test_score_k_15():
    score = align.score_k("GGAGCCAAGGTGAAGTTGTAGCAGTGTGTCC", "GACTTGTGGAACCTCTGTCCTCCGAGCTCTC", gap=-5, k=6)
    assert score == 8


def test_score_k_16():
    score = align.score_k("AAAAAAATTTTTTT", "TTTTTTTAAAAAAA", gap=-5, k=10)
    assert score == -35


for i in range(1, 21):
    eval(f'test_score_nomatrix_{i}()')

for i in range(1, 17):
    eval(f'test_score_k_{i}()')
