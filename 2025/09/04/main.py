import random

import click


@click.command()
@click.option('--count', default=20, help='number of items')
@click.option('--ceiling', default=100, help='ceiling for random')
@click.option('--drop-rate-green', default=50, help='drop rate for green items')
@click.option('--drop-rate-blue', default=30, help='drop rate for blue items')
@click.option('--drop-rate-purple', default=16, help='drop rate for purple items')
@click.option('--drop-rate-legendary', default=4, help='drop rate for legendary items')
def main(count: int, ceiling: int, drop_rate_green: int, drop_rate_blue: int, drop_rate_purple: int, drop_rate_legendary: int) -> None:
    print(f'Dropping {count} items!')
    print(f'Ceiling: {ceiling}')

    items = []
    seeds = []
    for i in range(count):
        seed = random.randint(0, 100)
        seeds.append(seed)

        if seed > ceiling - drop_rate_legendary:
            item = "L"
        elif seed > ceiling - (drop_rate_purple + drop_rate_legendary):
            item = "P"
        elif seed > ceiling - (drop_rate_blue + drop_rate_purple + drop_rate_legendary):
            item = "B"
        elif seed > ceiling - (drop_rate_green + drop_rate_blue + drop_rate_purple + drop_rate_legendary):
            item = "G"
        else:
            item = "No Item"

        items.append(item)

    print(f'Seeds: {", ".join(map(str, seeds))}')
    print(f'Loots: {",  ".join(items)}')




if __name__ == "__main__":
    main()
