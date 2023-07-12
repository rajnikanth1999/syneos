from azureml.core import Workspace

aml_workspace = Workspace.get(
    name="demodp-dev-machinelearning001",
    subscription_id="d9f56f19-917a-4893-883e-1a93932f741b",
    resource_group="iepdlz01-dev-demodp"
)

print(aml_workspace)

local_secret = "justarandomsecretofmlops" # Use random UUID as a substitute for real secret.
keyvault = aml_workspace.get_default_keyvault()
keyvault = keyvault.set_secret(name="1ftpipelineID", value = local_secret)

print(keyvault)
