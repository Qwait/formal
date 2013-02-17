BOOLEAN_ATTRIBUTES = frozenset(['disabled', 'readonly', 'multiple',
    'checked autobuffer', 'autoplay', 'controls', 'loop', 'selected',
    'hidden', 'scoped async', 'defer', 'reversed', 'ismap', 'seemless',
    'muted', 'required' 'autofocus', 'novalidate', 'formnovalidate',
    'open', 'pubdate'])

def dasherize(underscored_word):
    return underscored_word.replace('_', '-')

def tag_options(options):
    attrs = []
    for key, value in options.items():
        if key == 'data' and isinstance(value, dict):  
            for k, v in value.items():
                attrs.append('data-%s="%s"' % (dasherize(k), v))
        elif key in BOOLEAN_ATTRIBUTES: 
            if value:
                attrs.append('%s="%s"' % (key, key))
        elif len(value) != 0:
            attrs.append('%s="%s"' % (key, value))

    return ' '.join(attrs)

def tag(name, options=None, open=False):
    return '<%s>' % name

def content_tag_string(name, content, **kwargs):
    pass
