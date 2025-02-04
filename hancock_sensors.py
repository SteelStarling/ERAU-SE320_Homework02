#!/usr/bin/env python3

"""OOP testing for SE320 - Software Construction
Author: Taylor Hancock
Date:   01/30/2025
Class:  SE320 - Software Construction
Assignment: Assignment 02 - Object Oriented Programming
"""

class ParseObjectMixin:
    """Mixin class to print the data within an object for use
    """

    def parseObject(self) -> dict:
        """Returns the data within an object for use"""
        return self.__dict__
    
    def objectName(self):
        """Returns the name of an object for use (or unnamed object, if object has no name)"""
        if self.name != None:
            return self.name
        else:
            return "Unnamed Object"

class Sensor:
    """Sensors that regularly gets info from a source
    """

    def __init__(self, name: str, url: str, polling_frequency: int):
        """Create generic sensor for use

        Arguments:
            name (string): name of the sensor
            url  (string): url to search with the sensor
            polling_frequency (int): period between polling url in seconds (actually 1/frequency)
        """
        self.name = name
        self.url = url
        self.polling_frequency = polling_frequency

    def get_info(self) -> list[str]:
        """Returns a list of strings of data found by the sensor"""
        return ["Wow, this sure senses", "Sensor Output!"]

class StorySensor(Sensor, ParseObjectMixin):
    """Sensors that regularly get info from a source about a story (e.g. news)
    """

    def __init__(self, name: str, url: str, polling_frequency: int, category: str):
        """Create story sensor for use

        Arguments:
            name (string): name of the sensor
            url  (string): url to search with the sensor
            polling_frequency (int): period between polling url in seconds (actually 1/frequency)
            category (string): category of which the story is a type of
        """
        super().__init__(name, url, polling_frequency)
        self.category = category

    def get_info(self) -> list[str]:
        """Returns a list of strings of data found by the sensor"""
        return ["Wow, a story is happening!", "Once upon a time", "...", "The End"]

class EventSensor(Sensor, ParseObjectMixin):
    """Sensors that regularly get info from a source about the occurence of an event (e.g. parties)
    """

    def __init__(self, name: str, url: str, polling_frequency: int, event_type: str, location: str):
        """Create event sensor for use

        Arguments:
            name (string): name of the sensor
            url  (string): url to search with the sensor
            polling_frequency (int): period between polling url in seconds (actually 1/frequency)
            event_type (string): the type of event to search for
            location (string): the location in which to search for events within
        """
        super().__init__(name, url, polling_frequency)
        self.event_type = event_type
        self.location = location

    def get_info(self) -> list[str]:
        """Returns a list of strings of data found by the sensor"""
        return ["A party is happening nearby!", "A parade is happening nearby", "A carnival is happening nearby"]

class DataSensor(Sensor, ParseObjectMixin):
    """Sensors that regularly get info from a source about a set of data (e.g. weather)

    Functions:
        __init__: creates data sensors
        get_info: gets a list containing information about the sensor
    """
    def __init__(self, name: str, url: str, polling_frequency: int, data_type: str):
        """Create data sensor for use

        Arguments:
            name (string): name of the sensor
            url  (string): url to search with the sensor
            polling_frequency (int): period between polling url in seconds (actually 1/frequency)
            data_type (string): type of data to search for (e.g. temperature)
        """
        super().__init__(name, url, polling_frequency)
        self.data_type = data_type

    def get_info(self) -> list[str]:
        """Returns a list of strings of data found by the sensor"""
        return ["31 °F", "93 °F", "21 °C"]

if __name__ == "__main__":
    
    # create sensors
    generic_sensor = Sensor("a source", "www.website.com", 10)
    world_news_sensor = StorySensor("Reuters", "www.reuters.com", 60, "World News")
    dnd_sensor = EventSensor("Local Events", "www.localEventSource.com", 30, "Dungeons & Dragons Meetings", "Prescott, AZ, USA")
    temperature_sensor = DataSensor("National Weather Service", "forecast.weather.gov", 120, "Temperature - °C")

    # verify instances are of correct classes
    print("\nInstance checks:")
    print(f" Is generic_sensor a Sensor? {type(generic_sensor) is Sensor}")
    print(f" Is world_news_sensor a Sensor? {type(world_news_sensor) is StorySensor}")
    print(f" Is dnd_sensor a Sensor? {type(dnd_sensor) is EventSensor}")
    print(f" Is temperature_sensor a Sensor? {type(temperature_sensor) is DataSensor}")

    # verify classes are subclasses of sensor
    print("\nCheck if subclasses of Sensor:")
    print(f" Is StorySensor a subclass of Sensor? {issubclass(StorySensor, Sensor)}")
    print(f" Is EventSensor a subclass of Sensor? {issubclass(EventSensor, Sensor)}")
    print(f" Is DataSensor a subclass of Sensor? {issubclass(DataSensor, Sensor)}")

    # verify classes are subclasses of object
    print("\nCheck if subclasses of object:")
    print(f" Is Sensor a subclass of object? {issubclass(Sensor, object)}")
    print(f" Is StorySensor a subclass of object? {issubclass(StorySensor, object)}")
    print(f" Is EventSensor a subclass of object? {issubclass(EventSensor, object)}")
    print(f" Is DataSensor a subclass of object? {issubclass(DataSensor, object)}")

    # polymorphism verification
    print("\nPolymorphism testing:")
    sensors = [world_news_sensor, dnd_sensor, temperature_sensor]
    for sensor in sensors:
        print(f"{type(sensor)} output: {sensor.get_info()}")

    # mixin testing
    print("\nMixin testing:")
    for sensor in sensors:
        print(f"{sensor.objectName()} mixin output: {sensor.parseObject()}")