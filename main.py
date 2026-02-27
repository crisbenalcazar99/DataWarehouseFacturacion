import logging

from sqlalchemy import inspect

from common.session_manager import get_session
from config.logger_config import setup_logger
from models.base import Base
from pipelines.bronze.facturasPipeline import PipelineBronzeFacturas

from entities.bronze.facturasEntity import bronzeFacturaEntity


def create_all_tables():
    with get_session("QUANTA") as session:
        Base.metadata.create_all(session.bind)
        inspector = inspect(session.bind)
        print(inspector.get_table_names())


# create_all_tables()

if __name__ == "__main__":
    setup_logger()
    log = logging.getLogger(__name__)
    log.info("Inicio Proceso Datawarehouse Facturacion BY ZALY-CB")

    PipelineBronzeFacturas().run()
