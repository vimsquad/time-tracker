import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
import json
from os import getenv, path


class DataStore(ABC):
    """Stores Data in persistent storage"""

    @abstractmethod
    def create_data_store(self):
        """Creates Data Store If not Exists"""
        pass

    @abstractmethod
    def upsert_data(self):
        """Updates or Inserts Data"""
        pass

    @abstractmethod
    def delete_data(self):
        """Deletes Data"""
        pass

    @abstractmethod
    def load_data(self):
        """Loads data from datastore"""
        pass


class DataStoreJson(DataStore):
    """Stores Data in persistent storage"""

    data_location: str = "time_tracker_data_store.json"

    def create_data_store(self):
        """Creates Data Store If not Exists"""
        if path.exists(f"{os.getenv('HOME')}/{self.data_location}"):
            return True
        else:
            with open(f"{os.getenv('HOME')}/{self.data_location}", "w") as outfile:
                outfile.write(json.dumps({}))

    def upsert_data(self):
        """Updates or Inserts Data"""
        pass

    def delete_data(self):
        """Deletes Data"""
        pass

    def load_data(self):
        """Loads data from datastore"""
        pass


class DataStoreController:
    """Gets DataStore"""

    @staticmethod
    def get_factory(data_store_type: str = "json") -> DataStore:
        factories = {"json": DataStoreJson()}
        return factories.get(data_store_type)
