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
            'static',
            'templates',
            // Add any more template directories here
            'polls/templates'
        ],

        public: 'brunch'
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
