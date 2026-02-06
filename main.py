from AssassinGenerator import AssassinGenerator, Player
from TargetMailer import TargetMailer


def main():
    generator = AssassinGenerator(
        [
            # Player("Amelia", "amelia.bermack@tufts.edu"),
            Player("Avery", "avery.smart@tufts.edu"),
            Player("Dani", "danielle.price@tufts.edu"),
            Player("Hannah", "hannah.fiarman@tufts.edu"),
            Player("Holden", "holden.kittelberger@tufts.edu"),
            Player("Josh", "joshua.field@tufts.edu"),
            Player("Juan", "juan.garcia@tufts.edu"),
            Player("Marten", "marten.tropp@tufts.edu"),
            Player("Moizes", "moizes.almeida@tufts.edu"),
            Player("Naomi", "naomi.arnold@tufts.edu"),
            Player("Rachel", "rachel.snyder@tufts.edu"),
            Player("Vedant", "vedant.modi@tufts.edu"),
            Player("Will", "william.fowler@tufts.edu"),
            # Add players here
        ]
    )

    # Do not forget to set verbose=False, dry=False
    targets = generator.generate(verbose=True)
    # mailer = TargetMailer(targets, dry=False)
    # mailer.send_mails(
    # verbose=False,
    # )


if __name__ == "__main__":
    main()
