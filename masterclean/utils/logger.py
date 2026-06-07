import logging


# -----------------------------------
# Logger Configuration
# -----------------------------------

logging.basicConfig(

    level=logging.INFO,

    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )

)

# -----------------------------------
# Global Logger
# -----------------------------------

logger = logging.getLogger(
    "masterclean"
)
