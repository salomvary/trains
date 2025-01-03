# coding: utf-8

"""
    MÁV ELVIRA API

    Unofficial API for MÁV ELVIRA - Hungarian Railways (jegy.mav.hu)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ViszonylatObject(BaseModel):
    """
    Relation
    """ # noqa: E501
    start_station_code: StrictStr = Field(alias="startStationCode")
    start_time: datetime = Field(description="Scheduled departure time at the departure station", alias="startTime")
    start_time_zone: StrictStr = Field(alias="startTimeZone")
    end_station_code: StrictStr = Field(alias="endStationCode")
    end_time: datetime = Field(description="Scheduled arrival time at the arrival station", alias="endTime")
    end_time_zone: StrictStr = Field(alias="endTimeZone")
    travel_time: Union[StrictFloat, StrictInt] = Field(alias="travelTime")
    start_track: Optional[StrictStr] = Field(alias="startTrack")
    end_track: Optional[StrictStr] = Field(alias="endTrack")
    inner_station_codes: List[StrictStr] = Field(alias="innerStationCodes")
    __properties: ClassVar[List[str]] = ["startStationCode", "startTime", "startTimeZone", "endStationCode", "endTime", "endTimeZone", "travelTime", "startTrack", "endTrack", "innerStationCodes"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ViszonylatObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if start_track (nullable) is None
        # and model_fields_set contains the field
        if self.start_track is None and "start_track" in self.model_fields_set:
            _dict['startTrack'] = None

        # set to None if end_track (nullable) is None
        # and model_fields_set contains the field
        if self.end_track is None and "end_track" in self.model_fields_set:
            _dict['endTrack'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViszonylatObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startStationCode": obj.get("startStationCode"),
            "startTime": obj.get("startTime"),
            "startTimeZone": obj.get("startTimeZone"),
            "endStationCode": obj.get("endStationCode"),
            "endTime": obj.get("endTime"),
            "endTimeZone": obj.get("endTimeZone"),
            "travelTime": obj.get("travelTime"),
            "startTrack": obj.get("startTrack"),
            "endTrack": obj.get("endTrack"),
            "innerStationCodes": obj.get("innerStationCodes")
        })
        return _obj


