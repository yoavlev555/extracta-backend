import logging


def setup_logging(log_level: int = logging.INFO) -> None:
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s [%(name)s] %(message)s",
    )
