from AssassinGenerator import AssassinGenerator, Player
from TargetMailer import TargetMailer


def main():
    generator = AssassinGenerator(
        [
            Player("Vedant", "vedantmodi@gmail.com"),
            # Add players here
        ]
    )

    # Do not forget to set verbose=False, dry=False
    targets = generator.generate(verbose=False)
    mailer = TargetMailer(targets, dry=False)
    mailer.send_mails(
        verbose=True,
    )


if __name__ == "__main__":
    main()
