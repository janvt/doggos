import random
import click


@click.command()
@click.option('--count', default=3, help='number of items')
@click.option('--ceiling', default=100, help='ceiling for random')
@click.option('--drop-rate-green', default=50, help='drop rate for green items')
@click.option('--drop-rate-blue', default=30, help='drop rate for blue items')
@click.option('--drop-rate-purple', default=16, help='drop rate for purple items')
@click.option('--drop-rate-legendary', default=4, help='drop rate for legendary items')
def main(count: int, ceiling: int, drop_rate_green: int, drop_rate_blue: int, drop_rate_purple: int, drop_rate_legendary: int) -> None:
    if drop_rate_green + drop_rate_blue + drop_rate_purple + drop_rate_legendary != ceiling:
        raise ValueError("Drop rates must sum to ceiling")

    seeds = []
    items = []
    print(f"Dropping {count} items!")
    # TODO this does not work....
    for i in range(count):
        seed = random.randint(0, ceiling)
        seeds.append(str(seed))

        if seed < drop_rate_green:
            items.append("G")

        if seed < drop_rate_blue:
            items.append("B")

        if seed < drop_rate_purple:
            items.append("P")

        if seed < drop_rate_legendary:
            items.append("L")

    print(f"Seeds: {', '.join(seeds)}")
    print(f"Your weapons, sir: {', '.join(items)}")

if __name__ == "__main__":
    main()
