from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.base import Base


class Reply(Base):
    __tablename__ = 'board'

    bno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(index=True)
    userid: Mapped[str] = mapped_column(ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    views: Mapped[int] = mapped_column(default=0)
    contents: Mapped[str]
    replys = relationship('Reply', back_populates='board')



    class Reply(Base):
        __tablename__ = 'board'

    rno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    Reply: Mapped[str] = mapped_column(index=True)
    userid: Mapped[str] = mapped_column(ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    bno: Mapped[int] = mapped_column(ForeignKey('board.bno', index=True))
    rpno: Mapped[int] = mapped_column(ForeignKey('reply.rno', index=True))
    contents: Mapped[str]
    board = relationship('Board', back_populates='replys')