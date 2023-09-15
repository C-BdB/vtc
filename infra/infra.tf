provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = var.rg
  location = var.location_frcentral
}

resource "azurerm_service_plan" "plan" {
  name                = var.plan
  location            = var.location_frcentral
  resource_group_name = var.rg
  os_type             = var.os_type
  sku_name            = var.sku_name
}

resource "azurerm_storage_account" "st" {
  name                     = var.st
  resource_group_name      = var.rg
  location                 = var.location_frcentral
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_linux_function_app" "azf" {
  name                       = "fee"
  location                   = var.location_frcentral
  resource_group_name        = var.rg
  service_plan_id            = azurerm_service_plan.plan.id
  storage_account_name       = azurerm_storage_account.st.name
  storage_account_access_key = azurerm_storage_account.st.primary_access_key

  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME" = "python"
  }

  site_config {
    always_on        = false
  }
}

