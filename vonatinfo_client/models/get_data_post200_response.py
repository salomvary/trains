# coding: utf-8

"""
    MÁV API

    Unofficial API for MÁV - Hungarian Railways

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from vonatinfo_client.models.station_result import StationResult
from vonatinfo_client.models.train_result import TrainResult
from vonatinfo_client.models.train_schedule_result import TrainScheduleResult
from vonatinfo_client.models.trains_result import TrainsResult
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GETDATAPOST200RESPONSE_ONE_OF_SCHEMAS = ["StationResult", "TrainResult", "TrainScheduleResult", "TrainsResult"]

class GetDataPost200Response(BaseModel):
    """
    GetDataPost200Response
    """
    # data type: TrainsResult
    oneof_schema_1_validator: Optional[TrainsResult] = None
    # data type: TrainResult
    oneof_schema_2_validator: Optional[TrainResult] = None
    # data type: TrainScheduleResult
    oneof_schema_3_validator: Optional[TrainScheduleResult] = None
    # data type: StationResult
    oneof_schema_4_validator: Optional[StationResult] = None
    actual_instance: Optional[Union[StationResult, TrainResult, TrainScheduleResult, TrainsResult]] = None
    one_of_schemas: Set[str] = { "StationResult", "TrainResult", "TrainScheduleResult", "TrainsResult" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = GetDataPost200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: TrainsResult
        if not isinstance(v, TrainsResult):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TrainsResult`")
        else:
            match += 1
        # validate data type: TrainResult
        if not isinstance(v, TrainResult):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TrainResult`")
        else:
            match += 1
        # validate data type: TrainScheduleResult
        if not isinstance(v, TrainScheduleResult):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TrainScheduleResult`")
        else:
            match += 1
        # validate data type: StationResult
        if not isinstance(v, StationResult):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StationResult`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetDataPost200Response with oneOf schemas: StationResult, TrainResult, TrainScheduleResult, TrainsResult. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetDataPost200Response with oneOf schemas: StationResult, TrainResult, TrainScheduleResult, TrainsResult. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into TrainsResult
        try:
            instance.actual_instance = TrainsResult.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TrainResult
        try:
            instance.actual_instance = TrainResult.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TrainScheduleResult
        try:
            instance.actual_instance = TrainScheduleResult.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into StationResult
        try:
            instance.actual_instance = StationResult.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetDataPost200Response with oneOf schemas: StationResult, TrainResult, TrainScheduleResult, TrainsResult. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetDataPost200Response with oneOf schemas: StationResult, TrainResult, TrainScheduleResult, TrainsResult. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], StationResult, TrainResult, TrainScheduleResult, TrainsResult]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

