from datetime import datetime

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.base import Base


# back_populates : 양방향 관계설정, 관계의 상호참조
class Pds(Base):
    __tablename__ = 'pds'

    pno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    userid: Mapped[str] = mapped_column(String(18), ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    views: Mapped[int] = mapped_column(default=0)
    contents: Mapped[str] = mapped_column(Text)
    attachs = relationship('PdsAttach', back_populates='pds')    # 하나의 pds는 하나 이상의 attach가 존재  (1:n)


class PdsAttach(Base):
    __tablename__ = 'pdsattach'

    pano: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    pno: Mapped[int] = mapped_column(String(250), ForeignKey('pds.pno'), index=True)
    fname: Mapped[str] = mapped_column(String(18), nullable=False)
    fsize: Mapped[int] = mapped_column(default=0, nullable=False)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
    pds = relationship('Pds', back_populates='attachs')    # 하나의 attach는 하나의 pds에 속함 (1:1)



