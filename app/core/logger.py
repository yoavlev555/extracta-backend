import logging


def init_logger(name: str, log_level: int = logging.INFO) -> logging.Logger:
    """Initialize and configure a logger instance."""
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )
    return logging.getLogger(name)


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance for the given module name.

    Args:
        name: Usually __name__ to get a logger named after the module

    Returns:
        Configured logger instance
    """
    return logging.getLogger(name)
