exports.config = {
    // See http://brunch.io/#documentation for docs.
    files: {
        javascripts: {
            joinTo: 'app.js'

            // To use a separate vendor.js bundle, specify two files path
            // https://github.com/brunch/brunch/blob/stable/docs/config.md#files
            // joinTo: {
            //  "js/app.js": /^(static\/js)/,
            //  "js/vendor.js": /^(static\/vendor)|(deps)/
            // }
            //
            // To change the order of concatenation of files, explicitly mention here
            // https://github.com/brunch/brunch/tree/master/docs#concatenation
            // order: {
            //   before: [
            //     "static/vendor/js/jquery-2.1.1.js",
            //     "static/vendor/js/bootstrap.min.js"
            //   ]
            // }
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
            'templates'
            // Add any more template directories here
        ],

        public: 'brunch'
    },

    // Automatically require modules
    modules: {
        autoRequire: {
            // Uncomment the following line to automatically run javascript you write in 'static/js/main.js'
            //"app.js": ["static/js/main"]
        }
    },

    npm: {
        enabled: true
    }
};
