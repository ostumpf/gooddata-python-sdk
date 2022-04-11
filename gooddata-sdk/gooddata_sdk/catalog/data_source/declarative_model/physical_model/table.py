# (C) 2022 GoodData Corporation
from __future__ import annotations

from typing import Any

from gooddata_metadata_client.model.declarative_table import DeclarativeTable
from gooddata_sdk.catalog.data_source.declarative_model.physical_model.column import CatalogDeclarativeColumn
from gooddata_sdk.catalog.entity import CatalogTypeEntity


class CatalogDeclarativeTable(CatalogTypeEntity):
    def __init__(
        self,
        id: str,
        type: str,
        path: list[str],
        columns: list[CatalogDeclarativeColumn],
    ):
        super(CatalogDeclarativeTable, self).__init__(id, type)
        self.path = path
        self.columns = columns

    @classmethod
    def from_api(cls, entity: dict[str, Any]) -> CatalogDeclarativeTable:
        columns = [CatalogDeclarativeColumn.from_api(v) for v in entity["columns"]]
        return cls(
            id=entity["id"],
            type=entity["type"],
            path=entity["path"],
            columns=columns,
        )

    def to_api(self) -> DeclarativeTable:
        columns = [v.to_api() for v in self.columns]
        return DeclarativeTable(id=self.id, type=self.type, path=self.path, columns=columns)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CatalogDeclarativeTable):
            return False
        return (
            self.id == other.id
            and self.type == other.type
            and self.path == other.path
            and self.columns == other.columns
        )