from typing import Optional, Callable
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Boolean, BigInteger, Numeric
from sqlalchemy.orm import Session

from models.base import Base
from models.base_model import BaseModel


class bronzeFacturaEntity(Base, BaseModel):
    __tablename__ = "bronzeFactura"
    __table_args__ = {"schema": "prueba_bi"}

    id_numfac = Column(BigInteger, primary_key=True)
    creation_date = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        nullable=False,
    )
    numfac = Column(String(10))
    numdoc = Column(String(10))
    cliente = Column(String(15))
    numser = Column(String(6))
    secuencia = Column(String(10))
    comen1 = Column(String(200))
    comen2 = Column(String(100))
    comen3 = Column(String(70))
    subtotal = Column(Numeric)
    desc0 = Column(Numeric)
    iva = Column(Numeric)
    total_iva = Column(Numeric)
    total = Column(Numeric)
    codven = Column(String(10))
    fecha_hora = Column(DateTime(timezone=False))

    @classmethod
    def get_last_transaction_date(cls, session: Session, where_func=None):
        query = session.query(
            func.max(cls.fecha_hora)
        )
        if where_func:
            query = where_func(query)
        result = query.scalar()
        return str(result) if result else None





