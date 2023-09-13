from sqlalchemy import CHAR, TEXT
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
