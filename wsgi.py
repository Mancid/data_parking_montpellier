import os
import backend


app = backend.create_app('production')

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 9375))
    app.run(host='0.0.0.0', port=port)
