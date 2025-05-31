
from app.ontology_dc8f06af066e4a7880a5938933236037.config import ConfigClass
from app.ontology_dc8f06af066e4a7880a5938933236037.input import InputClass
from app.ontology_dc8f06af066e4a7880a5938933236037.output import OutputClass
from openfabric_pysdk.context import AppModel, State
from app.main import config, execute

# Simulate configuration
state = State()
config_data = {'super-user': ConfigClass(app_ids=['app1', 'app2'])}
config(config_data, state)

# Simulate input
input_obj = InputClass(prompt="What is OpenFabric?")
output_obj = OutputClass()

# Simulate app model
model = AppModel(request=input_obj, response=output_obj)

# Execute the app
execute(model)

# Output the result
print(model.response.message)
