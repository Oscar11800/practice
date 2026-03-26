from neetcode75.test_runner import assert_equal, run_tests

"""
Space Station Missions
Medium

A space station has Alpha and Beta hubs connected by shuttle. Alpha to Beta takes 100 time units.

Shuttle departures are given by two sorted integer arrays:
- alpha2beta: departure times from Alpha to Beta
- beta2alpha: departure times from Beta to Alpha

We need to complete a given number of missions, where each mission requires going from Alpha to Beta and back to Alpha.

Calculate the time unit when all missions are completed, assuming we take the earliest available shuttle.

Guaranteed that all missions can be completed using the shuttle schedule.

Example 1:
Input: alpha2beta = [0, 200, 500], beta2alpha = [99, 201, 450], missions = 1
Output: 310
Explanation: 
- Mission 1: Take alpha2beta[0]=0 to Beta (arrives at 100)
- Then take beta2alpha[0]=99 to Alpha (wait until 100, arrives at 200)
"""


def solution(alpha2beta, beta2alpha, missions):
    raise NotImplementedError


def test_example():
    sol = solution([0, 200, 500], [99, 201, 450], 1)
    assert_equal(sol, 310)


# Run: python3 -m neetcode75.specific.space_station_missions
if __name__ == "__main__":
    run_tests()
