# -*- coding: utf-8 -*-

from sqlalchemy.orm import declarative_base

from zvt.contract.register import register_schema
from zvt.contract.schema import ActorEntity

ActorMetaBase = declarative_base()


# 个股
class ActorMeta(ActorMetaBase, ActorEntity):
    __tablename__ = 'actor_meta'


register_schema(providers=['eastmoney'], db_name='actor_meta', schema_base=ActorMetaBase)
# the __all__ is generated
__all__ = ['ActorMeta']
