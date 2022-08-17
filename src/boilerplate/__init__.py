"""Start point for `boiler-plate`"""

from boilerplate.boilerplate import gather_requirements, execute_steps


def main() -> None:
    """Main Method to be called upon to create the `Project` as per user"""
    user_inputs = gather_requirements()

    if user_inputs["FINAL_CONF"] is True:
        execute_steps(user_inputs=user_inputs)
    else:
        print("Misson Abort !!! We'll get them next time ")


if __name__ == "__main__":
    main()
