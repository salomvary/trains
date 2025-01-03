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
from vonatinfo_client.models.station_request import StationRequest
from vonatinfo_client.models.train_request import TrainRequest
from vonatinfo_client.models.train_schedule_request import TrainScheduleRequest
from vonatinfo_client.models.trains_request import TrainsRequest
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GETDATAPOSTREQUEST_ONE_OF_SCHEMAS = ["StationRequest", "TrainRequest", "TrainScheduleRequest", "TrainsRequest"]

class GetDataPostRequest(BaseModel):
    """
    GetDataPostRequest
    """
    # data type: TrainsRequest
    oneof_schema_1_validator: Optional[TrainsRequest] = None
    # data type: TrainRequest
    oneof_schema_2_validator: Optional[TrainRequest] = None
    # data type: TrainScheduleRequest
    oneof_schema_3_validator: Optional[TrainScheduleRequest] = None
    # data type: StationRequest
    oneof_schema_4_validator: Optional[StationRequest] = None
    actual_instance: Optional[Union[StationRequest, TrainRequest, TrainScheduleRequest, TrainsRequest]] = None
    one_of_schemas: Set[str] = { "StationRequest", "TrainRequest", "TrainScheduleRequest", "TrainsRequest" }

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
        instance = GetDataPostRequest.model_construct()
        error_messages = []
        match = 0
        # validate data type: TrainsRequest
        if not isinstance(v, TrainsRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TrainsRequest`")
        else:
            match += 1
        # validate data type: TrainRequest
        if not isinstance(v, TrainRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TrainRequest`")
        else:
            match += 1
        # validate data type: TrainScheduleRequest
        if not isinstance(v, TrainScheduleRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TrainScheduleRequest`")
        else:
            match += 1
        # validate data type: StationRequest
        if not isinstance(v, StationRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StationRequest`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetDataPostRequest with oneOf schemas: StationRequest, TrainRequest, TrainScheduleRequest, TrainsRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetDataPostRequest with oneOf schemas: StationRequest, TrainRequest, TrainScheduleRequest, TrainsRequest. Details: " + ", ".join(error_messages))
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

        # deserialize data into TrainsRequest
        try:
            instance.actual_instance = TrainsRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TrainRequest
        try:
            instance.actual_instance = TrainRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TrainScheduleRequest
        try:
            instance.actual_instance = TrainScheduleRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into StationRequest
        try:
            instance.actual_instance = StationRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetDataPostRequest with oneOf schemas: StationRequest, TrainRequest, TrainScheduleRequest, TrainsRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetDataPostRequest with oneOf schemas: StationRequest, TrainRequest, TrainScheduleRequest, TrainsRequest. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], StationRequest, TrainRequest, TrainScheduleRequest, TrainsRequest]]:
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


