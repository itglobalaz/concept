SUMMERNOTE_CONFIG = {
    'iframe': True,
    'lang': 'en',
    'summernote': {
        'width': '100%',
        'height': '500px',
        'toolbar': [
            ['style', ['style', ]],
            [['fontsize', 'bold', 'italic', 'strikethrough', 'clear', ]],
            ['color', ['forecolor', 'backcolor', ]],
            ['para', ['ul', 'ol', 'height']],
            ['insert', ['link']],
            ['misc', ['picture', 'fullscreen', 'codeview', 'print', 'help', ]],
        ],
    },
    'js': (
        '/static/summernote-ext-print.js',
    ),
    'js_for_inplace': (
        '/static/summernote-ext-print.js',
    ),
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.40.0/theme/base16-dark.min.css',
    ),
    'css_for_inplace': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.40.0/theme/base16-dark.min.css',
    ),
    'codemirror': {
        'theme': 'base16-dark',
        'mode': 'htmlmixed',
        'lineNumbers': 'true',
    },
    'lazy': False,
}

SUMMERNOTE_THEME = 'bs4'
X_FRAME_OPTIONS = 'SAMEORIGIN'