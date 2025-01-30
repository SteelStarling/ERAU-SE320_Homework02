#!/usr/bin/env python3

"""OOP testing for SE320 - Software Construction
Author: Taylor Hancock
Date:   01/30/2025
Class:  SE320 - Software Construction
Assignment: Assignment 02 - Object Oriented Programming
"""

class Sensor():
    def __init__(self, name: str, url: str, polling_frequency: int):
        self.name = name
        self.url = url
        self.polling_frequency = polling_frequency

class StorySensor(Sensor):
    def __init__(self, name: str, url: str, polling_frequency: int, category: str):
        super().__init__(name, url, polling_frequency)
        self.category = category

class EventSensor(Sensor):
    def __init__(self, name: str, url: str, polling_frequency: int, event_type: str, location: str):
        super().__init__(name, url, polling_frequency)
        self.event_type = event_type
        self.location = location

class DataSensor(Sensor):
    def __init__(self, name: str, url: str, polling_frequency: int, data_type: str):
        super().__init__(name, url, polling_frequency)
        self.data_type = data_type

