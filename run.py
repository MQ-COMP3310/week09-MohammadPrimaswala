from project import create_app
import os

if __name__ == '__main__':
  app = create_app()
  debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
  app.run(host = '0.0.0.0', port = 8001, debug=debug_mode) 