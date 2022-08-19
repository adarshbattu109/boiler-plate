"""Start point for `boiler-plate`"""

from boilerplate.boilerplate import gather_requirements, execute_steps
from boilerplate.messages import MISSON_ABORT, WELCOME_MSG


def main() -> None:
    """Main Method to be called upon to create the `Project` as per user"""
    print(WELCOME_MSG)
    user_inputs = gather_requirements()

    if user_inputs["FINAL_CONF"] is True:
        execute_steps(user_inputs=user_inputs)
    else:
        print(MISSON_ABORT)


if __name__ == "__main__":
    main()
