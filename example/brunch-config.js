exports.config = {
    // See http://brunch.io/#documentation for docs.
    files: {
        javascripts: {
            joinTo: 'app.js'
        },
        stylesheets: {
            joinTo: 'app.css'
        },
        templates: {
            joinTo: 'app.js'
        }
    },

    // Django paths
    paths: {
        watched: [
            'app', 'test', 'vendor',
            'templates',
            // Add any more template directories here
            'polls/templates'
        ]
    },

    // Automatically require modules
    modules: {
        autoRequire: {
            "app.js": ["static/js/main"]
        }
    },

    npm: {
        enabled: true
    }
};
