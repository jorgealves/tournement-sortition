import argparse
import random
import os

from collections import namedtuple


def get_args():
    parser = argparse.ArgumentParser(
        description="",
        epilog=""
    )
    parser.add_argument(
        '-cs',
        '--cabeca_serie',
        required=True,
        help="Cabeças de Série (O numero de cabeças de série determina o numero de grupos)",
    )
    parser.add_argument(
        '-dp',
        '--duplas',
        required=True,
        help="Lista de todas as restantes duplas",
    )
    return parser.parse_args()


def get_teams_per_group(cabecas_de_serie, duplas):
    return int((len(cabecas_de_serie) + len(duplas)) / len(cabecas_de_serie)) - 1


def make_sortition(headers, teams, teams_per_group):
    result = list()
    group_number = 0
    for header in headers:
        group_number += 1
        Group = namedtuple("Grupo", "name teams")
        group = Group(
            name="Grupo {}".format(group_number),
            teams=[header]
        )

        for number in range(teams_per_group):
            choosed_team = random.choice(teams)
            teams.remove(choosed_team)
            group.teams.append(choosed_team)

        result.append(group)

    if len(teams) > 0:
        for team in teams:
            random_group = random.choice(result)
            random_group.teams.append(team)

    return result


def print_result(result):
    print("SORTEIO")
    print()
    for group in result:
        print()
        print("{} - {}".format(group.name, "  |  ".join(group.teams)))
        print()


if __name__ == '__main__':
    all_teams = get_args()

    headers = all_teams.cabeca_serie.split(',')
    teams = all_teams.duplas.split(',')

    teams_per_group = get_teams_per_group(headers, teams)

    groups = make_sortition(headers=headers, teams=teams, teams_per_group=teams_per_group)

    os.system('clear')

    print_result(groups)
