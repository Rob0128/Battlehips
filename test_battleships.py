import pytest
from battleships import *

s = (1, 2, False, 3, {(1,2), (2,3), (3,3)})


@pytest.mark.parametrize("test_input,expected_output",
                         [
                             ((2, 3, False, 1, {(2,3)}), True),
                             ((4, 6, True, 2, {}), False),
                             ((6, 1, True, 3, {(1,2), (2,3), (3,3)}), True),
                             ((8, 5, False, 4, {(8,5), (8,6), (8,7)}), False),
                             ((3, 6, False, 3, {(4,6), (5,6)}), False),
                             ((7, 4, True, 1, {}), False),
                             ((2, 5, True, 3, {(2,5), (2,7)}), False),
                             ((2, 5, True, 4, {(2,5), (2,6), (2,7), (2,8)}), True),
                             ((4, 6, True, 1, {}), False),
                             ((7, 6, False, 2, {(7,6), (8,6)}), True)

                         ])
def test_is_sunk1(test_input, expected_output):
    # tests is the given ships are sunk, based on the hits assigned to each ship vs it's size
    ship = is_sunk(test_input)
    assert ship == expected_output
    # add at least four more tests for is_sunk by the project submission deadline


@pytest.mark.parametrize("test_input,expected_output",
                         [
                             ((2, 3, False, 1, {(2, 3)}), "submarine"),
                             ((4, 6, True, 2, {}), "destroyer"),
                             ((6, 1, True, 3, {(6, 1), (6, 2), (6, 3)}), "cruiser"),
                             ((8, 5, False, 4, {}), "battleship"),
                             ((3, 6, False, 4, {(4, 6), (5, 6)}), "battleship")
                         ])
def test_ship_type1(test_input, expected_output):
    # tests ship names have been assigned correctly
    result = ship_type(test_input)
    assert result == expected_output
    # assert ship_type(s) == "submarine"


def test_is_open_sea1():
    # tests if the coordintes represent an open sea area that is not near any ship in the fleet
    fleet1 = [(1, 0, True, 1, 0), (1, 2, True, 4, 0), (1, 7, False, 2, 0), (3, 9, False, 1, 0), (4, 5, True, 3, 0),
              (5, 9, False, 2, 0), (6, 5, True, 2, 0), (7, 0, False, 3, 0), (7, 3, False, 1, 0), (9, 9, True, 1, 0)]
    assert is_open_sea(2, 3, fleet1) == False


def test_is_open_sea2():
    # tests if the coordintes represent an open sea area that is not near any ship in the fleet
    fleet1 = [(1, 0, True, 1, 0), (1, 2, True, 4, 0), (1, 7, False, 2, 0), (3, 9, False, 1, 0), (4, 5, True, 3, 0),
              (5, 9, False, 2, 0), (6, 5, True, 2, 0), (7, 0, False, 3, 0), (7, 3, False, 1, 0), (9, 9, True, 1, 0)]
    assert is_open_sea(4, 5, fleet1) == False


def test_is_open_sea3():
    # tests if the coordintes represent an open sea area that is not near any ship in the fleet
    fleet1 = [(1, 0, True, 1, 0), (1, 2, True, 4, 0), (1, 7, False, 2, 0), (3, 9, False, 1, 0), (4, 5, True, 3, 0),
              (5, 9, False, 2, 0), (6, 5, True, 2, 0), (7, 0, False, 3, 0), (7, 3, False, 1, 0), (9, 9, True, 1, 0)]
    assert is_open_sea(1, 1, fleet1) == False


def test_is_open_sea4():
    # tests if the coordintes represent an open sea area that is not near any ship in the fleet
    fleet1 = [(1, 0, True, 1, 1), (1, 2, True, 4, 4), (1, 7, False, 2, 2), (3, 9, False, 1, 1), (4, 5, True, 3, 3),
              (5, 9, False, 2, 2), (6, 5, True, 2, 2), (7, 0, False, 3, 3), (7, 3, False, 1, 1), (9, 9, True, 1, 1)]
    assert is_open_sea(1, 1, fleet1) == False


def test_is_open_sea5():
    # tests if the coordintes represent an open sea area that is not near any ship in the fleet
    fleet1 = []
    assert is_open_sea(3, 7, fleet1) == True


def test_is_open_sea6():
    # tests if the coordintes represent an open sea area that is not near any ship in the fleet
    fleet1 = [(3, 0, True, 1, 0), (6, 5, True, 4, 0), (9, 9, True, 1, 0)]
    assert is_open_sea(1, 1, fleet1) == True



tfleet = [(1, 0, True, 1, {}), (1, 2, True, 4, {}), (1, 7, False, 2, {}), (3, 9, False, 1, {}), (4, 5, True, 3, {}),
             (5, 9, False, 2, {}), (6, 5, True, 2, {}), (7, 0, False, 3, {}), (7, 3, False, 1, {}), (9, 9, True, 1, {})]

def test_ok_to_place_ship_at1():
    # test if coordinates are far enough away from fleet to place a ship
    fleet = [(3, 2, True, 2, 0), (1, 5, False, 1, 0)]
    assert ok_to_place_ship_at(2, 1, True, 3, fleet) == False


def test_ok_to_place_ship_at2():
    # test if coordinates are far enough away from fleet to place a ship
    fleet = [(1, 0, True, 1, 0), (1, 2, True, 4, 0), (1, 7, False, 2, 0), (3, 9, False, 1, 0), (4, 5, True, 3, 0)]
    assert ok_to_place_ship_at(2, 1, True, 3, fleet) == False


def test_ok_to_place_ship_at3():
    # test if coordinates are far enough away from fleet to place a ship
    fleet = [(1, 0, True, 1, 0), (1, 2, True, 4, 0), (1, 7, False, 2, 0), (3, 9, False, 1, 0), (4, 5, True, 3, 0),
             (5, 9, False, 2, 0), (6, 5, True, 2, 0), (7, 0, False, 3, 0), (7, 3, False, 1, 0)]
    assert ok_to_place_ship_at(9, 7, True, 3, fleet) == True


def test_ok_to_place_ship_at4():
    # test if coordinates are far enough away from fleet to place a ship
    assert ok_to_place_ship_at(7, 0, True, 1, tfleet) == False


def test_ok_to_place_ship_at5():
    # test if coordinates are far enough away from fleet to place a ship

    assert ok_to_place_ship_at(2, 1, True, 3, tfleet) == False


def test_ok_to_place_ship_at6():
    # test if coordinates are far enough away from fleet to place a ship
    assert ok_to_place_ship_at(4, 2, False, 2, tfleet) == True


def test_ok_to_place_ship_at7():
    # test if coordinates are far enough away from fleet to place a ship
    assert ok_to_place_ship_at(3, 0, False, 4, tfleet) == False


def test_ok_to_place_ship_at8():
    # test if coordinates are far enough away from fleet to place a ship

    assert ok_to_place_ship_at(3, 0, False, 3, tfleet) == True


def test_ok_to_place_ship_at9():
    # test if coordinates are far enough away from fleet to place a ship

    assert ok_to_place_ship_at(1, 9, False, 1, tfleet) == True


def test_ok_to_place_ship_at10():
    # test if coordinates are far enough away from fleet to place a ship

    assert ok_to_place_ship_at(7, 7, True, 1, tfleet) == False


def test_place_ship_at1():
    # returns a fleet with the new ship added
    fleet = [(4, 2, True, 3, {}), (7, 5, True, 1, {})]
    actual = place_ship_at(7, 3, False, 2, fleet)
    actual.sort()
    expected = [(4, 2, True, 3, {}), (7, 5, True, 1, {}), (7, 3, False, 2, set())]
    expected.sort()
    assert actual == expected


def test_place_ship_at2():
    # returns a fleet with the new ship added
    fleet = [(4, 2, True, 3, {}), (7, 5, True, 1, {})]
    actual = place_ship_at(7, 4, False, 2, fleet)
    actual.sort()
    expected = [(4, 2, True, 3, {}), (7, 5, True, 1, {})]
    expected.sort()
    assert actual == expected


def test_place_ship_at3():
    # returns a fleet with the new ship added
    fleet = [(4, 2, True, 3, {}), (3, 9, False, 4, {}), (7, 5, True, 1, {})]
    actual = place_ship_at(7, 3, False, 2, fleet)
    actual.sort()
    expected = [(4, 2, True, 3, {}), (3, 9, False, 4, {}), (7, 5, True, 1, {}), (7, 3, False, 2, set())]
    expected.sort()
    assert actual == expected


def test_place_ship_at4():
    # returns a fleet with the new ship added
    fleet = [(4, 2, True, 3, {}), (3, 9, False, 4, {}), (7, 5, True, 1, {})]
    actual = place_ship_at(7, 4, False, 2, fleet)
    actual.sort()
    expected = [(4, 2, True, 3, {}), (3, 9, False, 4, {}), (7, 5, True, 1, {})]
    expected.sort()
    assert actual == expected


def test_place_ship_at5():
    # returns a fleet with the new ship added
    fleet = [(4, 2, True, 3, {}), (3, 9, False, 4, {}), (7, 5, True, 1, {})]
    actual = place_ship_at(1, 2, False, 2, fleet)
    actual.sort()
    expected = [(4, 2, True, 3, {}), (3, 9, False, 4, {}), (7, 5, True, 1, {}), (1, 2, False, 2, set())]
    expected.sort()
    assert actual == expected

tfleet_2 = [(1, 0, True, 1, set()), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, set()),
             (5, 9, False, 2, {(5, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]

def test_check_if_hits1():
    # check if a shot hits any ship in the fleet
    assert check_if_hits(4, 4, tfleet_2) == False

def test_check_if_hits2():
    # check if a shot hits any ship in the fleet
    assert check_if_hits(5, 9, tfleet_2) == False

def test_check_if_hits3():
    # check if a shot hits any ship in the fleet
    assert check_if_hits(4, 5, tfleet_2) == True

def test_check_if_hits4():
    # check if a shot hits any ship in the fleet
    assert check_if_hits(1, 4, tfleet_2) == True

def test_check_if_hits5():
    # check if a shot hits any ship in the fleet
    assert check_if_hits(9, 9, tfleet_2) == True

def test_check_if_hits6():
    # check if a shot hits any ship in the fleet
    assert check_if_hits(1, 1, tfleet_2) == False

def test_check_if_hits7():
    # check if a shot hits any ship in the fleet
    assert check_if_hits(8, 0, tfleet_2) == False

def test_check_if_hits8():
    # check if a shot hits any ship in the fleet
    assert check_if_hits(5, 5, tfleet_2) == False


hit_fleet_1 = [(1, 0, True, 1, set()), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, set()),
             (5, 9, False, 2, {(5, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]

def test_hit1():
    # returns updated fleet and ship information after a hit
    (actual, s) = hit(1, 7, hit_fleet_1)
    actual.sort()
    expected = [(1, 0, True, 1, set()), (1, 2, True, 4, set()), (1, 7, False, 2, {(1, 7)}), (3, 9, False, 1, set()), (4, 5, True, 3, set()),
             (5, 9, False, 2, {(5, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (1, 7, False, 2,{(1, 7)}))


hit_fleet_2 = [(1, 0, True, 1, set()), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, set()),
             (5, 9, False, 2, {(5, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]

def test_hit2():
    # returns updated fleet and ship information after a hit
    (actual, s) = hit(2, 7, tfleet_2)
    actual.sort()
    expected = [(1, 0, True, 1, set()), (1, 2, True, 4, set()), (1, 7, False, 2, {(2, 7)}), (3, 9, False, 1, set()), (4, 5, True, 3, set()),
             (5, 9, False, 2, {(5, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (1, 7, False, 2, {(2, 7)}))


hit_fleet_3 = [(1, 0, True, 1, set()), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, set()),
             (5, 9, False, 2, {(5, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]

def test_hit3():
    # returns updated fleet and ship information after a hit
    (actual, s) = hit(6, 9, hit_fleet_3)
    actual.sort()
    expected = [(1, 0, True, 1, set()), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, set()),
             (5, 9, False, 2, {(5, 9), (6, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (5, 9, False, 2,{(5, 9), (6, 9)}))


hit_fleet_4 = [(1, 0, True, 1, set()), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, set()),
             (5, 9, False, 2, {(5, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]

def test_hit4():
    # returns updated fleet and ship information after a hit
    (actual, s) = hit(1, 5, hit_fleet_4)
    actual.sort()
    expected = [(1, 0, True, 1, set()), (1, 2, True, 4, {(1, 5)}), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, set()),
             (5, 9, False, 2, {(5, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (1, 2, True, 4,{(1, 5)}))


hit_fleet_5 = [(1, 0, True, 1, {(1, 0)}), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, {(4, 7)}),
             (5, 9, False, 2, {(5, 9), (6, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]

def test_hit5():
    # returns updated fleet and ship information after a hit
    (actual, s) = hit(4, 6, hit_fleet_5)
    actual.sort()
    expected = [(1, 0, True, 1, {(1, 0)}), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, {(4, 7), (4, 6)}),
             (5, 9, False, 2, {(5, 9), (6, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (4, 5, True, 3, {(4, 7), (4, 6)}))


def test_are_unsunk_ships_left1():
    # checks if there are any ships in the fleet that have not been sunk
    fleet = fleet = [(1, 0, True, 1, {(1, 0)}), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, set()),
             (5, 9, False, 2, set()), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]

    assert are_unsunk_ships_left(fleet) == True


def test_are_unsunk_ships_left2():
    fleet = [(1, 0, True, 1, set()), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()),
             (4, 5, True, 3, set()),
             (5, 9, False, 2, set()), (6, 5, True, 2, set()), (7, 0, False, 3, set()),
             (7, 3, False, 1, set()), (9, 9, True, 1, set())]

    assert are_unsunk_ships_left(fleet) == True


def test_are_unsunk_ships_left3():
    fleet = [(1, 0, True, 1, {(1, 0)}), (1, 2, True, 4, set()), (1, 7, False, 2, set()), (3, 9, False, 1, set()), (4, 5, True, 3, {(4, 7), (4, 6)}),
             (5, 9, False, 2, {(5, 9), (6, 9)}), (6, 5, True, 2, set()), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, set()), (9, 9, True, 1, set())]

    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left4():
    fleet = [(1, 0, True, 1, {(1, 0)}), (1, 2, True, 4, {(1, 2), (1, 3), (1, 4), (1, 5)}), (1, 7, False, 2, {(1, 7), (2, 7)}), (3, 9, False, 1, {(3, 9)}), (4, 5, True, 3, {(4, 5), (4, 6), (4, 7)}),
             (5, 9, False, 2, {(5, 9), (6, 9)}), (6, 5, True, 2, {(6, 5), (6, 6)}), (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, {(7, 3)}), (9, 9, True, 1, {(9, 9)})]

    assert are_unsunk_ships_left(fleet) == False

def test_are_unsunk_ships_left5():
    fleet = [(1, 0, True, 1, {(1, 0)}), (1, 2, True, 4, {(1, 3), (1, 4), (1, 5), (1, 2)}),
             (1, 7, False, 2, {(2, 7), (1, 7)}), (3, 9, False, 1, {(3, 9)}), (4, 5, True, 3, {(4, 6), (4, 5), (4, 7)}),
             (5, 9, False, 2, {(5, 9), (6, 9)}), (6, 5, True, 2, {(6, 6), (6, 5)}),
             (7, 0, False, 3, {(7, 0), (8, 0), (9, 0)}), (7, 3, False, 1, {(7, 3)}), (9, 9, True, 1, {(9, 9)})]

    assert are_unsunk_ships_left(fleet) == False