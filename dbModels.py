from datetime import datetime

from sqlalchemy import CHAR, TEXT, TIMESTAMP, text, event, DDL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ProjectBase(DeclarativeBase):
    pass


class Property(ProjectBase):
    __tablename__ = "properties"

    key: Mapped[str] = mapped_column(TEXT(), primary_key=True)
    value: Mapped[str] = mapped_column(TEXT(), primary_key=True)


class TagValue(ProjectBase):
    __tablename__ = "tag_values"

    tag: Mapped[str] = mapped_column(TEXT(), primary_key=True)
    value: Mapped[str] = mapped_column(TEXT(), primary_key=True)


class ClassifiedSample(ProjectBase):
    __tablename__ = "classified_samples"

    sampleNumpyMd5: Mapped[str] = mapped_column(
        "sample_numpy_md5", CHAR(32), primary_key=True, unique=True
    )
    tag: Mapped[str] = mapped_column(TEXT(), primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(
        TIMESTAMP(), server_default=text("CURRENT_TIMESTAMP")
    )


event.listen(
    ClassifiedSample.__table__,
    "after_create",
    DDL(
        """
        CREATE TRIGGER IF NOT EXISTS update_classified_samples_timestamp
            UPDATE OF sample_numpy_md5, tag
            ON classified_samples
        BEGIN
            UPDATE classified_samples
            SET timestamp = CURRENT_TIMESTAMP
            WHERE sample_numpy_md5 = old.sample_numpy_md5;
        END;"""
    ),
)
