import pytest
# from ..extract_position import extract_position
def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:] # from start_index to the end.
            else:
                pos = None
    return pos

# if __name__ == "__main__":
#     result1 = extract_position('|error| numerical calculations could not converge.')
#     print(result1)
#     result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
#     print(result2)
# def test_get_carbon_14_dating():
#   assert get_age_carbon_14_dating(.35) == pytest.approx(8680.34)
#   assert get_age_carbon_14_dating(1) == 0
#   with pytest.raises(ValueError):
#     get_age_carbon_14_dating(0)
#   with pytest.raises(ValueError):
#     get_age_carbon_14_dating(-1) 
#   with pytest.raises(TypeError):
#     get_age_carbon_14_dating('sdsd')

def test_extract_position():
  assert extract_position('|error| numerical calculations could not converge.') == None
  assert extract_position('|debug| numerical calculations could not converge.') == None
  assert extract_position('') == None
  assert extract_position('|update| the positron location in the particle accelerator is x:21.432') == "21.432"
  with pytest.raises(TypeError):
    extract_position()