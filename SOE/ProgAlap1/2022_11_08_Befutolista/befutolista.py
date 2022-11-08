import json

distances = ['5k', '10k', '21k', '42k']


def input_distance():
    distance = input(f"Melyik tavon szeretned latni a teljes toplistat? {'/'.join(distances)} ")
    while distance not in distances:
        distance = input(f"Ezen tavok valamelyiket add meg: {'/'.join(distances)} ")
    return distance


def fetch_results_for_distance(distance):
    with open("befutolista.json") as f:
        return [
            {
                "runner": runner,
                "time": results[distance]['time']
            }
            for club, runners in json.load(f).items()
            for runner, results in runners.items()
            if distance in results
        ]


def fetch_ordered_results_for_distance(distance):
    results = fetch_results_for_distance(distance)
    results.sort(key=lambda runner_result: runner_result['time'])
    return results


def fetch_and_print_toplist_for_distance(distance, limit=None):
    results = fetch_ordered_results_for_distance(distance)
    print_toplist(distance, results, limit)


def print_toplist(distance, ordered_results, limit=None):
    print(f"\n{distance} {'dobogo' if limit == 3 else 'befutolista'}:")
    if limit != None:
        ordered_results = ordered_results[:limit]
    for idx, result in enumerate(ordered_results):
        print(
            f" {result['time']} {'  ' if idx > 2 else '🥇' if idx == 0 else '🥈' if idx == 1 else '🥉'} {result['runner']} ")


for distance in distances:
    fetch_and_print_toplist_for_distance(distance, 3)
print()
distance = input_distance()
fetch_and_print_toplist_for_distance(distance)
