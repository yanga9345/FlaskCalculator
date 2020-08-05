from server.services import eval_service


def test_simple_eval():
    assert eval_service.safe_eval('21 * 4') == 84
