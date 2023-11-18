# coding: utf-8

"""
    MÁV API

    Unofficial API for MÁV - Hungarian Railways

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class TrainsResultDResultTrainsTrainInner(BaseModel):
    """
    TrainsResultDResultTrainsTrainInner
    """
    delay: Union[StrictFloat, StrictInt] = Field(..., alias="@Delay")
    lat: Union[StrictFloat, StrictInt] = Field(..., alias="@Lat")
    relation: StrictStr = Field(..., alias="@Relation")
    train_number: StrictStr = Field(..., alias="@TrainNumber")
    menetvonal: StrictStr = Field(..., alias="@Menetvonal")
    line: Optional[StrictStr] = Field(None, alias="@Line")
    lon: Union[StrictFloat, StrictInt] = Field(..., alias="@Lon")
    elvira_id: StrictStr = Field(..., alias="@ElviraID")
    __properties = ["@Delay", "@Lat", "@Relation", "@TrainNumber", "@Menetvonal", "@Line", "@Lon", "@ElviraID"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TrainsResultDResultTrainsTrainInner:
        """Create an instance of TrainsResultDResultTrainsTrainInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrainsResultDResultTrainsTrainInner:
        """Create an instance of TrainsResultDResultTrainsTrainInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrainsResultDResultTrainsTrainInner.parse_obj(obj)

        _obj = TrainsResultDResultTrainsTrainInner.parse_obj({
            "delay": obj.get("@Delay"),
            "lat": obj.get("@Lat"),
            "relation": obj.get("@Relation"),
            "train_number": obj.get("@TrainNumber"),
            "menetvonal": obj.get("@Menetvonal"),
            "line": obj.get("@Line"),
            "lon": obj.get("@Lon"),
            "elvira_id": obj.get("@ElviraID")
        })
        return _obj

