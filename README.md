Python Object-Oriented Programming Assignment
Local News Aggregation System
Background

You are tasked with designing a system for a website that displays aggregated local news. The website collects content from various sources that are regularly checked for updates. These sources can be thought of as "Software Sensors" that monitor different types of content: news stories, local events, and data feeds.
Learning Objectives

    Implement inheritance in Python
    Understand and apply polymorphism
    Create and use class hierarchies
    Work with class attributes and methods
    Implement and utilize mixins
    Practice type checking in Python

Requirements

    Create the following class hierarchy:
        Base class: Sensor
        Derived classes: StorySensor, EventSensor, and DataSensor

    Implement the Sensor class with these attributes:
        name (string)
        url (string)
        polling_frequency (integer, representing seconds)

    Implement the derived classes with these additional attributes:
        StorySensor: Add category (string)
        EventSensor: Add event_type (string) and location (string)
        DataSensor: Add data_type (string)

    Create test instances: ```python
    Example instantiation (complete with appropriate values):

    x = StorySensor("AZ-News", ...) y = DataSensor("National Weather Service", ...) ```

    Demonstrate instance and subclass checking:
        Test if instances are of their respective classes
        Check if your classes are subclasses of the built-in object class
        Print the results of these checks

    Demonstrate polymorphism:
        Create a list containing different types of sensors
        Iterate over the list and display sensor information
        Show how the same interface can be used for different sensor types

    Create and implement a Mixin class:
        Design a useful mixin that adds functionality to your sensors
        Demonstrate the mixin working with at least two different sensor types

Deliverables

Submit a Python file containing: 1. All class definitions 2. Example instances 3. Instance and subclass check demonstrations 4. Polymorphism demonstration 5. Mixin implementation and demonstration 6. Comments explaining your code
Example Output Format

Your program should produce output similar to this: ``` Instance checks: Is x a StorySensor? True Is x a Sensor? True ...

Polymorphism demonstration: Sensor: AZ-News Type: Story Category: Politics ... ```
Grading Criteria (see rubric)
Additional Notes

    Pay attention to proper Python naming conventions
    Include docstrings for your classes
    Use meaningful names for variables and methods
    Consider error handling where appropriate

Bonus Challenge (Optional)

Implement a method in each sensor class that simulates fetching data from the source URL and returns appropriate data structures for each sensor type.
Submission Guidelines

    Submit a single .py file named lastname_sensors.py
    Include your name and student ID in a comment at the top of the file
    Ensure your code runs without errors
    If an AI tool was used, you HAVE TO mention it in the module's doc-string!!!
