import popuko
from . import config


def main():
    bot = popuko.init(config)
    bot.run()


if __name__ == '__main__':
    main()
