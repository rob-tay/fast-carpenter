from fast_carpenter import expressions


def test_get_branches(infile):
    valid = infile.allkeys()

    cut = "NMuon > 1"
    branches = expressions.get_branches(cut, valid)
    assert branches == ["NMuon"]

    cut = "NMuon_not_found > 1 and NElectron > 3"
    branches = expressions.get_branches(cut, valid)
    assert branches == ["NElectron"]


def test_evaluate(wrapped_tree):
    Muon_py, Muon_pz = wrapped_tree.arrays(["Muon_Py", "Muon_Pz"], outputtype=tuple)
    mu_pt = expressions.evaluate(wrapped_tree, "sqrt(Muon_Px**2 + Muon_Py**2)")
    assert len(mu_pt) == 100
    assert all(mu_pt.counts == Muon_py.counts)


def test_evaluate_bool(wrapped_tree):
    all_true = expressions.evaluate(wrapped_tree, "Muon_Px == Muon_Px")
    assert all(all_true.all())
