from datetime import datetime

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.base import Base


class Board(Base):
    __tablename__ = 'board'
    __table_args__ = {'sqlite_autoincrement': True}

    bno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(100), index=True)
    userid: Mapped[str] = mapped_column(String(18), ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(String(100), default=datetime.now)
    views: Mapped[int] = mapped_column(default=0)
    contents: Mapped[str] = mapped_column(Text)
    replys = relationship('Reply', back_populates='board')


class Reply(Base):
    __tablename__ = 'reply'
    __table_args__ = {'sqlite_autoincrement': True}

    rno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    reply: Mapped[str] = mapped_column(String(250), index=True)
    userid: Mapped[str] = mapped_column(String(18), ForeignKey('member.userid'), index=True)
    # regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    regdate: Mapped[datetime] = mapped_column(default=lambda: datetime.now().replace(microsecond=0))
    bno: Mapped[int] = mapped_column(ForeignKey('board.bno'))
    rpno: Mapped[int] = mapped_column(ForeignKey('reply.rno'))
    board = relationship('Board', back_populates='replys')