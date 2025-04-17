from pydantic import BaseModel, Field, validator

class DataPoint(BaseModel):
    age: int = Field(ge=18, le=60)
    ratings: float = Field(ge=0.1, le=5.0)
    weather: str
    traffic: str
    vehicle_condition: int = Field(ge=0, le=2)
    type_of_order: str
    type_of_vehicle: str
    multiple_deliveries: float = Field(ge=0.0, le=4.0)
    festival: str
    city_type: str
    order_month: int = Field(ge=1, le=12)
    is_weekend: int = Field(ge=0, le=1)
    pickup_time_minutes: float
    order_time_of_day: str
    distance: float
    distance_type: str

    @validator("weather")
    def check_weather(cls, v):
        allowed = ['sunny', 'windy', 'sandstorms', 'fog', 'cloudy', 'stormy']
        if v not in allowed:
            raise ValueError(f"weather must be one of: {allowed}")
        return v

    @validator("traffic")
    def check_traffic(cls, v):
        allowed = ['jam', 'low', 'medium', 'high']
        if v not in allowed:
            raise ValueError(f"traffic must be one of: {allowed}")
        return v

    @validator("type_of_order")
    def check_order(cls, v):
        allowed = ['buffet', 'drinks', 'meal', 'snack']
        if v not in allowed:
            raise ValueError(f"order type must be one of: {allowed}")
        return v

    @validator("type_of_vehicle")
    def check_vehicle(cls, v):
        allowed = ['scooter', 'motorcycle', 'electric_scooter']
        if v not in allowed:
            raise ValueError(f"type_of_vehicle must be one of: {allowed}")
        return v

    @validator("festival")
    def check_festival(cls, v):
        allowed = ['no', 'yes']
        if v not in allowed:
            raise ValueError(f"festival must be 'yes' or 'no'")
        return v

    @validator("city_type")
    def check_city(cls, v):
        allowed = ['urban', 'semi-urban', 'metropolitan']
        if v not in allowed:
            raise ValueError(f"city_type must be one of: {allowed}")
        return v

    @validator("order_time_of_day")
    def check_time_of_day(cls, v):
        allowed = ['night', 'afternoon', 'evening', 'morning']
        if v not in allowed:
            raise ValueError(f"order_time_of_day must be one of: {allowed}")
        return v

    @validator("distance_type")
    def check_distance_type(cls, v):
        allowed = ['long', 'short', 'medium', 'very_long']
        if v not in allowed:
            raise ValueError(f"distance_type must be one of: {allowed}")
        return v





