from pylc import LendingClubAPI

lc = LendingClubAPI('', '')

def test_get_resources():
  resources = lc.get_resources()
  assert "account" in resources
  assert "loan" in resources
  assert len(resources) == 2