variable "location_frcentral" {
  type        = string
  default     = "France Central"
  description = "String of location"
}

variable "rg" {
  type        = string
  default     = "rg-fee"
  description = "RG name"
}

variable "os_type" {
  type        = string
  default     = "Linux"
  description = "OS type"
}

variable "sku_name" {
  type        = string
  default     = "F1"
  description = "F1 is free"
}

variable "st" {
  type        = string
  default     = "st"
  description = "storage account"
}