# loggers-django-practice
Django's built-in logging framework and configure it to format log messages as JSON.
- Install the python-json-logger library:
  ```
  pip install python-json-logger
  
  ```
- Configure Django's logging settings:
  ```
    import logging
    from pythonjsonlogger import jsonlogger
    
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': jsonlogger.JsonFormatter,
                'format': '%(asctime)s %(levelname)s %(message)s',
            },
        },
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': 'django_app.log',
                'formatter': 'json',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'json',
            },
        },
        'root': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        },
    }

  ```
- Use the Logger in Your Django Code:
  <img width="1017" alt="image" src="https://github.com/atique-ahmad/loggers-django-practice/assets/125459998/74659971-3169-4ff9-bd9d-1b124b051cca">
- logging: loggers, handlers, and formatters
  <img width="1016" alt="image" src="https://github.com/atique-ahmad/loggers-django-practice/assets/125459998/accc1bd5-c9ce-4fb4-8e98-67f0f0aeb5f6">

- **Results**
  - handlers': ['file']
    <img width="1644" alt="image" src="https://github.com/atique-ahmad/loggers-django-practice/assets/125459998/a40871c9-9295-426f-b087-476c8faac6e2">
  
  - handlers': ['console']
    <img width="1112" alt="image" src="https://github.com/atique-ahmad/loggers-django-practice/assets/125459998/d0655b8e-54a7-4458-92e5-115e4649b311">

- Reference Link:
  - YouTube: https://www.youtube.com/watch?v=b4Ms4wxJuPg&ab_channel=teclado
  - Doc.: https://www.youtube.com/watch?v=b4Ms4wxJuPg&ab_channel=teclado
  
