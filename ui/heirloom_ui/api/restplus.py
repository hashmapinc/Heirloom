from flask_restplus import Api

#==============================================================================
# Restplus setup 
#==============================================================================
# init restplus Api
restplus_api = Api(
  version='0.1.0', 
  title='Heirloom UI',
  description='A simple frontend for interacting with Heirloom'
)
#==============================================================================