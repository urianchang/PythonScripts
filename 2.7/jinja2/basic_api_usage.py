from jinja2 import Template

# IMPORTANT: Jinja2 uses unicode internally and the return
# value is an unicode string.

html_string = u"""
<html>
    <head>
        <title>Jinja!</title>
    </head>
    <body>
        <h1>Hello {{name}}</h1>
        {# This is a comment #}
        {% for num in some_list %}
        <p>{{num}}</p>
        {% endfor %}
    </body>
</html>
"""

template = Template(html_string)
print template.render(name="Urian", some_list=[1, 2, 3])

"""
By creating an instance of Template you get back a new template
object that provides a method called render() which when called
with a dict or keyword arguments expands the template. The dict
or keywords arguments passed to the template are the so-called
"context" of the template.
"""
