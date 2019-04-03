# Python Logging

## Logging Levels
| Level    | Numeric Value  |
| -------- |:--:|
| CRITICAL | 50 |
| ERROR    | 40 |
| WARNING  | 30 |
| INFO     | 20 |
| DEBUG    | 10 |
| NOTSET   |  0 |

## Logging Components

- __Loggers__ expose the interface that application code directly uses
- __Handlers__ send the log records (created by loggers) to the appropriate destination
- __Filters__ provide a finer grained facility for determining which log records to output
- __Formatters__ specify the layout of log records in the final output
- Log event information is passed between loggers, handlers, filters, and formatters in a LogRecord instance
- Default format set by basicConfig() for messages is: `severity:logger name:message`
- Programmers can configure logging in three ways:
  1. Creating loggers, handlers, and formatters explicitly using Python code that calls the configuration methods
  2. Creating a logging config file and reading it using the fileConfig() function
  3. Creating a dictionary of configuration information and passing it to the dictConfig() function

## Loggers

- Threefold job:
  1. Expose several methods to application code so that applications can log messages at runtime
  2. Logger objects determine which log messages to act upon based on severity or filter objects
  3. Logger objects pass along relevant log messages to all interested log handlers
- Most widely used methods on logger objects: configuration and message sending

## Handlers
- Responsible for dispatching appropriate log messages to the handler's specified destination
- Logger objects can add zero or more handler objects to themselves with an addHandler() method
- Application code should not directly instantiate and use instances of Handler. Instead, the Handler class is a base class that defines the interface that all handlers should have and establishes some default behavior that child classes can use (or override).

## Formatters
- Configure the final order, structure, and contents of the log message
- Application code may instantiate formatter classes, although you could likely subclass the formatter if your application needs special behavior
- Constructor takes two optional arguments, message format string and date format string: `logging.Formatter.__init__(fmt=None, datefmt=None)`

